# betterlife.python
=========================================================

## 快速搭建一个Web下载服务器
    - python -m SimpleHTTPServer 8890 #(py2) 直接在命令行运行
    - python3 -m http.server 8810 #(py3) 直接在命令行运行   

## 新手任务

- 路径: 根目录下

  :hi.py

      ```
      > python hi.py
      ```

## 运维命令行工具

- 路径: cmd

  :PyBB.py

      ```
      > python PyBB.py
        - (PyBB)> walk output2.txt
        - (PyBB)> find Tools
      ```

  :bbtools.py

      ```
      > python bbtools.py /Users/skygreen
      ```
      (命令行中运行)



## 常用工具

- 路径: tools

### 测试指定服务器是否正常运行，如无法访问返回502，会自动重启nginx并发邮件通知管理员

  - 包括发送邮件功能

  :maintain_work.py

      ```
      > python maintain_work.py
      ```

### 主要配合执行服务器上的定时任务

  :db_mysql_timer_bak.py

      ```
      > python db_mysql_timer_bak.py
      ```

### 数据库操作

  :db_handle.py

### 正则表达式

  :regex.py

### 文件处理

  :file.py

### 剪切板

  :clipboard.py
