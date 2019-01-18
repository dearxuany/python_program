#! /usr/bin/env python3

import monitor_data_collect
import send_email
import data_format

def main():
    email_user = 'sharonyunxuan@sina.com'  # 发件邮箱地址
    email_password ='****' # 发件邮箱密码
    mail_host = 'smtp.sina.com'  # 邮件服务器
    recipients = ['sharonyunxuan@sina.com']  # 收件邮箱地址
    
    # 以下两句不需要设格式的时候用
    # content = str(monitor_data_collect.collect_monitor_data())
    # send_email.send_contents(email_user,email_password,mail_host,content,recipients)

    data = monitor_data_collect.collect_monitor_data()
    content = data_format.render('monitor.html',**data)
    send_email.send_contents(email_user,email_password,mail_host,content,recipients)


if __name__ == '__main__':
   main()

