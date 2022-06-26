#! /usr/bin/python3

import ddt
import unittest
# baseinfo包中的__init__.py文件为存放数据文件
import baseinfo


@ddt.ddt
class MyTest(unittest.TestCase):
    def setUp(self):
        print("setUp")
    def tearDown(self):
        print("tearDown")
    # 数据提取采用调用方法的方式
    @ddt.data(*baseinfo.data)
    def test01(self, testdata):
        # print("start")
        print(testdata)
        # print("end")


if __name__ == '__main__':
    unittest.main()


#​ 从执行结果我们可以看到，三条数据对应下面显示的三条测试用例。
# 且每读取一次数据，都会先执行setUp方法，一条数据读取结束后会相应的执行tearDown方法。
# 所以我们就可以根据ddt读取数据的特点来设计对应的测试用例了。