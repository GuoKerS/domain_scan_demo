from __config__ import *
from multiprocessing import Process
from lib.Sublist3r import sublist3r
from lib.oneforall import oneforall


class DomainSublist(object):
    def __init__(self, domain):
        # super().__init__()
        self.domain = domain
        self.save_file = None
        # self.start()
        print('[*]Sublist3r 启动成功...')

    def run1(self):
        result = sublist3r.main(self.domain, threads, self.save_file, port_list, silent, verbose, enumeration, engines)
        return result


class OneforallScan(object):

    def __init__(self, domian):
        self.tmp_domain = domian

    def run(self):
        result = oneforall.OneForAll(self.tmp_domain).run()
        return result
