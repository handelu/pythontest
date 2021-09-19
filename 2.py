
#实例1：qq登录

while True:
 qq = input('请输入QQ账号:')
 pwd = input('请输入QQ密码:')
 if qq=='278585794' and pwd=='520520taorong':
  print('登录成功')
  break
 else:
  print('你的账号或密码不正确，请重新输入')

#实例2：猜价格

while True:
 import random
 price=random.randint(1000,1005)
 print('今天猜的产品价格在【1000-1500】')
 guess=int(input())
 if guess>price:
  print('大了')
 elif guess<price:
  print('小了')
 else:
  print('恭喜！猜对了！')
 print('今天的价格是：',price)