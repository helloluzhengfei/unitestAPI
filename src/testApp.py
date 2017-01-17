#coding=GBK  
import requests
import unittest
import json
import os
import numbers
from ctypes.test.test_numbers import bool_types
import string
import re
class testApp(unittest.TestCase):
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

    def test1_cat_list_api(self):
        url = self.base_url + self.cat_list_uri        
        response = requests.get(url)                
        jResp = response.json()  
        
        jData = jResp["data"]

        for jCat in jData:
            self.cat_listId.append(jCat['id'])                                                      
            self.cat_listParent_id.append(jCat['parent_id'])            

        self.cat_listParent_idRemSm=list(set(self.cat_listParent_id))
        self.cat_listId.append(u'0')

       
        for parent_Id in self.cat_listParent_idRemSm:
            self.cat_listId.remove(parent_Id)
#        print self.cat_listId
        
        print '去除parent_id的id列表'
        print self.cat_listId
  
        i=1    
        for category_id in self.cat_listId: 
            print '\t'           
            print '第%d个应用' %i
            print '该应用的id是%r '  %category_id 
           
            i=i+1
            self.get_app_info1(category_id)  
            self.get_app_info2(category_id)
            self.get_app_info3(category_id)
            self.get_app_info4(category_id)
            self.get_app_info5(category_id)
            
            
    def get_app_info1(self, category_id):
        self.list_tmp_id=[] 
        url = self.base_url + self.cat_app_uri+category_id
        print url
        #print self.cat_list
        response = requests.post(url)
        self.assertEqual(response.status_code, 200)
        print 'app的状态码是200'

        jResp = response.json()
        
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 405) 
        print 'result_code值为200'
       
        code = jResp["code"]
        self.assertEqual(code, 'method_not_allowed') 
        print code
        
        message = jResp["message"]
        message1='http://10.110.1.55/1.0/cat/app/'+category_id
        print message1
        self.assertEqual(message,message1) 
        print message
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id
        
    
    def get_app_info2(self, category_id):
        self.list_tmp_id=[] 
        url = self.base_url + self.cat_app_uri+category_id
        print url
        #print self.cat_list
        response = requests.put(url)
        self.assertEqual(response.status_code, 200)
        print 'app的状态码是200'

        jResp = response.json()
        
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 405) 
        print 'result_code值为200'
       
        code = jResp["code"]
        self.assertEqual(code, 'method_not_allowed') 
        print code
        
        message = jResp["message"]
        message1='http://10.110.1.55/1.0/cat/app/'+category_id
        print message1
        self.assertEqual(message,message1) 
        print message
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id
        
        
        
    
    
    def get_app_info3(self, category_id):
        self.list_tmp_id=[] 
        url = self.base_url + self.cat_app_uri+category_id
        print url
        #print self.cat_list
        response = requests.patch(url)
        self.assertEqual(response.status_code, 200)
        print 'app的状态码是200'

        jResp = response.json()
        
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 500) 
        print 'result_code值为200'
       
        code = jResp["code"]
        self.assertEqual(code, 'internal_server_error') 
        print code
        
        message = jResp["message"]
        message1='unknown error type'
        print message1
        self.assertEqual(message,message1) 
        print message
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id
    
    def get_app_info4(self, category_id):
        self.list_tmp_id=[] 
        url = self.base_url + self.cat_app_uri+category_id
        print url
        #print self.cat_list
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)
        print 'app的状态码是200'

        jResp = response.json()
        
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 405) 
        print 'result_code值为200'
       
        code = jResp["code"]
        self.assertEqual(code, 'method_not_allowed') 
        print code
        
        message = jResp["message"]
        message1='http://10.110.1.55/1.0/cat/app/'+category_id
        print message1
        self.assertEqual(message,message1) 
        print message
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id   
        
        
  