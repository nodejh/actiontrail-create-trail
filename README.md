## 通过 SDK 创建跟踪

- 编程语言: python3

目前创建跟踪分为两步：

- 配置日志服务 `create_log.py`
- 创建并启用跟踪 `create_trail.py`

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