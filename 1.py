
'''a = 0
while a < 3:
    han = input('请输入han的数字：')
    if  han == '520520':
        print('密码正确')
        break
    else:
             print('密码不正确，请重新输入')
             a += 1'''

a=0
while a<3:
    pwd=input('请输入密码：')
    if pwd=='520520':
        print('密码正确')
        break
    else:
        print('密码错误')
        a+=1
else:
    print('对不起，三次输入错误，再见！')