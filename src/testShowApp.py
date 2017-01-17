#coding=GBK
import requests
import unittest
import json
import os
import numbers
class testShowApp(unittest.TestCase):
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
        self.get_commentlist_uri='app/c/list/'###########�¼�
        self.get_app_allinfo_uri='app/'
       
        
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
        
        self.comment_id=[] 
        self.comment_app_id=[]    
        self.comment_msg=[]   
        self.comment_ip=[] 
        self.comment_stars=[] 
        self.comment_create_date=[] 
        
#��һ�β���   10.110.1.55:8081/1.0/cat/list/cat/list
    def test1_cat_list_api(self):
        url = self.base_url + self.cat_list_uri        
        response = requests.get(url)                
        jResp = response.json()  
        
        jData = jResp["data"]
#��data�е�id�������α��������뵽self.cat_list��
        for jCat in jData: 
            self.cat_listId.append(jCat['id'])                     
            self.cat_listParent_id.append(jCat['parent_id'])            
       
        self.cat_listParent_idRemSm=list(set(self.cat_listParent_id))
        self.cat_listId.append(u'0')

#ɾ����id�е�parent_id        
        for parent_Id in self.cat_listParent_idRemSm:
            self.cat_listId.remove(parent_Id)

#����ѭ�������ų�parent_id��list����id����app����     
        i=1    
        for category_id in self.cat_listId: 
            print '\t'           
            print '���Ե�%d��Ӧ��' %i
            print 'cat_id���Ե�ID��%r '  %category_id 
           
            i=i+1
            self.get_app_info(category_id)  
        
        
       
        for  app_id in self.list_app_id:                               
            print app_id
            self.get_comment_list1(app_id)
            self.get_comment_list2(app_id)
            self.get_comment_list3(app_id)
#            self.get_comment_list4(app_id)
             
            

                    
#��Ҫ�����ǽ�ȥ��parentid��id���������й����ڵĵ���
             
#�ڶ��β���        10.110.1.55:8081/1.0/cat/app/app_id
#ѭ����������app_id,apk_id,icon_id,scree����idȫ����������
    def get_app_info(self, category_id):
        
        url = self.base_url + self.cat_app_uri+category_id
#        print url       
        response = requests.get(url)
        jResp = response.json()
        jData = jResp["data"]
        for appData in jData:            
                
                self.list_app_id.append(appData['id'])               


    def get_comment_list1(self, app_id):
        
#        a=input("������pos��ֵ")
#        b=input("������limit��ֵ")
#        self.commentcontent='?pos=%d&limit=%d' %(a,b)
        
        ###########�˴���Ҫ�޸�
        
        url = self.base_url + self.get_app_allinfo_uri + app_id#+self.commentcontent #http://10.110.1.55:8081/1.0/file/
        print '½����  ���β��Ե�URL��'
        print url
        
        response = requests.post(url) 
        self.assertEqual(response.status_code, 200) #�жϷ������Ƿ����200
       
        
 
 
        jResp = response.json()
        
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 405) 
        print 'result_codeֵΪ200'
       
        code = jResp["code"]
        self.assertEqual(code, 'method_not_allowed') 
        print code
        
        message = jResp["message"]
        message1='http://10.110.1.55/1.0/app/'+app_id
        print message1
        self.assertEqual(message,message1) 
        print message
        
        request_id = jResp["request_id"]
 
        print request_id
        
    

        
        
        
    def get_comment_list2(self, app_id):
        self.list_tmp_id=[] 
        url = self.base_url + self.get_app_allinfo_uri + app_id
        print url
        #print self.cat_list
        response = requests.put(url)
        self.assertEqual(response.status_code, 200)
        print 'app��״̬����200'

        jResp = response.json()
        
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 400) 
        print 'result_codeֵΪ200'
       
        code = jResp["code"]
        self.assertEqual(code, 'bad_request') 
        print code
        
        message = jResp["message"]
        message1=""
        print message1
        self.assertEqual(message,message1) 
        print message
        
        request_id = jResp["request_id"]
  #      self.assertEqual(request_id, 405) 
        print request_id
        
    
    def get_comment_list3(self, app_id):
        self.list_tmp_id=[] 
        url = self.base_url + self.get_app_allinfo_uri + app_id
        print url
        #print self.cat_list
        response = requests.patch(url)
        self.assertEqual(response.status_code, 200)
        print 'app��״̬����200'

        jResp = response.json()
        
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 500) 
        print 'result_codeֵΪ200'
       
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

'''    
    def get_app_info4(self, app_id):
        self.list_tmp_id=[] 
        url = self.base_url + self.get_app_allinfo_uri + app_id
        print url
        #print self.cat_list
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)
        print 'app��״̬����200'

        jResp = response.json()
        
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 405) 
        print 'result_codeֵΪ200'
       
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
'''  