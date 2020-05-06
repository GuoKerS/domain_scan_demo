import pymysql
import contextlib
from __config__ import *


@contextlib.contextmanager
def mysql_conn():
    conn = pymysql.connect(host=hostname, port=sql_port, user=username, password=password, database=database, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor) # 游标设置返回值为字典类型
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()


def conn(sql, *args):
    with mysql_conn() as cursor:
        cursor.execute(sql, *args)
        result = cursor.fetchall()
        return result


def mysql_get_domain():
    """
    取域名
    :return: 返回一个域名
    """
    domain = conn('''SELECT domain FROM domains WHERE task_done = 0 ORDER BY RAND() LIMIT 1''') # 随机取一条
    try:
        conn('''UPDATE domains SET task_done = 1 WHERE domain = %s;''''', (domain[0]['domain']))  # 标记已取到
        return domain[0]['domain']
    except Exception as e:
        print(e)
        return False



def mysql_save_domain(result, domain):
    """
    保存扫描结果 update
    :param result: 扫描结果
    :return:
    """
    try:
        conn('''UPDATE domains SET subdomains = %s, task_done = 1 WHERE domain = %s;''''', (result, domain))
    except Exception as e:
        print('入库失败', e)


def mysql_save_subdomain(result_dict, domain):
    """
    insert
    用来储存子域名的相关信息(关联的主域名、子域名、解析IP、url、状态码、网络连接结果、title、banner)
    :param result:  子域名信息字典
    :param domain:
    :return:
    """
    sql = f'''
    INSERT INTO subdomains (domain,subdomain,url,content,status,reason,title,banner)
    VALUES ({domain!r},%s,%s,%s,%s,%s,%s,%s)'''
    try:
        with mysql_conn() as cursor:
            cursor.executemany(sql, result_dict)
    except Exception as e:
        print(e)



def mysql_scan_end(domain):
    try:
        conn('''UPDATE domains SET scan_end = 1 WHERE domain = %s;''', (domain))
    except Exception as e:
        print('任务状态修改失败', e)

def mysql_task_done(table, domain):
    try:
        conn('''UPDATE %s SET task_done = 1 WHERE subdomain = %s;''', (table, domain))
    except Exception as e:
        print('任务状态修改失败', e)

if __name__ == '__main__':
    pass