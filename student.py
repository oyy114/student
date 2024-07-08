import json
import time
str_info = """
**************************************************
欢迎使用【学生信息管理系统】V1.98 (测试版)
本项目已开源在github 地址: https://github.com/oyy114/student 欢迎star
请选择你想要进行的操作
1. 新建学生信息
2. 显示全部信息
3. 查询学生信息
4. 删除学生信息
5. 修改学生信息

0. 退出系统

**************************************************
"""

# 读取文件
with open('students.json', mode='r', encoding='utf-8') as f:
    students_str = f.read()

students = json.loads(students_str)

def wite_file(students):
    with open('students.json', mode='w', encoding='utf-8') as f:
        f.write(json.dumps(students, indent=2))

while True:
    # 1. 程序启动，显示信息管理系统欢迎界面，并显示功能菜单 (print)
    print(str_info)
    # 2.用户用数字选择不同的功能(input)
    action = input('请选择你要进行的操作(输入数字):')
    if action == '1':
        print('1. 新建学生信息')
        name = input('请输入学生的姓名:')
        name = name.strip()
        name = str(name)
        chinese = input('请输入学生的语文成绩:')
        math = input('请输入学生的数学成绩:')
        english = input('请输入学生的英语成绩:')

        total = str(float(chinese) + float(math) + float(english))
        # 新的学生
        stu = {'name': name, 'chinese': chinese,
               'math': math, 'english': english, 'total': total}
        students.append(stu)
        wite_file(students)
        print('学生信息添加成功!')
        time.sleep(3)
    elif action == '2':
        print('2. 显示全部信息')
        print('姓名\t\t语文\t    数学\t\t英语\t    总分')

        for stu in students:
            print(f'{stu["name"]}\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')
            time.sleep(0.5)
        time.sleep(3)

    elif action == '3':
        print('3. 查询学生信息')
        name = input('请输入你要查询学生的姓名:')

        # 先遍历所有学生
        for stu in students:
            # 如果满足条件, 就是查询到了
            if name == stu['name']:
                print('姓名\t\t语文\t    数学\t\t英语\t    总分')
                print(
                    f'{stu["name"]}\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')
                # 一旦查询到了就停止查询
                time.sleep(3)
                break
        else:
            # 没找到
            print('该学生不存在, 请检查名字是否输入正确!')
            time.sleep(3)

    elif action == '4':
        print('4. 删除学生信息')
        name = input('请输入你要删除学生的姓名:')

        # 先遍历所有学生
        for stu in students:
            # 找到学生
            if name == stu['name']:
                # 删除学生
                students.remove(stu)
                wite_file(students)
                print('学生信息删除成功!')
                time.sleep(3)
                break

        else:
            # 没找到
            print('该学生不存在, 请检查名字是否输入正确!')
            time.sleep(3)
    elif action == '5':
        print('5. 修改学生信息')
        name = input('请输入你要修改学生的姓名:')
        chinese = input('请输入学生的语文成绩:')
        math = input('请输入学生的数学成绩:')
        english = input('请输入学生的英语成绩:')
        # 先遍历所有学生
        for student in students:
            if student['name'] == name:
                student['chinese'] = str(chinese)
                student['math'] = str(math)
                student['english'] = str(english)
                student['total'] = str(int(math) + int(english) + int(chinese))
                break
        else:
            print(f"未找到名为{name}的学生")
            time.sleep(3)
            break

        # 写入更新后的JSON文件
        with open("students.json", 'w', encoding='utf-8') as f:
            json.dump(students, f, ensure_ascii=False, indent=2)
        print(f"学生{name}的成绩已成功更新")
        time.sleep(3)
    elif action == '0':
        print('即将退出系统...')
        time.sleep(1)
        print('感谢使用!')
        time.sleep(1)
        print('10%')
        time.sleep(1)
        print('50%')
        time.sleep(1)
        print('100%')
        time.sleep(1)
        print('程序已关闭!')
        time.sleep(1)
        break
    else:
        print('请输入正确的选项!')
