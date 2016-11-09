# 项目名及简介
* 此项目是在[appium](https://github.com/appium/appium)和[Selenium](https://github.com/SeleniumHQ/selenium)开源工具封装而成的自动化app和web测试工具

# 功能
* 都是基于python3
* 都是基于webdriver，大部分代码都可以通用，只是配置文件不一样
* APP监控了常用的men,cpu,fps
* 数据维护用的YMAL
* 邮件发送excel的测试报告

# 用法

**下载项目:**

```
git clone git@github.com:284772894/appiumn_auto.git
```

**配置ini**

```
[DEFAULT]
selenium_appium=appium
[appium]
devices=DU2TAN15AJ049163
Remote=127.0.0.1
appiumjs=node D:\\app\Appium\\node_modules\\appium\\bin\\appium.js
port=4723
[selenium]
selenium_jar = java -jar D:\\app\\appium_study\\img\\selenium-server-standalone-3.0.1.jar
sel_remote=http://127.0.0.1:4444/wd/hub
open_url=http://182.254.228.211:9000/index.php/Admin/index/login.html
```

**配置用例ymal**

* [case的api](mark.md)

```
--- 
- 
  element_info: cn.ibona.t1_beta:id/start_button
  find_type: by_id
  operate_type: click
  test_id: 1002
  test_intr: 登陆
- 
  element_info: cn.ibona.t1_beta:id/passwordEditText
  find_type: by_id
  operate_type: send_keys
  test_id: 1002
  text: 111111
- 
  element_info: cn.ibona.t1_beta:id/phoneNumberEditText
  find_type: by_id
  operate_type: send_keys
  text: 18576759587
- 
  element_info: cn.ibona.t1_beta:id/loginButton
  find_type: by_id
  operate_type: click
- 
  element_info: cn.ibona.t1_beta:id/toolbar
  find_type: by_id

```



**命名行运行:**

```
pyhton testRunner/runner.py
```

# 使用截图

* 运行方式

![run.gif](img/run.gif "run.gif")

* APP运行情况

![app.gif](img/app.gif "app.gif")

* 结果展示

![testEmail.png](img/testEmail.png "testEmail.png")

![1.png](img/1.png "1.png")

![2.png](img/2.png "2.png")


# 其他
* 更多信息查看我的[更新日志](channel_log.md)






