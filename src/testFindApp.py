#coding=GBK  
import requests
import unittest

class testFindApp(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://10.110.1.55:8081/1.0/'
        self.comment_url='app/find'
  
        
    def test1_cat_list_api(self):
        
        url = self.base_url + self.comment_url           
        
        print url      
        response = requests.post(url) 
        jResp = response.json() 
        self.assertEqual(response.status_code, 200) #判断返回码是否等于200
        
         
        result_code = jResp["result_code"]
               
        self.assertEqual(result_code, 405) #判断result_code是否等于200
        print 'result_code的结果是405'
        print result_code
        
        
        code = jResp["code"]
        self.assertEqual(code, "method_not_allowed")
        print code
        
        
        message= jResp["message"]
        self.assertEqual(message, "http://10.110.1.55/1.0/app/find")
        print message
        
        request_id= jResp["request_id"]
      #  self.assertEqual(request_id, "NEVFASD01eef9576a-48db-4893-aabe-3db05c905eb6") 
          
    def test2_cat_list_api(self):
        url = self.base_url + self.comment_url
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
        self.assertEqual(message, "")
        print message
        
        request_id= jResp["request_id"]
      #  self.assertEqual(request_id, "NEVFASD01eef9576a-48db-4893-aabe-3db05c905eb6")     
        
    def test3_cat_list_api(self):
        url = self.base_url + self.comment_url
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
      
'''    
    def test4_cat_list_api(self):
        url = self.base_url + self.comment_url
        print url
        
        response = requests.delete(url)        
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
'''          
    
        