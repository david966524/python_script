from createEIP import EIP as eip
from createEC2 import EC2 as ec2
from configparser import ConfigParser
import time



if __name__ == "__main__":
    print("读取配置文件")
    cfg=ConfigParser()
    cfg.read("aliyun/config.ini")
    print(cfg.sections())
    
    access_key_id=cfg.get("Aliyun","access_key_id")
    access_key_secret=cfg.get("Aliyun","access_key_secret")
    region_id=cfg.get("Aliyun","region_id")
    
    instanceName=cfg.get("Aliyun","instanceName")
    instanceType = cfg.get("Aliyun","instanceType") 
    imageId = cfg.get("Aliyun","imageId")  
    securityGroupId = cfg.get("Aliyun","securityGroupId")  
    description = cfg.get("Aliyun","description")
    zoneId = cfg.get("Aliyun","zoneId") 
    vSwitchId = cfg.get("Aliyun","vSwitchId") 
    systemDisk_Size = cfg.getint("Aliyun","systemDisk_Size")
    category = cfg.get("Aliyun","category")
    KeyPairName = cfg.get("Aliyun","KeyPairName")
    dry_run = cfg.getboolean("Aliyun","dry_run")
    #print(type(dry_run))
    ec2Client=ec2.create_client(access_key_id,access_key_secret,region_id)
    ec2ID,ec2_status_code=ec2.run_instances(instanceType, imageId, region_id, securityGroupId, instanceName,
                                   description, zoneId, category, systemDisk_Size, vSwitchId, KeyPairName, dry_run,ec2Client)
    
    eipClient=eip.create_client(access_key_id,access_key_secret)
    
    if ec2_status_code == 200 :
        eipID,eip_status_code=eip.allocateEip(instanceName,eipClient)
        if eip_status_code ==200:
            print("等待10秒")
            time.sleep(10)
            result=eip.associateEip(eipID,ec2ID,eipClient)
            if result == 200:
                print("eip绑定成功")
        else:
            pass
    else :
        pass

    
    
    
    