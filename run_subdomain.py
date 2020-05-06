import time
from lib.domain_class import *
from lib.DatabaseClass import *
from ast import literal_eval


# 扫描目标
def scan_domain(domain):
    """
    扫描二级域名

    :param domain: 主域名
    :return: 扫描结果
    """
    subdomains = OneforallScan(domain).run()
    return subdomains


def date_clean(result):
    """
    清洗oneforall返回的结果
    :param result:
    :return:
    url\subdomain\content\status\reason\title\banner
    """
    result_dict = []
    for subdomain_dict in result:  # 将列表中的字典循环出来
        if subdomain_dict['status'] is not None or subdomain_dict['content'] is not None:
            result_tmp = []  # 错误  1.要元组()  2.集合的顺序不对应
            result_tmp.append(subdomain_dict['url'])
            result_tmp.append(subdomain_dict['subdomain'])
            result_tmp.append(subdomain_dict['content'])
            result_tmp.append(subdomain_dict['status'])
            result_tmp.append(subdomain_dict['reason'])
            result_tmp.append(subdomain_dict['title'])
            result_tmp.append(subdomain_dict['banner'])
            result_dict.append(tuple(result_tmp))
    return result_dict


# 存放结果
def main():
    """
    控制程序运行

    :return:
    """
    domain = mysql_get_domain() # hzeu.net
    # domain = 'hzeu.net'
    if domain:
        try:
            result = scan_domain(domain)
            result_dict = date_clean(result)
        except Exception as e:
            return
        print(result_dict)
        mysql_save_subdomain(result_dict, domain)
        mysql_scan_end(domain)
    else:
        print('[-]暂无无新域名..休眠5秒')
        time.sleep(30)


if __name__ == '__main__':
    while True:
        try:
            main()
        except:
            pass