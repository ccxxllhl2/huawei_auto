class App:
    def __init__(self, sysname):
        print(f"系统{sysname}已经开始运行了！")
        self.db = []

    def register(self):
        print("***开始账号注册***")
        username = input("请输入您的用户名: ")
        password = input("请输入您的密码：")
        while True:
            email = input("请输入你的邮箱地址：")
            if '@' in email:
                break #邮件格式正确
            else:
                print("请输入正确的邮件格式")
        while True:
            age = input("请输入您的年龄：")
            if age.isnumeric():
                break #年龄格式正确
            else:
                print("请输入正确的年龄格式")
        info_dict = {'username': username,
                     'password': password,
                     'email': email,
                     'age': age}
        self.db.append(info_dict)

    def login(self):
        print("***开始账号登录***")
        while True:
            username = input("请输入您的用户名: ")
            password = input("请输入您的密码：")
            user_list = [info['username'] for info in self.db]
            if username not in user_list:
                print('该账号不存在，请重新登录！')
                continue
            for info_dict in self.db:
                if info_dict['username'] == username:
                    if info_dict['password'] != password:
                        print("账号密码不正确，请重新登录")
                        continue
                    print("登录成功，您的信息如下：")
                    print(info_dict)
            break

app = App('YESLAB系统')
app.register()
app.login()

