#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/15 21:19
# @Author  : RookieDay
# @Site    : 
# @File    : yamltest.py
# @Software: PyCharm Community Edition
import yaml,json

lst = '{"success":true,"requestId":null,"msg":null,"resubmitToken":null,"content":{"pageNo":1,"pageSize":15,"hrInfoMap":{"3604550":{"canTalk":true,"userId":916967,"phone":null,"positionName":"HR","receiveEmail":null,"realName":"微咔世纪","portrait":"i/image/M00/6E/D8/CgpFT1m5FK2AQwgaAAAfV2gjs-U890.jpg","userLevel":"G1"},"3513312":{"canTalk":true,"userId":1842805,"phone":null,"positionName":"微贷网","receiveEmail":null,"realName":"rxwu@weidai.com","portrait":"i/image/M00/62/6C/CgpFT1mdJw2AXEqxAAA-PxAhbfw357.jpg","userLevel":"G1"},"3123853":{"canTalk":true,"userId":1369370,"phone":null,"positionName":"hr","receiveEmail":null,"realName":"hr","portrait":"i/image/M00/14/D4/CgqKkVbqTISAZAL9AAAtZ3zrZo4984.jpg","userLevel":"G1"},"657586":{"canTalk":true,"userId":1393556,"phone":null,"positionName":"","receiveEmail":null,"realName":"hrbp@dooioo.com","portrait":null,"userLevel":"G1"},"3473754":{"canTalk":true,"userId":8615393,"phone":null,"positionName":"HR","receiveEmail":null,"realName":"Ella.sun","portrait":"i/image/M00/5B/13/CgpFT1mNn4yAHIm_AABGdwIlCjE337.png","userLevel":"G1"},"3590112":{"canTalk":true,"userId":5983683,"phone":null,"positionName":"招聘专员","receiveEmail":null,"realName":"liuhong30142","portrait":"i/image2/M00/0D/21/CgotOVnizTWAFidfAAEJWp2A1vk405.jpg","userLevel":"G1"},"3699715":{"canTalk":true,"userId":827864,"phone":null,"positionName":"招聘主管","receiveEmail":null,"realName":"linying@sunland","portrait":"i/image/M00/4C/A3/CgpFT1lwdMuAboT6AABUbM-Vr9s980.jpg","userLevel":"G1"},"3681436":{"canTalk":true,"userId":2117266,"phone":null,"positionName":"HR","receiveEmail":null,"realName":"tanghuijun@ishumei.com","portrait":"i/image/M00/4B/CC/CgpEMllnaAuARvblAAAgJXYyQFE826.jpg","userLevel":"G1"},"3557942":{"canTalk":true,"userId":8085298,"phone":null,"positionName":"","receiveEmail":null,"realName":"拉勾用户y.yj","portrait":null,"userLevel":"G1"},"3347946":{"canTalk":true,"userId":7766650,"phone":null,"positionName":null,"receiveEmail":null,"realName":"king","portrait":null,"userLevel":"G1"},"2071202":{"canTalk":true,"userId":2162767,"phone":null,"positionName":"","receiveEmail":null,"realName":"王怡","portrait":null,"userLevel":"G1"},"3310790":{"canTalk":true,"userId":651726,"phone":null,"positionName":"运营经理","receiveEmail":null,"realName":"guchuankeji@163","portrait":null,"userLevel":"G1"},"2530164":{"canTalk":true,"userId":38272,"phone":null,"positionName":"招聘经理","receiveEmail":null,"realName":"安晓婷","portrait":"i/image2/M00/02/8B/CgoB5lnAwqWABQMEAAEDOuet4Ks774.jpg","userLevel":"G1"},"3058921":{"canTalk":true,"userId":757541,"phone":null,"positionName":"HR","receiveEmail":null,"realName":"网营","portrait":"i/image/M00/69/6F/CgpEMlmlWVOAfweIAAHITbrf82g406.png","userLevel":"G1"},"3661386":{"canTalk":true,"userId":1005253,"phone":null,"positionName":"数据资源管理组组长","receiveEmail":null,"realName":"郑艳莹","portrait":"i/image/M00/5C/44/CgpFT1mRN3-Af4HcAAi_FVfYgd8760.png","userLevel":"G1"}},"positionResult":{"totalCount":2206,"resultSize":15,"locationInfo":{"city":null,"district":null,"queryByGisCode":false,"businessZone":null,"locationCode":null},"queryAnalysisInfo":{"positionName":"数据分析","companyName":null,"usefulCompany":false,"industryName":null},"strategyProperty":{"name":"dm-csearch-useUserInterest","id":0},"hotLabels":null,"result":[{"createTime":"2017-10-13 10:59:15","companyId":165939,"positionId":3557942,"positionName":"资深数据分析师","education":"本科","city":"杭州","financeStage":"成长型(不需要融资)","companyShortName":"橙鹰","companyLogo":"i/image/M00/62/D3/CgpEMlmVb3iAFU6AAACDJlHBp1Y023.png","salary":"15k-30k","industryField":"数据服务","district":"余杭区","positionAdvantage":"阿里巴巴,大数据,蓝海,牛人多","companyLabelList":["年底双薪","带薪年假","午餐补助","定期体检"],"jobNature":"全职","workYear":"5-10年","approve":1,"positionLables":["信息安全","大数据","数据挖掘","SPSS"],"industryLables":["信息安全","大数据","数据挖掘","SPSS"],"publisherId":8085298,"companySize":"150-500人","businessZones":["仓前"],"score":0,"formatCreateTime":"2天前发布","companyFullName":"杭州橙鹰数据技术有限公司","adWord":0,"imState":"disabled","lastLogin":1507688941000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发/测试/运维类","secondType":"数据开发","isSchoolJob":0},{"createTime":"2017-10-12 16:30:32","companyId":33618,"positionId":3513312,"positionName":"数据分析师","education":"本科","city":"杭州","financeStage":"成熟型(C轮)","companyShortName":"微贷网","companyLogo":"i/image/M00/9A/54/CgqKkVihUt2ABzkYAAAPLLiT2Ig630.jpg","salary":"14k-28k","industryField":"金融","district":"江干区","positionAdvantage":"金融,数据分析,业务敏感","companyLabelList":["年底双薪","专项奖金","绩效奖金","岗位晋升"],"jobNature":"全职","workYear":"3-5年","approve":1,"positionLables":["金融","高级","图像处理","数据挖掘"],"industryLables":["金融","高级","图像处理","数据挖掘"],"publisherId":1842805,"companySize":"2000人以上","businessZones":null,"score":0,"formatCreateTime":"3天前发布","companyFullName":"微贷（杭州）金融信息服务有限公司","adWord":0,"imState":"threeDays","lastLogin":1507886141000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发/测试/运维类","secondType":"数据开发","isSchoolJob":0},{"createTime":"2017-09-30 16:32:28","companyId":3422,"positionId":3473754,"positionName":"数据分析师","education":"本科","city":"上海","financeStage":"成熟型(C轮)","companyShortName":"英语流利说","companyLogo":"i/image/M00/4D/EE/CgpEMllsh2iAJ_u8AAAx6RdgCFY178.png","salary":"15k-30k","industryField":"移动互联网,教育","district":"杨浦区","positionAdvantage":"N+1奖金,硅谷系,私厨三餐,顶尖团队","companyLabelList":["弹性工作","五险一金","年度旅游","年底双薪"],"jobNature":"全职","workYear":"不限","approve":1,"positionLables":["高级","大数据","数据挖掘","R"],"industryLables":[],"publisherId":8615393,"companySize":"500-2000人","businessZones":["周家嘴路","和平公园"],"score":0,"formatCreateTime":"2017-09-30","companyFullName":"上海流利说信息技术有限公司","adWord":0,"imState":"threeDays","lastLogin":1507899726000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发/测试/运维类","secondType":"数据开发","isSchoolJob":0},{"createTime":"2017-10-06 14:23:19","companyId":147,"positionId":3661386,"positionName":"数据分析师","education":"本科","city":"北京","financeStage":"成熟型(D轮及以上)","companyShortName":"拉勾网","companyLogo":"i/image/M00/76/40/Cgp3O1g1TNOAB2yxAAA9bQUyc4g814.png","salary":"15k-20k","industryField":"企业服务,招聘","district":"海淀区","positionAdvantage":"发展空间、免费午晚餐","companyLabelList":["五险一金","弹性工作","带薪年假","免费两餐"],"jobNature":"全职","workYear":"3-5年","approve":1,"positionLables":["Tableau"],"industryLables":[],"publisherId":1005253,"companySize":"150-500人","businessZones":["苏州街","中关村","万泉河"],"score":0,"formatCreateTime":"2017-10-06","companyFullName":"北京拉勾网络技术有限公司","adWord":0,"imState":"today","lastLogin":1508044933000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"产品/需求/项目类","secondType":"数据分析","isSchoolJob":0},{"createTime":"2017-10-13 11:56:15","companyId":159688,"positionId":3347946,"positionName":"数据分析","education":"本科","city":"上海","financeStage":"成长型(A轮)","companyShortName":"口袋理财","companyLogo":"i/image/M00/7A/E1/Cgp3O1hA4naAC6EyAAAUFvwNubM603.jpg","salary":"15k-25k","industryField":"金融,移动互联网","district":"长宁区","positionAdvantage":"五险一金,年终双薪","companyLabelList":["年底双薪","绩效奖金","年终分红","带薪年假"],"jobNature":"全职","workYear":"3-5年","approve":1,"positionLables":["金融","支付","可视化","风控","量化"],"industryLables":["金融","支付","可视化","风控","量化"],"publisherId":7766650,"companySize":"150-500人","businessZones":null,"score":0,"formatCreateTime":"2天前发布","companyFullName":"上海鱼耀金融信息服务有限公司","adWord":0,"imState":"disabled","lastLogin":1507866983000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"产品/需求/项目类","secondType":"数据分析","isSchoolJob":0},{"createTime":"2017-10-15 10:53:39","companyId":16831,"positionId":3590112,"positionName":"数据挖掘/数据分析","education":"本科","city":"佛山","financeStage":"成熟型(不需要融资)","companyShortName":"武汉佰钧成技术有限公司","companyLogo":"i/image/M00/02/AB/CgqKkVaXX_6AaLKaAAAX52Kvjjg750.jpg","salary":"20k-25k","industryField":"移动互联网","district":"顺德区","positionAdvantage":"大小周,六险一金,环境好","companyLabelList":["带薪年假","计算机软件","管理规范","定期体检"],"jobNature":"全职","workYear":"3-5年","approve":1,"positionLables":["物流","大数据","SPSS","sas"],"industryLables":["物流","大数据","SPSS","sas"],"publisherId":5983683,"companySize":"2000人以上","businessZones":null,"score":0,"formatCreateTime":"10:53发布","companyFullName":"武汉佰钧成技术有限责任公司","adWord":0,"imState":"today","lastLogin":1508035981000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发/测试/运维类","secondType":"数据开发","isSchoolJob":0},{"createTime":"2017-10-15 19:24:39","companyId":35713,"positionId":657586,"positionName":"数据分析师","education":"硕士","city":"上海","financeStage":"成长型(B轮)","companyShortName":"链家上海研发中心","companyLogo":"image1/M00/45/B9/Cgo8PFXcJ-OAdN7iAAGgbRX9H0g507.png","salary":"10k-19k","industryField":"企业服务","district":"静安区","positionAdvantage":"万亿级O2O平台 一年两次调薪 半年度奖金","companyLabelList":["技能培训","带薪年假","年度旅游","岗位晋升"],"jobNature":"全职","workYear":"1-3年","approve":1,"positionLables":["大数据"],"industryLables":[],"publisherId":1393556,"companySize":"500-2000人","businessZones":["吴江路","上海电视台","南京西路"],"score":0,"formatCreateTime":"19:24发布","companyFullName":"德佑房地产经纪有限公司","adWord":0,"imState":"today","lastLogin":1508066256000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"市场与销售","secondType":"市场/营销","isSchoolJob":0},{"createTime":"2017-10-14 01:13:19","companyId":82991,"positionId":3681436,"positionName":"数据分析师","education":"本科","city":"北京","financeStage":"成长型(A轮)","companyShortName":"数美","companyLogo":"i/image/M00/76/C2/CgqKkVg2fVCASEreAABS01Upo_A221.jpg","salary":"15k-25k","industryField":"企业服务,数据服务","district":"朝阳区","positionAdvantage":"大牛如云,技术氛围,大牛云集,待遇给力","companyLabelList":["年底双薪","大数据","带薪年假","通讯津贴"],"jobNature":"全职","workYear":"1-3年","approve":1,"positionLables":["大数据","数据挖掘"],"industryLables":[],"publisherId":2117266,"companySize":"150-500人","businessZones":["望京","来广营"],"score":0,"formatCreateTime":"1天前发布","companyFullName":"北京数美时代科技有限公司","adWord":0,"imState":"today","lastLogin":1508060582000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发/测试/运维类","secondType":"数据开发","isSchoolJob":0},{"createTime":"2017-10-15 18:40:28","companyId":3954,"positionId":2530164,"positionName":"数据分析师","education":"本科","city":"北京","financeStage":"成熟型(C轮)","companyShortName":"杏树林","companyLogo":"i/image/M00/2E/98/CgpFT1k2cu-Ae5eNAAEDTPHkf_A479.jpg","salary":"15k-20k","industryField":"移动互联网,医疗健康","district":"东城区","positionAdvantage":"团队氛围好,学习空间大,六险一金","companyLabelList":["A类人才","股票期权","带薪年假","年度旅游"],"jobNature":"全职","workYear":"3-5年","approve":1,"positionLables":["医疗健康","MySQL","python"],"industryLables":["医疗健康","MySQL","python"],"publisherId":38272,"companySize":"150-500人","businessZones":["广渠门"],"score":0,"formatCreateTime":"18:40发布","companyFullName":"杏树林信息技术（北京）有限公司","adWord":0,"imState":"today","lastLogin":1508070151000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"运营","secondType":"运营","isSchoolJob":0},{"createTime":"2017-10-13 08:37:55","companyId":36984,"positionId":3310790,"positionName":"数据分析","education":"不限","city":"天津","financeStage":"成长型(不需要融资)","companyShortName":"谷川联行","companyLogo":"image1/M00/00/59/CgYXBlTUXS6AM71tAABaGk6uIAM528.jpg","salary":"8k-10k","industryField":"电子商务","district":"和平区","positionAdvantage":"加班补贴,年底奖金","companyLabelList":["年底双薪","技能培训","带薪年假","绩效奖金"],"jobNature":"全职","workYear":"不限","approve":1,"positionLables":["中级","数据挖掘","大数据","BI","数据开发"],"industryLables":[],"publisherId":651726,"companySize":"50-150人","businessZones":null,"score":0,"formatCreateTime":"2天前发布","companyFullName":"谷川联行有限公司","adWord":0,"imState":"today","lastLogin":1508060518000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发/测试/运维类","secondType":"数据开发","isSchoolJob":0},{"createTime":"2017-10-15 19:56:01","companyId":212032,"positionId":3699715,"positionName":"数据分析师/BI","education":"本科","city":"广州","financeStage":"成熟型(D轮及以上)","companyShortName":"尚德机构","companyLogo":"i/image/M00/54/31/CgpEMll4bayAfOV7AAAeSuy3bJc944.jpg","salary":"5k-7k","industryField":"教育","district":"天河区","positionAdvantage":"五险一金,周末双休,节日福利,免费学习","companyLabelList":["年底双薪","年终分红","绩效奖金","专项奖金"],"jobNature":"全职","workYear":"不限","approve":1,"positionLables":["高级","大数据","专员","助理"],"industryLables":[],"publisherId":827864,"companySize":"2000人以上","businessZones":["天河公园","棠下","天河公园"],"score":0,"formatCreateTime":"19:56发布","companyFullName":"北京尚德在线教育科技有限公司","adWord":0,"imState":"today","lastLogin":1508068554000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"产品/需求/项目类","secondType":"数据分析","isSchoolJob":0},{"createTime":"2017-10-13 14:41:31","companyId":40823,"positionId":3058921,"positionName":"数据分析师","education":"本科","city":"杭州","financeStage":"上市公司","companyShortName":"网营科技","companyLogo":"i/image/M00/83/FB/CgqKkVhbUdaAMGYIAABvZcn5gmQ521.jpg","salary":"8k-10k","industryField":"电子商务","district":"西湖区","positionAdvantage":"周末双休,五险一金,活动丰富,氛围超嗨","companyLabelList":["五险一金","周末双休","午餐补助","晚餐补助"],"jobNature":"全职","workYear":"1-3年","approve":1,"positionLables":["电商","高级","SPSS","数据管理"],"industryLables":["电商","高级","SPSS","数据管理"],"publisherId":757541,"companySize":"150-500人","businessZones":["西溪"],"score":0,"formatCreateTime":"2天前发布","companyFullName":"杭州网营科技股份有限公司","adWord":0,"imState":"threeDays","lastLogin":1507884104000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"运营/编辑/客服","secondType":"运营","isSchoolJob":0},{"createTime":"2017-10-13 11:18:14","companyId":72030,"positionId":2071202,"positionName":"数据分析师","education":"本科","city":"上海","financeStage":"成长型(A轮)","companyShortName":"FlowerPlus","companyLogo":"i/image/M00/4B/9E/CgpEMllnKaCAVxuDAAAYcZvs2Sc597.png","salary":"15k-25k","industryField":"O2O","district":"嘉定区","positionAdvantage":"领导nice,氛围轻松","companyLabelList":["鲜花订阅","简单高效","行业颠覆","迅速发展"],"jobNature":"全职","workYear":"3-5年","approve":1,"positionLables":["大数据"],"industryLables":[],"publisherId":2162767,"companySize":"150-500人","businessZones":null,"score":0,"formatCreateTime":"2天前发布","companyFullName":"上海分尚网络科技有限公司","adWord":0,"imState":"today","lastLogin":1508059309000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"设计","secondType":"用户研究","isSchoolJob":0},{"createTime":"2017-10-13 11:00:56","companyId":54974,"positionId":3123853,"positionName":"数据分析","education":"本科","city":"成都","financeStage":"成长型(不需要融资)","companyShortName":"文轩在线","companyLogo":"image1/M00/0D/91/CgYXBlT4E46ALUlsAAC08rgIGEY907.png","salary":"6k-8k","industryField":"电子商务","district":"金牛区","positionAdvantage":"知名电商,数据分析","companyLabelList":["节日礼物","园林式办公","带薪年假","绩效奖金"],"jobNature":"全职","workYear":"1-3年","approve":1,"positionLables":["商业","大数据","数据挖掘","SPSS"],"industryLables":[],"publisherId":1369370,"companySize":"150-500人","businessZones":["沙河源","双水碾","凤凰山"],"score":0,"formatCreateTime":"2天前发布","companyFullName":"四川文轩在线电子商务有限公司","adWord":0,"imState":"threeDays","lastLogin":1507881014000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"产品/需求/项目类","secondType":"数据分析","isSchoolJob":0},{"createTime":"2017-10-14 11:03:14","companyId":47413,"positionId":3604550,"positionName":"数据分析师","education":"不限","city":"广州","financeStage":"成长型(A轮)","companyShortName":"Wecut","companyLogo":"i/image/M00/81/DF/CgqKkVhUskiAJgIQAAAvPiGSBvg385.png","salary":"8k-15k","industryField":"移动互联网,社交网络","district":"海珠区","positionAdvantage":"绩效期权,13薪,六险一金","companyLabelList":["年度旅游","萌妹纸","股票期权","绩效奖金"],"jobNature":"全职","workYear":"1-3年","approve":1,"positionLables":["数据挖掘","SPSS"],"industryLables":[],"publisherId":916967,"companySize":"15-50人","businessZones":["琶洲","官洲"],"score":0,"formatCreateTime":"1天前发布","companyFullName":"广州微咔世纪信息科技有限公司","adWord":0,"imState":"threeDays","lastLogin":1507977498000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"产品/需求/项目类","secondType":"数据分析","isSchoolJob":0}]}},"code":0}'
print(yaml.safe_load(lst))

list_org = '["a", "b"]'
print(json.loads(list_org))
print(yaml.safe_load(list_org))
