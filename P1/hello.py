# 开始编写自己的代码了！

# 四种基本的单体数据类型
one_int = 11
one_float = -15.1
one_str = 'Huawei Datacom IE 是世界上最好的网络认证！'
one_bool = True

## 变量被定义后是有类型的
#print(type(one_str))

## 字符串特性：字符串拼接
example_1 = "1000"
result_1 = example_1 + "100"
#print(result_1)

## 字符串特性：字符串索引
#print(one_str[7:17])
#print(one_str[-12:])

## 字符串特性：格式化输出
vendor = 'Cisco'
device = 'CSR1000V'
ip = '1.1.1.2'
#print(f"我们购买了{vendor}产品，是设备{device}，给它配置了管理IP是{ip}")
#print("我们购买了{}产品，是设备{}，给它配置了管理IP是{}".format(vendor, device, ip))

# 字符串特性：字符串分割(字符串->列表)
one_list = one_str.split()[1:3]

# 字符串特性：字符串组合(列表->字符串)
new_str = " ".join(one_list)
print(new_str)