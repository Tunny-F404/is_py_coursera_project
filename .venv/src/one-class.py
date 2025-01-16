# coursera的py的课程测试
'''
print('Hello World')

month = 24
money = 5000
horse = 1000
eat = 1500
subsidize = 3000

sun = month * (money - horse - eat + subsidize)

print('赚的总价钱: ', sun)

x = 1 + 2 * 3 - 8 / 4
print(x)
x = int(98.6)
'''
# 上面是py的课程测试（我忘了具体哪个是哪个的了）；下面的是3.1的测试
'''
hrs = input('输入工作时间：')
rate = input('输入小时费用：')
h = float(hrs)
r = float(rate)
sun = 0

if h <= 40:
    sun = r * h
elif h > 40:
    sun = (h - 40) * r * 1.5 + 40 * r

print(sun)
'''
# 下面是3.3的测试
'''
score = input('输入你的成绩：')
score = float(score)
if score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
elif score < 0.6:
    print('F')
else:
    print('请输入0～1之间的数字哦！')
'''
# 下面是4.6的测试
'''
def computerpay(hrs,hour):
    pay = 0
    if hour <= 40:
        pay = hrs * hour
    elif hour > 40:
        pay = (hour - 40) * hrs * 1.5 + 40 * hrs
    return pay
hrs = input('输入工作时间：')
rate = input('输入小时费用：')
h = float(hrs)
r = float(rate)
print('Pay', computerpay(r,h))
'''
# 下面是5.2的测试
'''
5.2编写一个程序，反复提示用户输入整数，直到用户输入“完成”。
输入“ done”后，打印出最大和最小的数字。
如果用户输入了除有效数字之外的任何内容，则使用 try/other 捕获该内容，并输出适当的消息，忽略该数字。
输入7、2、 bob、10和4并匹配下面的输出。

输出：
Invalid input
Maximum is 10
Minimum is 2
'''
# 下面是最后一个测试
'''
arr = []
min_num = None
max_num = None

while True:
    iarr = input('请输入数字：')
    if iarr == 'done':
        break
    try:
        iarr = int(iarr)
    except:
        print(iarr,'您输入的不是数字')
        continue
    arr.append(iarr)
for i in arr:
    if min_num is None or i < min_num:
        min_num = i
    if max_num is None or i > max_num:
        max_num = i
print('Invalid input')
print('Maximum is', max_num)
print('Minimum is', min_num)
'''