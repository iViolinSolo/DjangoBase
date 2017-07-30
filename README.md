# DjangoBase
A Django App Architecture Project, django app with basic django config and MySQL

# 环境安装
1. 大环境：`Python 2.7`、`pip`

2. 安装`virtalenv`，如果以前没有安装过的话：
```shell
$ pip install virtualenv
```

3. 开启`virtualenv`并运行虚拟化环境：
```shell
$ virtualenv Django
$ source Django/bin/activate
```

4. 安装所需依赖，在本项目根目录（`*/TJGSU-HRS`）下运行：
```shell
$ pip install -r requirements.txt
```

5. 如果使用`PyCharm`协助开发的话，请记得在将刚才自己创建的`virtualenv`的python环境加入到PyCharm的`Project Interpreter`，方法如下图：

  * 打开`Preference`:
  ![Step 1](https://raw.githubusercontent.com/iViolinSolo/MarkdownPhotos/master/Images/TJGSU-HRS/doc/setting-step-1.png)
  
  * 打开并更新`Project Interpreter`的信息
  ![Step 2](https://raw.githubusercontent.com/iViolinSolo/MarkdownPhotos/master/Images/TJGSU-HRS/doc/setting-step-2.png)
  
6. 添加Python的package以后，请重新更新`requirements.txt`，方法为：
```shell
$ pip freeze > requirements.txt
```

#运行项目
1. 直接运行项目
```shell
$ python manage.py runserver 0.0.0.0:8000
```

#MySQL 接入
1. 安装mysql的驱动
```shell
$ pip install mysqlclient
(如果是以 `pip install -r requirements.txt` 的方式
安装的，会自动安装这一个依赖)
```

2. 如果遇到报错 `EnvironmentError: mysql_config not found` 如下图：
```shell
$ pip install mysqlclient

Collecting mysqlclient
  Downloading mysqlclient-1.3.10.tar.gz (82kB)
    100% |████████████████████████████████| 92kB 80kB/s 
    Complete output from command python setup.py egg_info:
    sh: mysql_config: command not found
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/private/var/folders/jr/x67lbn9978x277l0xm0fvyy00000gn/T/pip-build-AcPhby/mysqlclient/setup.py", line 17, in <module>
        metadata, options = get_config()
      File "setup_posix.py", line 44, in get_config
        libs = mysql_config("libs_r")
      File "setup_posix.py", line 26, in mysql_config
        raise EnvironmentError("%s not found" % (mysql_config.path,))
    EnvironmentError: mysql_config not found
    
    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /private/var/folders/jr/x67lbn9978x277l0xm0fvyy00000gn/T/pip-build-AcPhby/mysqlclient/

```
请更新`环境变量`，[参考](http://www.jianshu.com/p/0d80366ca60c)文中举的例子：
在当前命令行输入以下命令，临时export更新环境变量内容：
```shell
$ export PATH=$PATH:/usr/local/mysql/bin/:
```
回车后重新安装`mysqlclient`就好
```shell
$ pip install mysqlclient
```
便能愉快的安装依赖了

#Reference
1.[Django入门](http://www.runoob.com/django/django-tutorial.html)
里面包含了好多东西，包括Django的一些配置到模版到引入mysql等等，感觉讲的很简单和详细

2.[Django + MySQL 配置](http://www.runoob.com/django/django-model.html)
里面写了具体如何引入mysql及对应配置方法