import requests,json
from configparser import ConfigParser

class FangNeng():
    def __init__(self, domain_name,groups="3654",user_package="1779",backenIp="11.22.33.44",port="80"):
        self.api_url = "https://api.funnullv8.com/"
        self.apiKey = "roYEe3nSatTqRV2G"
        self.apiSecret = "JFZTaBScVDrMGkgf0z93qlsYXU2jA4"
        self.domain_name = domain_name # 需要添加的域名
        self.groups = groups   # 分组id
        self.user_package = user_package  # 套餐id
        self.backenIp = backenIp # 回源地址
        self.backend_http_port = port  # 回源端口

    def AddDomain(self):
        addDomain_url = self.api_url+"/sites"
        post_headers = {"Content-Type": "application/json","api-key": self.apiKey, "api-secret": self.apiSecret}
        add_domain_data = {"groups": self.groups, "user_package": self.user_package, "domain": self.domain_name, "backend": [{"addr": self.backenIp}], "backend_http_port": self.backend_http_port}
        r = requests.post(addDomain_url, headers=post_headers,data=json.dumps(add_domain_data))
        print(r.json())
        return r.json()

    def AddCerts(self):
        addCerts_url = self.api_url+"/certs"
        post_headers = {"Content-Type": "application/json","api-key": self.apiKey, "api-secret": self.apiSecret}
        add_certs_data = {"name": self.domain_name, "des": self.domain_name,"type": "lets", "domain": self.domain_name}
        r = requests.post(addCerts_url, headers=post_headers,data=json.dumps(add_certs_data))
        print(r.json())
        return r.json()

    def ChangeCerts(self,domainID,certsID):
        ChangeCerts_url = self.api_url+"/sites/"+domainID
        post_headers = {"Content-Type": "application/json","api-key": self.apiKey, "api-secret": self.apiSecret}
        data={"https_listen": {"cert":str(certsID),"force_ssl_enable": True}}
        #data={"https_listen": {"force_ssl_enable": "ture"}}
        r=requests.put(ChangeCerts_url,headers=post_headers,data=json.dumps(data))
        print(r.json())
        return r.json()

if __name__ == "__main__":
    # myFangneng=FangNeng("www.111.com","3654","1779","11.23.44.55","80")
    # myFangneng.AddDomain()
    print("读取配置文件")
    cfg=ConfigParser()
    cfg.read("cloudflare_add_domain\config.ini")
    print(cfg.sections())
    email=cfg.get("CloudFlare","email")
    apikey=cfg.get("CloudFlare","apikey")
    cname=cfg.get("CloudFlare","cname")
    groups=cfg.get("FangNeng","groups")
    user_package=cfg.get("FangNeng","user_package")
    backendIP=cfg.get("FangNeng","backendIP")
    backendPort=cfg.get("FangNeng","backendPort")

    post_headers = {"Content-Type": "application/json","api-key": "roYEe3nSatTqRV2G", "api-secret": "JFZTaBScVDrMGkgf0z93qlsYXU2jA4"}
    url="https://cdn.funnullv8.com/sites/435455"
    data={"https_listen": {"force_ssl_enable": True,"force_ssl_port": "443"}}
    #data={"https_listen": {"force_ssl_enable": True}}
    print(json.dumps(data))
    r=requests.put(url,headers=post_headers,data=json.dumps(data))
    print(r.json)
    
