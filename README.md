## Create Trail By SDK

English | [简体中文](./README-zh_CN.md)


- Language: python3

There are currently two steps to creating a trail:

- Create Log Project and Log Store
- Create and start a trail

### 文件说明

- [create_log.py](./create_log.py) Create Log Project and Log Store
- [create_trail.py](./create_trail.py) Create and start a trail
- [log_config/log_index.json](./log_config/log_index.json) SLS Log Index config
- [log_config/log_dashboard.json](./log_config/log_dashboard.json) SLS Log Dashboard config

### Create Log Project and Log Store:

```sh
$ pip install -U aliyun-log-python-sdk
$ python create_log.py
```

### Create and start a trail to Log Project

```sh
$ pip install aliyun-python-sdk-core
$ pip install aliyun-python-sdk-actiontrail
$ python create_trail.py
```