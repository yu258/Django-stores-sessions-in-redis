# Django-stores-sessions-in-redis

# 第一种配置方法
[官网地扯:django-redis](https://pypi.org/project/django-redis/)
## 安装模块
`pip install django-redis`

## settings.py文件
增加如下配置信息：
```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",  # 指明使用redis的1号数据库
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/3",  # 指明使用redis的3号数据库
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# session使用的存储方式
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 指明使用哪一个库保存session数据
SESSION_CACHE_ALIAS = "session"
```

# 第二种配置方法
[官网地扯:django-redis-sessions](https://pypi.org/project/django-redis-sessions/)
## 安装模块
`pip install django-redis-sessions`

## settings文件
```python
SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 1, # 指明使用1号数据库
    'password': '',
    'prefix': 'session',
    'socket_timeout': 1
}
```

# 用法

### 配置路由
```python
from django.urls import path

from . import views

urlpatterns = [
    path("set_session/",views.set_session,name="set_session"),
    path("get_session/",views.get_session,name="get_session"),
]
```

### 配置视图
```python
from django.shortcuts import render, HttpResponse

# Create your views here.

def set_session(request):
    # 设置session
    request.session['username'] = 'long'
    request.session['password'] = '123456'
    return HttpResponse("设置成功")


def get_session(request):
    # 获取session
    username = request.session.get('username')
    password = request.session.get('password')
    text = 'username=%s, password=%s' % (username, password)
    return HttpResponse(text)

```
### 地扯栏访问
`http://127.0.0.1:8000/set_session/`,效果图如下：

![](https://user-gold-cdn.xitu.io/2019/12/27/16f4640aafcf5376?w=383&h=134&f=png&s=8211)
`http://127.0.0.1:8000/get_session/`,效果图如下：

![](https://user-gold-cdn.xitu.io/2019/12/27/16f46411357c90ad?w=405&h=109&f=png&s=9118)


### 最后进入redis客户端中查看
#### 第一种配置方法的截图
![](https://user-gold-cdn.xitu.io/2019/12/27/16f46441f112d116?w=615&h=103&f=png&s=6031)

#### 第二种配置方法的截图

![](https://user-gold-cdn.xitu.io/2019/12/27/16f4669bb00e457a?w=415&h=98&f=png&s=4689)