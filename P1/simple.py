# 数组形式的数据结构（列表，元组，字典）
one_list = ['DeviceName', 'ManageIP', 'Location', 'Power', 'HA']

# 列表
## 列表特性：索引
base_info = one_list[0:3]
#print(base_info)

base_info[1] = 'ManageIPaddress'
#print(base_info)

## 列表特性：尾部添加新元素
one_list.append('CPU')
one_list.append('MEM')
#print(one_list)

# 字典
one_dict = {'DeviceName': 'CE12800',
            'ManageIP': '192.168.1.1',
            'Location': 'Beijing',
            'Power': 'Single',
            'HA': True}
## 字典特性：查询
#print(one_dict['ManageIP'])

## 字典特性：获取所有key
all_keys = list(one_dict.keys())
#print(all_keys)

## 字典特性：获取所有value
all_values = list(one_dict.values())
#print(all_values)

## 字典特性：字典解构
all_items = list(one_dict.items())
#print(all_items)
#print(all_items[1][1])

# 程序的基本输入与输出
## 命令行 输出是print，输入是input
username = input("请输入您的账号：")
password = input("请输入您的密码：")
print(f'您的用户名为{username}，密码是{password}')
