#coding=GBK 
'''
Created on 2017��1��6��

@author: zhengfei.lu
'''
import unittest
from testApk_idDownload import testApk_idDownload

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(testApk_idDownload)
    unittest.TextTestRunner(verbosity=2).run(suite)