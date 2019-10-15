# Django 搭建个人网站

## 写在前面

之前实习的时候Manager让我在两个月做一个web工具出来，为了快速开发选择了Python开发，又鬼使神差的选择了Django框架。虽然在实习期顺利的搭建出Manager需要的东西，但是感觉对于web开发和Django的一些东西并没有很深的理解。刚好之前薅阿里羊毛，买了一年半的阿里云学生套餐加自己名字的域名，就想着自己重新搭建一个个人网站之类的东西，也算是重温一下实习学到的一些东西吧。

这几年Python随着人工智能的概念火的一塌糊涂，作为一种解释型高级语言，Python最大的优点就是开发效率高。Python为我们提供了非常完善的基础代码库，覆盖了网络、文件、GUI、数据库、文本等大量内容。用Python开发，许多功能重新造轮子，直接使用现成的即可。除了内置的库外，Python还有大量的第三方库，也就是别人开发的，供你直接使用的东西。

Django是一个由Python写成的web应用框架，使用它，可以快速的搭建出一个想要的个人网站。更多关于Django的介绍，请查看[Django官方网站](https://www.djangoproject.com/)。

### 资源列表

- 代码托管: [github/pippin.top](https://github.com/Pippinrao/pippin.top)
- Python基础：[廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/1016959663602400)
- 本文参考：[杜赛的个人网站](https://www.dusaiphoto.com/article/detail/2/)

## 搭建开发环境

### 本教程环境

- Windows 10
- [Python 3.6.5](https://www.python.org/ftp/python/3.6.5/python-3.6.5-embed-amd64.zip)
- [Django 2.2.2](https://www.djangoproject.com/download/)
- [MySQL 8.0.15](https://dev.mysql.com/downloads/mysql/)

Python安装和MySQL安装网上有很多相关的教程在这里就不予赘述。

### Python安装方法

[下载](https://www.python.org/ftp/python/3.6.5/python-3.6.5-embed-amd64.zip) 合适的Python版本（通常来说选择最新版本的不容易出错，如果是小白做好选择和我相同的版本），将下载的Python压缩包解压到不含中文的路径下（虽然有中文也没问题，但是为了防止后边出现各种小白解决不了的奇奇怪怪的问题，路径下最好不要有中文），并且将 Python.exe 所在的路径添加到系统路径下。方法如下：

> 右键此电脑，点击属性-->高级系统设置-->环境变量，在弹出的窗口中系统变量（不是用户变量）的滑动框中找到Path变量并双击。在弹出的窗口中点击新建，将Python.exe的绝对路径复制进去，确定。

点击WIN键，键入CMD（或者PowerShell）选中命令提示符，回车打开命令提示符（或者叫shell），输入

```shell
Python --version
```

若出现 Python 3.x.x 则说明Python安装成功，若有错误，检查以上操作是否有误。

### 配置虚拟环境

虚拟环境可以将同一台电脑下开发的不同项目开发环境互相隔离，从而减少不同版本之间的干扰。

新建一个目录，在命令提示符中进入该目录，输入

```shell
python -m venv django
django\Scripts\activate.bat
```

即可创建名称为django的虚拟Python开发环境，如果命令行开头有(django)标识说明进入虚拟环境成功。

### 安装 Django

pip为Python的包管理器，通过pip可以安装需要的Python第三方包。

在虚拟环境下输入

```shell
pip install django==2.2.2
```

等待网络安装完毕。若网络错误，可以[下载](https://files.pythonhosted.org/packages/b2/79/df0ffea7bf1e02c073c2633702c90f4384645c40a1dd09a308e02ef0c817/Django-2.2.6-py3-none-any.whl)安装文件，并使用

```shell
pip install django-xxx-xxx.whl
```

来安装。

在命令提示符进入Python提示符，输入

```python
import django
```

若没有报错，则安装成功。

### 创建项目

在虚拟环境下

```shell
django-admin startproject pippin
```

创建一个django项目，pippin为项目名称。

### 运行测试服务器

Django自带一个轻量的，用于开发的web服务器，进入项目根目录，输入

```shell
python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified some issues:

WARNINGS:
note.Note.tag: (fields.W340) null has no effect on ManyToManyField.

System check identified 1 issue (0 silenced).
October 06, 2019 - 22:49:14
Django version 2.2.2, using settings 'pippin.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

系统打印出以上信息，说明启动成功，在浏览器中输入http://127.0.0.1:8000/即可访问django的欢迎界面。

![django_start_page](S:/Document/SEU/计算机/web/img/django_start_page.JPG)

### 更改数据库为 MySQL

[下载](https://dev.mysql.com/downloads/mysql/)安装合适版本的MySQL，使用pip安装Python mysqlclient: 

```shell
pip install mysqlclient
```

打开新建的Django工程，打开setting.py，可以看到数据库设置为：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

```

将其修改为：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #数据库类型
        'NAME': 'pippin',                     #数据库名
        'USER': 'root',                       #用户名
        'PASSWORD': 'xxx',                    #密码
        'HOST': '127.0.0.1',                  #本机地址
        'PORT': '3306',                       #端口

    }
}
```

顺便修改一下时区和语言：

```python
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
```

### 关于代码编辑器

上述所有的操作均是在命令提示符内完成的，这样的开发方式虽然也能够完成目的，但是集成开发环境（IDE）显然能极大地提高我们的开发效率。这里推荐两款Python开发的IDE，PyCharm和VScode。

#### PyCharm

以下引自维基百科：

> **PyCharm**是一个用于计算机编程的集成开发环境（IDE），主要用于Python语言开发，由捷克公司JetBrains开发[[2\]](https://zh.wikipedia.org/wiki/PyCharm#cite_note-2)，提供代码分析、图形化调试器，集成测试器、集成[版本控制系统](https://zh.wikipedia.org/wiki/版本控制)，并支持使用Django进行网页开发。
>
> PyCharm是一个跨平台开发环境，拥有[Microsoft Windows](https://zh.wikipedia.org/wiki/Microsoft_Windows)、[macOS](https://zh.wikipedia.org/wiki/MacOS)和[Linux](https://zh.wikipedia.org/wiki/Linux)版本。社区版在[Apache许可证](https://zh.wikipedia.org/wiki/Apache许可证)下发布[[3\]](https://zh.wikipedia.org/wiki/PyCharm#cite_note-community-3) ，另外还有专业版在专用许可证下发布，其拥有许多额外功能。

JetBrains公司提供免费社区版和专业版两种，对于免费版只能用来开发纯Python脚本，显然是不符合我们的要求的。好消息是JetBrains给教育用户提供免费的激活证书，只需要用教育邮箱申请即可免费使用专业版PyCharm。

使用PyCharm开发Django工程，能够极大地提高我们的开发效率。

#### VScode

VScode是微软推出的一款及其良心的代码编辑器（鉴于其强大的功能，我们也可以称其为IDE）。若无法申请教育版PyCharm，个人推荐使用VScode来开发Django工程。

前面安装好了Python环境和虚拟环境，[下载](https://code.visualstudio.com/Download)安装VScode，点击Ctrl+Shift+X打开VScode插件界面，搜索Python和Django插件并安装。在工程根目录下的.vscode文件夹下创建settings.json文件并写入：

```json
{
    "python.pythonPath": "[virtual_env_path]/Scripts/python.exe"
}
```

打开manage.py，按F5进入调试选择Django即可调试Django工程。

## Django框架介绍

Django设计模式与传统MVC框架类似，Django叫MTV设计模式，即Model, Template, View。

Model为网站数据模型，对数据库进行封装，在Model中定义了数据库的表和表与表之间的关系。我们可以通过操作Model模块来对数据库进行读写操作。

Template模块是网站前端模板，是标准前端语言（HTML, CSS, JavaScript）添加了一些Python特性（for, if）。Django在运行时，将View模块传递过来的数据解释到模板中，然后通过HTTP协议传输给请求者。

View模块是Django的核心控制模块，通过View模块操作Model创建对象和对数据库读写，将数据传递给Template，对HTTP响应作出对应的反应。

## 设计网站模型（Model）