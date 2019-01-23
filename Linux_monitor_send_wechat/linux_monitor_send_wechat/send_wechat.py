#! usr/bin/env python3

from wxpy import *

def who_to_send():
    who = str(input('Do you want to send massage to a wechat user or a wechat group?(u/g)'))
    usrinfo={}
    if who == 'u':
        nickname = str(input('Place input the nickname of the wechat user: '))
        sex = str(input('Place input the wechat user gender (MALE/FEMALE): '))
        city = str(input('Place input the city of wechat user (example:广州):'))
        if nickname == '' or city == '':
            print('Nickname and city can\'t be null!')
            return who_to_send()
        else :
            usrinfo.update(dict(who=who,nickname=nickname,sex=sex,city=city))
    elif who == 'g':
        groupname = str(input('Place input the groupname of the wechat group: '))
        if groupname == '':
            print('Groupname can\'t be null!')
            return who_to_send()
        else :
            usrinfo.update(dict(who=who,groupname=groupname))
    else :
        print('Place input u or g!')
        return who_to_send()
    return usrinfo

def send_massage(content):
    bot = Bot(console_qr=True, cache_path=True) # 扫码缓存登录

    sendto = who_to_send()

    if sendto['who'] == 'u': 
        # 查找单个微信用户
        if sendto['sex'] == '':
            data_user = bot.friends().search(sendto['nickname'],city=sendto['city'])[0]
        else:
            data_user = bot.friends().search(sendto['nickname'],sex=sendto['sex'],city=sendto['city'])[0]
        # 发送信息给查找到的用户
        data_user.send(content)
        print('Massage send to {}: OK!'.format(data_user))
        return 
    elif sendto['who'] == 'g':
        # 查找并发信息给单个微信群
        data_group = ensure_one(bot.groups().search(sendto['groupname']))
        data_group.send(content)
        print('Massage send to {}: OK!'.format(data_group))
        return

if __name__ == '__main__':
    send_massage('Hello,testing!')
