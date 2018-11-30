#!/usr/bin/env python
# -*- conding:utf-8 -*-

def login():
    pass

def register():
    pass

def find_pwd():
    pass

def execute():
    while True:
        print('欢迎登陆权限管理系统: 1:登陆 2:注册 3:找回密码;\n')
        dic = {
            '1': login,
            '2': register,
            '3': find_pwd,
            }
        choice = input('请输入选项: ')
        if choice not in dic.keys():
            print('选项输入错误')
            continue

        func = dic[choice]

        result = func()

        if result:
            chocie_menu()
    
