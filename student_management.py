1# -*- coding: utf-8 -*-
import json
import os
import time

def load_data():
    """加载所有数据文件"""
    try:
        with open('student.json', 'r', encoding='utf-8') as f:
            students = json.load(f)
        with open('teacher.json', 'r', encoding='utf-8') as f:
            teachers = json.load(f)
        with open('results.json', 'r', encoding='utf-8') as f:
            results = json.load(f)
        return students, teachers, results
    except FileNotFoundError:
        print("数据文件不存在，请确保所有数据文件已创建")
        return {}, {}, {}

def save_data(students, teachers, results):
    """保存所有数据"""
    with open('student.json', 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=4)
    with open('teacher.json', 'w', encoding='utf-8') as f:
        json.dump(teachers, f, ensure_ascii=False, indent=4)
    with open('results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

def student_login(students, results):
    """学生登录功能"""
    student_id = input("请输入学生证号：")
    
    if student_id in students:
        while True:
            print("\n=== 学生菜单 ===")
            print("1. 查询本人信息")
            print("2. 修改本人信息")
            print("3. 查询考试成绩")
            print("4. 退出登录")
            
            choice = input("\n请选择操作：")
            
            if choice == "1":
                print("\n个人信息：")
                for key, value in students[student_id].items():
                    if key != "password":
                        print(f"{key}: {value}")
            elif choice == "3":
                if student_id in results:
                    print("\n考试成绩：")
                    for subject, score in results[student_id].items():
                        print(f"{subject}: {score}")
                else:
                    print("暂无成绩记录")
            elif choice == "4":
                break
            else:
                print("功能开发中...")
    else:
        print("学号不存在！")

def view_student_info(students):
    """查看学生信息"""
    student_id = input("请输入要查询的学生学号：")
    if student_id in students:
        print("\n学生信息：")
        for key, value in students[student_id].items():
            print(f"{key}: {value}")
    else:
        print("该学号不存在！")

def modify_student_info(students):
    """修改学生信息"""
    student_id = input("请输入要修改的学生学号：")
    if student_id in students:
        print("\n当前学生信息：")
        for key, value in students[student_id].items():
            print(f"{key}: {value}")
        
        print("\n请输入新的信息：")
        students[student_id]["name"] = input("姓名：")
        students[student_id]["age"] = int(input("年龄："))
        students[student_id]["gender"] = input("性别：")
        students[student_id]["grade"] = input("年级：")
        students[student_id]["class"] = input("班级：")
        return True
    else:
        print("该学号不存在！")
        return False

def add_student(students):
    """添加学生信息"""
    student_id = input("请输入新学生学号：")
    if student_id in students:
        print("该学号已存在！")
        return False
    
    students[student_id] = {
        "name": input("姓名："),
        "age": int(input("年龄：")),
        "gender": input("性别："),
        "grade": input("年级："),
        "class": input("班级：")
    }
    return True

def delete_student(students, results):
    """删除学生信息"""
    student_id = input("请输入要删除的学生学号：")
    if student_id in students:
        del students[student_id]
        if student_id in results:
            del results[student_id]
        print("删除成功！")
        return True
    else:
        print("该学号不存在！")
        return False

def manage_scores(results):
    """管理成绩"""
    while True:
        print("\n=== 成绩管理 ===")
        print("1. 查询成绩")
        print("2. 录入成绩")
        print("3. 修改成绩")
        print("4. 删除成绩")
        print("5. 返回上级菜单")
        
        choice = input("\n请选择操作：")
        
        if choice == "1":
            student_id = input("请输入学号：")
            if student_id in results:
                print("\n成绩信息：")
                for subject, score in results[student_id].items():
                    print(f"{subject}: {score}")
            else:
                print("未找到该学生的成绩记录！")
                
        elif choice == "2" or choice == "3":
            student_id = input("请输入学号：")
            subject = input("请输入科目：")
            try:
                score = float(input("请输入分数："))
                if student_id not in results:
                    results[student_id] = {}
                results[student_id][subject] = score
                print("成绩录入成功！")
            except ValueError:
                print("分数输入无效！")
                
        elif choice == "4":
            student_id = input("请输入学号：")
            if student_id in results:
                subject = input("请输入要删除的科目：")
                if subject in results[student_id]:
                    del results[student_id][subject]
                    print("成绩删除成功！")
                else:
                    print("未找到该科目成绩！")
            else:
                print("未找到该学生的成绩记录！")
                
        elif choice == "5":
            break

def teacher_login(teachers, students, results):
    """教师登录功能"""
    teacher_id = input("请输入教师工号：")
    
    if teacher_id in teachers:
        while True:
            print("\n=== 教师菜单 ===")
            print("1. 查询学生信息")
            print("2. 管理考试成绩")
            print("3. 退出登录")
            
            choice = input("\n请选择操作：")
            
            if choice == "1":
                view_student_info(students)
            elif choice == "2":
                manage_scores(results)
            elif choice == "3":
                break
    else:
        print("教师工号不存在！")

def manage_teachers(teachers):
    """管理教师信息"""
    while True:
        print("\n=== 教师管理 ===")
        print("1. 查询教师信息")
        print("2. 添加教师信息")
        print("3. 修改教师信息")
        print("4. 删除教师信息")
        print("5. 返回上级菜单")
        
        choice = input("\n请选择操作：")
        
        if choice == "1":
            teacher_id = input("请输入教师工号：")
            if teacher_id in teachers:
                print("\n教师信息：")
                for key, value in teachers[teacher_id].items():
                    print(f"{key}: {value}")
            else:
                print("该工号不存在！")
                
        elif choice == "2":
            teacher_id = input("请输入新教师工号：")
            if teacher_id not in teachers:
                teachers[teacher_id] = {
                    "name": input("姓名："),
                    "gender": input("性别："),
                    "subject": input("任教科目：")
                }
                print("教师信息添加成功！")
            else:
                print("该工号已存在！")
                
        elif choice == "3":
            teacher_id = input("请输入要修改的教师工号：")
            if teacher_id in teachers:
                teachers[teacher_id]["name"] = input("姓名：")
                teachers[teacher_id]["gender"] = input("性别：")
                teachers[teacher_id]["subject"] = input("任教科目：")
                print("教师信息修改成功！")
            else:
                print("该工号不存在！")
                
        elif choice == "4":
            teacher_id = input("请输入要删除的教师工号：")
            if teacher_id in teachers:
                del teachers[teacher_id]
                print("教师信息删除成功！")
            else:
                print("该工号不存在！")
                
        elif choice == "5":
            break

def load_admin_password():
    """加载管理员密码"""
    try:
        with open('admin.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # 如果文件不存在，创建默认密码文件
        admin_data = {"password": "123", "is_first_login": True}
        with open('admin.json', 'w', encoding='utf-8') as f:
            json.dump(admin_data, f, indent=4)
        return admin_data

def save_admin_password(admin_data):
    """保存管理员密码"""
    with open('admin.json', 'w', encoding='utf-8') as f:
        json.dump(admin_data, f, indent=4)

def change_admin_password(admin_data):
    """更改管理员密码"""
    if not admin_data["is_first_login"]:
        old_password = input("请输入原密码：")
        if old_password != admin_data["password"]:
            print("原密码错误！")
            return False
    
    new_password = input("请输入新密码：")
    confirm_password = input("请确认新密码：")
    
    if new_password == confirm_password:
        admin_data["password"] = new_password
        admin_data["is_first_login"] = False
        save_admin_password(admin_data)
        print("密码修改成功！")
        return True
    else:
        print("两次输入的密码不一致！")
        return False

def admin_login(students, teachers, results):
    """管理员登录功能"""
    admin_data = load_admin_password()
    login_attempts = 0
    last_attempt_time = 0
    
    while login_attempts < 5:  # 最多允许5次尝试
        current_time = time.time()
        if login_attempts > 0 and current_time - last_attempt_time < 30:  # 失败后需要等待30秒
            wait_time = int(30 - (current_time - last_attempt_time))
            print(f"请等待{wait_time}秒后再试...")
            time.sleep(1)
            continue
            
        password = input("请输入管理员密码：")
        
        if password == admin_data["password"]:
            if admin_data["is_first_login"]:
                print("\n首次登录，请修改默认密码！")
                if not change_admin_password(admin_data):
                    return
            
            while True:
                print("\n=== 管理员菜单 ===")
                print("1. 管理教师信息")
                print("2. 管理学生信息")
                print("3. 管理考试成绩")
                print("4. 修改管理员密码")
                print("5. 退出登录")
                
                choice = input("\n请选择操作：")
                
                if choice == "1":
                    manage_teachers(teachers)
                elif choice == "2":
                    while True:
                        print("\n=== 学生管理 ===")
                        print("1. 查询学生信息")
                        print("2. 添加学生信息")
                        print("3. 修改学生信息")
                        print("4. 删除学生信息")
                        print("5. 返回上级菜单")
                        
                        sub_choice = input("\n请选择操作：")
                        if sub_choice == "1":
                            view_student_info(students)
                        elif sub_choice == "2":
                            if add_student(students):
                                save_data(students, teachers, results)
                        elif sub_choice == "3":
                            if modify_student_info(students):
                                save_data(students, teachers, results)
                        elif sub_choice == "4":
                            if delete_student(students, results):
                                save_data(students, teachers, results)
                        elif sub_choice == "5":
                            break
                elif choice == "3":
                    manage_scores(results)
                elif choice == "4":
                    change_admin_password(admin_data)
                elif choice == "5":
                    break
                
                # 保存所有更改
                save_data(students, teachers, results)
            break
        else:
            login_attempts += 1
            last_attempt_time = current_time
            remaining_attempts = 5 - login_attempts
            if remaining_attempts > 0:
                print(f"密码错误！还剩{remaining_attempts}次尝试机会")
            else:
                print("尝试次数过多，请稍后再试！")

def main():
    """主程序"""
    # 初始化数据
    students, teachers, results = load_data()
    
    while True:
        print("\n=== 学生管理系统 ===")
        print("1. 学生登录")
        print("2. 教师登录")
        print("3. 管理登录")
        print("4. 退出系统")
        
        choice = input("\n请选择用户权限：")
        
        if choice == "1":
            student_login(students, results)
        elif choice == "2":
            teacher_login(teachers, students, results)
        elif choice == "3":
            admin_login(students, teachers, results)
        elif choice == "4":
            print("感谢使用！再见！")
            break
        else:
            print("无效的选择，请重试！")

if __name__ == "__main__":
    main() 