from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkactiontrail.request.v20171204.CreateTrailRequest import CreateTrailRequest
from aliyunsdkactiontrail.request.v20171204.StartLoggingRequest import StartLoggingRequest


# 华东 1 (杭州)  Region 
region = 'cn-hangzhou'
# 用户访问密钥对中的AccessKey ID
access_key_id = 'ABCDEFGHIJK****'
# 用户访问密钥对中的AccessKey Secret
access_key_secret = 'OPQRSTUV****'
# 阿里云账号ID
account_id = '1234567'

# 跟踪名称
trail_name = 'cloud_trail'
# 日志项目名称，阿里云全局唯一
log_project_name = 'cloud-trail-project'


client = AcsClient(access_key_id, access_key_secret, region)


# 创建跟踪
sls_project_arn = 'acs:log:{region}:{account_id}:project/{log_project_name}'.format(
    region=region,
    account_id=account_id,
    log_project_name=log_project_name,
)
request = CreateTrailRequest()
request.set_accept_format('json')
# 设置跟踪名称
request.set_Name(trail_name)
# 设置 SLS project arn
request.set_SlsProjectArn(sls_project_arn)
# 跟踪所有事件
request.set_EventRW("All")
# 跟踪所有地域
request.set_TrailRegion("All")
response = client.do_action_with_exception(request)
print(str(response, encoding='utf-8'))


# 启用跟踪
request = StartLoggingRequest()
request.set_accept_format('json')
request.set_Name(trail_name)
response = client.do_action_with_exception(request)
print(str(response, encoding='utf-8'))