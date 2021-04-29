student_list = ["1","2","3","4"]
flag = 1
# 运行时显示操作界面
def show():
    print("1代表添加学生")
    print("2代表删除学生")
    print("3代表查询某个学生")
    print("4代表修改某个学生")
    print("5代表显示所有学生信息")
    print("6代表退出")
    print("请输入对应的指令:",end=" ")

# 主函数
while flag:
    show()
    cmd = input()
    if cmd == "1":
        print("请输入要添加的学生姓名:",end=" ")
        name = input()
        student_list.append(name)
    elif cmd == "2":
        print("请输入要删除的学生序号:",end=" ")
        num = input()
        student_list.__delitem__(int(num))
    elif cmd =="3":
        print("请输入要查询的学生序号:",end=" ")
        num = input()
        print("该学生是:",student_list[int(num)])
    elif cmd == "4":
        print("请输入要修改的学生序号:",end=" ")
        num = input()
        print("请输入新的学生姓名:", end=" ")
        name = input()
        student_list[int(num)] = name
    elif cmd == "5":
        for i_num in student_list:
            print(i_num)
    else:
        print("退出系统")
        flag = 0

