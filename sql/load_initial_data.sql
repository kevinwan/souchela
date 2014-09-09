
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


# 导入初始汽车配置参数数据
insert into souche.carmodel_config_parameter(para_cat, para_name, para_value, isdefault, model, detail_model)
select para_cat, para_name, para_value, isdefault, global_slug, detail_model_slug from pingjia.open_cat_detail
where status='Y';


