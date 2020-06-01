from hyrobot.common import *
from lib.webapi import apimgr


class c1:
    name = '客户API-0101'
    # tags = 'customer1'

    # 初始化方法
    def setUp(self):
        INFO('删除客户订单')
        apimgr.mgr_login()
        apimgr.order_del_all()
        apimgr.customer_del_all()
        apimgr.medicine_del_all()

        INFO('添加10个客户')
        for i in range(10):
            apimgr.customer_add(
                f'医院_{i+1}',
                f'100000000{i+1:02d}',
                f'定位球为_{i+1}'




            )
    # #清除
    def tearDown(self):
        apimgr.customer_del(self.addedcsid)

    def teststeps(self):
        STEP(1, '添加客户')
        r = apimgr.customer_add('wuhanshi',
                                '15378963254',
                                "阿发请问请问穷人区围绕"
                                )

        addret = r.json()
        self.addedcsid = addret['id']


        STEP(2, '确认返回值')
        CHECK_POINT('返回的ret是0',
                    addret['ret'] == 0)

        # r = apimgr.customer_list()
        #
        # listret == {
        #
        #
        #
        #
        #
        # }

        # listret == apimgr.customer_list()
