"""
print("hello world!")#字符串
print(2333)#整数
print(2.33)#小数
print(True)#布尔值
print(())#元祖
print([])#数组
print({})#字典



print("哈哈，23333,12.5")
print("哈哈"+"嘻嘻")#字符串的拼接
print("哈哈"*100)#打印100个哈哈
print((1+2*100-9.9)/2)#整数和小数不是同一种数据类型，但是可以放在一起用
print(2>3)#输出结果为false，布尔值一般用于判断中
a = "张三"#把张三这个值赋值给了a这个变量
print(a)
a = input("请输入：")#对于input来说，输入的都是字符串
b = input("请输入：")
print("input获取的内容：",a+b)



#数据格式的转换
print(type(2333))
c = type(2333)
print(c)
print(type(2333))#int
print(type(23.33))#float
print(type(True))#bool
print(type(()))#tuple
print(type([]))#list
print(type({}))#dict
a = int("2333")
print(type(a))
a = str(2333)
print(type(a))
a = float (input("请输入："))
b = float (input("请输入："))
print("input获取的内容：",a+b)
print(float(10))


#长度计算
a = "aaaa  nnnnn    nnnn   xxxx   xxx"
print(len(a))
"""

#通过代码获取两段内容，并计算他们的长度

a = "乌拉拉家族首领"
b = len(a)
c = "国庆也不乐"
d = len(c)
int(b)
int(d)
print(b+d)

#input需要使用
a = input("请输入：")
b = input("请输入：")
print("字数：",len(a)+len(b))
