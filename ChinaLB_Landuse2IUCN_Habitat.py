dic_erdiao = { 
"011":"水田",
"012":"水浇地",
"013":"旱地",
"021":"果园",
"022":"茶园",
"023":"其他园地",
"031":"有林地",
"032":"灌木林地",
"033":"其他林地",
"041":"天然草地",
"042":"人工牧草地",
"043":"其他草地",
"051":"批发零售用地",
"052":"住宿餐饮用地",
"053":"商务金融用地",
"054":"其他商服用地",
"061":"工业用地",
"062":"采矿用地",
"063":"仓储用地",
"071":"城镇住宅用地",
"072":"农村宅基地",
"081":"机关团体用地",
"082":"新闻出版用地",
"083":"科教用地",
"084":"医卫慈善用地",
"085":"文体娱乐用地",
"086":"公共设施用地",
"087":"公园与绿地",
"088":"风景名胜设施用地",
"091":"军事设施用地",
"092":"使领馆用地",
"093":"监教场所用地",
"094":"宗教用地",
"095":"殡葬用地",
"101":"铁路用地",
"102":"公路用地",
"103":"街巷用地",
"104":"农村道路",
"105":"机场用地",
"106":"港口码头用地",
"107":"管道运输用地",
"111":"河流水面",
"112":"湖泊水面",
"113":"水库水面",
"114":"坑塘水面",
"115":"沿海滩涂",
"116":"内陆滩涂",
"117":"沟渠",
"118":"水工建筑用地",
"119":"冰川及永久积雪",
"121":"空闲地",
"122":"设施农用地",
"123":"田坎",
"124":"盐碱地",
"125":"沼泽地",
"126":"沙地",
"127":"裸地",
"201":"城市",
"202":"建制镇",
"203":"村庄",
"204":"采矿用地",
"205":"风景名胜及特殊用地",
}

dic_erdiao_r = dict(map(lambda t:(t[1],t[0]),li.items()))
# dic.get(!YDDM!)
# dic_r.get(!地类名称!)
# 2007年7月1日启动第二次土地调查工作，采用土地利用分类国家标准
# 以2009年12月31日为标准时点汇总数据
# ArcGIS字段计算时，需在中文后添加.decode('utf-8')，形如"205":"风景名胜及特殊用地".decode('utf-8')

dic_erdiao2iucn = {
"011":"15.7",
"012":"14.1",
"013":"14.1",
"021":"14.3",
"022":"14.3",
"023":"14.3",
"031":"1.5/1.6",
"032":"3.5/3.6",
"033":"1.5/1.6",
"041":"4.5/4.6/4.7",
"042":"14.2",
"043":"4.5/4.7",
"051":"14.5",
"052":"14.5",
"053":"14.5",
"054":"14.5",
"061":"14.5",
"062":"14.5",
"063":"14.5",
"071":"14.5",
"072":"14.5",
"081":"14.5",
"082":"14.5",
"083":"14.5",
"084":"14.5",
"085":"14.5",
"086":"14.5",
"087":"14.4/14.5/14.6",
"088":"14.5",
"091":"14.5",
"092":"14.5",
"093":"14.5",
"094":"14.5",
"095":"14.5",
"101":"14.5",
"102":"14.5",
"103":"14.5",
"104":"14.5",
"105":"14.5",
"106":"14.5",
"107":"14.5",
"111":"5.1/5.2",
"112":"5.5/5.6",
"113":"15.1",
"114":"15.2/15.3",
"115":"12.4",
"116":"5.4",
"117":"15.9",
"118":"14.5",
"119":"8.3",
"121":"14.5",
"122":"14.5",
"123":"14.1",
"124":"5.15/5.16/5.17/12.5",
"125":"5.4",
"126":"8",
"127":"6/8",
"201":"14.5",
"202":"14.5",
"203":"14.5",
"204":"14.5",
"205":"14.5",
}

dic_iucn3_1 = {

}