# 下面为6.1的测试
'''
arr_one = ' 1234567890'
arr_two = ' abcdefghijklmnopqrstuvwxyz'
arr_len_num = len(arr_one)
print(arr_len_num)
for i in arr_one:
    print(i)

if 'ban' > 'Ban':
    print('Ban')
print(arr_one[1])
print(arr_one[1:7])
print(len('banana')*7)
o = arr_two.upper()
k = arr_two.find('g')
print(k)
print(o)
print(dir(''))
'''
#下面为6.5的测试
'''
text = "X-DSPAM-Confidence:    0.8475"
i = text.find('0')
out = text[i:i+6]
out = float(out)
print(out)
'''
# 下面为7.1的测试
# 7.1编写一个程序，提示输入一个文件名，然后打开该文件并通读该文件，并打印该文件的大写内容。
# 使用 words.txt 文件生成以下输出。
# 你可以在 http://www.py4e.com/code3/words.txt 下载样本数据
'''
file = input('请输入要打开的文件： ')
try:
    of = open(file,'r')
    of_up = of.read()
    of_up = of_up.rstrip()
    of_up = of_up.upper()
    print(of_up)
except:
    print('文件不存在')
'''
# 下面为7.2的测试
# 7.2编写一个程序，提示输入文件名，然后打开该文件并通读该文件，查找以下格式的行：
# X-DSPAM-Confidence:    0.8475
# 计算这些线，从每条线中提取浮点值，计算这些值的平均值，并产生如下所示的输出。
# 不要在解决方案中使用sum（）函数或名为sum的变量。
# 您可以在以下网址下载示例数据http://www.py4e.com/code3/mbox-short.txt在下面进行测试时，请输入mbox-short.txt作为文件名。
'''
input_file_name = ('../data/mbox-short.txt')
find_str = 'X-DSPAM-Confidence: '
i = 0
sun = 0
bu = 0
try:
    file_name = open(input_file_name,'r')
    pu = 1
except:
    print('文件名错误or文件不存在')
if pu == 1:
    file_content = file_name.read()
    while True:
        i = file_content.find(find_str,i)
        if i == -1:
            break
        # print('find ',find_str,' in ',i)
        i += len(find_str)
        bu +=1
        j = file_content[i:i+6]
        int_j = float(j)
        sun += int_j
    sun = sun/bu
    print('Average spam confidence:',sun)
'''
# 下面为8.2的测试
'''
arr = []
arr.append('apple')
arr.append('banana')
arr.append('orange')
arr.append('pear')
arr.append('kiwi')
print('arr:',arr)
arr_one = list()
arr_one.append(arr)
print('arr_one:',arr_one)
arr_two = 'a b c     d e -f -g -h'
arr_two_1 = arr_two.split()
arr_two_2 = arr_two.split('-')
print('arr_two_1:',arr_two_1)
print('arr_two_2:',arr_two_2)
str_one = '      apple banana     '
str_one = str_one.rstrip()
print('str_one:',str_one)
'''
# 下面为8.4的测试
# 8.4打开romeo.txt文件，逐行读取。对于每一行，使用split（）方法将行拆分为单词列表。
# 程序应该建立一个单词列表。
# 对于每行中的每个单词，检查该单词是否已经在列表中，如果没有，则将其附加到列表中。
# 当程序完成时，按照python sort（）的顺序对结果单词进行排序和打印，如所需的输出所示。
# 您可以在以下网址下载示例数据http://www.py4e.com/code3/romeo.txt
'''
file_name = '../data/romeo.txt'
du = 0
word_list = []
try:
    file_data = open(file_name,'r')
    du = 1
except:
    print('文件名错误or文件打开失败')
if du == 1:
    for line in file_data:
        line = line.rstrip()
        word = line.split()
        # print('word:',word)
        for word in word:
            if word not in word_list:
                word_list.append(word)
word_list.sort()
print('word_list:',word_list)
'''
# 下面是8.5的测试
# 8.5打开mbox-short.txt文件，逐行阅读。当你发现一行以“From”开头时，如下所示：
# 从stephen.marquard@uct.ac.za2008年1月5日星期六09:14:16
# 您将使用split（）解析From行，并打印出该行中的第二个单词（即发送消息的人的整个地址）。然后在末尾打印一个计数。
# 提示：确保不要包含以“From：”开头的行。还要查看示例输出的最后一行，了解如何打印计数。
# 您可以在以下网址下载示例数据http://www.py4e.com/code3/mbox-short.txt
'''
line_num = 0
file_name = ('../data/mbox-short-one.txt')
file_content = open(file_name,'r')
for line in file_content:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    line_data = line.split()
    line_num += 1
    print(line_data[1])
print('There were',line_num,'lines in the file with From as the first word')
'''
# 下面是9.2的测试
'''
ccc = dict()
ccc['a'] = 1
ccc['b'] = 2
ccc['c'] = 3
ccc['a'] += 3
print(ccc)
aaa = ccc.get('g','funk')
print(aaa)
print('**********')
cou = dict()
aou = ['alice','fank','laughing','baby','laughing','baby']
for i in aou:
    cou[i] = cou.get(i,0) + 1
    # if i not in cou:
    #     cou[i] = 0
    # else:
    #     cou[i] = cou[i] + 1
print(cou)
print('**********')
arr_cou = list(cou)
arr_cou_one = list(cou.items())
print(cou.keys())
print(arr_cou_one)
print(arr_cou_one[0])
print(arr_cou)
for word,count in counter:
'''
# 下面是9.4的测试
# 9.4编写一个程序来阅读mbox-short.txt，并找出谁发送了最多的邮件。
# 程序会查找“发件人”行，并将这些行中的第二个单词作为发送邮件的人。
# 该程序创建了一个Python字典，将发件人的邮件地址映射到它们在文件中出现的次数。
# 生成词典后，程序使用最大值循环遍历词典，以找到最多产的提交者。
'''
dic_sun = dict()
line_num = 0
file_data = open('../data/mbox-short-one.txt')
for line in file_data:
    line_num += 1
    line = line.rstrip()
    if line.startswith('From '):
        str_line = line.split()
        if str_line[1] not in dic_sun:
            dic_sun[str_line[1]] = 1
        else:
            dic_sun[str_line[1]] = dic_sun[str_line[1]] + 1
arr_dic_v = list(dic_sun.values())
max_arr_dic = max(arr_dic_v)
arr_index = arr_dic_v.index(max_arr_dic)
arr_dic_k = list(dic_sun.keys())
print(arr_dic_k[arr_index],max_arr_dic)
'''
# 下面是10.1的测试
'''
if (1,2) < (2,2):
    print('ok')
if (6,3) < (3,2):
    print('ook')
# print(sorted([(v,k) for k,v in dic_sun.items()]))
x,y = 3,4
print(x,y)
'''
# 下面是10.2的测试
# 10.2编写一个程序来阅读mbox-short.txt，并计算出每条消息在一天中的小时分布。
# 您可以通过查找时间，然后使用冒号再次拆分字符串，从“from”行中提取小时。
# 从stephen.marquard@uct.ac.za2008年1月5日星期六09:14:16
# 一旦您累积了每个小时的计数，请打印出计数，按小时排序，如下所示。
'''
def get_10_2():
    dict_data = dict()
    file_data = open('../data/mbox-short-one.txt')
    for line in file_data:
        line = line.rstrip()
        if line.startswith('From '):
            str_line = line.split()
            str_arr_line = str(str_line[5])
            str_arr_line = str_arr_line[0:2]
            if str_arr_line not in dict_data:
                dict_data[str_arr_line] = 1
            else:
                dict_data[str_arr_line] = dict_data[str_arr_line] + 1
    print(dict_data)
    dict_data_new = dict(sorted(dict_data.items()))
    print(dict_data_new)
    try:
        for key, value in dict_data_new.items():
            print(key,value)
    except:
        print("***************")
get_10_2()
'''