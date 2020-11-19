## 通过 SDK 创建跟踪

[English](./README.md) | 简体中文

- 编程语言: python3

目前创建跟踪分为两步:

- 配置日志服务
- 创建并启用跟踪 

### 文件说明

- [create_log.py](./create_log.py) 配置日志服务
- [create_trail.py](./create_trail.py) 创建并启用跟踪
- [log_config/log_index.json](./log_config/log_index.json) SLS 日志索引配置
- [log_config/log_dashboard.json](./log_config/log_dashboard.json) SLS 日志报表索引配置

### 配置日志服务

```sh
$ pip install -U aliyun-log-python-sdk
$ python create_log.py
```

### 创建并启用跟踪

```sh
$ pip install aliyun-python-sdk-core
$ pip install aliyun-python-sdk-actiontrail
$ python create_trail.py
```
