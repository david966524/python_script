from alibabacloud_vpc20160428.client import Client as Vpc20160428Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_vpc20160428 import models as vpc_20160428_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_console.client import Client as ConsoleClient

class EIP():
    def __init__(self) -> None:
        pass
    
    #创建 vpc client 对象
    def create_client(access_key_id: str,access_key_secret: str,) -> Vpc20160428Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 必填，您的 AccessKey ID,
            access_key_id=access_key_id,
            # 必填，您的 AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = f'vpc.aliyuncs.com'
        return Vpc20160428Client(config)

    # EIP绑定EC2
    def associateEip(eipID, ec2ID, client):
        associate_eip_address_request = vpc_20160428_models.AssociateEipAddressRequest(
            region_id='cn-hongkong',
            allocation_id=eipID,
            instance_id=ec2ID
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            response = client.associate_eip_address_with_options(
                associate_eip_address_request, runtime)
            return response.status_code 
        
            
        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)
    
    # 申请EIP
    def allocateEip(name, client):
        allocate_eip_address_request = vpc_20160428_models.AllocateEipAddressRequest(
            region_id='cn-hongkong',
            instance_charge_type='PostPaid',
            bandwidth='200',
            internet_charge_type='PayByTraffic',
            isp='BGP_PRO',
            netmode='public',
            name=name+"-精品",
            description=name
            )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            response = client.allocate_eip_address_with_options(
                allocate_eip_address_request, runtime)
            ConsoleClient.log(
                    f'创建EIP实例成功,实例ID:{response.body.allocation_id} ip为{response.body.eip_address}')
            print(response.body.allocation_id)
            return response.body.allocation_id,response.status_code
        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)