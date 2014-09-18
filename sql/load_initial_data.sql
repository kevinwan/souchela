
# 导入初始省份数据
insert into souche.souche_province (name, slug, pinyin)
select name, slug, pinyin from pingjia.open_city
where parent =0;


# 导入初始城市数据
insert into souche.souche_city (name, slug, province, pinyin, quhao, priority, longitude, latitude)
select c.name, c.slug, p.name, c.pinyin, c.quhao, c.priority, c.longitude, c.latitude
from pingjia.open_city p, pingjia.open_city c
where p.id=c.parent;


# 导入初始汽车品牌数据
insert into souche.carmodel_brand(name, slug, logo_img, first_letter, pinyin, keywords)
select name, slug, logo_img, first_letter, pinyin, keywords from pingjia.open_category
where parent is null and status='Y';


# 导入初始汽车型号数据
insert into souche.carmodel_model(name, slug, brand, logo_img, pinyin, manufactor, classification, keywords, attribute)
select name, slug, parent, logo_img, pinyin, mum, classified, keywords, attribute from pingjia.open_category
where parent is not null and status='Y';


# 导入初始汽车详细型号数据
insert into souche.carmodel_detail_model(name, slug, model, price_bn, year, volume)
select detail_model, detail_model_slug, global_slug, price_bn, year, volume from pingjia.open_model_detail
where status='Y';

update souche.carmodel_detail_model a, pingjia.export_vehicle_model_for_youxinpai_version_copy b
set a.emission_standard=b.`排放标准`
where a.slug=b.detail_model_slug;


# 导入初始汽车配置参数数据
insert into souche.carmodel_config_parameter(para_cat, para_name, para_value, isdefault, model, detail_model)
select para_cat, para_name, para_value, isdefault, global_slug, detail_model_slug from pingjia.open_cat_detail
where status='Y';

update carmodel_config_parameter
set kind='P'
where para_cat in ('主要参数', '内部尺寸', '发动机', '发动机/变速箱', '变速器', '变速箱', '基本信息', '基本参数', '基本性能', '外部尺寸', '底盘/车轮制动', '底盘操控', '底盘转向', '性能参数', '燃油&发动机', '电动机', '越野性能', '车型结构', '车身', '车轮制动', '车辆基本信息', '轮胎轮毂');

