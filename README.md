 # Inerface 接口测试
 
 ## 入口文件：
 * RunnerAll.py
 
 ## unit 目录：
  * abs_api.py 构建用例
  * base_api.py request 请求基本封装
  * base_path.py 常用地址定义
  * common.py   文件读取
  * db_common.py 数据库连接
  * logger.py   日志文件
      * 调用：
      ```
      from unit.logger import Logger
      
      mylogger = Logger("loggerName").get_log()
      
      mylogger.info("输出一个日志")  

       ```
  * report.py  将测试结果写入到excel
 
# testcase 
 * 作用： 存放用例目录
 * 注意： 所有用例文件必须是以.yaml 结尾的文件，否则检查不到用例
 
 ## YAML文件
   * [yaml文件基础语法](https://www.jianshu.com/p/97222440cd08)
   * 文件内容格式：
      * base_url: http://news.baidu.com   # 设置该文件的全局基础url
      * set_monitor: 该字段为可变字段，用于区别接口
      * url_path: /guonei  请求地址
      * headers: {"Content-Type":"application/json"}  请求头 必须以字典的形式传入
      * method: get  请求方式
      * case: 真正的用例从这里开始,每个用例必须以列表的形式展示
          
          ````
           - params1: 第一参数
             params2: 第二参数
             check: 检查点（目前只支持code 校验，要看你们的返回结果具体修改）
                - code: 200
             set_up: 初始化操作主要是sql语句
             tear_down:
               - delete: delete from im_group where id = (select committeeGroupId from bt_course_class_info where id = 3694)
                （什么操作类型要写，select，delete，update,inster）
           
           - params1: 第一参数
             params2: 第二参数
             check: 检查点（目前只支持code 校验，要看你们的返回结果具体修改）
                - code: 200
             set_up: 初始化操作主要是sql语句
             tear_down:
               - delete: delete from im_group where id = (select committeeGroupId from bt_course_class_info where id = 3694)
                （什么操作类型要写，select，delete，update,inster）
            (以上就是一个接口的两条用例)
           ````
 # 未实行功能
 * 登录校验
 * 签名校验
 * 如果有需要可以实行，需要新增方法
 
# 依赖库
```
pip install requests
pip install PyMySQL
pip install XlsWriter 
pip install pyyaml
pip install xlrd

```



