#coding=GBK
import requests
import unittest
import json

class testDiscussComment(unittest.TestCase):
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
        self.get_commentlist_uri='app/c/list/'###########新加
       
        
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
        
        
        i=1     
        for  app_id in self.list_app_id:   
            print "第%d个app评论测试。。。。" %i  
            i=i+1                          
            print app_id
            self.discuss_comment_list1(app_id)
            self.discuss_comment_list2(app_id)
            self.discuss_comment_list3(app_id)
            self.discuss_comment_list4(app_id) 
        
        wrong_id='0000-3b85e060-14ab-4f2a-a5f3-16cec8ebf9a8'
        self.discuss_comment_list5(wrong_id)
        empty_id=''
        self.discuss_comment_list6(empty_id)
        
    def get_app_info(self, category_id):
        
        url = self.base_url + self.cat_app_uri+category_id
#        print url       
        response = requests.get(url)
        jResp = response.json()
        jData = jResp["data"]
        for appData in jData:            
                
                self.list_app_id.append(appData['id'])               

              

    def discuss_comment_list1(self, app_id):
                
        url = self.base_url + self.comment_add_uri + app_id #http://10.110.1.55:8081/1.0/file/
        print '陆正飞  本次测试的URL是'
        print url
########################,此处可以修改        
        
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        
        
        jResp = response.json()
        
         
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 400)
        
         
        code = jResp["code"]
        self.assertEqual(code, 'bad_request')
        
        message = jResp["message"]
        message1='comment '+app_id+" can't find"
       
        self.assertEqual(message,message1) 
        print message
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id
        
        
        
    def discuss_comment_list2(self, app_id):
                
        url = self.base_url + self.comment_add_uri + app_id #http://10.110.1.55:8081/1.0/file/
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
        message1='http://10.110.1.55/1.0/app/c/'+app_id
       
        self.assertEqual(message,message1) 
        print message
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id    


    def discuss_comment_list3(self, app_id):
                
        url = self.base_url + self.comment_add_uri + app_id #http://10.110.1.55:8081/1.0/file/
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

    def discuss_comment_list4(self, app_id):
                
        url = self.base_url + self.comment_add_uri + app_id #http://10.110.1.55:8081/1.0/file/
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
        message1='http://10.110.1.55/1.0/app/c/'+app_id
       
        self.assertEqual(message,message1) 
        print message
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id 

#错误的id        
    def discuss_comment_list5(self, wrong_id):
         
        url = self.base_url + self.comment_add_uri + wrong_id
        print url
        #print self.cat_list
        
        payload = {"stars":"3","msg":"luzhengfei:)"}
        response = requests.post(url, data=json.dumps(payload)) 
        self.assertEqual(response.status_code, 200) #判断返回码是否等于200
        
        
        
        print 'app的状态码是200'

        jResp = response.json()
        
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 400) 
        
       
        code = jResp["code"]
        self.assertEqual(code,"bad_request") 
        
        
        message = jResp["message"]
        message1="can't find app"+wrong_id
        self.assertEqual(message,message1) 
        
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id 
    #空的id        
    def discuss_comment_list6(self,empty_id):
      
        url = self.base_url + self.comment_add_uri + empty_id
        print url
        #print self.cat_list
        
        payload = {"stars":"3","msg":"luzhengfei:)"}
        response = requests.post(url, data=json.dumps(payload)) 
        self.assertEqual(response.status_code, 200) #判断返回码是否等于200
        
        
        print 'app的状态码是200'

        jResp = response.json()
        
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 404) 
        print 'result_code值为200'
       
        code = jResp["code"]
        self.assertEqual(code, 'not_found') 
        print code
        
        message = jResp["message"]
        message1="Unresolvable URL: http://10.110.1.55/1.0/app/c/"
        print message1
        self.assertEqual(message,message1) 
        print message
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id      