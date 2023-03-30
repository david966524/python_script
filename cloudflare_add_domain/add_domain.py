import CloudFlare as cloudflare  # Import CloudFlare client library
import time
from FangNeng  import *
from configparser import ConfigParser


# pip3 install cloudflare


def checkDomain(cf, domain_name):
    domains = cf.zones.get()  # 获取所有cloudflare 上的 domain
    for domain in domains:   # Iterate through the list of domains
        if domain['name'] == domain_name:   # Check if the domain name matches
            print("%s Domain exists!" % domain_name)  # Print a message if it does
            return True
        else:   # If it doesn't match, keep looping through the list of domains
            continue
    # Print a message if it doesn't exist after looping through all domains
    print(' %s Domain does not exist!' % domain_name)
    return False


def addDomain(cf, domain_name,cname_url,ttl=60):
    domain_name_list=[]
    if checkDomain(cf, domain_name):
        pass
    else:
        try:
        # Add a new domain to your account
            cf.zones.post(data={'name': domain_name})

        # Get the zone ID of the domain you just added
            zone_id = cf.zones.get(params={'name': domain_name})[0]['id']

        # Add a new DNS record to the domain's zone file
            cf.zones.dns_records.post(
                zone_id, data={'type': 'cname', 'name': '@', 'content': cname_url, 'ttl': ttl})

        # Add another DNS record to the domain's zone file
            cf.zones.dns_records.post(
                zone_id, data={'type': 'cname', 'name': 'www', 'content': cname_url, 'ttl': ttl})
            cf.zones.dns_records.post(zone_id, data={
                                      'type': 'cname', 'name': 'mobile', 'content': cname_url, 'ttl': ttl})
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


def getDomainList(file_path):
    with open(file_path, "r", encoding="utf8") as f:
        domain_list = []
        for domain in f.readlines():
            if domain != "\n":
                domain_list.append(domain.strip())
            else :
                break
        return domain_list

    # Delete a DNS record from this domain's zone file
    # cf.zones.dns_records._delete('<record-id>')

    # Delete a domain from your account
    # cf .zones._delete('<zone-id>')

def deleteDomain(cf,domain_name):
    # 获取域名ID，以便删除解析记录 
    zone_name = domain_name  # 替换为你的域名 
    zones = cf.zones.get(params={'name':zone_name})  # 获取域名ID 
    if zones :
        print("%s 存在于cloudflare" %domain_name)
        zone_id = zones[0]['id']   # 获取第一个匹配的域名ID 
        dns_records = cf.zones.dns_records.get(zone_id)  # 获取该域名下所有解析记录 

        # 删除所有解析记录 
        for dns_record in dns_records:   # 遍历所有解析记录，并删除它们  
            cf.zones.dns_records.delete(zone_id, dns_record['id'])  

        # 删除域名  
        cf.zones.delete(zone_id)
        print("%s 删除" %domain_name)
    else :
        print("%s 不存在于cloudflare" %domain_name)


if __name__ == "__main__":
    

    
    print("读取配置文件")
    cfg=ConfigParser()
    cfg.read("cloudflare_add_domain/config.ini")
    print(cfg.sections())
    #cloudflare email账号 和 api key
    email=cfg.get("CloudFlare","email")
    apikey=cfg.get("CloudFlare","apikey")
    cname=cfg.get("CloudFlare","cname")# cname需要解析到方能cdn  
    #Fangneng 添加域名需要用的参数
    groups=cfg.get("FangNeng","groups") #分组 id
    user_package=cfg.get("FangNeng","user_package") #套餐id
    backendIP=cfg.get("FangNeng","backendIP")  #回源ip
    backendPort=cfg.get("FangNeng","backendPort") #回源端口


    #向cloudflare添加域名
    file_path="cloudflare_add_domain\domain.txt"
    domain_list= getDomainList(file_path)
    new_domain_list=[]
    cf = cloudflare.CloudFlare(email=email, token=apikey) 
    for domain_name in domain_list:
        deleteDomain(cf,domain_name)
        result_list=addDomain(cf, domain_name,cname)
        if result_list != None:
            new_domain_list.append(result_list)
        time.sleep(1)
    
    time.sleep(60)
    
    if  len(new_domain_list) != 0 :
        with open("cloudflare_add_domain/fullDomain.txt","w",encoding="utf-8") as f:
            for i in new_domain_list:
                for j in i :    
                    f.write("https://"+j+'\n')

        #向方能cdn 添加域名
        domain_id=None
        cert_id=None
        for i in new_domain_list: #嵌套list
            for domain_name in i :
                myfangNeng=FangNeng(domain_name,groups,user_package,backendIP,backendPort)
                addDomain_result_dict=myfangNeng.AddDomain() #得到 添加域名 返回的json
                if addDomain_result_dict["code"] == 0 :
                    print(" %s  CDN添加成功 " % myfangNeng.domain_name)
                    time.sleep(2)
                    domain_id=addDomain_result_dict["data"]
                    addCert_result_dict=myfangNeng.AddCerts() ##向方能cdn 申请证书 并得到 添加证书 返回的json
                    if addCert_result_dict["code"] == 0 :
                        print(" %s  证书添加成功 " % myfangNeng.domain_name) ## 向新增域名 添加证书配置
                        cert_id=addCert_result_dict["data"]  
                        time.sleep(2)
                        result=myfangNeng.ChangeCerts(domain_id,cert_id)
                        if result["code"] == 0 :
                            print("证书 修改成功")
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
                time.sleep(1.5)

        #time.sleep(120)
        
        # for i in new_domain_list: #嵌套list
        #     for domain_name in i :
        #         myfangNeng=FangNeng(domain_name)
        #         dict=myfangNeng.AddCerts()
        #         if dict["code"] == 0 :
        #             print(" %s  证书申请添加成功 " % myfangNeng.domain_name)
        #         time.sleep(1.5)
            
            