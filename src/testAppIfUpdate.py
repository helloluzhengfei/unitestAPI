#coding=utf-8 
import requests
import unittest
import json
import os
import numbers
from ctypes.test.test_numbers import bool_types
import string
import re
class testAppIfUpdate(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://10.110.1.55:8081/1.0/'
        self.cat_list_uri = 'cat/list'
        self.cat_app_uri = 'cat/app/'
        self.update_url='app/update/query'
        self.cat_listId = []   #data
        self.cat_listParent_idRemSm=[]
        self.cat_listParent_id=[]
        self.cat_len = 0;     
        self.package_name=[]
        self.version_code=[]      

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
        
        print self.cat_listId  
        i=1    
        for category_id in self.cat_listId: 
            print '\t'           
            print '第%d个应用' %i
            print 'id是%r '  %category_id         
            i=i+1
            
       
            self.get_test1_cat_list_api1()  
            self.get_test1_cat_list_api2() 
            self.get_test1_cat_list_api3() 
            self.get_test1_cat_list_api4() 
         
    def get_test1_cat_list_api1(self):
       
        url = self.base_url + self.update_url           
     
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        
        
        jResp = response.json()
        
         
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 405)
        
         
        code = jResp["code"]
        self.assertEqual(code, 'method_not_allowed')
        
        message = jResp["message"]
        message1="http://10.110.1.55/1.0/app/update/query"
       
        self.assertEqual(message,message1) 
        print message
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id
        
        
        
    def get_test1_cat_list_api2(self):
                
        url = self.base_url + self.update_url #http://10.110.1.55:8081/1.0/file/
        print '陆正飞  本次测试的URL是'
        print url
########################,此处可以修改        
        
        response = requests.put(url)
        self.assertEqual(response.status_code, 200)
        
        
        jResp = response.json()
        
         
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 405)
        
         
        code = jResp["code"]
        self.assertEqual(code, 'method_not_allowed')
        
        message = jResp["message"]
        message1="http://10.110.1.55/1.0/app/update/query"
       
        self.assertEqual(message,message1) 
        print message
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id    


    def get_test1_cat_list_api3(self):
                
        url = self.base_url + self.update_url #http://10.110.1.55:8081/1.0/file/
        print '陆正飞  本次测试的URL是'
        print url
########################,此处可以修改        
        
        response = requests.patch(url)
        self.assertEqual(response.status_code, 200)
        
        
        jResp = response.json()
        
         
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 500)
        
         
        code = jResp["code"]
        self.assertEqual(code, 'internal_server_error')
        
        message = jResp["message"]
        message1='unknown error type'
       
        self.assertEqual(message,message1) 
        print message
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id

    def get_test1_cat_list_api4(self):
                
        url = self.base_url + self.update_url #http://10.110.1.55:8081/1.0/file/
        print '陆正飞  本次测试的URL是'
        print url
########################,此处可以修改        
        
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)
        
        
        jResp = response.json()
        
         
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 405)
        
         
        code = jResp["code"]
        self.assertEqual(code, 'method_not_allowed')
        
        message = jResp["message"]
        message1="http://10.110.1.55/1.0/app/update/query"
       
        self.assertEqual(message,message1) 
        print message
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id 
    