#coding=GBK
import requests
import unittest
import json
import os
import numbers
import re
class testFileInfo(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://10.110.1.55:8081/1.0/'
        self.cat_list_uri = 'cat/list'
        self.cat_app_uri = 'cat/app/'
        self.file_prop_uri = 'file/'
        self.dlwd_icon_uri = 'app/icon/cont/'
        self.dlwd_screen_uri = 'app/screen/cont/'
        self.dlwd_apk_uri = 'app/cont/'
        self.comment_add_uri = 'app/c/' #  POST /app/c/{app_id}
        self.comment_get_uri = 'app/screen/cont/' #GET app/c/list/{app_id}?pos={pos}&limit={limit}
        self.cat_listId = []   #data
        self.cat_len = 0;
        self.cat_listName=[]   #name
        self.cat_listSeq_num=[]   #seq_num
        self.cat_listFile_size=[]   #file_size
        self.cat_listMime_type=[]   #mime_type
        self.cat_listParent_id=[]    #parent_id
        self.cat_listMime_type=[]   
        self.list_app_id=[]
        self.list_icon_id=[]
        self.list_apk_id=[]
        self.list_screen_id=[]
        
#第一次测试   10.110.1.55:8081/1.0/cat/list/cat/list
    def test1_cat_list_api(self):
        url = self.base_url + self.cat_list_uri        
        response = requests.get(url)                
        jResp = response.json()  
        
        jData = jResp["data"]
#把data中的id部分依次遍历，放入到self.cat_list中
        for jCat in jData: 
            self.cat_listId.append(jCat['id'])                     
            self.cat_listParent_id.append(jCat['parent_id'])            
       
        self.cat_listParent_idRemSm=list(set(self.cat_listParent_id))
        self.cat_listId.append(u'0')

#删除在id中的parent_id        
        for parent_Id in self.cat_listParent_idRemSm:
            self.cat_listId.remove(parent_Id)

#依次循环带入排除parent_id的list——id进行app测试     
        i=1    
        for category_id in self.cat_listId: 
            print '\t'           
            print '测试第%d个应用' %i
            print 'cat_id测试的ID是%r '  %category_id 
           
            i=i+1
            self.get_app_info(category_id)  
        
        
        print 'app_id的file测试。。。。。。。' 
        for  app_id in self.list_app_id:                               
            print app_id
            print '\t' 
            
        print 'apk_id的file测试。。。。。。。'    
        for apk_id in self.list_apk_id:
             
            print apk_id
            print '\t' 
            self.get_file_info1(apk_id, 1)
            self.get_file_info2(apk_id, 1)
            self.get_file_info3(apk_id, 1)
            self.get_file_info4(apk_id, 1)
        
        wrong_id='0000-3b85e060-14ab-4f2a-a5f3-16cec8ebf9a8'        
        self.get_file_info5(wrong_id, 1) 
        empty_id=''
        self.get_file_info6(empty_id, 1)    
           
        print 'icon_id的file测试。。。。。。。'     
        for icon_id in self.list_icon_id:
            
            print icon_id
            print '\t' 
            self.get_file_info1(icon_id, 2)
            self.get_file_info2(icon_id, 2)
            self.get_file_info3(icon_id, 2)
            self.get_file_info4(icon_id, 2)
        
        wrong_id='0000-3b85e060-14ab-4f2a-a5f3-16cec8ebf9a8'        
        self.get_file_info5(wrong_id, 2) 
        empty_id=''
        self.get_file_info6(empty_id, 2)  
        
            
        print 'screen_id的file测试。。。。。。。'    
        for screen_id in self.list_screen_id:
             
            print screen_id
            print '\t' 
            for screen_id1 in screen_id:
                self.get_file_info1(screen_id1, 3)
                self.get_file_info2(screen_id1, 3)
                self.get_file_info3(screen_id1, 3)
                self.get_file_info4(screen_id1, 3) 
        
        wrong_id='0000-3b85e060-14ab-4f2a-a5f3-16cec8ebf9a8'        
        self.get_file_info5(wrong_id, 3) 
        empty_id=''
        self.get_file_info6(empty_id, 3)            
#主要作用是将去除parentid的id放在数组中供后期的调用
             
#第二次测试        10.110.1.55:8081/1.0/cat/app/app_id
    def get_app_info(self, category_id):
        
        url = self.base_url + self.cat_app_uri+category_id
        print url
       
        response = requests.get(url)

        jResp = response.json()
 
        jData = jResp["data"]

        for appData in jData:            
                
                self.list_app_id.append(appData['id'])               
                self.list_apk_id.append(appData['apk_id'])
                self.list_icon_id.append(appData['icon_id'])
                self.list_screen_id.append(appData['screen_id'])

############################################################
              

    def get_file_info1(self, file_id, file_type):
        url = self.base_url + self.file_prop_uri + file_id #http://10.110.1.55:8081/1.0/file/
        print '陆正飞  本次file测试的URL是'
        print url
        #print self.cat_list
        response = requests.post(url)
        self.assertEqual(response.status_code, 200)
        
        
        jResp = response.json()
        
         
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 405)
        
         
        code = jResp["code"]
        self.assertEqual(code, 'method_not_allowed')
        
        message = jResp["message"]
        message1='http://10.110.1.55/1.0/file/'+file_id
        print message1
        self.assertEqual(message,message1) 
        print message
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id
     
     
     
    def get_file_info2(self, file_id, file_type):
        url = self.base_url + self.file_prop_uri + file_id #http://10.110.1.55:8081/1.0/file/
        print '陆正飞  本次file测试的URL是'
        print url
        #print self.cat_list
        response = requests.put(url)
        self.assertEqual(response.status_code, 200)
        
        
        jResp = response.json()
        
         
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 405)
        
         
        code = jResp["code"]
        self.assertEqual(code, 'method_not_allowed')
        
        message = jResp["message"]
        message1='http://10.110.1.55/1.0/file/'+file_id
        print message1
        self.assertEqual(message,message1) 
        print message
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id     
    
    
    def get_file_info3(self, file_id, file_type):
        url = self.base_url + self.file_prop_uri + file_id #http://10.110.1.55:8081/1.0/file/
        print '陆正飞  本次file测试的URL是'
        print url
        #print self.cat_list
        response = requests.patch(url)
        self.assertEqual(response.status_code, 200)
        
        
        jResp = response.json()
        
         
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 500)
        
         
        code = jResp["code"]
        self.assertEqual(code, 'internal_server_error')
        
        message = jResp["message"]
        
        
        self.assertEqual(message,'unknown error type') 
        print message
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id     
        
    def get_file_info4(self, file_id, file_type):
        url = self.base_url + self.file_prop_uri + file_id #http://10.110.1.55:8081/1.0/file/
        print '陆正飞  本次file测试的URL是'
        print url
        #print self.cat_list
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)
        
        
        jResp = response.json()
        
         
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 405)
        
         
        code = jResp["code"]
        self.assertEqual(code, 'method_not_allowed')
        
        message = jResp["message"]
        message1='http://10.110.1.55/1.0/file/'+file_id
        print message1
        self.assertEqual(message,message1) 
        print message
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id        
        
    #错误的id        
    def get_file_info5(self, wrong_id, file_type):
        self.list_tmp_id=[] 
        url = self.base_url + self.cat_app_uri+wrong_id
        print url
        #print self.cat_list
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        print 'app的状态码是200'

        jResp = response.json()
        
        limit = jResp["limit"]
        self.assertEqual(limit, 0) 
        
       
        total = jResp["total"]
        self.assertEqual(total, 0) 
        
        
        result_code = jResp["result_code"]
        
        self.assertEqual(result_code,404) 
        
        
        data = jResp["data"]
        self.assertEqual(data, []) 
    #空的id        
    def get_file_info6(self, empty_id, file_type):
        self.list_tmp_id=[] 
        url = self.base_url + self.cat_app_uri+empty_id
        print url
        #print self.cat_list
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        print 'app的状态码是200'

        jResp = response.json()
        
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 404) 
        print 'result_code值为200'
       
        code = jResp["code"]
        self.assertEqual(code, 'not_found') 
        print code
        
        message = jResp["message"]
        message1='Unresolvable URL: '+'http://10.110.1.55/1.0/cat/app/'
        print message1
        self.assertEqual(message,message1) 
        print message
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id           
        