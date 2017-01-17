#coding=GBK
import requests
import unittest
import json
import os
import numbers
import re
class testCatlist(unittest.TestCase):
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
        self.app_Id=[]
        self.cat_list_create_date=[]
        self.cat_list_mod_date=[]
    #第一次测试   10.110.1.55:8081/1.0/cat/list/cat/list
    def test1_cat_list_api(self):
        url = self.base_url + self.cat_list_uri
        print url
        
        response = requests.post(url)        
        self.assertEqual(response.status_code, 200) #判断返回码是否等于200
        print '服务器响应码是200'
        
        jResp = response.json()  
        result_code = jResp["result_code"]
               
        self.assertEqual(result_code, 405) #判断result_code是否等于200
        print 'result_code的结果是405'
        print result_code
        
        
        code = jResp["code"]
        self.assertEqual(code, "method_not_allowed")
        print code
        
        
        message= jResp["message"]
        self.assertEqual(message, "http://10.110.1.55/1.0/cat/list")
        print message
        
        request_id= jResp["request_id"]
      #  self.assertEqual(request_id, "NEVFASD01eef9576a-48db-4893-aabe-3db05c905eb6") 
         
    def test2_cat_list_api(self):
        url = self.base_url + self.cat_list_uri
        print url
        
        response = requests.put(url)        
        self.assertEqual(response.status_code, 200) #判断返回码是否等于200
        print '服务器响应码是200'
        
        jResp = response.json()  
        result_code = jResp["result_code"]
               
        self.assertEqual(result_code, 400) #判断result_code是否等于200
        print 'result_code的结果是405'
        print result_code
        
        
        code = jResp["code"]
        self.assertEqual(code, "bad_request")
        print code
        
        
        message= jResp["message"]
        self.assertEqual(message, "not found category")
        print message
        
        request_id= jResp["request_id"]
      #  self.assertEqual(request_id, "NEVFASD01eef9576a-48db-4893-aabe-3db05c905eb6")     
        
    def test3_cat_list_api(self):
        url = self.base_url + self.cat_list_uri
        print url
        
        response = requests.patch(url)        
        self.assertEqual(response.status_code, 200) #判断返回码是否等于200
        print '服务器响应码是200'
        
        jResp = response.json()  
        result_code = jResp["result_code"]
               
        self.assertEqual(result_code, 500) #判断result_code是否等于200
        print 'result_code的结果是405'
        print result_code
        
        
        code = jResp["code"]
        self.assertEqual(code, "internal_server_error")
        print code
        
        
        message= jResp["message"]
        self.assertEqual(message, "unknown error type")
        print message
        
        request_id= jResp["request_id"]
      #  self.assertEqual(request_id, "NEVFASD01eef9576a-48db-4893-aabe-3db05c905eb6")
      
    def test4_cat_list_api(self):
        url = self.base_url + self.cat_list_uri
        print url
        
        response = requests.delete(url)        
        self.assertEqual(response.status_code, 200) #判断返回码是否等于200
        print '服务器响应码是200'
        
        jResp = response.json()  
        result_code = jResp["result_code"]
               
        self.assertEqual(result_code, 400) #判断result_code是否等于200
        print 'result_code的结果是400'
        print result_code
        
        
        code = jResp["code"]
        self.assertEqual(code, "bad_request")
        print code
        
        
        message= jResp["message"] 
        self.assertEqual(message, "not found category")
        print message
        
        request_id= jResp["request_id"]
      #  self.assertEqual(request_id, "NEVFASD01eef9576a-48db-4893-aabe-3db05c905eb6")        
        