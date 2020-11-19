from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkactiontrail.request.v20171204.CreateTrailRequest import CreateTrailRequest
from aliyunsdkactiontrail.request.v20171204.StartLoggingRequest import StartLoggingRequest


# 华东 1 (杭州)  Region 
# cn-hangzhou region
region = 'cn-hangzhou'
# 用户访问密钥对中的AccessKey ID
# The access key id of your account
access_key_id = 'ABCDEFGHIJK****'
# 用户访问密钥对中的AccessKey Secret
# The access secret key of your account
access_key_secret = 'OPQRSTUV****'
# 阿里云账号ID
# The root account id
account_id = '1234567'

# 跟踪名称
# The trail name
trail_name = 'cloud_trail'
# 用来存储操作日志的日志项目
# The SLS Log Project name to save action events
log_project_name = 'cloud-trail-project'

client = AcsClient(access_key_id, access_key_secret, region)


# 创建跟踪
# Create a trail
sls_project_arn = 'acs:log:{region}:{account_id}:project/{log_project_name}'.format(
    region=region,
    account_id=account_id,
    log_project_name=log_project_name,
)
request = CreateTrailRequest()
request.set_accept_format('json')
request.set_Name(trail_name)
request.set_SlsProjectArn(sls_project_arn)
# 跟踪所有类型的事件（读事件和写事件）
# Trail events of all types, includes `write` events and `read` events
request.set_EventRW("All")
# 跟踪所有地域
# Trail events of all regions
request.set_TrailRegion("All")
response = client.do_action_with_exception(request)
print(str(response, encoding='utf-8'))


# 启用跟踪
# Start a trail
request = StartLoggingRequest()
request.set_accept_format('json')
request.set_Name(trail_name)
response = client.do_action_with_exception(request)
print(str(response, encoding='utf-8'))