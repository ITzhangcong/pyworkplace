#print('中文')
#输入程序
#name=input()  
#print('hello',name)
#带有提示的输入
# name=input('please enter your name:')  
# print('hello',name)
#动态指向，结果还是ABC
# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)
#转义字符
# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
# print(n,f,s1,s2,s3,s4)
#以Unicode表示的str通过encode()方法可以编码为指定的bytes
#'ABC'.encode('ascii')
#'中文'.encode('utf-8')
# '中文'.encode('ascii')提示：超出范围
#在Python中，采用的格式化方式和C语言是一致的
#'Hi, %s, you have $%d.' % ('Michael', 1000000)
#'%2d-%02d' % (3, 1)
# '%.2f' % 3.1415926
#递归函数
# def fact(n):
    # if n==1:
        # return 1
    # return n*fact(n-1)
#汉诺塔
# def move(n, a, b, c):
    # if n == 1:
        # print('move', a, '-->', c)
        # return
    # move(n-1, a, c, b)
    # print('move', a, '-->', c)
    # move(n-1, b, a, c)
#使用内建的isinstance函数判断变量是否是一个字符串
L = ['Hello', 'World', 18, 'Apple', None]
[s.lower() for s in L if isinstance(s,str)==True]

