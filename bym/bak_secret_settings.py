# 数据库连接信息
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bym',
        'USER': 'xxx',
        'PASSWORD': 'xxx',
        'HOST': '127.0.0.1',
        "OPTIONS": {"init_command": "SET default_storage_engine=INNODB;"}
    }
}