## House Hental and Sale Website

> 一个基于Python3.7 + Django 2.2 制作的 “房屋租赁和出售网站项目“

------

### IDE
- Pycharm

### DataBase
- MySQL：5.7版

### 技术栈
- Django：2.2
- Python：3.7
- Pillow：7.1.2
- mysqlclient：1.4.6


------

### 项目部署（本人是Windows10系统）

1. 下载项目

    * 访问 https://github.com/csyu12/RS_System 下载本项目源码解压

    * 通过PyCharm直接下载，如图：

      <img src="./README_img/image-20200719215449282.png" alt="image-20200719215449282" style="zoom:50%;" />

      <img src="./README_img/image-20200719215320304.png" alt="image-20200719215320304" style="zoom:50%;" />

2. 安装项目依赖

   ```
   pip install -r requirements.txt
   ```

3. 创建数据库

    MySQL数据库中执行：

    ```mysql
    CREATE DATABASE `HRS` CHARSET UTF8;
    ```

    修改`RS_system/setting.py` 修改数据库配置，如下所示：

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': 'localhost',
            'PORT': '3306',
            'NAME': 'HRS',
            'USER': 'root',
            'PASSWORD': '123456',
        }
    }
    ```

    在终端下执行:

    ```python
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

4. 创建后台管理员账户

    ```python
    python3 manage.py createsuperuser
    ```

    按要求输入用户名、邮箱（格式要合法）、密码

5. 运行服务器

   * 第一种方法：在终端中输入

   ```python
   python3 manage.py runserver
   ```

   `在浏览器打开 http://127.0.0.1:8000/ 即可访问主页`

   * 第二种方法：可以运行manage.py文件，修改配置，如下图。后续只需要运行manage.py即可

     <img src="./README_img/image-20200719212535828.png" alt="image-20200719212535828" style="zoom: 67%;" />

     <img src="./README_img/image-20200719212620738.png" alt="image-20200719212620738" style="zoom: 50%;" />

6. 进入后台

   - 在浏览器输入127.0.0.1:8000/admin
   - 使用第5步创建的后台管理员账户进行登录