import sqlite3
import urllib.request
import urllib.parse

'''
a = [1,2,3,4,5,6,7,8,9,0]
b = [108, 105, 115, 116]

class a_car:
    def __init__(self,b,a):
        self.b = b
        self.a = a
    def pa(self):
        print(self.a)
    def pb(self):
        print(self.b)
    def __del__(self):
        print('***********')

car = a_car(b,a)
car.pb()
car.pa()

car = 43
'''


# 下面的没一个能用的，傻逼了才写出来的
def open_web_file(url):
    # 去除url的空格
    url = url.strip()
    # 打开网站（字节流）并转换为str
    get_web_content_byte = urllib.request.urlopen(url)
    get_web_content_str = get_web_content_byte.read().decode('utf-8')
    print(get_web_content_str)
    # 循环字符串
def open_file(file_name):
    f = open(file_name, 'r')
    file_content = f.read()
    f.close()
    return file_content
def str_to_list(str):
    to_db_list = list()
    print(str)
    for line in str:
        line = line.rstrip()
        if not line.startswith('From:'):
            continue
        to_db_list.append(line)
        print(line)
    print(to_db_list)
def file_to_list_text(file_name):
    content = open_file(file_name)
    str_to_list(content)
# 上面的没一个能用的，傻逼了才写出来的

# 文件命名
file_name = '../data/sql/DB-unit2.txt'
# 导入数据库
database_coursera_py = 'E:/database_t460p/DB_Browser_for_SQLite/coursera_py_db.db'
try:
    conn = sqlite3.connect(database_coursera_py)
    cur = conn.cursor()
    print('数据库 '+database_coursera_py+' 导入成功')
except sqlite3.Error as e:
    print('数据库 '+database_coursera_py+' 导入失败')
    print(e)
def file_to_list(file_name):
    to_db_list = list()
    with open(file_name, 'r') as content:
        for line in content:
            line = line.strip()
            if not line.startswith('From:'):
                continue
            line = line.split()[1]
            line = line.split('@')[1]
            to_db_list.append(line)
        print(to_db_list)
        print('len======',len(to_db_list))
    return to_db_list
def list_to_db(file_list):
    for line in file_list:
        cur.execute('select count from Counts where org = ?',(line,))
        if cur.fetchone() is None:
            print(line)
            cur.execute('insert into Counts(org,count) values (?,1)',(line,))
        else:
            cur.execute('update Counts set count = count + 1 where org = ?',(line,))
    conn.commit()

def coursera_unit_two_test(file_name):
    file_list = file_to_list(file_name)
    print(file_list)
    list_to_db(file_list)


coursera_unit_two_test(file_name)








