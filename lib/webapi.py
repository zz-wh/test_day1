import requests
from pprint import  pprint
from hyrobot.common import *


class APIMgr:
    def _printResponse(self,response):
        print('\n\n-------- HTTP response * begin -------')
        print(response.status_code)

        for k,v in response.headers.items():
            print(f'{k}: {v}')

        print('')

        print(response.content.decode('utf8'))
        print('-------- HTTP response * end -------\n\n')

    # 登录
    def mgr_login(self,username='byhy',password='88888888'):
        self.s = requests.Session()
        response = self.s.post("http://127.0.0.1/api/mgr/signin",
                               data={
                                   'username': username,
                                   'password': password
                               }
                               )

        self._printResponse(response)
        return response


    # 添加客户
    def customer_add(self,name,phonenumber,address):
        response = self.s.post("http://127.0.0.1/api/mgr/customers",
                               json={
                                   'action' :'add_customer',
                                   'data' : {
                                       'name' : name,
                                       'phonenumber' : phonenumber,
                                       'address' : address
                                   }
                               })

        self._printResponse(response)
        return response




    # 列出客户
    def customer_list(self,pagesize,pagenumber,keywords):
        response = self.s.get("http://127.0.0.1/api/mgr/customers",
                              params={
                                  'action' :'list_customer',
                                  'pagesize': pagesize,
                                  'pagenum': pagenumber,
                                  'keywords': keywords,
                              })

        self._printResponse(response)
        return response







    # 删除客户
    def customer_del(self,cid):
        response = self.s.delete("http://127.0.0.1/api/mgr/customers",
                                 json={
                                     "action":"del_customer",
                                     "id": cid

                                 })

        self._printResponse(response)
        return response



    # 删除所有客户
    def customer_del_all(self):
        response = self.customer_list(100,1,'')

        the_list = response.json()["retlist"]
        for one in the_list:
            self.customer_del(one["id"])

        self._printResponse(response)
        return response







    # 列出药品
    def medicine_list(self,pagesize,pagenumber,keywords):
        response = self.s.get("http://127.0.0.1/api/mgr/medicines",
                              params={
                                  'action' :'list_medicine',
                                  'pagesize' :pagesize,
                                  'pagenum' :pagenumber,
                                  'keywords' :keywords,
                              })

        self._printResponse(response)
        return response



    # 删除药品
    def medicine_del(self,mid):
        response = self.s.delete("http://127.0.0.1/api/mgr/medicines",
                                 json={
                                     "action":"del_medicine",
                                     "id": mid

                                 })

        self._printResponse(response)
        return response


    # 删除所有药品
    def medicine_del_all(self):
        response = self.medicine_list(100,1,'')

        the_list = response.json()["retlist"]
        for one in the_list:
            self.customer_del(one["id"])

        self._printResponse(response)
        return response



    # 列出订单
    def order_list(self,pagesize,pagenumber,keywords):
        response = self.s.get("http://127.0.0.1/api/mgr/orders",
                              params={
                                  'action' :'list_order',
                                  'pagesize' :pagesize,
                                  'pagenum' :pagenumber,
                                  'keywords' :keywords,
                              })

        self._printResponse(response)
        return response



    # 删除订单
    def order_del(self,oid):
        response = self.s.delete("http://127.0.0.1/api/mgr/orders",
                                 json={
                                     "action":"delete_order",
                                     "id": oid
                                 })

        self._printResponse(response)
        return response



    # 删除所有订单
    def order_del_all(self):
        response = self.order_list(100,1,'')

        the_list = response.json()["retlist"]
        for one in the_list:
            self.customer_del(one["id"])

        self._printResponse(response)
        return response


apimgr = APIMgr()
