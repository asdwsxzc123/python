userList = []
def menu():
    print('='*50)
    print('1. 添加用户')
    print('2. 删除用户')
    print('3. 更新用户')
    print('4. 查询用户信息')
    print('5. 查询所有用户信息')
    print('6. 保存用户信息')
    print('7. 退出系统')


def add_user_info():
    name = input('请输入姓名:')
    age = int(input('请输入年龄:'))
    obj = {
        'name': name,
        'age': age
    }
    global userList
    userList.append(obj)
    print('录入成功')


def find_user():
    global userList
    name = input('请输入姓名:')
    for temp in userList:
        if temp['name'] == name:
            print('姓名\t年龄')
            print('%s\t%d' % (temp['name'], temp['age']))
        else:
            print('查无此人')


def find_all_user():
    print('姓名\t年龄')
    global userList
    for temp in userList:
        print('%s\t%d' % (temp['name'], temp['age']))


def save_2_file():
    global userList
    f = open('./file/backup.data', 'w')

    f.write(str(userList))
    f.close()
    print('保存成功')

def get_file_data():
    global userList
    try:
        f = open('./file/backup.data', 'r')
        content = f.read()
        f.close()
        userList = eval(content)
        print(content)
    except Exception:
        pass

def main():
    menu()
    # 加载数据
    get_file_data()
    while True:
        num = int(input('请输入操作序号:'))
        if num == 1:
            add_user_info()
        elif num == 2:
            pass
        elif num == 3:
            pass
        elif num == 4:
            find_user()
        elif num == 5:
            find_all_user()
        elif num == 6:
            save_2_file()
        else:
            break


if __name__ == '__main__':
    main()
