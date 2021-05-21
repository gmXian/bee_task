# -*- coding: utf-8 -*-
"""
作者：XGM
日期：2021年05月18日23时52分33秒
"""
# 记录所有名片字典
card_list = []

def show_menu():
    """显示菜单"""
    print("*"*30)
    print(" "*2,"欢迎使用【学生管理系统】1.0版本")
    print(" "*4,"【1】 新增名片")
    print(" "*4,"【2】 显示全部")
    print(" "*4,"【3】 搜索名片")
    print(" "*4,"【0】 退出系统")
    print("*"*30)

def new_card():
    """新增名片"""
    print("-"*100)
    print("您正在使用【新增名片】功能")

    # 1.提示用户输入名片的详细信息
    stu_name = input("请输入姓名：")
    stu_num = input("请输入学号：")
    stu_class = input("请输入班级：")
    email = input("请输入邮箱：")
    s_ma = float(input("请输入高数成绩："))
    s_ph = float(input("请输入大物成绩："))
    s_en = float(input("请输入英语成绩"))

    # 2.使用用户输入的信息建立一个名片字典
    card_dict = {"name":stu_name,
                 "stu_num":stu_num,
                 "stu_class":stu_class,
                 "email":email,
                 "math":s_ma,
                 "physics":s_ph,
                 "English：":s_en,
                 "总分":s_ph+s_en+s_ma,
                 "平均分":(s_ph+s_en+s_ma)/3}

    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_dict)
    # 4.提示用户添加成功
    print("添加 %s 的信息成功"%stu_name)

def show_all():
    """显示所有名片"""
    print("-" * 100)
    print("您正在使用【显示所有学生信息】功能")
    # 判断是否存在学生信息记录，如果没有就提示用户并返回
    if len(card_list) == 0:
        print("当前并没有任何学生信息，请先添加")
        return

    # 打印表头
    for name in ['姓名','学号','班级','邮箱','math','physics','English','总分','平均分']:
        print(name,end='\t\t')
    print("")

    # 打印分割线
    print("="*100)

    # 遍历名片列表依次输出字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t%.1f\t\t%.1f\t\t%.1f\t\t%.1f\t\t%.1f"%(card_dict['name'],
                                                                              card_dict['stu_num'],
                                                                              card_dict['stu_class'],
                                                                              card_dict['email'],
                                                                              card_dict['math'],
                                                                              card_dict['physics'],
                                                                              card_dict['English'],
                                                                              card_dict['总分'],
                                                                              card_dict['平均分']))

    # 打印分割线
    print("="*100)

def search_card():
    """搜索学生"""
    print("-" * 100)
    print("您正在使用【搜索学生】功能")

    # 1.提示用户要搜索的姓名
    find_name = input("请输入要搜索的姓名：")

    # 2.遍历学生列表，查询要搜索的名字，如果没有找到，需要提示用户
    for card_dict in card_list:
        if card_dict['name'] == find_name:
            print("找到了")
            print("姓名\t\t学号\t\t班级\t\t邮箱\t\tmath\t\tphysics\t\tEnglsih\t\t总分\t\t平均分")
            print("="*150)
            print("%s\t\t%s\t\t%s\t\t%s\t\t%.1f\t\t%.1f\t\t%.1f\t\t%.1f\t\t%.1f" % (card_dict['name'],
                                                                                    card_dict['stu_num'],
                                                                                    card_dict['stu_class'],
                                                                                    card_dict['email'],
                                                                                    card_dict['math'],
                                                                                    card_dict['physics'],
                                                                                    card_dict['English'],
                                                                                    card_dict['总分'],
                                                                                    card_dict['平均分']))
            # 针对找到的学生记录执行修改和删除
            deal_card(card_dict)
            break
    else:
        print("抱歉，没找到%s"%(find_name))

def deal_card(find_dict):
    """对查找到的学生信息进行处理（修改/删除）
    :param find_dict:将查找到的名片传入
    """
    action_str = input("请选择要执行的操作："
                       "[1] 修改 [2] 删除 [0] 返回上级菜单")
    if action_str == '1':

        find_dict['name'] = input_card_info(find_dict['name'],"姓名：")
        find_dict['stu_num'] = input_card_info(find_dict['stu_num'],"学号：")
        find_dict['stu_class'] = input_card_info(find_dict['stu_class'],"班级：")
        find_dict['email'] = input_card_info(find_dict['email'],"邮箱：")
        find_dict['math'] = input_card_info(find_dict['math'],"math：")
        find_dict['physics'] = input_card_info(find_dict['physics'], "physics：")
        find_dict['English'] = input_card_info(find_dict['English'], "English：")
        find_dict["总分"] = find_dict['math']+find_dict['physics']+find_dict['English']
        find_dict["平均分"] = find_dict['平均分']/3
        print("修改学生信息成功")

    elif action_str == '2':
        card_list.remove(find_dict)
        print("删除学生信息成功")

def input_card_info(dict_value,tip_message):
    """ 输入学生信息
    :param dict_value:字典中原有的值
    :param tip_message:输入提示性文字
    :return:如果用户输入了内容直接返回结果，如果没有输入返回原有的值
    """
    # 1.提示用户输入内容：
    result_str = input(tip_message)
    # 2.针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str)>0:
        return result_str
    # 3.如果用户没有输入内容，返回字典中原有的值
    else:
        return dict_value