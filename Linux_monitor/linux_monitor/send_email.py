import yagmail
import time

def send_contents(email_user,email_password,mail_host,content,recipients):

    # 链接邮箱服务器以及发件邮箱信息
    yag = yagmail.SMTP(user = email_user,
                       password = email_password,
                       host = mail_host)

    subtract = str(time.asctime())+' linux 系统监控信息'
    # 邮件内容
    contents = content
   

    # 收件邮箱地址、标题、内容
    yag.send(recipients,subtract,contents)
        

