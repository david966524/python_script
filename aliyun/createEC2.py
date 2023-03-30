from typing import List
from Tea.core import TeaCore

from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_darabonba_number.client import Client as NumberClient
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_darabonba_env.client import Client as EnvClient
from alibabacloud_ecs20140526.client import Client as EcsClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_models
from alibabacloud_darabonba_array.client import Client as ArrayClient

class EC2():
    def __init__(self) -> None:
        pass

    def create_client(access_key_id, access_key_secret, region_id):
        config = open_api_models.Config()
        config.access_key_id = access_key_id
        config.access_key_secret = access_key_secret
        config.region_id = region_id
        return EcsClient(config)
    
    def run_instances(
        instance_type: str,
        image_id: str,
        region_id: str,
        security_group_id: str,
        instance_name: str,
        description: str,
        zone_id: str,
        category: str,
        systemDisk_Size: str,
        v_switch_id: str,
        KeyPairName: str,
        dry_run: bool,
        client: EcsClient,
    ) -> List[str]:
        """
        创建并运行实例
        """
        request = ecs_models.RunInstancesRequest(
            region_id=region_id,
            instance_type=instance_type,
            image_id=image_id,
            security_group_id=security_group_id,
            instance_name="IMServer-"+instance_name,
            description=description,
            zone_id=zone_id,
            v_switch_id=v_switch_id,
            key_pair_name=KeyPairName,
            dry_run=dry_run,
            system_disk=ecs_models.RunInstancesRequestSystemDisk(
                category=category,
                size=systemDisk_Size
            )
        )
        ConsoleClient.log(f'--------创建实例开始-----------')
        responces = client.run_instances(request)
        ConsoleClient.log(
            f'-----------创建实例成功,实例ID:{UtilClient.to_jsonstring(responces.body.instance_id_sets.instance_id_set)}--------------')

        print(responces.body.instance_id_sets.instance_id_set[0])
        
        return responces.body.instance_id_sets.instance_id_set[0] , responces.status_code