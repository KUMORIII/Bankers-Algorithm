# Bankers-Algorithm
AHU 系统软件综合训练 银行家算法

## 题目要求

1. 界面友好
2. n个客户，m类资源（每个资源的上限随机生成，每个客户占用资源的个数、以及每类资源的时间随机生成）
3. 已分配资源的初始值是随机生成的
4. 需求资源的初始值是随机生成的
5. 生成尽可能多的安全序列，并从资源利用效率方面给出这些安全序列的排序
6. 相关文档完整

## 项目开发

采用DJango Web框架开发实现，[django官网](https://www.djangoproject.com/)

服务器采用阿里云学生免费服务器

## 项目使用方法

### 1 配置python环境
首先确保自己安装了python，建议使用anaconda配置环境

我的Python版本：3.8.3

[Anaconda](https://www.anaconda.com/)

### 2 下载django和simpleui

命令行输入 `conda install django` / `pip install django`

我的Django版本: 3.2.8

命令行输入`conda install django-simpleui` / `pip install django-simpleui`

### 3 运行
cd 至根目录下 `python manage.py runserver`

## 展示

在浏览器中（推荐chrome，不建议火狐）输入IP：`http://47.113.218.219/`即可

进入管理系统：在IP后加`/admin/`即可

---

![Home](https://pic.imgdb.cn/item/623de2c627f86abb2a9e98e2.png)
![Mainpage](https://pic.imgdb.cn/item/623de30d27f86abb2aa095c9.png)
![SCheck](https://pic.imgdb.cn/item/623de32727f86abb2aa15d1a.png)

## Django的基本使用方法

对Django的基本使用请见：[Django初见教程](https://www.cnblogs.com/kumori/p/15962582.html)

## 已完成模块

- [x] 初始化系统
- [x] 安全序列搜索
- [x] 资源利用效率算法排序
- [x] 独立倒计时显示
- [x] 管理系统
- [ ] 手动申请资源
- [ ] 自定义资源种类和进程数

## Thanks

有疑问或bug欢迎留言，如果您喜欢这个小作品或者有帮到您，请点一个⭐，谢谢！
