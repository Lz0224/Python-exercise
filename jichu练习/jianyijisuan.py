#!/usr/bin/env python
#coding=utf-8

print ("hello, 你好！")
number1 = int(raw_input("请输入数字1 :"))
fuhao = raw_input("请选择 + - * / :")


if   fuhao == '+':
    number2 = int(raw_input("请输入数字2 :"))
elif fuhao == '-':
    number2 = int(raw_input("请输入数字2 :"))
elif fuhao == '*':
    number2 = int(raw_input("请输入数字2 :"))
elif fuhao == '/':
    number2 = int(raw_input("请输入数字2 :"))
else :
     print("请重新输入,并正确选择 + - * / ：")


if fuhao == '+':
    print(number1),
    print('+' ),
    print(number2),
    print('='),
    print(number1+number2)
elif fuhao == '-':
    print(number1),
    print('-'),
    print(number2),
    print('=')   ,
    print(number1-number2)
elif fuhao == '*':
    print(number1),
    print('*'),
    print(number2),
    print('='),
    print(number1*number2)
elif fuhao == '/':
    print(number1),
    print('/'),
    print(number2),
    print('='),
    print(umber1/number2)
else  :
    print(' ')
