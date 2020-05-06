import sys
from lib.domain_class import *

def main1(url):
    domain_list = Domain_Sublist(url).run1()
    file_name = url + '_domain.txt'
    with open(file_name, 'a') as f:
        for i in domain_list:
            url = i + '\n'
            f.write(url)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main1(sys.argv[1])
    else:
        print('''
Usage: python main.py baidu.com
        ''')