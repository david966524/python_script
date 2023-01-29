import CloudFlare as cloudflare  # Import CloudFlare client library
import fileinput
# pip install cloudflare


def checkDomain(cf, domain_name):
    domains = cf.zones.get()  # 获取所有cloudflare 上的 domain
    for domain in domains:   # Iterate through the list of domains

        if domain['name'] == domain_name:   # Check if the domain name matches
            print("Domain exists!")  # Print a message if it does
            return True
        else:   # If it doesn't match, keep looping through the list of domains
            continue
    # Print a message if it doesn't exist after looping through all domains
    print(' Domain does not exist!')
    return False


def addDomain(cf, domain_name):
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
                zone_id, data={'type': 'A', 'name': '@', 'content': '0.0.0.0', 'ttl': 120})

        # Add another DNS record to the domain's zone file
            cf.zones.dns_records.post(
                zone_id, data={'type': 'A', 'name': 'www', 'content': '0.0.0.0', 'ttl': 120})
            cf.zones.dns_records.post(zone_id, data={
                                      'type': 'A', 'name': 'mobile', 'content': '0.0.0.0', 'ttl': 120})
        # Print out all of the records in this domain's zone file
            CFresult_list = cf.zones.dns_records.get(zone_id)
            for domainInfo in CFresult_list:  # CFresult_list   domainInfo是dict
                print(
                    "##################################################################")
                for k, v in domainInfo.items():
                    print("%s   : %s" % (k, v))
        except Exception as result:
            print("error: %s" % result)


def getDomainList(file_path):
    with open(file_path, "r", encoding="utf8") as f:
        domain_list = []
        for domain in f.readlines():
            domain_list.append(domain.rstrip())
        return domain_list

    # Delete a DNS record from this domain's zone file
    # cf.zones.dns_records._delete('<record-id>')

    # Delete a domain from your account
    # cf .zones._delete('<zone-id>')


if __name__ == "__main__":
    file_path = "cloudflare_add_domain\domain.txt"
    domain_list = getDomainList(file_path)
    # 定义cloudflare email账号 和 api key
    email = ""
    apiKey = ""
    cf = cloudflare.CloudFlare(email=email, token=apiKey)
    for domain_name in domain_list:
        addDomain(cf, domain_name)
