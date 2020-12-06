import yagmail

# 1.这是一个测试发送邮件的示例程序
ya_obj = yagmail.SMTP(user="wy13708@163.com", password="CMZVHFZVRQWATMUS", host="smtp.163.com")
content = "你好"
ya_obj.send(to="2482432123@qq.com", subject="test", contents=content)
