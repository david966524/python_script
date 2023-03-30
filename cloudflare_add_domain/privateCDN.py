import json,requests
import CloudFlare as cloudflare  # Import CloudFlare client library
import time
from configparser import ConfigParser
from add_domain import *


def addDomain(cf, domain_name,ttl=60):
    domain_name_list=[]
    if checkDomain(cf, domain_name):
        pass
    else:
        try:
        # Add a new domain to your account
            cf.zones.post(data={'name': domain_name})
            cname_url = domain_name.replace(".","_")
        # Get the zone ID of the domain you just added
            zone_id = cf.zones.get(params={'name': domain_name})[0]['id']

        # Add a new DNS record to the domain's zone file
            cf.zones.dns_records.post(
                zone_id, data={'type': 'cname', 'name': '@', 'content': cname_url+".cnddosekdnsmcos.com", 'ttl': ttl})

        # Add another DNS record to the domain's zone file
            cf.zones.dns_records.post(
                zone_id, data={'type': 'cname', 'name': 'www', 'content': "www_"+cname_url+".cnddosekdnsmcos.com", 'ttl': ttl})
            cf.zones.dns_records.post(zone_id, data={
                                      'type': 'cname', 'name': 'mobile', 'content': "mobile_"+cname_url+".cnddosekdnsmcos.com", 'ttl': ttl})
        # Print out all of the records in this domain's zone file
            CFresult_list = cf.zones.dns_records.get(zone_id)
            for domainInfo_dict in CFresult_list:  # CFresult_list   domainInfo是dict
                print(
                    "##################################################################")
                print("name:"+domainInfo_dict["name"])
                print("type:"+domainInfo_dict["type"])
                print("content:"+domainInfo_dict["content"])
                print("ttl:"+str(domainInfo_dict["ttl"]))
                domain_name_list.append(domainInfo_dict["name"])
            return domain_name_list
        except Exception as result:
            print("ERROR : %s" % result)




def getToken()-> str:
        payload = {"username":"admin2898802427","password":"V3UkEfuPlN"}
        post_headers = {"Content-Type": "application/json"}
        url="http://good.brrencdnaomsecan.com/auth-user/login"
        r=requests.post(url,data=json.dumps(payload),headers=post_headers)
        print(r.json())
        token ="Token "+r.json()['data']['auth_token']
        return token

class privateCdn():
    def __init__(self,domain: str,backendIP:str,remarks :str,token :str) -> None:
        self.domain=domain
        self.backendIP=backendIP
        self.remarks=remarks
        self.Token=token

    def add_domain(self) :
        add_post_headers = {"Content-Type": "application/json","Authorization":self.Token}
        add_payload={
            "full_domain": self.domain,
            "remarks": self.remarks,
            "sale": 2,
            "options": 3,
            "balance_option": "",
            "port": "80",
            "port_https": "443",
            "https": True,
            "backend_https": "0",
            "ssl": 1,
            "http2": False,
            "auto_ssl": True,
            "http_redirect_https": True,
            "upstream": [{"ip":self.backendIP,"port": 80}],
            "site_multi": []
        }
        addUrl="http://good.brrencdnaomsecan.com/domain/multi/"
        r1=requests.post(addUrl,data=json.dumps(add_payload),headers=add_post_headers)
        print(r1.json())

if __name__ == "__main__":
    
    print("读取配置文件")
    cfg=ConfigParser()
    cfg.read("cloudflare_add_domain/config.ini")
    print(cfg.sections())
    #cloudflare email账号 和 api key
    email=cfg.get("CloudFlare","email")
    apikey=cfg.get("CloudFlare","apikey") 

    backendIP=cfg.get("privateCDN","backendIP")  #回源地址
    remarks=cfg.get("privateCDN","remarks")    #平台备注


    #读取文件获取需要添加的域名
    file_path="cloudflare_add_domain\domain.txt"
    domain_list= getDomainList(file_path)

    new_domain_list=[]
    cf = cloudflare.CloudFlare(email=email, token=apikey) 
    for domain_name in domain_list:
        deleteDomain(cf,domain_name)
        result_list=addDomain(cf, domain_name)
        if result_list != None:
            new_domain_list.append(result_list)
        time.sleep(1)
    
    # 批量添加的域名 写入文件中
    if  len(new_domain_list) != 0 :
        with open("cloudflare_add_domain/fullDomain.txt","w",encoding="utf-8") as f:
            for i in new_domain_list:
                for j in i :    
                    f.write("https://"+j+'\n')
    token=getToken()
    for i in new_domain_list: #嵌套list
        for domain_name in i :
                mycdn=privateCdn(domain_name,backendIP,remarks,token)
                mycdn.add_domain()
            
            