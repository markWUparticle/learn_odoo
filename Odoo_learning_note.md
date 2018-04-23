中文社区：http://odoo.net.cn/category/19/odoo-%E5%9F%B9%E8%AE%AD

开发文档：http://www.odoo.com/documentation/10.0/index.html

使用文档：http://www.odoo.com/documentation/user/10.0/index.html

odoo 10 开发教程 https://www.kancloud.cn/hx78/odoo_10/416215#Odoo_18

odoo 10 学习笔记 http://www.cnblogs.com/qjtjh/category/1146375.html

Odoo学习专栏  https://zhuanlan.zhihu.com/80serp



主要补充：

- linux下的环境搭建
- odoo 前端网页开发 



学习日记：

- 了解了odoo系统结构、可以做哪些开发、模块的开发流程


- odoo开发环境搭建，安装、配置Odoo

- 学习创建自己模块

  - 建立模块骨架
    - 模块的组成
    - 模块的结构
  - 安装模块

- 基本视图

- 模块的关联



学习设计请假模块、工作计划模块

- 模块最常用的元素：模型
- 三种基本视图（表单、列表、搜索）
- 模型方法中的业务逻辑
- 访问的安全性
- 熟悉了模块的开发过程

  > 改变Python代码要重启
  > 更改XML\CSV 需要升级


### 扩展模块

- 学习扩展现有的模块：了解继承机制，使用机制去扩展模块，在现有的模块上添加和修改功能
  - 扩展了odoo模型来添加新字段，扩展其业务逻辑方法
  - 修改视图，新字段可用学习了如何从其他模型继承特性，添加了社交网络功能


### 模块数据

- 数据序列化、XML和CSV数据文件的使用
- 外部标识符
- 向模块中添加初始、演示数据

### 模型-构建应用程序数据

模型和字段，定义模型的关系，分层的父/子关系




XML 被设计为传输和存储数据



**权限管理的四个层次**

**菜单级别：** 即不属于指定菜单所包含组的用户看不到该菜单。**不安全**，只是隐藏菜单，若用户知道菜单ID，仍然可以通过指定URL访问

**对象级别：** 即对某个对象是否有‘创建，读取，修改，删除“的权限。Odoo中的对象可以简单理解为表对象，比如“客户”，“产品”，“销售订单”等都是对象

**记录级别：** 即对对象表中的数据的访问权限。比如同样访问“客户”对象，业务员只能对自己创建的客户有访问的权限，而经理可以访问其所辖的业务员的所有“客户”对象，这里的访问也可以进一步明细到“创建，读取，修改，删除”的权限

**字段级别：** 即一个对象或表上的某些字段的访问权限。比如产品的成本字段只有经理有读权限，比如订单上的单价字段只有经理才有修改的权限等





# 1 简介

> ### 企业资源规划ERP
>
> **E**nterprise **R**esource **P**lanning
>
> 指建立在信息技术基础上，以系统化的管理思想，为企业决策层及员工提供决策运行手段的管理平台

## 1.1 系统结构（框架）

- 数据库服务器：postgreSQL数据库服务器
- odoo应用服务器：业务逻辑代码，业务逻辑由各业务对象实现，可以通过远程直接调用（Net-PRC、XML-PRC）对象的方法
  - ORM：对象关系映射，负责数据对象到数据库的访问
  - BMD：底层模块，可任意添加其他模块
  - Report Engine：报表引擎，生产各种报表
  - Workflow Engine：工作流引擎，支持任意复杂度的工作流
  - WebService：提供网络调用接口，支持JSON-RPC、Net-RPC、XML-RPC
- 客户端：GTK-Client、Web-Client

## 1.2 开发

- 数据库访问功能：MVC开发模式
- 工作流开发：工作协作关系
- 报表开发：数据打印
- 集成开发：定制模板
  - init
  - openerp
- 数据段开发：postgreSQL

## 1.3 模块开发流程

- 分析模块模型：所需字段、定义模型类
- 构建菜单对象：views:xml定义菜单项
- 构建动作对象：管理具体菜单项的响应
- 构建视图对象：List、tree、form、search视图
- 配置：init、openerp

## 1.4 工作流开发

主要使用XML，有三种组成元素：workflow、activity、transition



# 2 开发环境搭建

## 2.1 Windows

###  2.1.1 下载安装

odoo 10.0 https://github.com/odoo/odoo/tree/10.0

Python 2.7  +pip

postgreSQL  

> https://www.postgresql.org/download/
>
> 创建一个新的登录角色 odoo_user 密码：root    所有权限

PyCharm

Node.js   #less CSS预处理器，为了正确呈现web页面

```
npm install -g less
npm install -g less-plugin-clean-css
```

###  2.1.2 环境配置

debian/odoo.conf

```
#数据库配置
db_host = 127.0.0.1
db_port = 5432
db_user = odoo_user
db_password = root
#源码路径
addons_path = C:\Users\cognichain\PycharmProjects\odoo\odoo-10.0\addons
```

###  2.1.3 安装所需模块

```
pip install -r requirements.txt
pip install pypiwin32
```

###  2.1.4 IDE(Pycharm)配置启动环境

**Debug Configurations**：

Script path: C:\Users\cognichain\PycharmProjects\odoo\odoo-10.0\odoo-bin

Parameters: --config=C:\Users\cognichain\PycharmProjects\odoo\odoo-10.0\debian\odoo.conf

Working dicretory: C:\Users\cognichain\PycharmProjects\odoo\odoo-10.0

## 2.2 Linux

### 2.2.1 源码安装Odoo

```
sudo apt-get update && apt-get upgrade # 安装系统更新 
sudo apt-get install git
sudo apt-get install npm  #安装Node.js及其管理器
sudo ln -s /usr/bin/nodejs /usr/bin/node
sudo npm install -g less less-plugin-clean-css #安装less编译器
```

```
mkdir ~/odoo-dev
cd ~/odoo-dev
git clone https://github.com/odoo/odoo.git -b 10.0 --depth=1 
./odoo/setup/setup_dev.py setup_deps  #安装odoo依赖包
./odoo/setup/setup_dev.py setup_pg	#安装PostgreSQL
```

```
~/odoo-dev/odoo/odoo-bin  #运行服务器命令
```

http://127.0.0.1:8069

### 2.2.2 初始化一个新的Odoo数据库

```
sudo createuser --superuser $(whoami)  
createdb demo
~/odoo-dev/odoo/odoo-bin -d demo   #使用odoo数据模式初始化该数据库
```

默认账户：admin 密码：admin

### 2.2.3 管理数据库

```
createdb --template=domo demo-test  #以demo为模板创建demo-test
psql -l  #查看现有数据库
dropdb demo-test #删除
```

### 2.2.4 服务器配置

服务器配置文件

```
~/odoo-dev/odoo/odoo-bin --save --stop-after-init #保存配置文件
more ~/.odoorc # 显示配置
```

改变监听端口

```
~/odoo-dev/odoo/odoo-bin --xmlrpc-port=8070
```

数据库过滤选项

```
$ ~/odoo-dev/odoo/odoo-bin --db-filter=^demo$ #只允许demo数据库
```

管理服务器日志消息

```
––log–level=debug  #调试日志级别
––dev=all   #打开python调试器
```



### 2.2.5 工作站

文本编辑器

```
sudo apt-get install nano
sudo apt-get install vim
```

安装配置Samba

```
sudo apt-get install samba samba-common-bin
sudo smbpasswd -a mark  #设置密码
sudo vim /etc/samba/smb.conf  (修改配置，读写访问权限)

[homes]
    comment = Home Directories 
    browseable = yesread only = no 
    create mask = O64O
    directory mask = O75O
    
$ sudo /etc/init.d/smbd restart  #重启服务
```

安装ssh服务

```
sudo apt-get install sshd 或者 openssh-server
sudo service sshd start   #启动服务
sudo service sshd status	#看服务器状态
ifconfig #查看IP地址
```

https://blog.csdn.net/keeplingshi/article/details/52760208 Pycharm远程开发

### 2.2.6 配置插件的路径

```
cd ~/odoo-dev/odoo
./odoo-bin -d demo --addons-path="./todo_app,./addons"
```



# 3 初入Odoo

## 数据库管理

初始化Odoo数据库

- 创建超级用户

- 新建新的数据库

- 使用Odoo数据模式初始化该数据库

  python odoo-bin -d <database>

创建数据库、管理员

```
database:odoo_db
user:wuzq@cognichain.com
password:root   #一般默认admin
```

管理数据库：http://127.0.0.1:8069/web/database/manager



# 4 构建模块

启动Odoo服务器

```
python odoo-bin
```

## 4.1 模块的组成

- 业务对象：会被框架自动持久化（持久化的方式取决于类的定义）
- 数据文件：视图、菜单、动作、工作流、权限、演示数据等（以XML或CSV文件定义）
- Web控制器：处理Web浏览器请求
- 静态页面数据：网站或界面使用的图片、CSS或JavaScript文件

## 4.2 模块结构

每个模块都是模块目录的一个子目录 --addons-path制定模块目录路径

> 大多数命令行可以通过配置文件进行设置

_ _init__.py文件包含了模块所需要的导入的各Python文件

比如包含mymodule.py，_ _init__.py应该加入

```
from . import mymodule
```

## 4.3 快速创建新模块

```
python odoo-bin scaffold <模块名> addons
```

> **属性值**
>
> name 模块名
>
> summary 简介
>
> description 详细介绍
>
> website 模块网站
>
> category 模块分类
>
> license 版权信息(默认AGPL-3)
>
> depends 模块以来
>
> data 必加载的数据文件
>
> demo     demonstration下才加载的数据文件
>
> installble 默认True，False 禁用
>
> auto_install 默认False，True将依赖模块自动安装
>
> application 默认False，将模块表示为应用，主要模块设置成True 

## 4.4 对象关系映射

-  Odoo关键组件ORM层：避免手写SQL，提供安全性、扩展性
-  业务对象被声明为Model类的扩展类，自动集成到持久层
-  _name，必填属性，定义了模块在系统中的名称
-  _description，为模型记录提供了一个用户友好的名称

models/models.py

```
from odoo import models, fields, api
class MinimalModel(models.Model):
    _name = 'test.model'
    #模型字段：定义了模型中需要储存的内容和储存的位置
    #字段通过类的属性来定义、通过属性参数的方式来配置
    name = fields.Char(required=True)
```

> #### 常见属性
>
> `string(unicode,default: field's name)`  字段标签
>
> `required(bool,default:False)`如果为True,这个字段不能为空
>
> `help (unicode, default: '')`长格式，在用户界面上显示的提示
>
> `index (bool, default: False)`请求Odoo在列上创建数据库索引

## 4.5 模型字段

#### 简单字段：

- 简单字段：Boolean、Date、Char
- 关联字段：Many2One、One2Many、Many2Many

#### 保留字段：

所有模型都创建的固定字段，由系统管理，用户程序可读取

- id(Id)  唯一标识符
- create_date(Datetime)
- create_uid(Many2one)
- write_date(Datetime)
- write_udi(Many2one)

#### 特殊字段

_rec_name：显示和搜索



**练习**

```
from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
```

## 4.6 数据文件

Odoo是高度数据驱动的系统，一些模块值是加载时通过数据文件来设置的。

> 一些模块的作用仅仅是为了将数据添加到Odoo中

模块数据通过带有`<record>`元素的XML数据文件来声明

每个`<record>`元素创建或更新数据中的一个记录行

```
<odoo>
    <data>
        <record model="{model name}" id="{record identifier}">
            <field name="{a field name}">{a value}</field>
        </record>
    </data>
</odoo>
```

- `model`是在记录行中记录的Odoo模型名称
- `id`是外部标识符，它允许引用记录（而不必知道其在数据库中的标识符）
- `<field>`，每个`<field>`对应数据行中的一个字段，name属性是字段名（例如*description*）,而`body`就是字段的值。

数据文件通过在manifest文件声明而被载入，他们既可以在data列表声明（始终载入）也可以在demo列表声明（仅在演示模式下载入）



**定义演示数据，添加演示数据以填充Course模型的数据**

openacademy/demo/demo.xml

```
<odoo>
    <data>
        <record model="openacademy.course" id="course0">
            <field name="name">Course 0</field>
            <field name="description">Course 0's description

Can have multiple lines
            </field>
        </record>
        <record model="openacademy.course" id="course1">
            <field name="name">Course 1</field>
            <!-- no description for this one -->
        </record>
        <record model="openacademy.course" id="course2">
            <field name="name">Course 2</field>
            <field name="description">Course 2's description</field>
        </record>
    </data>
</odoo>
```

## 4.7 操作和菜单

数据库中常规数据中，通常以数据文件声明，三种触发方式：

1. 点击菜单项（链接到特定操作）
2. 点击视图中的按钮（按钮已被连接到操作）
3. 作为对象的上下文操作

因菜单的声明相对复杂，可用`<menuitem>`快捷方式声明ir.ui.menu菜单对象，并将其更容易连接到相应操作

```
<record model="ir.actions.act_window" id="action_list_ideas">
    <field name="name">Ideas</field>
    <field name="res_model">idea.idea</field>
    <field name="view_mode">tree,form</field>
</record>
<menuitem id="menu_ideas" parent="menu_root" name="Ideas" sequence="10"
          action="action_list_ideas"/>
```

> 操作必须在XML文件中对应的菜单之前声明，数据文件是按顺序执行的，操作的ID必须在对应的菜单建立前就存于数据库中。



**练习**：定义新菜单项，在开放学院菜单项来 访问课程

- 显示所有课程的列表

- 建立或编辑课程

  1. 建立`openacademy/views/openacademy.xml`以创建操作和能够触发操作的菜单项

     ```python
     <?xml version="1.0" encoding="UTF-8"?>
     <odoo>
         <data>
             <!-- window action -->
             <!--
                 The following tag is an action definition for a "window action",
                 that is an action opening a view or a set of views
             -->
             <record model="ir.actions.act_window" id="course_list_action">
                 <field name="name">Courses</field>
                 <field name="res_model">openacademy.course</field>
                 <field name="view_type">form</field>
                 <field name="view_mode">tree,form</field>
                 <field name="help" type="html">
                     <p class="oe_view_nocontent_create">Create the first course
                     </p>
                 </field>
             </record>

             <!-- top level menu: no parent -->
             <menuitem id="main_openacademy_menu" name="Open Academy"/>
             <!-- A first level in the left side menu is needed
                  before using action= attribute -->
             <menuitem id="openacademy_menu" name="Open Academy"
                       parent="main_openacademy_menu"/>
             <!-- the following menuitem should appear *after*
                  its parent openacademy_menu and *after* its
                  action course_list_action -->
             <menuitem id="courses_menu" name="Courses" parent="openacademy_menu"
                       action="course_list_action"/>
             <!-- Full id location:
                  action="openacademy.course_list_action"
                  It is not required when it is the same module -->
         </data>
     </odoo>
     ```

  2. 添加这个文件到`openacademy/__manifest__.py`下的`data`列表。

     ```
      'data': [
             # 'security/ir.model.access.csv',
             'templates.xml',
             'views/openacademy.xml',
         ],
         # only loaded in demonstration mode
         'demo': [
     ```



# 5 基本视图

- 定义了模型数据的呈现方式
- 不同的视图类型决定了数据的可视化方式
- 视图可以通过类型（partners列表）或id被请求
- 每个类型的最低请求优先级视图是该类型的默认视图
- 视图继承允许更改其他声明的视图

## 5.1 通用视图声明

通过ir.ui.view的模型记录来声明，视图类型arch字段的根元素隐含定义

```
<record model="ir.ui.view" id="view_id">
    <field name="name">view.name</field>
    <field name="model">object_name</field>
    <field name="priority" eval="16"/>
    <field name="arch" type="xml">
        <!-- view content: <form>, <tree>, <graph>, ... -->
    </field>
</record>	
```

> 视图内容是XML，所以arch字段必须被声明为type='xml'以正确解析

## 5.2 树视图

列表视图，以表格形式显示记录，根元素是`<tree>`

```
<tree string="Idea list">
    <field name="name"/>
    <field name="inventor_id"/>
</tree>
```

## 5.3 表单视图

通常用来建立和编辑单条记录，根元素是`<form>`,由结构元素和交互元素组成。

```
<form string="Idea form">
    <group colspan="4">
        <group colspan="2" col="2">
            <separator string="General stuff" colspan="2"/>
            <field name="name"/>
            <field name="inventor_id"/>
        </group>

        <group colspan="2" col="2">
            <separator string="Dates" colspan="2"/>
            <field name="active"/>
            <field name="invent_date" readonly="1"/>
        </group>

        <notebook colspan="4">
            <page string="Description">
                <field name="description" nolabel="1"/>
            </page>
        </notebook>

        <field name="state"/>
    </group>
</form>
```



**练习**

> 使用XML定制窗口视图
>
> 建立课程对象的表单视图，显示课程名称和描述字段

openacademy/views/openacademy.xml

```
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <data>
        <record model="ir.ui.view" id="course_form_view">
            <field name="name">course.form</field>
            <field name="model">openacademy.course</field>
            <field name="arch" type="xml">
                <form string="Course Form">
                    <sheet>
                        <group>
                            <field name="name"/>
                            <field name="description"/>
                        </group>
                    </sheet>
                </form>
            </field>
        </record>
```

**练习notebook结构元素**

> 在课程的表单视图中，将描述字段放在一个选项卡中，然后再添加选项卡放置其他字段

openacademy/views/openacademy.xml

```
<form string="'Course Form">
	<sheet>
		<gruop>
			<field name="name"/>
		</gruop>
		<notebook>
			<page string="Description">
				<field name="description"/>
			</page>
			<page string="About">
				This is an example of note books
			</page>
		</notebook>
	</sheet>
</form>
```

表单视图也可以使用纯HTML来进行灵活布局

```
<form string="Idea Form">
    <header>
        <button string="Confirm" type="object" name="action_confirm"
                states="draft" class="oe_highlight" />
        <button string="Mark as done" type="object" name="action_done"
                states="confirmed" class="oe_highlight"/>
        <button string="Reset to draft" type="object" name="action_draft"
                states="confirmed,done" />
        <field name="state" widget="statusbar"/>
    </header>
    <sheet>
        <div class="oe_title">
            <label for="name" class="oe_edit_only" string="Idea Name" />
            <h1><field name="name" /></h1>
        </div>
        <separator string="General" colspan="2" />
        <group colspan="2" col="2">
            <field name="description" placeholder="Idea description..." />
        </group>
    </sheet>
</form>
```

## 5.4 搜索视图

对列表视图（其他聚合视图）中的字段进行搜索，根元素是`<search>`

```
<search>
    <field name="name"/>
    <field name="inventor_id"/>
</search>
```

如果在模型中没有定义搜索视图，Odoo会生产只包含name字段的搜索视图



**练习**

> 练习搜索课程，通过标题和描述来搜索课程

openacademy/views/openacademy.xml

```
</field>
        </record>

        <record model="ir.ui.view" id="course_search_view">
            <field name="name">course.search</field>
            <field name="model">openacademy.course</field>
            <field name="arch" type="xml">
                <search>
                    <field name="name"/>
                    <field name="description"/>
                </search>
            </field>
        </record>
```



# 6 模型关联

**练习建立一个授课模型**

> - 一个授课是在给定的时间中对给定的受众教授指定的课程
> - 为授课建立模型：名称、开放时间、持续时间、席位数
> - 添加操作和菜单项来显示新的模型

在openacademy/models/models.py文件中创建*Session*类

```
class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
```

> digits=(6,2)指定浮点数的精度：6是数字的总和，而2是小数位长度，表明整数位的最大长度是4

在openacademy/view/openacademy.xml文件中添加访问授课对象的菜单和操作

```
       <!-- Full id location:
             action="openacademy.course_list_action"
             It is not required when it is the same module -->

        <!-- session form view -->
        <record model="ir.ui.view" id="session_form_view">
            <field name="name">session.form</field>
            <field name="model">openacademy.session</field>
            <field name="arch" type="xml">
                <form string="Session Form">
                    <sheet>
                        <group>
                            <field name="name"/>
                            <field name="start_date"/>
                            <field name="duration"/>
                            <field name="seats"/>
                        </group>
                    </sheet>
                </form>
            </field>
        </record>

        <record model="ir.actions.act_window" id="session_list_action">
            <field name="name">Sessions</field>
            <field name="res_model">openacademy.session</field>
            <field name="view_type">form</field>
            <field name="view_mode">tree,form</field>
        </record>

        <menuitem id="session_menu" name="Sessions"
                  parent="openacademy_menu"
                  action="session_list_action"/>
    </data>
</odoo>
```

## 关联字段

链接同一模型（不同层次结构）或不同结构模型之间的记录

- **Many2one(other_model, ondelete='set null')**

  ```
  print foo.other_id.name
  ```


- **One2many(other_model, related_field)**

  虚拟关联，是many2one的逆，one2many作为记录容器，访问它将返回一个记录集

  ```
  for other in foo.other_ids:
      print other.name
  ```

  > 因为One2many是一个虚拟关联，所以必须有一个Many2one字段存在于other_model,其名称也必须是related_field

- **Many2many(other_model)**

  双向多对多的关联，一方的任一记录可以与另一方的任一数量记录关联

  作为记录的容器，访问它也可能导致返回空记录集

  ```
  for other in foo.other_ids:
      print other.name
  ```



**练习Many2one关联**

编辑Course和Session模型以反映他们与其他模型的关联：

- 课程有一个负责的用户；该字段的值是内置模型res.users的记录
- 一个授课有一个教师；该字段的值是内置模型res.partner的记录
- 授课与课程相关；该字段的值是openacademy.course模型的记录，并且是必填项
- 在模型中添加Many2one关联，并在视图显示

openacademy/models.py

```
name = fields.Char(string="Title", required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)

class Session(models.Model):
    _name = 'openacademy.session'
    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)
```

openacademy/views/openacademy.xml

```
				 <sheet>
                        <group>
                            <field name="name"/>
                            <field name="responsible_id"/>
                        </group>
                        <notebook>
                            <page string="Description">
```

```
            </field>
        </record>

        <!-- override the automatically generated list view for courses -->
        <record model="ir.ui.view" id="course_tree_view">
            <field name="name">course.tree</field>
            <field name="model">openacademy.course</field>
            <field name="arch" type="xml">
                <tree string="Course Tree">
                    <field name="name"/>
                    <field name="responsible_id"/>
                </tree>
            </field>
        </record>

        <!-- window action -->
        <!--
            The following tag is an action definition for a "window action",
```

```
                <form string="Session Form">
                    <sheet>
                        <group>
                            <group string="General">
                                <field name="course_id"/>
                                <field name="name"/>
                                <field name="instructor_id"/>
                            </group>
                            <group string="Schedule">
                                <field name="start_date"/>
                                <field name="duration"/>
                                <field name="seats"/>
                            </group>
                        </group>
                    </sheet>
                </form>
            </field>
        </record>

        <!-- session tree/list view -->
        <record model="ir.ui.view" id="session_tree_view">
            <field name="name">session.tree</field>
            <field name="model">openacademy.session</field>
            <field name="arch" type="xml">
                <tree string="Session Tree">
                    <field name="name"/>
                    <field name="course_id"/>
                </tree>
            </field>
        </record>

        <record model="ir.actions.act_window" id="session_list_action">
            <field name="name">Sessions</field>
            <field name="res_model">openacademy.session</field>
```



**练习逆关联one2many**

编辑模型以反映课程和授课之间的关系

- 编辑Course类，并且加入字段到它的表单视图

openacademy/models.py

```
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")

class Session(models.Model):
```

openacademy/views/openacademy.xml

```
                            <page string="Description">
                                <field name="description"/>
                            </page>
                            <page string="Sessions">
                                <field name="session_ids">
                                    <tree string="Registered sessions">
                                        <field name="name"/>
                                        <field name="instructor_id"/>
                                    </tree>
                                </field>
                            </page>
                        </notebook>
                    </sheet>
```



**练习多对多关联many**

在授课模型中添加关键字段many2many，每次授课和参与的听众做关联

听众来自于内置模型res.partner

- 修改Session类并且加入字段到它的表单视图中

openacademy/models.py

```
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
```

openacademy/views/openacademy.xml

```
                                <field name="seats"/>
                            </group>
                        </group>
                        <label for="attendee_ids"/>
                        <field name="attendee_ids"/>
                    </sheet>
                </form>
            </field>
```





# 构建第一个Odoo应用程序

构建一个To-Do应用程序，允许我们添加新任务，标记他们完成，清除已完成的任务列表

## 1 开发工作流程

- 建立一个新的实例
- 创建并安装一个新模块
- 更新模块以应用再发开迭代中所做的更改

## 2 Odoo遵循MVC构架

- model层：定义应用程序数据结构
- view层：描述用户界面
- controller层：支持应用程序的业务逻辑

## 3 理解应用程序和模块

### Module addons

- 应用程序构建块，可以添加新功能/修改功能
- 是一个目录，包含`__manifest__.py`，加上实现其特性的其余文件

### Applications

- 将主要特性添加到Odoo的方式
- 提供了功能领域的核心元素
- 给予附加的addon模块修改或扩展特性

模块复杂、向Odoo添加新的或主要功能>>>应用程序创建

只是对Odoo中现有功能进行更改>>>模块

## 4 创建模块的基本骨架

Odoo服务器在~/odoo–dev/odoo/

为了方便在旁边创建一个新目录来托管我们自定义模块~/odoo–dev/custom–addons

```
~/odoo-dev/odoo/odoo-bin scaffold <name> <dest>     #default: .
```

`__manifest__.py`文件内容：

```
(
'name': 'To–Do Application', 'description': 
'Manage your personal To–Do tasks.',
'author': 'Daniel Reis', 
'depends': ['base'], 
'application': True,
}
```

添加路径

```
$ cd ~/odoo-dev
$ ./odoo/odoo-bin -d todo --addons-path="custom-addons,odoo/addons" --save
```

升级模块

```
./odoo-bin -d todo -u todo_app

./odoo-bin -u todo_app
```

开发模式

```
––dev=all
```

## 5 model层

模型描述业务对象：属性列表、特定业务

### 创建数据类型模型

todo_app/models/todo_model.py

```
# -*- coding: utf-8 -*-

from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-do Task'
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
```

> 第三行声明了我们的新模型，来自models.Model的类
>
> 定义标识符_name属性，TodoTask对其他Odoo模块没有意义
>
> _description模型属性，记录了用户友好名称（非必要）
>
> name、active是特殊字段名
>
> name作为记录的标题，active激活记录

`models/__init__.py`

```
from . import todo_model
```

> 加载模块

- id 模型中每个记录的唯一标识符
- create_date/create_uid 创建记录/创建记录时间
- write_date/write_uid 最后修改/修改时间时确认
- ___last_update 用于并发检查

### 添加自动化测试

tests/test_todo.py

```
# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase

class TestTodo(TransactionCase):

    def test_create(self):
        'Create a simple Todo'
        Todo = self.env['todo.task']
        task = Todo.create({'name':'Tesk Task'})
        self.asserEqual(task.is_done,False)
```

`tests/__init__.py`

```
from . import test_todo
```

```
python odoo-bin -i todo_app --test-enable
```

## 6 view层

视图层描述用户界面

视图使用XML定义，由web框架使用，生成具有数据感知的HTML视图

### 添加菜单项

views/todo_menu.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<odoo>
<!--Action to open To–do Task list-->
    <act_window id="action_todo_task"
        name="To-do Task"
        res_model="todo.task"
        view_mode="tree,form"/>
<!--Menu item to open To–do Task list-->
    <menuitem id="menu_todo_task"
        name="Todos"
        action="action_todo_task"/>
</odoo>
```

用户界面（包括菜单选项和操作）储存在数据表中

> <act_window>元素定义了一个客户端操作，可以打开todo.task模型，启动tree、form视图
>
> `<menuitem>`元素定义了一个顶级菜单项，调用action_todo_task操作

两个元素都包含id属性(XML ID):唯一标识模块内部的每个元素，并可以由别的元素来引用它

`_mainfest_.py`

```
'data':['views/todo_menu.xml'],
```



**最重要的视图：tree(列表视图)、form和search视图**

### 创建form视图

所有视图都存在数据库中，在ir.ui.view模型中

为了向模块添加视图声明`<record>`元素，当模块安装时，将被加载到数据库中

views/todo_view.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<odoo>
    <record id="view_form_todo_task" model="ir.ui.view">
        <field name="name">To-do Task Form</field>
        <field name="model">todo.task</field>
        <field name="arch" type="xml">
            <form string="To-do Task">
                <group>
                    <field name="name"/>
                    <field name="is_done"/>
                    <field name="active" readonly="1"/>                    
                </group>
            </form>
        </field>
    </record>
</odoo>
```

- 向ir.ui.view模型添加一个记录，并使用标识符view_form_todo_task
- 视图是todo.task模型，命名为To-do Task Form（仅是为了获取信息，不必是唯一的，省略就自动生成）
- 重要的属性arch：包含视图定义,`<form>`标记定义了视图类型

### 业务form视图

> 对于文档模型,odoo有一个模仿纸质页面的演示样式
>
> 该表单包含两个元素：`<header>`包含操作按钮，`<sheet>`包含数据字段

将<from>替换为

```
 <form string="To-do Task">
               <header>
                   <!--Buttons go here-->
               </header>
                <sheet>
                    <!--Content goes here:-->
                    <group>
                        <field name="name"/>
                        <field name="is_done"/>
                        <field name="active" readonly="1"/>
                    </group>
                </sheet>
            </form>
```

### 添加action按钮

对于文档样式表单推荐位置`<header>`

添加两个按钮来运行todo.task模型的方法：

```
              <header>
                   <!--Buttons go here-->
                    <button name="do_toggle_done" type="object"
                        string="Toggle Done" class="oe_highlight"/>
                    <button name="do_clear_done" type="object"
                        string="Clear All Done"/>
               </header>
```

> 按钮的基本属性
>
> - string 显示在按钮上的文本
> - type 执行的动作
> - name 动作的标识符
> - class 是否使用css样式的可选属性

### 使用组来组织表单

`<group>`标记允许您组织表单内容

在`<group>`元素内放置`<group>`元素，在外部组内创建一个两列布局

建议组元素有一个name属性，以便其他模块可以更容易扩展他们

```
                <sheet>
                    <!--Content goes here:-->
                    <group name="group_top">
                        <group name="group_left">
                            <field name="name"/>
                        </group>
                        <group name="group_right">
                             <field name="is_done"/>
                            <field name="active" readonly="1"/>
                        </group>
                    </group>
                </sheet>
```

### 完整的form视图

```
 <form string="To-do Task">
                <header>
                   <!--Buttons go here-->
                    <button name="do_toggle_done" type="object"
                        string="Toggle Done" class="oe_highlight"/>
                    <button name="do_clear_done" type="object"
                        string="Clear All Done"/>
               </header>
                <sheet>
                    <!--Content goes here:-->
                    <group name="group_top">
                        <group name="group_left">
                            <field name="name"/>
                        </group>
                        <group name="group_right">
                             <field name="is_done"/>
                            <field name="active" readonly="1"/>
                        </group>
                    </group>
                </sheet>
            </form>
```

### 添加列表和search视图

当列表模式中查看模型时，使用`<tree>`视图

树视图能够显示在层次结构中组织的行，但多数用来显示普通列表

```
 <field name="model">todo.task</field>
        <field name="arch" type="xml">
            <tree colors="decoration-muted:is_done==True">
                    <field name="name"/>
                    <field name="is_done"/>
            </tree>
```

定义了只有两列的列表：name、is_done

添加了一个漂亮的触摸：完成任务行显示为灰色（通过Bootstrap类muted来完成）



右上角搜索框，搜索字段可用过滤器`<search>`视图定义

```python
   <field name="arch" type="xml">

            <search>
                <field name="name"/>
                <filter string="Not Done"
                        domain="[('is_done','=',False)]"/>
                <filter string="Done"
                        domain="[('is_done','!=',False)]"/>
            </search>
```

`<field>`元素定义在搜索框中输入的字段

`<filter>`元素添加预定义的筛选条件，可以通过特定语法定义的用户单机进行切换

**完整XML文件代码**

```python
<?xml version="1.0" encoding="UTF-8" ?>
<odoo>


     <record id="view_form_todo_task1" model="ir.ui.view">
        <field name="name">To-do Task Form</field>
        <field name="model">todo.task</field>
        <field name="arch" type="xml">
            <tree colors="decoration-muted:is_done==True">
                    <field name="name"/>
                    <field name="is_done"/>
            </tree>
        </field>
    </record>


    <record id="view_form_todo_task2" model="ir.ui.view">
        <field name="name">To-do Task Form</field>
        <field name="model">todo.task</field>
        <field name="arch" type="xml">

            <form string="To-do Task">
                <header>
                   <!--Buttons go here-->
                    <button name="do_toggle_done" type="object"
                        string="Toggle Done" class="oe_highlight"/>
                    <button name="do_clear_done" type="object"
                        string="Clear All Done"/>
              </header>
                   <sheet>
                    <!--Content goes here:-->
                    <group name="group_top">
                          <group name="group_left">
                           <field name="name"/>
                        </group>
                        <group name="group_right">
                             <field name="is_done"/>
                            <field name="active" readonly="1"/>
                        </group>
                    </group>
                </sheet>

            </form>
        </field>
    </record>

     <record id="view_form_todo_task3" model="ir.ui.view">
        <field name="name">To-do Task Form</field>
        <field name="model">todo.task</field>
        <field name="arch" type="xml">
         <search>
            <field name="name"/>
            <filter string="Not Done" domain="[('is_done','=',False)]"/>
            <filter string="Done" domain="[('is_done','!=',False)]"/>
        </search>
        </field>
    </record>

</odoo>
```



## 7 业务逻辑层

在按钮上添加一些逻辑，在模型的Python类中使用方法

### 添加业务逻辑

```
from odoo import models,fields,api

class TodoTask(models.Model):    
    @api.multi
    def do_toggle_done(self):
        for task in self:
            task.is_done = not task.is_done
        return True

    @api.multi
    def do_clear_done(self):
        dones = self.search([('is_done', '=', True)])
        dones.write({'active': False})
        return True
```

Toggle Done按钮：切换Is Done? 标记

对于记录的逻辑，使用@api.multi装饰器

self将代表一个记录集，然后我们每个记录进行循环

> 代码便利所有todo记录，然后为每个记录修改is_done字段，从而改变值
>
> 方法不需要返回任何东西，但应该至少返回一个True
>
> 客户机可以使用XML-RPC调用这些方法，而这个协议不支持只返回None值服务器函数

Clear All Done按钮：查找已经完成的所有活动记录，并使他们不活动，通常情况下，表单只会在选定的记录下执行，但在这种情况下，我们希望它也能根据当前的记录采取行动

> 以@aop.model为装饰的方法，self变量代表了没有特别的记录模型
>
> 构建一个包含所有被标记的任务的dones记录集，然后将active标记设置为False
>
> search方法是一种返回满足某些条件的记录API方法
>
> write方法在记录集的所有元素上设置值，使用字典描述要写入的值

### 添加测试

```
   task.do_toggle_done()
        self.asserTrue(task.is_done)

        Todo.do_clear_done()
        self.asserFalse(task.active)
```

## 8 设置访问安全

新模型没有定义访问规则，除了超级管理员外，其他任何人都不嗯呢该使用它

我么希望to-do任务对每个用户都是私有的

### 测试访问安全

由于缺少访问规则，测试失败

```
    def setUp(self,*args,**kwargs):
        result = super(TestTodo,self).setUp(*args,**kwargs)
        user_demo = self.env.ref(user='base.user_demo')
        self.env = self.env(user=user_demo)
        return result
```

> 第一个指令调用父类的setUp代码
>
> 然后改变环境，用于测试
>
> self.env 到一个新的使用演示用户



向测试类添加一个额外的方法：

```
from odoo.exceptions import AccessError

class TestTodo(TransactionCase):
    def test_record_rule(self):
        'Test per user record rules'
        Todo = self.env['todo.task']
        task = Todo.sudo().create({'name':'Admin Task'})
        with self.assertRaises(AccessError):
            Todo.browse([task.id]).name
```

由于我们的env方法现在使用了演示用户，所以我们使用sudo()方法将上下文改成admin用户

然后使用它来创建一个不应该被演示的用户访问任务

当尝试访问这个任务数据时，我们提高AccessError异常。

### 行级访问规则

> 记录规则在ir.rule模型中定义
>
> 通常规则适用于某些特定的安全组
>
> 我们将它应用于Employees组（如果没有安全组，则被认为是全局global自动设置为True)

添加记录规则

security/todo_access_rules.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<odoo>
    <data noupdate="1">
        <record id="todo_user_rule" model="ir.rule">
            <field name="name">ToDo Tasks only for owner</field>
            <field name="model_id" ref="model_todo_task"/>
            <field name="domain_force">
                [('create_uid','=',user.id)]
            </field>
            <field name="groups" eval="[(4,ref('base.group_user'))]"/>
        </record>
    </data>
</odoo>
```

> noupdate='1'属性，该数据不会再模块升级中更新，这将允许他在以后定制
>
> 模块升级不会破坏用户做出的改变

`_manifest .py`

```
'data': 
[ 'security/ir.model.access.csv', ]
```

## 9 更好的描述模块

应用程序图标：todo_app/static/description/icon.png

README.rst 文件放到模块根目录  

# 继承-扩展现有的应用程序

- 在现有对象之上的修改层
- 所有级别（模型、视图、业务逻辑）都可以修改
- 不直接修改现有模块，而是创建一个新的模块来修改

将实现的功能：

- 扩展任务模型：负责该任务的用户
- 修改业务逻辑：只在当前用户上运行
- 扩展视图：将必要的字段添加到视图中
- 社交网络功能：消息墙、关注




## 1 创建新模块 

```
python odoo-bin scaffold todo_user addons
```

todo_user/ manifest .py

```
{'name': 'Multiuser To–Do',
'description': 'Extend the To–Do app to multiuser.', 
'author': 'Daniel Reis',
'depends': ['todo_app'], }
```

```
python odoo-bin -u todo_user
```

## 2 扩展模型

- 使用带有_inherit属性的Python类，标识了要扩展的模型
- 这个新类继承了父Odoo模型的所有特性，我们只需要声明想要引入的修改
- Odoo模型还存于中央注册表中：使用`self.env[<model name>]`的模型访问
- 服务器启动时，一个附加模块所做的修改只会在随后加载的附加组件上可见

## 3 模型中添加字段

`todo_user/models/__init__.py`

```
from . import todo_task
```

todo_user/models/todo_task.py

```
from odoo import models, fields, api

class TodoTask(models.Model):
    _inherit = 'todo.task'
    user_id = fields.Many2one('res.users','Responsible')
    date_deadline = fields.Date('Deadline')
    name = fields.Char(help='What needs to be done?')

```

- 类名TodoTask是Python文件的本地名称，与其他模块无关
- _inherit类属性告诉Odoo这个类继承并修改了todo.task模型
- _name属性继承自父模型

> user_id字段：来自用户模型res.users的用户，Many2one字段，外键
>
> date_deadline：日期字段
>
> 为name字段添加了一个帮助提示

## 4 修改模型方法

- 添加新方法：在继承类中声它们的函数
- 要扩展或更改现有逻辑，通过使用的名称声明方法来覆盖相应的方法
- 新方法将取代以前的方法，而且还可以继承类的代码，使用super( )调用父方法
- 可以调用super()方法之前和之后，原有的逻辑上添加新逻辑

> 避免更发方法的函数签名，以确保现有的调用将继续正常工作
>
> 如果添加额外的参数，请将他们设置为可选的关键字参数（带有默认值）



最初的Claer All Done操作不适合我们的任务共享模块，清除了所有的任务，而不考虑其他的用户

修改为只清除当前的用户任务，我们将重写原来的方法，使用一个新版本，首先找到当前用户完成的任务列表，然后激活它们：

```
    @api.multi
    def do_clear_done(self):
        domain = [('is_done','=',True),'|',('user_id','=',self.env.uid),('user_id','=',False)]
        dones = self.search(domain)
        dones.write({'active':False})
        return True
```

- domanin：一个条件列表，每个条件都是一个元组，默认&操作符链接，OR操作‘|’，- 
- 筛选了已完成的任务，然后要么有属于当前用户，要么没有当前用户
- 然后使用search方法将记录集与所做的记录进行操作，最后批量写入，将active设置为False（null)

但是重写父方法，并不合适，我们应该讲现有的逻辑扩展到一些额外操作

使用super()构造该放的父版本

```
from odoo.exceptions import ValidationError
#...

	@api.multi
    def do_toggle_done(self):
        for task in self:
            if task.user_id != self.env.user:
                raise ValidationError('Only the responsible can do this!')
        return super(TodoTask,self).do_toggle_done()
```

继承类中的方法从一个for循环开始，检查是否要切换到另一个用户的任务

如果检查通过将使用super()调用父方法，否则抛出异常。

## 5 扩展

表单、列表、搜索都是使用arch XML结构定义

为了扩展视图，我们要修改XML，先定位XML元素，然后在这些点上修改

```
<odoo>
    <record id="view_form_todo_task_inherited1" model="ir.ui.view">
        <field name="name">Todo Task form - User extension</field>
        <field name="model">todo.task</field>
        <field name="inherit_id" ref="todo_app.view_form_todo_task2"/>
        <field name="arch" type="xml">
            <!--mathch and extend elements here! ...-->
        </field>
    </record>
</odoo>
```

- inherit_id字段通过使用特殊的ref属性来表示其外部标识符，从而将视图扩展。
- XML，定位XML元素的最佳方法使用XPath表达式
- `<field name='is_done'>`元素的XPath表达式//field[@name]='is_done'
- 这个表达式可以找到任何带有name属性field元素，它等于is_done
- 如果XPath表达匹配多个元素，则只会第一元素会被修改（尽量使用唯一属性）
- 使用name属性是确保我们找到要扩展点准确元素的最简单方法
- 一旦扩展点被定位，可以修改它附件添加XML元素

> is_done字段之前添加date_deadline字段，我们将在arch中编写一下代码：

```python
<field name="arch" type="xml">
	<xpath expr="//field[@name]='is_done" position="before">
	<field name="date_deadline"/>
	</xpath>
```

Odoo为这个提供提供了快捷方式，因此大多数时候避免使用XPath语法

我们可以使用与元素类型，相关的信息来定位和它的独特属性

```
       <field name="is_done" position="before">
                <field name="date_deadline"/>
            </field>
```

如果字段在同一视图中出现不止一次，那么您应该始终使用XPath语法

因为Odoo将在字段的第一次出现时停止，它可能将会您的更改应用到错误的字段

`<field>`标记 通常会被用作定位器（其他也可以）

名称属性通常是匹配元素的最佳选择

> 定位器元素使用的position属性是可选的，可以具有以下值
>
> - after将内容添加到父元素，在匹配的节点后
> - before在匹配的节点前
> - inside（默认值）附加在匹配节点内的内容
> - replace 替换匹配的节点，如果为空，则删除，还将允许一个元素与其他标记包在一起，$0表示被替换的元素
> - attributes 修改匹配元素的XML属性，<attribute name='attr-name'>元素和新的属性值设置中使用

例：在任务表单中，我们有active字段，我们需要隐藏

```
  <field name="active" position="attributes">
                <attribute name="invisible">1</attribute>
            </field>

```

> 避免使用replace定位器删除节点，因为它可以根据被删除的节点作为一个占位符来添加其他元素。

### 扩展form视图

```
<odoo>
 <record id="view_form_todo_task_inherited1" model="ir.ui.view">
        <field name="name">Todo Task form - User extension</field>
        <field name="model">todo.task</field>
        <field name="inherit_id" ref="todo_app.view_form_todo_task2"/>
        <field name="arch" type="xml">
            <field name="name" postion="after">
                <field name="user_id"></field>
            </field>
            <field name="is_done" position="before">
                <field name="date_deadline"/>
            </field>
            <field name="active" position="attributes">
                <attribute name="invisible">1</attribute>
            </field>
        </field>
    </record>
</odoo>
```

### 扩展tree和search视图

Tree和search视图扩展也被定义为使用arch XML结构

它们可以与form视图相同的方式扩展

```

     <record id="view_form_todo_task_inherited2" model="ir.ui.view">
        <field name="name">Todo Task form - User extension</field>
        <field name="model">todo.task</field>
        <field name="inherit_id" ref="todo_app.view_form_todo_task1"/>
        <field name="arch" type="xml">
            <field name="name" position="after">
                <field name="user_id"/>
            </field>
        </field>
    </record>
```

```
<record id="view_form_todo_task_inherited3" model="ir.ui.view">
        <field name="name">Todo Task form - User extension</field>
        <field name="model">todo.task</field>
        <field name="inherit_id" ref="todo_app.view_form_todo_task"/>
        <field name="arch" type="xml">
            <field name="name" position="after">
                <field name="user_id"/>
                <filter name="filter_my_tasks" string="My Tasks" domain="[('user_id','in',[uid,False])]"/>
                <filter name="filter_not_assigned" string="Not Assigned" domain="[('user_id','=',[uid,False])]"/>

            </field>
        </field>
    </record>
```

## 6 更多的模型继承机制

- class inheritance
  - 常见的继承：in-place extension
  - 集成多个父模型，将值列表设置为_inherit属性，可以使用mixin classes
  - Mixin classes是实现泛型特性的模型，不期望被直接使用，而是准备被添加到其他模型的特性容器


- prototype inheritance
  - 使用与父模型不同的_name属性，得到新模型
  - 模型重用继承的特性，但是用自己的数据库表和数据
  - 新模型，旧副本，添加新特性，原来的模型不改变
- delegation inhertance
  - 使用_inherits属性
  - 允许模型以透明的方式包含其他模型
  - 在幕后每个模型都处理自己的数据
  - 添加新特性，原模型不改变
  - 新模型的记录与原始模型记录有关联
  - 原始的模型字段可被新模型使用

### 复制具有原型继承的特性 

仅使用了_inherit属性，定义了继承todo.task模型，并添加特性的类，类属性 _name没有显式设置

_name属性允许我们创建一个新的模型，复制继承的特性

```
from odoo import models
	class TodoTask(models.Model):
	_name = 'todo.task'
	_inherit = 'mail.thread'
```

扩展了todo.task模型，将其复制到mail.thread模型的特性中

mail.thread模型实现了odoo消息和追随者特性，并且是可重复使用

赋值意味着继承的方法和字段也将在继承模型中可用。

对于字段，这意味着他们也将被创建并储存在目标模型的数据表中

原始和新的模型记录不相关，仅定义是共享的

### 委托继承嵌入模型

通过字典映射集成的模型和连接到他们的字段来使用_inherits属性

```
from odoo import models, fields 
	class User(models.Model):
	_name = 'res.users'
	_inherits = ('res.partner': 'partner_id'} 
	partner_id = fields.Many2one('res.partner')	
```

有了授权继承，res.users模型嵌入了继承模型的res.partner

当创建一个新的User类时，也会创建一个合作伙伴，并将它保存在User类的partner_id字段中（多态性）

- 无须重复数据结构
- 授权继承的字段是继承的，方法不是

### 添加社交网络功能

- 社交网络模块(mail)提供了许多表单底部
- Followers功能底部发现的消息板
- 消息和通知逻辑
- 由mail模块的mail.thread模型提供

要添加到自定义模块中，要以下操作

- 模块依赖于mail
- 有从mail.thread继承的类
- 在窗体视窗中添加了追随者和线程的小部件
- 为关注着简历记录规则

1. 基于mail模块

```
'depends': ['todoapp', 'mail']
```

2. 接受一个模型列表来继承

```
 _name = 'todo.task'
 _inherit = ['todo.task','mail.thread']
```

> mail.thread是一个抽象模型
>
> 没有数据表示，被用作mixin类，具有现成功能的模块
>
> 为了创建一个抽象类，我们只需要使用model.AbstractModel

3. 将社交网络小部件添加到表单的底部

```
<sheet position="after">
                <div class="oe_chatter">
                    <field name="message_follower_ids" widget="mail_followers"/>
                    <field name="message_ids" widget="mail_thread"/>
                </div>
</sheet>
```

这里的添加的个两个字段并没有被我们明确声明，但是它是由mail.thread模型提供的。

4. 为关注者设置记录规则：行级访问控制（模型被要求限制其他用户访问记录）

   每个To-do任务记录能被它的关注者看到

#### 修改数据

常规数据记录没有XML arch结构，不能用XPath表达式扩展

> `<record id="x" model="y">`数据加载元素实际上在模型y上执行insert或update操作
>
> 如果model x不存在,则创建
>
> 由于其他模块中的记录可以使用`<model>.<identifiler>`全局标识符访问，所以模块可以覆盖其他模块之前编写的内容

修改菜单和动作记录

```
           <!--Modify menu item-->
   <record id="todo_app.menu_todo_task" model="ir.ui.menu">
        <field name="name">My To_Do</field>
    </record>

    <!--Action to open To-Do Task list-->
    <record model="ir.actions.act_window"
        id="todo_app.action_todo_task">
        <field name="context">
            {'search_default_filter_my_tasks': True}
        </field>

    </record>
```

### 修改安全记录规则

确保每个任务只对创建它的用户课件

随着社交工程加入，我们需要任务的关注者也能来访问他们

让访问规则来处理负责人的用户

- 覆盖todo_app.todo_task_user_rule，新的域筛选器可以让负责、user_id或每个人都可见的任务，如果负责人没有设置（等于False），所有的任务关注者都可见

- 记录规则运行在user变量的上下文中，标识当前会话用户的记录，关注者是合作伙伴:user.partner_id

- group是to-many关系，代码4是附加相关记录的列表。代码6是将相关记录完全替换为一个新列表

- noupdate=‘1’,这个记录仅会写在安装操作上，模块升级时候将被忽略

  > -i  来重新安装模块

- domain_force字段修改为一个新值

security/todo_access_rules.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<odoo>
    <data noupdate="1">
        <record id="todo_app.todo_task_jper_user_rule" model="ir.rule">
            <field name="name">ToDo Task for owner and followers</field>
            <field name="model_id" ref="model_todo_task"/>
            <field name="groups" eval="[(4,ref('base.group_user'))]"/>
            <field name="domain_force">['|',('user_id','in',[user.id,False]),
                ('message_follower_ids','in',[user.partner_id.id])]
            </field>
        </record>
    </data>
</odoo>
```

```
'data': ['views/todo_task.xml', 'security/todo_access_rules.xml']
```

# 模块数据

- Odoo模块定义，比如用户接口、安全规则都是储存在特定数据库表中的数据记录
- XML、CSV文件将这些定义加载到数据库表中的一种方法
- 使用文件表示（序列化）数据，以便以后可以加载到数据库中
- 模块也有默认和演示数据，数据表示允许将其加入到我们的模块中

## 1 外部表示

external identifier(XML ID)可读的字符串标识符，唯一表示了特定记录

当升级一个模块时，它的数据文件将再次被加载到数据库中，我们需要检测已存在的数据，以便更新，而不是创建新的重复记录

数据记录必须能引用其他数据记录，外部标识提供了一种方法来引用相关记录

Odoo负责将外部标识符名称转换为分配给他们的实际数据库id

> Odoo保存一个表，表中由命名的外部标识符与其相应的数字数据库id之间的映射：ir.model.data模型

Complete ID：todo_app.action_todo_task

外部标识符只需要在一个模块内唯一

可以选择使用完整的标识符（可以从其他模块引用数据记录）、外部标识符名（简单）

> action_todo_task外部标识符映射到ir.actins.act_window模型中的特定记录ID
>
> Odoo自动导出一个额外的ID列，这是分配给每个记录的外部标识符
>
> 如果没有制定模块，会自动使用`_export_`替代实际模块名称的新功能
>
> 导入数据：id列留空，将为他们创建新的记录
>
> 只建议在导出导入相同的数据库时使用数据库id，通常使用外部标识符

## 2 模块数据

模块使用数据文件将其配置加载到数据库、默认数据和演示数据，使用CSV和XML文件完成

数据CSV文件：访问安全定义，加载到ir.mode.access模型，通常命名为ir.model.access.csv

## 3 演示数据

由于主为测试中使用模块和数据集提供使用示例

`__mainfest__.py`中demo属性，声明模块的演示数据

这些数据文件保存在todo_suer addon模块中作为data/todo.task.csv

由于该数据将由我们的模块拥有，我们应该编辑id值以删除表示服的`_export_`前缀

```
id,name,user_id/id,date_deadline
todo_task_a,"Install Odoo","base.user_root","2Ol5–Ol–3O" 
todo_task_b","Create dev database","base.user_root",""
```

## 4 XML数据文件

XML文件更加强大，并对加载过程提供了更多的控制

文件名不需要匹配要加载的模型

- `<odoo>`top元素
- 有几个与CSV数据行对应的`<record>`元素（等价于旧版本`<data>`）
- `<record>`元素有两个必须属性，model、id(记录的外部标识符)、`<field>`标记（用于每个字段的写入）
- 字段名中的斜杠符号/不可用

## 5 数据noupdate属性

noupdate=’1‘在模式创建时建立，升级时不进行任何操作

> -i 重新安装 -u 升级

## 6 XML中定义记录

### 设置字段值

`<record>`定义过了一个数据记录，并包含每个字段上设置值的`<field>`元素

field元素的name属性表示必要的写入字段

日期：YYYY-mm-dd 、  YYYY-mm-dd  HH:MM:SS

布尔字段: 非空会转换为True，0会转换为False

### 使用表达式设置值

- eval

- time,datetime,timedalte,relativedalta

  ```
  <field name="date_deadline"
  eval="(datetime.now() + timedelta(–l)).strftime('%Y–%m–%d')" />
  ```

- ref   用于外部标识符转换成相应的数据库id，可用于为关系字段设置值

  ```
  <field name="user_id" eval="ref('base.group_user')" />
  ```

  one-to-many和many-to-many的字段，需要一个相关id列表，因此需要不同的语法

  ```
  <field name="tag_ids" 
  	eval="[(6,0,
  		[ref('vehicle_tag_leasing'), 
  		ref('fleet.vehicle_tag_compact'), 
  		ref('fleet.vehicle_tag_senior')]
  )]" />	
  ```

> (0, _ ,{'field':value}) 创建一个新的记录并链接到这个记录
>
> (1,id,{'field':value}) 更新已链接的记录上的值
>
> (3,id, _ ) 取消链接并删除相关记录
>
> (4,id, _ ) 链接一个已经存在的记录
>
> (5, _ , _ ) 取消链接，但不会删除所有链接的记录
>
> (6, _ , [ids] ) 用提供的列表提出按链接记录的列表

下划线符号表示无关的值，通常填0或False

### 常用的模型的快捷方式

`<act_window>` 窗口操作模型，ir.actions.act_window

`<menuitem>` 菜单项的模型，ir.ui.menu

`<report>` 报告操作模型，ir.actions.report.xml

`<template>` 用于储存在模型ir.ui.view中的QWeb模板

`<url>` RUL操作模型ir.actions.act_url

## 7 XML数据文件中的其他操作

### 删除记录

使用搜索域来查找并删除

```
<delete model='ir.rule' search=''[('id','=',ref('todo_app.todo_task_user_rule'))]/>
```

删除特定ID可以

```
<delete model='ir.rule' id='todo_app.todo_task_user_rule'/>
```

### 触发功能和工作流

XML文件还可以通过`<function>`元素在其加载过程中执行方法

可以用来设置演示和测试数据

```
<function 
	model="crm.lead" 
	name="action_set_lost"
	eval="[ref('crm_case_7'), ref('crm_case_9')
	, ref('crm_case_ll'), ref('crm_case_l2')]
	, ('install_mode': True}" />
```

> 调用了crm.lead模型的action_set_lost方法，通过eval属性传递了两个参数

第一个是要使用的id列表，接下来是是要使用的上下文

`<workflow>`元素触发工作流

如：工作流可以更改销售订单的状态，或者将其转换为发票

```
<workflow model="sale.order" 
	ref="sale_order_4" 
	__action="orderconfirm" />
```

ref表示了我们正在执行的工作流实例，action是发送到这个工作流实例的信号

# 模型--构建应用程序数据

## 将应用程序特性组织成模块

以模块为导向的开发模式，大型应用程序可以分成更小的功能，足够丰富，可独立运行

通过附加addon模块改进我们的To-Do应用程序

## 引入todo_ui模块

- 每个任务都有一个阶段，每个阶段都有很多任务
- 每个任务可以由很多标记，每个标记可以附加到许多任务

> 任务具有与多个阶段的many-to-one关系，以及与标签many-to-many关系
>
> 阶段与任务和标记之间的many-to-many关系

我们将从建新的todo_ui模块开始，添加任务阶段和待办事项标签模型

```
{
    'name': "User interface improvements to the To-Do app",
    'description': 'User friendly features.',
    'author': "mark",
        'depends': ['todo_user'],
} 
```

## 创建模型

改进用户界面，包括看板，把应用程序带到下一个层次