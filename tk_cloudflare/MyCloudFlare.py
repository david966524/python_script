import CloudFlare as cloudflare

class mycloudflare():
    def __init__(self) -> None:
        self.email="cloudflare Email"
        self.apikey="cloudflare apikey"

    def get_all_domain(self) -> list:
        cf = cloudflare.CloudFlare(self.email, self.apikey,raw=True) 
        page_number = 0
        zonelist=[]
        while True:
            page_number += 1
            raw_results = cf.zones.get(params={'per_page':150,'page':page_number})
            zones = raw_results['result']

            for zone in zones:
                zonelist.append(zone['name'])

            total_pages = raw_results['result_info']['total_pages']
            if page_number == total_pages:
                break
        return zonelist

    def search_domain(self,domain: str) -> list:
        zone_name = domain
        cf = cloudflare.CloudFlare(self.email, self.apikey)
        # query for the zone name and expect only one value back
        try:
            zones = cf.zones.get(params = {'name':zone_name,'per_page':1})
        except cloudflare.exceptions.CloudFlareAPIError as e:
            print('/zones.get %d %s - api call failed' % (e, e))
        except Exception as e:
            print('/zones.get - %s - api call failed' % (e))

        if len(zones) == 0:
            print('No zones found')
            return None

        # extract the zone_id which is needed to process that zone
        zone = zones[0]
        zone_id = zone['id']

        # request the DNS records from that zone
        try:
            dns_records = cf.zones.dns_records.get(zone_id)
        except cloudflare.exceptions.CloudFlareAPIError as e:
            exit('/zones/dns_records.get %d %s - api call failed' % (e, e))

        # print the results - first the zone name
        print("zone_id=%s zone_name=%s" % (zone_id, zone_name))

        # then all the DNS records for that zone
        strtable =None
        strtableall =[]
        for dns_record in dns_records:
            r_name = dns_record['name']
            r_type = dns_record['type']
            r_value = dns_record['content']
            strtable="{}\t{}\t{}\n".format(r_name,r_type,r_value)
            strtableall.append(strtable)    
        return strtableall

    def delete_domain(self,domain: str) -> str:
        cf = cloudflare.CloudFlare(self.email, self.apikey)
        # 获取域名ID，以便删除解析记录 
        zone_name = domain  # 替换为你的域名 
        zones = cf.zones.get(params={'name':zone_name})  # 获取域名ID 
        if zones :
            print("%s 存在于cloudflare" %domain)
            zone_id = zones[0]['id']   # 获取第一个匹配的域名ID 
            dns_records = cf.zones.dns_records.get(zone_id)  # 获取该域名下所有解析记录 

            # 删除所有解析记录 
            for dns_record in dns_records:   # 遍历所有解析记录，并删除它们  
                cf.zones.dns_records.delete(zone_id, dns_record['id'])  

            # 删除域名  
            cf.zones.delete(zone_id)
            print("%s 删除" %domain)
            return "%s 删除" %domain
        else :
            print("%s 不存在于cloudflare" %domain)
            return "%s 不存在于cloudflare" %domain
    
    def addDomain(self,domain: list,nameList:list ,type : str ,content: str):
        cf = cloudflare.CloudFlare(self.email, self.apikey)
        if self.search_domain(domain):
            print("域名已经存在")
        else:
            try:
                cf.zones.post(data={'name': domain})
                # Get the zone ID of the domain you just added
                zone_id = cf.zones.get(params={'name': domain})[0]['id']
                for name in nameList:
                    fullName="%s.%s" %name,domain
                    print(fullName)
                    cf.zones.dns_records.post(zone_id, data={'type': type, 'name': name, 'content': content, 'ttl': 60})
            except Exception as result:
                print("ERROR : %s" % result)