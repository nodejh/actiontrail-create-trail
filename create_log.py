import json
from aliyun.log import LogClient
from aliyun.log import IndexConfig
import time

def get_json_data(path):
    with open(path) as f:
        return json.load(f)


# 华东 1 (杭州)  Region 
# cn-hangzhou region
region = 'cn-hangzhou'

# 日志服务入口
# The endpoint of SLS
endpoint = '{region}.log.aliyuncs.com'.format(region=region)
# 用户访问密钥对中的AccessKey ID
# The access key id of your account
access_key_id = 'ABCDEFGHIJK****'
# 用户访问密钥对中的AccessKey Secret
# The access secret key of your account
access_key_secret = 'OPQRSTUV****'
# 阿里云账号ID
# The root account id
account_id = '1234567'

client = LogClient(endpoint, access_key_id, access_key_secret)


# 跟踪名称
# The trail name
trail_name = 'cloud_trail'
# 日志项目名称，阿里云全局唯一
# The SLS Log Project name, it should by unique in Alibaba Cloud
log_project_name = 'cloud-trail'
# 日志库名称
# The SLS Log Store name
log_store_name = 'actiontrail_{trail_name}'.format(trail_name=trail_name)

# 创建日志服务
# Create a Log Project
res = client.create_project(log_project_name, '操作审计事件日志项目')
res.log_print()


# 等待一段时间，因为创建日志项目是异步的
# Wait for a while, because create a Log Project is asynchronous
time.sleep(120)

# 创建日志库
# Create Log Store
res = client.create_logstore(log_project_name, log_store_name, shard_count=3, preserve_storage=True)
res.log_print()

# 从log_index.json中读取索引配置
# Get Log Index config from json file
index_json = get_json_data('./log_config/log_index.json')
index_detail = IndexConfig()
index_detail.from_json(index_json)
# 创建索引
# Create Log Index
res = client.create_index(log_project_name, log_store_name, index_detail)
res.log_print()


#  从log_dashboard.json中读取报表配置
# Get Log Dashboard config from json file
dashboard_detail = get_json_data('./log_config/log_dashboard.json')
# 创建报表 
# Create Log Dashboard
client.create_dashboard(log_project_name, dashboard_detail)
