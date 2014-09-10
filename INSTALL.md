# 搭建souche本地开发环境

本文主要介绍在Linux环境下搭建souche项目的本地开发环境。

主要分为几步：

1. python开发工具搭建
2. 安装依赖包
3. 其他依赖
4. 运行项目

## Python开发工具搭建

利用python 工具 `virtualenv`和`virtualenvwrapper`来管理python的环境是非常方便的。

### virtualenv和virtualenvwrapper

[`virtualenv`][virtualenv home]是一个隔离python环境的工具。

[`virtualenvwrapper`][virtualenvwrap home]是virtualenv的扩展。
其中扩展包括：

* 创建和删除虚拟化环境;
* 管理开发工作流，使得在多个项目之间不引起冲突且工作更简单;


#### 安装
利用yum进行安装：

    yum install python-virtualenv

或利用`pip`进行安装：

    pip install virtualenv

#### virtualenvwrapper安装
利用yum进行安装：

    yum install python-virtualenvwrapper

或利用`pip`进行安装：

    pip install virtualenvwrapper

### virtualenv和virtualenvwrapper配置

* 设置virtualenvwrapper，（注意python版本）在`~/.bashrc`文件末尾添加以下命令：

        export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python (默认使用的python版本) #设置python版本和工作目录
        export WORKON_HOME=~/.venvs (工作目录，如果没有默认为~/.virutalenvs)
        source /usr/local/bin/virtualenvwrapper.sh    # 创建virtualenvwrap的虚拟工作环境
        export PIP_DOWNLOAD_CACHE=$HOME/.pip-downloads  # (可选)创建PIP下载软件包的缓存位置
        

* 为项目pingjia设置虚拟环境

        mkvirtualenv  souche
        workon  souche

* 若后面要退出虚拟环境，可输入命令：

        deactivate

## 安装依赖包

确保系统的python版本为2.7，若不是，请升级或者安装python2.7。

**系统需要安装的包：**

* mysql mysql-devel
* [redis]


利用`yum`依次安装以上库即可：

    yum install mysql mysql-devel
    yum install redis


**python环境需要安装的包：**

* 激活前面创建的python虚拟环境`souche`

        workon souche

    则在终端命令行左边会出现`(souche)`，表示已经启用python虚拟环境souche。

* 需要的Python依赖包在项目的`requirements.txt`文件中有列出，直接利用`pip`安装即可。

        pip install -r requirements.txt


## 其他依赖

* 若采用本地数据库，则需要将备份数据库导入恢复到本地。若采用远程连接数据库，则请联系管理员。

* Django cache的相关设置，需要设置`CACHE_FILE_DIR`。
若本地没有安装`redis`，可以将default设置成和file_cache一样。

        CACHES = {
            'default': {
                'BACKEND': 'redis_cache.cache.RedisCache',
                'LOCATION': '127.0.0.1:6379:1',
                'OPTIONS': {
                    'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
                    'PASSWORD': '',
                }
            },
            'file_cache': {
                'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
                'LOCATION': 'CACHE_FILE_DIR',   # Set file cache directory
                'TIMEOUT': 61200, # 07-24 17 hours
                'OPTIONS': {
                    'MAX_ENTRIES': 100000,
                    'CULL_FREQUENCY': 3,
                }
            },
        }

## 运行项目

在本地开发环境运行项目：

    ./runserver runserver

在生产环境下部署项目，我们在其他文档里面会给出部署方式和配置。



[virtualenv home]: http://www.virtualenv.org
[virtualenvwrap home]: http://virtualenvwrapper.readthedocs.org/en/latest/
[virtualenvwrap command]:  http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html 
[redis]: http://redis.io/
[redis-zh]: http://redis.cn/