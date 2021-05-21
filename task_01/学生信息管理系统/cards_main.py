# -*- coding: utf-8 -*-
"""
作者：XGM
日期：2021年05月18日23时52分00秒
"""
import cards_tools
while True:

    # 显示功能菜单
    cards_tools.show_menu()

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【 %s 】"%action_str)

    # 1，2，3对名片进行操作
    if action_str in ['1','2','3']:

        # 新增学生及其信息
        if action_str == '1':
            cards_tools.new_card()
        # 显示所有学生信息
        elif action_str == '2':
            cards_tools.show_all()
        # 查询某个学生
        elif action_str == '3':
            cards_tools.search_card()

    # 退出系统
    elif action_str == '0':
        print("欢迎再次使用【学生管理系统】")
        break

    # 其他输入时提示用户重新输入
    else:
        print("您的输入有误，请重新输入")