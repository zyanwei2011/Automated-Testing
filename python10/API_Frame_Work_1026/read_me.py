# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 20:42
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : read_me.py
#完成接口的自动化
#接口参数化  单元测试  ddt
#logging email
#jenkins

#数据与代码分离-->提醒老师

#第一阶段：
#目标接口：http://119.23.241.154:8080/futureloan/mvc/api/member/register
#mobilephone pwd regname
#1：完成单一接口的请求:
#1) requests 模块完成 http接口的请求  封装成类
#2)加异常处理 try...except

#2：完成测试数据和测试结果的批量操作以及批量写回测试结果
#1）:测试数据是放在Excel里面，利用openpyxl去读数据
#2)读取数据之后要存储，用什么类型的数据去存储比较合适呢？---字典
#3)写回数据 实际结果 以及测试结论
#4)电话号码 不能自己去自动加吗？

#问题：什么时候才去做自动化？回归 功能稳定的时候
#错误码对照表：不会轻易变动

#1）全部对照--不现实 2）怎么去选择判断成功的标准呢？ code msg


#第二阶段：
#1：怎么解决手机号码自加的问题：
#1）利用随机数 写一个函数 随机生成一个手机号码
#2）利用时间戳截取11位作为手机号码
#3）在之前的电话号码上面+1-->手机号码存在Excel里面--->读取电话号码--->传递参数
#>取完了之后+1--->回写到Excel里面去
#2：集成单元测试、ddt 生成测试报告  写回测试结果
#3：配置文件的新增：测试用例可配置
#4：数据与代码分离:
# 测试数据
# 测试结果：测试报告 日志
#公共代码
#配置文件

#第三阶段：（2节课）
# 1：项目路径的配置---绝对路径--自己去考虑？---推荐使用绝对路径
#2：如果在一次测试过程中，需要用到多个不一样未使用过的手机号，怎么去做优化--自己去考虑？
#3：接口路径问题怎么解决？之前是写死在test_api.py
#4:写多条注册用例 以及加入登录用例 充值 用例集成cookie 怎么跑通
#5:加入日志 ---已经加入成功，但是呢：日志没有写入进去。---跟你设置的级别有关系
#6:发送邮件-->sendEmail-->掌握怎么用 就OK  重点去拓展之后的Jenkins

#第四阶段：（2节课）
#1：加入充值、投资 等用例（另外一条线是去自行准备标Id)
#2:检查数据库的结果与期望是否一致(new)
#3:用例之间有关联性强一点比较好 还是关联性弱一点比较好

#第五阶段：10-26
#1：如果要同时跑多个模块的话 怎么去写代码？
#A： 我可以写多个test_api模块
#B： 改变我们的配置文件
#2:利用反射来完成的数据的读取和存储 loan_id  COOKIES
#疑问:如果你的某个一个用例 需要用到上一个请求或者是前面某一个请求的响应结果
#A：统统存到Excel
#B:全局变量
#C：反射
# cookies，每个用户登录之后产生的cookies
# 都可以给之后的别的用户的充值提现投标使用，
# 这样是没有问题的吗？只要有cookies就行了吗，
# 随便一个cookies吗
#2：请自行补充好投资接口的用例

#第六阶段：（2节课）
#1：jenkins集成
#3：webservice项目实战安排：（请参照老师的博客关于webservice项目实战的的步骤去做、
#写好测试计划以及解决问题的过程步骤和体会以及最后的代码提交到课堂派）
#讲解时间：一周后的周天会进行讲解


