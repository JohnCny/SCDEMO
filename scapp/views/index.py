# coding:utf-8

from flask import Module,request, render_template,flash,redirect
from flask.ext.login import login_user, logout_user, current_user, login_required

from scapp.config import logger
from scapp import app

# 登陆
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template("welcome.html")
    else:
        return render_template("login.html")

# 注销
@app.route('/change_password')
def change_password():
    return render_template("change_password.html")
	
# 修改密码
@app.route('/logout')
def logout():
    return render_template("login.html")
	    
# 登录
@app.route('/login1', methods=['GET'])
def login1():
    return render_template("login1.html")
    
# 欢迎界面
@app.route('/welcome', methods=['GET'])
def welcome():
    return render_template("welcome.html")

# 信息管理
@app.route('/xxgl', methods=['GET'])
def xxgl():
    return render_template("index.html",menu = 'xxgl')
	
# 新增客户
@app.route('/Xzkh', methods=['GET'])
def Xzkh():
	return render_template("index.html",menu = 'Xzkh')
	
# 客户分配
@app.route('/Khfp', methods=['GET'])
def Khfp():
	return render_template("index.html",menu = 'Khfp')
	
# 客户信息管理
@app.route('/Khxxgl', methods=['GET'])
def Khxxgl():
	return render_template("index.html",menu = 'Khxxgl')

# 贷款信息管理
@app.route('/Dkxxgl', methods=['GET'])
def Dkxxgl():
	return render_template("index.html",menu = 'Dkxxgl')
	
# 流程管理
@app.route('/lcgl', methods=['GET'])
def lcgl():
    return render_template("index.html",menu = 'lcgl')
		
# 新增贷款
@app.route('/Xzdk', methods=['GET'])
def Xzdk():
	return render_template("index.html",menu = 'Xzdk')
			
# 贷款申请审核
@app.route('/Dksqsh', methods=['GET'])
def Dksqsh():
	return render_template("index.html",menu = 'Dksqsh')
				
# 贷前调查
@app.route('/Dqdc', methods=['GET'])
def Dqdc():
	return render_template("index.html",menu = 'Dqdc')
					
# 贷后管理
@app.route('/Dhgl', methods=['GET'])
def Dhgl():
	return render_template("index.html",menu = 'Dhgl')
	
# 进件管理
@app.route('/jjgl', methods=['GET'])
def jjgl():
    return render_template("index.html",menu = 'jjgl')
	
# 新增进件
@app.route('/Xzjj', methods=['GET'])
def Xzjj():
    return render_template("index.html",menu = 'Xzjj')
	
# 进件审批
@app.route('/Jjsp', methods=['GET'])
def Jjsp():
    return render_template("index.html",menu = 'Jjsp')
	
# 台账管理
@app.route('/tzgl', methods=['GET'])
def tzgl():
    return render_template("index.html",menu = 'tzgl')	
	
# 评分管理
@app.route('/pfgl', methods=['GET'])
def pfgl():
    return render_template("index.html",menu = 'pfgl')	
	
# 绩效管理
@app.route('/jxgl', methods=['GET'])
def jxgl():
    return render_template("index.html",menu = 'jxgl')	
		
# 新增工时
@app.route('/Xzgs', methods=['GET'])
def Xzgs():
	return render_template("index.html",menu = 'Xzgs')
	
# 个人薪酬
@app.route('/Grxc', methods=['GET'])
def Grxc():
	return render_template("index.html",menu = 'Grxc')
	
# 在岗评估
@app.route('/Zgpg', methods=['GET'])
def Zgpg():
	return render_template("index.html",menu = 'Zgpg')
		
# 晋级审核
@app.route('/Jjsh', methods=['GET'])
def Jjsh():
	return render_template("index.html",menu = 'Jjsh')
		
# 统计报表
@app.route('/tjbb', methods=['GET'])
def tjbb():
    return render_template("index.html",menu = 'tjbb')
			
# 已发放的贷款
@app.route('/Yffddk', methods=['GET'])
def Yffddk():
    return render_template("index.html",menu = 'Yffddk')
	
# 被拒绝的贷款
@app.route('/Bjjddk', methods=['GET'])
def Bjjddk():
    return render_template("index.html",menu = 'Bjjddk')
		
# 贷后变更的贷款
@app.route('/Dhbgddk', methods=['GET'])
def Dhbgddk():
    return render_template("index.html",menu = 'Dhbgddk')
			
# 系统工具
@app.route('/xtgj', methods=['GET'])
def xtgj():
    return render_template("index.html",menu = 'xtgj')
				
# 系统管理
@app.route('/xtgl', methods=['GET'])
def xtgl():
    return render_template("index.html",menu = 'xtgl')
###############################信息管理##########################################	
# 客户登记-搜索
@app.route('/Information/lfdj/lfdj_search', methods=['GET'])
def lfdj_search():
    return render_template("Information/lfdj/lfdj_search.html")
	
# 客户登记列表
@app.route('/Information/lfdj/lfdj', methods=['GET'])
def lfdj():
    return render_template("Information/lfdj/lfdj.html")
	
# 新增客户登记
@app.route('/Information/lfdj/new_lfdj', methods=['GET'])
def new_lfdj():
    return render_template("Information/lfdj/new_lfdj.html")
		
# 编辑客户登记
@app.route('/Information/lfdj/edit_lfdj', methods=['GET'])
def edit_lfdj():
    return render_template("Information/lfdj/edit_lfdj.html")
	
# 客户筛选-搜索
@app.route('/Information/khsx/khsx_search', methods=['GET'])
def khsx_search():
    return render_template("Information/khsx/khsx_search.html")	
	
# 客户筛选列表
@app.route('/Information/khsx/khsx', methods=['GET'])
def khsx():
    return render_template("Information/khsx/khsx.html")		
	
# 新增自动筛选配置
@app.route('/Information/khsx/new_zdsxpz', methods=['GET'])
def new_zdsxpz():
    return render_template("Information/khsx/new_zdsxpz.html")		
	
# 编辑自动筛选配置
@app.route('/Information/khsx/edit_zdsxpz', methods=['GET'])
def edit_zdsxpz():
    return render_template("Information/khsx/edit_zdsxpz.html")	
	
# 客户分配-搜索
@app.route('/Information/khfp/khfp_search', methods=['GET'])
def khfp_search():
    return render_template("Information/khfp/khfp_search.html")
	
# 客户分配列表
@app.route('/Information/khfp/khfp', methods=['GET'])
def khfp():
    return render_template("Information/khfp/khfp.html")	
		
# 客户信息管理-搜索
@app.route('/Information/khxxgl/khxxgl_search', methods=['GET'])
def khxxgl_search():
    return render_template("Information/khxxgl/khxxgl_search.html")
			
# 客户信息管理
@app.route('/Information/khxxgl/khxxgl', methods=['GET'])
def khxxgl():
    return render_template("Information/khxxgl/khxxgl.html")	
	
# 新增客户信息选择
@app.route('/Information/khxxgl/new_customer', methods=['GET'])
def new_customer():
    return render_template("Information/khxxgl/new_customer.html")
	
# 新增公司客户信息
@app.route('/Information/khxxgl/new_company_customer', methods=['GET'])
def new_company_customer():
    return render_template("Information/khxxgl/new_company_customer.html")
		
# 新增个人客户信息
@app.route('/Information/khxxgl/new_individual_customer', methods=['GET'])
def new_individual_customer():
    return render_template("Information/khxxgl/new_individual_customer.html")
	
# 编辑个人客户信息
@app.route('/Information/khxxgl/edit_individual', methods=['GET'])
def edit_individual():
    return render_template("Information/khxxgl/edit_individual.html")
		
# 编辑个人客户信息-基础信息
@app.route('/Information/khxxgl/edit_individual_customer', methods=['GET'])
def edit_individual_customer():
    return render_template("Information/khxxgl/edit_individual_customer.html")
			
# 编辑个人客户信息-我行业务往来
@app.route('/Information/khxxgl/sc_dealings', methods=['GET'])
def sc_dealings():
    return render_template("Information/khxxgl/sc_dealings.html")
				
# 编辑个人客户信息-关系人信息
@app.route('/Information/khxxgl/sc_relations', methods=['GET'])
def sc_relations():
    return render_template("Information/khxxgl/sc_relations.html")
					
# 编辑个人客户信息-经营信息
@app.route('/Information/khxxgl/sc_manage_info', methods=['GET'])
def sc_manage_info():
    return render_template("Information/khxxgl/sc_manage_info.html")
						
# 编辑个人客户信息-资产信息
@app.route('/Information/khxxgl/sc_asset_info', methods=['GET'])
def sc_asset_info():
    return render_template("Information/khxxgl/sc_asset_info.html")
							
# 编辑个人客户信息-财务信息
@app.route('/Information/khxxgl/sc_financial_affairs', methods=['GET'])
def sc_financial_affairs():
    return render_template("Information/khxxgl/sc_financial_affairs.html")
								
# 编辑个人客户信息-其他信息及附加
@app.route('/Information/khxxgl/sc_other_info', methods=['GET'])
def sc_other_info():
    return render_template("Information/khxxgl/sc_other_info.html")
								
# 贷款信息管理-搜索
@app.route('/Information/dkxx/dkxxgl_search', methods=['GET'])
def dkxxgl_search():
    return render_template("Information/dkxx/dkxxgl_search.html")
									
# 贷款信息管理列表
@app.route('/Information/dkxx/dkxxgl', methods=['GET'])
def dkxxgl():
    return render_template("Information/dkxx/dkxxgl.html")
										
# 查看贷款信息
@app.route('/Information/dkxx/dkxx', methods=['GET'])
def dkxx():
    return render_template("Information/dkxx/dkxx.html")
											
# 查看贷款信息-基础信息
@app.route('/Information/dkxx/jcxx', methods=['GET'])
def jcxx():
    return render_template("Information/dkxx/jcxx.html")
												
# 查看贷款信息-基础信息
@app.route('/Information/dkxx/hkjh', methods=['GET'])
def hkjh():
    return render_template("Information/dkxx/hkjh.html")
													
# 查看贷款信息-基础信息
@app.route('/Information/dkxx/dksqsh_info', methods=['GET'])
def dksqsh_info():
    return render_template("Information/dkxx/dksqsh_info.html")
														
# 查看贷款信息-调查表-基本情况
@app.route('/Information/dkxx/dqdcXed_jbqk', methods=['GET'])
def dqdcXed_jbqk():
    return render_template("Information/dkxx/dqdcXed_jbqk.html")
															
# 查看贷款信息-调查表-资产负债表
@app.route('/Information/dkxx/dqdcXed_zcfzb', methods=['GET'])
def dqdcXed_zcfzb():
    return render_template("Information/dkxx/dqdcXed_zcfzb.html")
																
# 查看贷款信息-调查表-交叉检验
@app.route('/Information/dkxx/dqdcXed_jcjy', methods=['GET'])
def dqdcXed_jcjy():
    return render_template("Information/dkxx/dqdcXed_jcjy.html")
																	
# 查看贷款信息-调查表-损益情况分析
@app.route('/Information/dkxx/dqdcXed_ysqkfx', methods=['GET'])
def dqdcXed_ysqkfx():
    return render_template("Information/dkxx/dqdcXed_ysqkfx.html")
																		
# 查看贷款信息-调查表-现金流分析
@app.route('/Information/dkxx/dqdcXed_xjlfx', methods=['GET'])
def dqdcXed_xjlfx():
    return render_template("Information/dkxx/dqdcXed_xjlfx.html")
																		
# 查看贷款信息-调查表-担保抵押调查表
@app.route('/Information/dkxx/dqdcXed_dbdydcb', methods=['GET'])
def dqdcXed_dbdydcb():
    return render_template("Information/dkxx/dqdcXed_dbdydcb.html")
																		
# 查看贷款信息-调查表-固定资产清单
@app.route('/Information/dkxx/dqdcXed_gdzcqd', methods=['GET'])
def dqdcXed_gdzcqd():
    return render_template("Information/dkxx/dqdcXed_gdzcqd.html")
																		
# 查看贷款信息-调查表-库存
@app.route('/Information/dkxx/dqdcXed_kc', methods=['GET'])
def dqdcXed_kc():
    return render_template("Information/dkxx/dqdcXed_kc.html")
																		
# 查看贷款信息-调查表-账款清单
@app.route('/Information/dkxx/dqdcXed_zkqd', methods=['GET'])
def dqdcXed_zkqd():
    return render_template("Information/dkxx/dqdcXed_zkqd.html")	
																		
# 查看贷款信息-审批决议
@app.route('/Information/dkxx/edit_sdhjyd', methods=['GET'])
def edit_sdhjyd():
    return render_template("Information/dkxx/edit_sdhjyd.html")
																		
# 查看贷款信息-放款信息
@app.route('/Information/dkxx/fkxx', methods=['GET'])
def fkxx():
    return render_template("Information/dkxx/fkxx.html")
	
#################################流程管理#########################################		
###########################贷款申请###############################																	
# 贷款申请-搜索
@app.route('/Process/dksq/dksq_search', methods=['GET'])
def dksq_search():
    return render_template("Process/dksq/dksq_search.html")
	
# 贷款申请
@app.route('/Process/dksq/dksq', methods=['GET'])
def dksq():
    return render_template("Process/dksq/dksq.html")
		
# 新增贷款申请
@app.route('/Process/dksq/new_dksq', methods=['GET'])
def new_dksq():
    return render_template("Process/dksq/new_dksq.html")
			
# 新增贷款申请信息
@app.route('/Process/dksq/new_dksq_info', methods=['GET'])
def new_dksq_info():
    return render_template("Process/dksq/new_dksq_info.html")
			
# 编辑贷款申请
@app.route('/Process/dksq/edit_dksq_info', methods=['GET'])
def edit_dksq_info():
    return render_template("Process/dksq/edit_dksq_info.html")

###########################贷款申请审核###############################	
# 贷款申请审核-搜索
@app.route('/Process/dksqsh/dksqsh_search', methods=['GET'])
def dksqsh_search():
    return render_template("Process/dksqsh/dksqsh_search.html")
	
# 贷款申请审核列表
@app.route('/Process/dksqsh/dksqsh', methods=['GET'])
def dksqsh():
    return render_template("Process/dksqsh/dksqsh.html")
		
# 编辑贷款申请审核
@app.route('/Process/dksqsh/edit_dksqsh', methods=['GET'])
def edit_dksqsh():
    return render_template("Process/dksqsh/edit_dksqsh.html")
			
# 编辑贷款申请审核信息
@app.route('/Process/dksqsh/edit_dksqsh_info', methods=['GET'])
def edit_dksqsh_info():
    return render_template("Process/dksqsh/edit_dksqsh_info.html")
	
###########################贷前调查###############################			
# 贷前调查-搜索
@app.route('/Process/dqdc/dqdc_search', methods=['GET'])
def dqdc_search():
    return render_template("Process/dqdc/dqdc_search.html")
	
# 贷前调查
@app.route('/Process/dqdc/dqdc', methods=['GET'])
def dqdc():
    return render_template("Process/dqdc/dqdc.html")
		
# 上传征信材料
@app.route('/Process/dqdc/credit_upload', methods=['GET'])
def credit_upload():
    return render_template("Process/dqdc/credit_upload.html")
		
# 贷前调查——微贷
@app.route('/Process/dqdc/dqdc_wd', methods=['GET'])
def dqdc_wd():
    return render_template("Process/dqdc/dqdc_wd.html")
			
# 贷前调查——微贷——资产负债表
@app.route('/Process/dqdc/dqdcWd_zcfzb', methods=['GET'])
def dqdcWd_zcfzb():
    return render_template("Process/dqdc/dqdcWd_zcfzb.html")
				
# 贷前调查——微贷——损益表
@app.route('/Process/dqdc/dqdcWd_syb', methods=['GET'])
def dqdcWd_syb():
    return render_template("Process/dqdc/dqdcWd_syb.html")
					
# 贷前调查——微贷——基本勤快
@app.route('/Process/dqdc/dqdcWd_jbqk', methods=['GET'])
def dqdcWd_jbqk():
    return render_template("Process/dqdc/dqdcWd_jbqk.html")
			
# 贷前调查——小额贷
@app.route('/Process/dqdc/dqdc_xed', methods=['GET'])
def dqdc_xed():
    return render_template("Process/dqdc/dqdc_xed.html")
				
# 贷前调查——小额贷——资产负债表
@app.route('/Process/dqdc/dqdcXed_Zcfzb', methods=['GET'])
def dqdcXed_Zcfzb():
    return render_template("Process/dqdc/dqdcXed_zcfzb.html")
					
# 贷前调查——小额贷——交叉检验
@app.route('/Process/dqdc/dqdcXed_Jcjy', methods=['GET'])
def dqdcXed_Jcjy():
    return render_template("Process/dqdc/dqdcXed_jcjy.html")
						
# 贷前调查——小额贷——损益情况分析
@app.route('/Process/dqdc/dqdcXed_Ysqkfx', methods=['GET'])
def dqdcXed_Ysqkfx():
    return render_template("Process/dqdc/dqdcXed_ysqkfx.html")
							
# 贷前调查——小额贷——现金流分析
@app.route('/Process/dqdc/dqdcXed_Xjlfx', methods=['GET'])
def dqdcXed_Xjlfx():
    return render_template("Process/dqdc/dqdcXed_xjlfx.html")
	
# 贷前调查——小额贷——担保抵押调查表
@app.route('/Process/dqdc/dqdcXed_Dbdydcb', methods=['GET'])
def dqdcXed_Dbdydcb():
    return render_template("Process/dqdc/dqdcXed_dbdydcb.html")
		
# 贷前调查——小额贷——固定资产清单
@app.route('/Process/dqdc/dqdcXed_Gdzcqd', methods=['GET'])
def dqdcXed_Gdzcqd():
    return render_template("Process/dqdc/dqdcXed_gdzcqd.html")
			
# 贷前调查——小额贷——库存
@app.route('/Process/dqdc/dqdcXed_Kc', methods=['GET'])
def dqdcXed_Kc():
    return render_template("Process/dqdc/dqdcXed_kc.html")
				
# 贷前调查——小额贷——库存
@app.route('/Process/dqdc/dqdcXed_Zkqd', methods=['GET'])
def dqdcXed_Zkqd():
    return render_template("Process/dqdc/dqdcXed_zkqd.html")
					
# 贷前调查——小额贷——基本情况
@app.route('/Process/dqdc/dqdcXed_Jbqk', methods=['GET'])
def dqdcXed_Jbqk():
    return render_template("Process/dqdc/dqdcXed_jbqk.html")	
	
###########################贷款审批分配###############################			
# 贷款审批分配-搜索
@app.route('/Process/dksp/dksp_search', methods=['GET'])
def dksp_search():
    return render_template("Process/dksp/dksp_search.html")
	
# 贷款审批分配列表
@app.route('/Process/dksp/dksp', methods=['GET'])
def dksp():
    return render_template("Process/dksp/dksp.html")
	
# 编辑贷款审批分配
@app.route('/Process/dksp/edit_dksp', methods=['GET'])
def edit_dksp():
    return render_template("Process/dksp/edit_dksp.html")
		
# 编辑贷款审批分配信息
@app.route('/Process/dksp/edit_dksp_info', methods=['GET'])
def edit_dksp_info():
    return render_template("Process/dksp/edit_dksp_info.html")

###########################审核决议###############################			
# 审核决议-搜索
@app.route('/Process/shjy/shjy_search', methods=['GET'])
def shjy_search():
    return render_template("Process/shjy/shjy_search.html")
	
# 审核决议列表
@app.route('/Process/shjy/shjy', methods=['GET'])
def shjy():
    return render_template("Process/shjy/shjy.html")
		
# 编辑审核决议
@app.route('/Process/shjy/edit_shjy', methods=['GET'])
def edit_shjy():
    return render_template("Process/shjy/edit_shjy.html")
			
# 编辑审核决议信息
@app.route('/Process/shjy/edit_Sdhjyd', methods=['GET'])
def edit_Sdhjyd():
    return render_template("Process/shjy/edit_sdhjyd.html")
	
###########################还款计划###############################			
# 还款计划-搜索
@app.route('/Process/hkjh/hkjh_search', methods=['GET'])
def hkjh_search():
    return render_template("Process/hkjh/hkjh_search.html")
	
# 还款计划列表
@app.route('/Process/hkjh/Hkjh', methods=['GET'])
def Hkjh():
    return render_template("Process/hkjh/hkjh.html")
		
# 编辑还款计划
@app.route('/Process/hkjh/edit_hkjh', methods=['GET'])
def edit_hkjh():
    return render_template("Process/hkjh/edit_hkjh.html")
		
##########################还款记录###############################
# 还款记录-搜索
@app.route('/Process/hkjl/hkjl_search', methods=['GET'])
def hkjl_search():
    return render_template("Process/hkjl/hkjl_search.html")	
	
# 还款记录列表
@app.route('/Process/hkjl/hkjl', methods=['GET'])
def hkjl():
    return render_template("Process/hkjl/hkjl.html")	
		
# 编辑还款记录
@app.route('/Process/hkjl/edit_hkjl', methods=['GET'])
def edit_hkjl():
    return render_template("Process/hkjl/edit_hkjl.html")
			
##########################贷后管理###############################
# 贷后管理-搜索
@app.route('/Process/dhgl/dhgl_search', methods=['GET'])
def dhgl_search():
    return render_template("Process/dhgl/dhgl_search.html")	
	
# 贷后管理列表
@app.route('/Process/dhgl/dhgl', methods=['GET'])
def dhgl():
    return render_template("Process/dhgl/dhgl.html")	
		
# 新增标准监控
@app.route('/Process/dhgl/new_bz', methods=['GET'])
def new_bz():
    return render_template("Process/dhgl/new_bz.html")	
	
# 非标准监控
@app.route('/Process/dhgl/fbz', methods=['GET'])
def fbz():
    return render_template("Process/dhgl/fbz.html")	
			
# 新增非标准监控
@app.route('/Process/dhgl/new_fbz', methods=['GET'])
def new_fbz():
    return render_template("Process/dhgl/new_fbz.html")	
				
# 编辑非标准监控
@app.route('/Process/dhgl/edit_fbz', methods=['GET'])
def edit_fbz():
    return render_template("Process/dhgl/edit_fbz.html")	
	
#################################进件管理#########################################	
# 进件申请列表
@app.route('/Jinjian/jinjianList', methods=['GET'])
def jinjianList():
    return render_template("Jinjian/jinjianList.html")	
	
# 新增进件申请
@app.route('/Jinjian/new_jinjian', methods=['GET'])
def new_jinjian():
    return render_template("Jinjian/new_jinjian.html")		
	
# 编辑进件申请
@app.route('/Jinjian/edit_jinjian', methods=['GET'])
def edit_jinjian():
    return render_template("Jinjian/edit_jinjian.html")	
		
# 录入打分资料—卡种选择
@app.route('/Jinjian/dfb_kzxz', methods=['GET'])
def dfb_kzxz():
    return render_template("Jinjian/dfb_kzxz.html")	
	
# 打分表列表
@app.route('/Jinjian/dfbList', methods=['GET'])
def dfbList():
    return render_template("Jinjian/dfbList.html")		
	
# 打分表信息
@app.route('/Jinjian/dfb_info', methods=['GET'])
def dfb_info():
    return render_template("Jinjian/dfb_info.html")	
	
# 打分表列表(微贷)
@app.route('/Jinjian/wd_dfbList', methods=['GET'])
def wd_dfbList():
    return render_template("Jinjian/wd_dfbList.html")		
		
# 财务数据调查
@app.route('/Jinjian/cwsjdc', methods=['GET'])
def cwsjdc():
    return render_template("Jinjian/cwsjdc.html")
						
# 财务数据调查(打印)
@app.route('/Print/dy_cwsjdc', methods=['GET'])
def dy_cwsjdc():
    return render_template("Print/dy_cwsjdc.html")
	
# 调查表
@app.route('/Jinjian/dcList', methods=['GET'])
def dcList():
    return render_template("Jinjian/dcList.html")	
		
# 调查表信息
@app.route('/Jinjian/dc_info', methods=['GET'])
def dc_info():
    return render_template("Jinjian/dc_info.html")	
			
# 调查表信息（资产负债表）
@app.route('/Jinjian/dc_zcfzb', methods=['GET'])
def dc_zcfzb():
    return render_template("Jinjian/dc_zcfzb.html")	
			
# 调查表信息（交叉检验）
@app.route('/Jinjian/dc_jcjy', methods=['GET'])
def dc_jcjy():
    return render_template("Jinjian/dc_jcjy.html")	
			
# 调查表信息（损益情况分析）
@app.route('/Jinjian/dc_ysqkfx', methods=['GET'])
def dc_ysqkfx():
    return render_template("Jinjian/dc_ysqkfx.html")	
			
# 调查表信息（现金流分析）
@app.route('/Jinjian/dc_xjlfx', methods=['GET'])
def dc_xjlfx():
    return render_template("Jinjian/dc_xjlfx.html")	
	
# 进件审批列表
@app.route('/Jinjian/jjspList', methods=['GET'])
def jjspList():
    return render_template("Jinjian/jjspList.html")	
	
# 进件审批
@app.route('/Jinjian/jjsp_info', methods=['GET'])
def jjsp_info():
    return render_template("Jinjian/jjsp_info.html")	
	
# 一级审批信息
@app.route('/Jinjian/yjsp_zxspcz', methods=['GET'])
def yjsp_zxspcz():
    return render_template("Jinjian/yjsp_zxspcz.html")	
	
# 黑名单列表
@app.route('/Jinjian/hmdList', methods=['GET'])
def hmdList():
    return render_template("Jinjian/hmdList.html")	
	
# 编辑黑名单
@app.route('/Jinjian/edit_hmd', methods=['GET'])
def edit_hmd():
    return render_template("Jinjian/edit_hmd.html")	
	
# 已持卡列表
@app.route('/Jinjian/yckxxList', methods=['GET'])
def yckxxList():
    return render_template("Jinjian/yckxxList.html")	
	
# 历史申请列表
@app.route('/Jinjian/lssqjList', methods=['GET'])
def lssqjList():
    return render_template("Jinjian/lssqjList.html")	
	
# 异常数据处理列表
@app.route('/Jinjian/ycsjclList', methods=['GET'])
def ycsjclList():
    return render_template("Jinjian/ycsjclList.html")		
	
# 打印审批表
@app.route('/Jinjian/dy_spb', methods=['GET'])
def dy_spb():
    return render_template("Jinjian/dy_spb.html")	
	
# 事件日志列表
@app.route('/Jinjian/sjrzList', methods=['GET'])
def sjrzList():
    return render_template("Jinjian/sjrzList.html")	
	
# 事件日志信息
@app.route('/Jinjian/sjrz_info', methods=['GET'])
def sjrz_info():
    return render_template("Jinjian/sjrz_info.html")
	
# 补件列表
@app.route('/Jinjian/bjList', methods=['GET'])
def bjList():
    return render_template("Jinjian/bjList.html")		
	
# 补件信息
@app.route('/Jinjian/bj_info', methods=['GET'])
def bj_info():
    return render_template("Jinjian/bj_info.html")	
	
# 照会列表
@app.route('/Jinjian/zhList', methods=['GET'])
def zhList():
    return render_template("Jinjian/zhList.html")		
	
# 照会信息
@app.route('/Jinjian/zh_info', methods=['GET'])
def zh_info():
    return render_template("Jinjian/zh_info.html")	
	
# 致电结果
@app.route('/Jinjian/zdjg', methods=['GET'])
def zdjg():
    return render_template("Jinjian/zdjg.html")		
	
# 修改产品类型
@app.route('/Jinjian/cplx', methods=['GET'])
def cplx():
    return render_template("Jinjian/cplx.html")	
	
#################################台账管理#########################################	
# 台账列表
@app.route('/Taizhang/taizhangList', methods=['GET'])
def taizhangList():
    return render_template("Taizhang/taizhangList.html")	
	
# 新增台账
@app.route('/Taizhang/new_taizhang', methods=['GET'])
def new_taizhang():
    return render_template("Taizhang/new_taizhang.html")	
#################################评分管理#########################################	
# 评分卡管理
@app.route('/Score/pfkgl', methods=['GET'])
def pfkgl():
    return render_template("Score/pfkgl.html")	

# 评分卡管理-新增
@app.route('/Score/new_pfkgl', methods=['GET'])
def new_pfkgl():
    return render_template("Score/new_pfkgl.html")	

# 评分卡管理-编辑
@app.route('/Score/edit_pfkgl', methods=['GET'])
def edit_pfkgl():
    return render_template("Score/edit_pfkgl.html")	
	
# 处理要素评分卡管理
@app.route('/Score/clyspfkgl', methods=['GET'])
def clyspfkgl():
    return render_template("Score/clyspfkgl.html")	
	
# 处理要素评分卡管理-新增
@app.route('/Score/new_clyspfkgl', methods=['GET'])
def new_clyspfkgl():
    return render_template("Score/new_clyspfkgl.html")	
	
# 处理要素评分卡管理-编辑
@app.route('/Score/edit_clyspfkgl', methods=['GET'])
def edit_clyspfkgl():
    return render_template("Score/edit_clyspfkgl.html")	
	
# 申请要素分类设置
@app.route('/Score/sqysflsz', methods=['GET'])
def sqysflsz():
    return render_template("Score/sqysflsz.html")	
	
# 申请要素分类设置-新增
@app.route('/Score/new_sqysflsz', methods=['GET'])
def new_sqysflsz():
    return render_template("Score/new_sqysflsz.html")	
	
# 申请要素分类设置-编辑
@app.route('/Score/edit_sqysflsz', methods=['GET'])
def edit_sqysflsz():
    return render_template("Score/edit_sqysflsz.html")	
	
# 申请要素专案设置
@app.route('/Score/sqyszasz', methods=['GET'])
def sqyszasz():
    return render_template("Score/sqyszasz.html")		
	
# 申请要素专案设置-新增
@app.route('/Score/new_sqyszasz', methods=['GET'])
def new_sqyszasz():
    return render_template("Score/new_sqyszasz.html")			
	
# 申请要素专案设置-编辑
@app.route('/Score/edit_sqyszasz', methods=['GET'])
def edit_sqyszasz():
    return render_template("Score/edit_sqyszasz.html")	
	
# 处理要素设置
@app.route('/Score/clyssz', methods=['GET'])
def clyssz():
    return render_template("Score/clyssz.html")		
	
# 处理要素设置-新增
@app.route('/Score/new_clyssz', methods=['GET'])
def new_clyssz():
    return render_template("Score/new_clyssz.html")			
	
# 处理要素设置-编辑
@app.route('/Score/edit_clyssz', methods=['GET'])
def edit_clyssz():
    return render_template("Score/edit_clyssz.html")	
	
# 评分参数设置
@app.route('/Score/pfcssz', methods=['GET'])
def pfcssz():
    return render_template("Score/pfcssz.html")		
	
###############################绩效管理##########################################
#####################绩效薪酬############################	
# 工时记录——搜索
@app.route('/Performance/gsjl/gsjl_search', methods=['GET'])
def gsjl_search():
    return render_template("Performance/gsjl/gsjl_search.html")	
	
# 工时记录列表
@app.route('/Performance/gsjl/gsjl', methods=['GET'])
def gsjl():
    return render_template("Performance/gsjl/gsjl.html")	
		
# 新增工时记录
@app.route('/Performance/gsjl/new_gsjl', methods=['GET'])
def new_gsjl():
    return render_template("Performance/gsjl/new_gsjl.html")
	
# 个人薪酬——搜索
@app.route('/Performance/jxxc/grxc_search', methods=['GET'])
def grxc_search():
    return render_template("Performance/jxxc/grxc_search.html")		

# 个人薪酬——列表
@app.route('/Performance/jxxc/grxc', methods=['GET'])
def grxc():
    return render_template("Performance/jxxc/grxc.html")	
	
# 薪酬查询——搜索
@app.route('/Performance/jxxc/xccx_search', methods=['GET'])
def xccx_search():
    return render_template("Performance/jxxc/xccx_search.html")	
		
# 薪酬查询列表
@app.route('/Performance/jxxc/xccx', methods=['GET'])
def xccx():
    return render_template("Performance/jxxc/xccx.html")	
		
# 业务差错统计——搜索
@app.route('/Performance/jxxc/ywcctj_search', methods=['GET'])
def ywcctj_search():
    return render_template("Performance/jxxc/ywcctj_search.html")	
			
# 业务差错统计列表
@app.route('/Performance/jxxc/ywcctj', methods=['GET'])
def ywcctj():
    return render_template("Performance/jxxc/ywcctj.html")	
				
# 新增业务差错统计
@app.route('/Performance/jxxc/new_ywcc', methods=['GET'])
def new_ywcc():
    return render_template("Performance/jxxc/new_ywcc.html")	
	
# 风险保证金——搜索
@app.route('/Performance/jxxc/fxbzj_search', methods=['GET'])
def fxbzj_search():
    return render_template("Performance/jxxc/fxbzj_search.html")	
		
# 风险保证金列表
@app.route('/Performance/jxxc/fxbzj', methods=['GET'])
def fxbzj():
    return render_template("Performance/jxxc/fxbzj.html")	
			
# 风险保证金信息
@app.route('/Performance/jxxc/fxbzj_list', methods=['GET'])
def fxbzj_list():
    return render_template("Performance/jxxc/fxbzj_list.html")	
			
# 风险保证金列表
@app.route('/Performance/jxxc/xccspz', methods=['GET'])
def xccspz():
    return render_template("Performance/jxxc/xccspz.html")		
	
#####################员工评估考核############################		
# 培训期评估——搜索
@app.route('/Performance/ygpgkh/pxqpg_search', methods=['GET'])
def pxqpg_search():
    return render_template("Performance/ygpgkh/pxqpg_search.html")	
	
# 培训期评估列表
@app.route('/Performance/ygpgkh/pxqpglist', methods=['GET'])
def pxqpglist():
    return render_template("Performance/ygpgkh/pxqpglist.html")	
		
# 课堂培训评估
@app.route('/Performance/ygpgkh/ktpxpg', methods=['GET'])
def ktpxpg():
    return render_template("Performance/ygpgkh/ktpxpg.html")	
			
# 实际操作评估
@app.route('/Performance/ygpgkh/sjczpg', methods=['GET'])
def sjczpg():
    return render_template("Performance/ygpgkh/sjczpg.html")	
				
# 最终评估
@app.route('/Performance/ygpgkh/zzpg', methods=['GET'])
def zzpg():
    return render_template("Performance/ygpgkh/zzpg.html")	
	
# 在岗评估——搜索
@app.route('/Performance/ygpgkh/zgpg_search', methods=['GET'])
def zgpg_search():
    return render_template("Performance/ygpgkh/zgpg_search.html")	
		
# 在岗评估列表
@app.route('/Performance/ygpgkh/zgpglist', methods=['GET'])
def zgpglist():
    return render_template("Performance/ygpgkh/zgpglist.html")	
			
# 客户经理KPI
@app.route('/Performance/ygpgkh/khjlKPI', methods=['GET'])
def khjlKPI():
    return render_template("Performance/ygpgkh/khjlKPI.html")	
				
# 后台岗KPI
@app.route('/Performance/ygpgkh/htgKPI', methods=['GET'])
def htgKPI():
    return render_template("Performance/ygpgkh/htgKPI.html")	
	
#####################客户经理管理############################	
# 级别定义——搜索
@app.route('/Performance/khjlgl/jbdy_search', methods=['GET'])
def jbdy_search():
    return render_template("Performance/khjlgl/jbdy_search.html")	
	
# 级别定义列表
@app.route('/Performance/khjlgl/jbdy', methods=['GET'])
def jbdy():
    return render_template("Performance/khjlgl/jbdy.html")	
	
# 层级查询——搜索
@app.route('/Performance/khjlgl/cjcx_search', methods=['GET'])
def cjcx_search():
    return render_template("Performance/khjlgl/cjcx_search.html")	
		
# 层级查询列表
@app.route('/Performance/khjlgl/cjcx', methods=['GET'])
def cjcx():
    return render_template("Performance/khjlgl/cjcx.html")		
			
# 层级评估
@app.route('/Performance/khjlgl/cjpg', methods=['GET'])
def cjpg():
    return render_template("Performance/khjlgl/cjpg.html")	
	
# 晋级审核——搜索
@app.route('/Performance/khjlgl/jjsh_search', methods=['GET'])
def jjsh_search():
    return render_template("Performance/khjlgl/jjsh_search.html")
		
# 晋级审核列表
@app.route('/Performance/khjlgl/jjshlist', methods=['GET'])
def jjshlist():
    return render_template("Performance/khjlgl/jjshlist.html")
	
###############################统计报表##########################################	
# 客户
@app.route('/Report/kh', methods=['GET'])
def kh():
    return render_template("Report/kh.html")
	
# 贷款根据状态分类
@app.route('/Report/dkgjztfl', methods=['GET'])
def dkgjztfl():
    return render_template("Report/dkgjztfl.html")
	
# 贷款根据状态分类——1.已发放贷款
@app.route('/Report/dkgjztfl_1', methods=['GET'])
def dkgjztfl_1():
    return render_template("Report/dkgjztfl_1.html")
	
# 贷款根据状态分类——1.已发放贷款
@app.route('/Report/dkgjztfl_1_search', methods=['GET'])
def dkgjztfl_1_search():
    return render_template("Report/dkgjztfl_1_search.html")
	
# 贷款根据状态分类——2.被拒绝的贷款
@app.route('/Report/dkgjztfl_2', methods=['GET'])
def dkgjztfl_2():
    return render_template("Report/dkgjztfl_2.html")
	
# 贷款根据状态分类——2.被拒绝的贷款
@app.route('/Report/dkgjztfl_2_search', methods=['GET'])
def dkgjztfl_2_search():
    return render_template("Report/dkgjztfl_2_search.html")
	
# 贷款根据状态分类——3.贷后变更的贷款
@app.route('/Report/dkgjztfl_3', methods=['GET'])
def dkgjztfl_3():
    return render_template("Report/dkgjztfl_3.html")
	
# 贷款根据状态分类——3.贷后变更的贷款
@app.route('/Report/dkgjztfl_3_search', methods=['GET'])
def dkgjztfl_3_search():
    return render_template("Report/dkgjztfl_3_search.html")
		
# 贷款根据状态分类——4.到期终止的贷款
@app.route('/Report/dkgjztfl_4', methods=['GET'])
def dkgjztfl_4():
    return render_template("Report/dkgjztfl_4.html")
	
# 贷款根据状态分类——4.到期终止的贷款
@app.route('/Report/dkgjztfl_4_search', methods=['GET'])
def dkgjztfl_4_search():
    return render_template("Report/dkgjztfl_4_search.html")
	
# 信贷工作流程列表
@app.route('/Report/xdgzlclb', methods=['GET'])
def xdgzlclb():
    return render_template("Report/xdgzlclb.html")
		
# 批次生成报表查询
@app.route('/Report/pcscbbcx', methods=['GET'])
def pcscbbcx():
    return render_template("Report/pcscbbcx.html")
			
# 总行管理类报表
@app.route('/Report/zhgllbb', methods=['GET'])
def zhgllbb():
    return render_template("Report/zhgllbb.html")
				
# 折线图
@app.route('/Report/line', methods=['GET'])
def line():
    return render_template("Report/line.html")	
					
# 柱状图
@app.route('/Report/bar', methods=['GET'])
def bar():
    return render_template("Report/bar.html")
						
# 饼图
@app.route('/Report/pie', methods=['GET'])
def pie():
    return render_template("Report/pie.html")

###############################系统工具##########################################							
# 饼图
@app.route('/Tools/hkjhjsgj', methods=['GET'])
def hkjhjsgj():
    return render_template("Tools/hkjhjsgj.html")

###############################系统管理##########################################	
# 业务参数配置
@app.route('/System/ywcspz', methods=['GET'])
def ywcspz():
    return render_template("System/ywcspz.html")
	
# 接口配置
@app.route('/System/jkpz', methods=['GET'])
def jkpz():
    return render_template("System/jkpz.html")
		
# 日终日结
@app.route('/System/rzrj', methods=['GET'])
def rzrj():
    return render_template("System/rzrj.html")
			
# 数据字典
@app.route('/System/sjzd', methods=['GET'])
def sjzd():
    return render_template("System/sjzd.html")
				
# 机构管理
@app.route('/System/jggl', methods=['GET'])
def jggl():
    return render_template("System/jggl.html")
					
# 新增机构
@app.route('/System/new_jggl', methods=['GET'])
def new_jggl():
    return render_template("System/new_jggl.html")
						
# 使用者管理
@app.route('/System/syzgl', methods=['GET'])
def syzgl():
    return render_template("System/syzgl.html")
							
# 新增使用者
@app.route('/System/new_user', methods=['GET'])
def new_user():
    return render_template("System/new_user.html")
								
# 编辑使用者
@app.route('/System/edit_user', methods=['GET'])
def edit_user():
    return render_template("System/edit_user.html")
	
# 角色权限管理
@app.route('/System/jsqxgl', methods=['GET'])
def jsqxgl():
    return render_template("System/jsqxgl.html")
	
# 新增角色权限
@app.route('/System/new_role', methods=['GET'])
def new_role():
    return render_template("System/new_role.html")
	
# 编辑角色权限
@app.route('/System/edit_role', methods=['GET'])
def edit_role():
    return render_template("System/edit_role.html")