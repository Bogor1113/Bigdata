# ---------------------------------打印---------------------------------
print(3+2,3-2 ,3*2,3/2,3//2,3%2,3**2)  #逗号不换行打印
import math

print(math.sqrt(3))

# ---------------------------------变量---------------------------------
a = 3
b = 2
print(a+b)

#  ctrl+/  代码块注释
# ---------------------------------输入---------------------------------
# name = input("请输入你的名字：")
# print(name)

# ---------------------------------逻辑运算  and  or  not---------------------------------
print(1<2 and  2>3)
print(1<2 or  2>3)
print(not  1<2)

# ---------------------------------数据类型转换 --------------------------------- 
x=int('123')
print(x)
x=str(123)
print(x)
x=float(1)
print(x)

print(int('123')+100)
print('123'+str(100))

姓名='laowang'
print(姓名)

# 输入要转换
# num=float(input('请输入一个数字：'))
# print(num+100)

# ---------------------------------条件判断  ---------------------------------
# year=int(input('请输入年份：'))
# if  1900<=year<=2500: # 嵌套判断
#     if year%4 == 0   and year%100!=0  or  year%400==0:  # 冒号结尾
#         print(year,'闰年')  
#     else:  #结尾
#         print(year,'平年')
# else:
#     print('输入年份范围错误')

# 多分支判断
# score=float(input('请输入你的分数：'))
# if 0<=score<=100:
#     if  score<60:
#         print('D')
#     elif  score==60:  #多分支写法
#         print('C')
#     elif  60<score<=90:
#         print('B')
#     else:
#         print('A')
# else:
#     print('百分制，不要瞎输')

# ---------------------------------循环for---------------------------------
#    范围不包含最后一个数字
for  i in range(10):   # 结尾冒号
    print('hello',i)

print('-'*100)
# for区间
for i  in range(10,20):
    print('hello',i)

print('-'*100)
# for 步长跳跃
for i in range(10,20,2):
    print('hello',i)

print('-'*100)
# for反向
for i in range(20,10,-1):
    print('hello',i)

# 双层for
for i in range(4):
    for j in range(3): # 一定要等里面的内循环做完，才能继续下一次的外循环
        print(i,j)

# 乘法表 
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j}',end='\t')
    print('')

# ---------------------------------while循环---------------------------------
# 也称之为死循环，当你的代码需要一直运行的时候，就写到while后面
while 1>2: # 由这个条件控制循环的次数
    print('python')

i=1
while i<=10:
    print('python',i)
    i+=1   # 自加一次

# ---------------------------------break-------------------------------------
# 退出循环
for i in range(1000):
    print(i)
    if i==5 :  #当满足你定义的条件的时候，就退出附近的（for while），只能退出一层循环
        break


print("asdfsadf" \
"asdfsadf" \
"sadfasdf")

print(
'''
asdfsad
sa
df
asd
fsa
d                                                   fsf
sa
df
                                                asd
                                                f
'''

)