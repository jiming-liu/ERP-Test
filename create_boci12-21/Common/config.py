# self.login_url = "http://erp1.yishou.com/erp/Admin/login"  # 登录接口
#         self.order_info_url = "http://test2.yishou.com/os/order/orderDetail"  # 查询订单详情接口
#         self.check_orders_url = "http://erp1.yishou.com/erp/wcgPlan/getInfo"  # 进入需审核的采购订单
#         self.updata_check_url = "http://erp1.yishou.com/erp/wcgPlan/updateCheck"  # 更新审核状态
#         self.supply_list_url = "http://erp1.yishou.com/erp/WcgPlan/waitConfirmSupplyList"  # 查询当前供应商采购核单列表
#         self.purchase_url = "http://erp1.yishou.com/buyer/purchase/goodsDetailOfVerifyPurchase"  # 进入采购核单详情页面
#         self.edit_purchase_url = "http://erp1.yishou.com/buyer/purchase/editOfVerifyPurchase"  # 提交开单操作
#         self.orders_list_url = "http://erp1.yishou.com/erp/WcgOrder/list2"  # 查询已垫付采购订单审核列表
#         self.get_order_info_url = "http://erp1.yishou.com/erp/WcgOrder/getOrderInfo"  # 进入采购订单详情进行审核
#         self.check_orderinfo_url = "http://erp8.yishou.com/erp/WcgOrder/checkRepeat"  # 采购订单审核提交接口
#         self.check_orderinfo_Prepay_url = "http://erp8.yishou.com/erp/WcgOrder/checkOrderPrepay"  # 采购订单审核接口
#         self.create_pici_url = "http://erp8.yishou.com/erp/Tally2/createPici"  # 创建批次进行点货
#         self.slet_goods_no_url = "http://erp1.yishou.com/erp/TakeStock/getTakeStockGoodsList"  # 查询当前供应商下可点货数据
#         self.close_box_url = "http://erp1.yishou.com/erp/TakeStock/closeBox"  # 关闭容器
#         self.get_dh_list_url = "http://erp8.yishou.com/erp/pici/getlist"  # 查询点货单列表
#         self.select_goods_url = "http://erp8.yishou.com/erp/Common/selectSPUGoodsLib"  # 查询采购订单可选商品
#         self.save_goods_url = "http://erp8.yishou.com/erp/WcgOrder/saveUnplannOrder"  # 手动创建采购订单
#         self.emptyboxurl = 'http://erp1.yishou.com/erp/box/index'  # 获取容器号接口
#         self.upshelf_url = "http://erp1.yishou.com/erp/Upshelf/getList"  # 获取上架任务列表
#         self.detail_url = 'http://erp1.yishou.com/erp/Upshelf/detail'  # 进入上架单详情
#         self.binddesknourl = "http://erp1.yishou.com/erp/TakeStock/bindDeskNo"  # 绑定工作台
#         self.binfboxnourl = "http://erp1.yishou.com/erp/TakeStock/bindBoxNo"  # 绑定容器号
#         self.select_pgid_url = "http://erp4.yishou.com/erp/PurchaseGroup/getList"  # 查询采购组ID
#         self.getgoodsinfo = "http://erp1.yishou.com/erp/TakeStock/getTakeStockGoodsInfo"  # 根据款号进入点货详情
#         self.nomraldabiaourl = "http://erp1.yishou.com/erp/TakeStock/nomralTakeStock"  # 打标操作
#         self.dianhuo_url = "http://erp1.yishou.com/erp/pici/getlist"  # 获取点货单数据
#         self.get_order_sn = "http://test2.yishou.com/os/order/orderList"  # 查询订单接口
#         self.select_pici_url = "http://erp1.yishou.com/erp/WavePicking/getWavePickingList"  # 波次查询接口
#         self.check_url = "http://erp5.yishou.com/storage/WavePicking/check"  # 校验打标ID
#         self.zhongfen_url = "http://erp1.yishou.com/erp/SurpassSummary/surpassSummaryList"  # 查询中分任务
#         self.zhongfen_info_url = "http://erp1.yishou.com/erp/SurpassSummary/confirmAssembleDiff"  # 查询中分任务详情
#         self.get_jiaoyan_url = "http://erp1.yishou.com/storage/WavePicking/getWavePickingGoods"  # 获取波次信息接口
#         self.get_kuaidi_url = "http://erp1.yishou.com/storage/WavePicking/getWayBill"  # 获取快递信息接口
#         self.YueKu_imgurl = 'http://cdn-cloudprint.cainiao.com/waybill-print/cloudprint-imgs/9ab62bf1544248e9a99a36f995b6a733.png'  # 是否越库标凭证
#         self.space_url = 'http://erp1.yishou.com/erp/ShippingSpace/spaceList'  # 获取控仓位
#         self.select_shangjia_url = "http://erp8.yishou.com/erp/Upshelf/getList"#获取未领取的上架单
#         self.select_shangjiainfo_url = "http://erp6.yishou.com/erp/Upshelf/detail"#获取上架单明细数据
#         self.get_box_url = "http://erp5.yishou.com/suzaku/UpShelf/receive"#领取上架任务
#         self.get_box_url1 = "http://erp7.yishou.com/suzaku/UpShelf/upSku"#上架操作
#         self.get_bangdrq_url = "http://erp5.yishou.com/suzaku/UpShelf/getUpshelfOnScan"#扫容器号
#         self.lock_pici_url = "http://erp5.yishou.com/erp/WavePicking/lockWavePicking"  # 锁定批次
#         self.generate_url = "http://erp5.yishou.com/erp/PickingAssignment/generatePickingAssignment"  # 生成拣货任务
#         self.select_generate_url = "http://erp5.yishou.com/erp/PickingAssignment/pickingAssignmentList"  # 查询拣货任务列表
#         self.pda_jh_url = "http://erp6.yishou.com/suzaku/Picking/receive"#领取拣货任务
#         self.pda_jhinfo_url = "http://erp6.yishou.com/suzaku/Picking/picking"#拣货操作扫描打标ID
#         self.pda_tjjhinfo_url = "http://erp6.yishou.com/suzaku/Picking/sub"#提交拣货操作
#         self.cangwei_url = "http://erp8.yishou.com/erp/AdminSetting/stockDetailSeparateSetting"  # 获取点货库存分离配置
#         self.header_login = {}
#         self.name = "刘继明"  # 需配置成自己的账户密码
#         self.password = '123456'# 需配置成自己的账户密码
#         self.box_no = ""
#         self.deskno = 'GZGZT123'
#         self.is_numble = 0#默认为0则表示非越库标
#         self.pgname = ""
#         self.order_sn = ""
#         self.pgid = ""
#         self.supply_id = ""
#         self.goods_on_list = []
#         self.goods_ary = []
#         self.sku_list = []
#         self.qrCode = []
#         self.token = ""
#         self.boci_id = ""
#         self.us_no = ""
#         self.order_id = ""
#         self.today = datetime.date.today()
#         self.tomorrow = self.today + datetime.timedelta(days=1)