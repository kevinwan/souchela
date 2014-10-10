$(function(){
	var plateStart =  "#plate-start-time .start-time";
	var plateEnd = "#plate-end-time .end-time";
	var carMileEle = "#car-mile";
	var controlEle = "#car-control";
	
	(function(){
		if ($(plateEnd).val() === '') {
			var date = new Date(),
				thisYear = date.getFullYear();
				
			$(plateEnd).val(thisYear)
		}
	})();
	
	//上牌时间下拉框生成
	var TimePlate = function(inputEle) {
		this.init(inputEle);
	};
	
	TimePlate.prototype = new DropDownList();

	
	//里程
	var CarMileList = function(inputEle) {
		this.init(inputEle);
	};
	
	CarMileList.prototype = new DropDownList();
	
	CarMileList.prototype.setList = function(start,end,step) {
		step = step ? step : 1;
		for (var i=start; i<=end; i+=step) {
			var a = $("<a>",{
				"html" : i+"万公里内",
				"href" : this.SetATag.setUrl(this.url,"mile","0-"+i)
			});
			
			var li = $("<li>",{ "html":a });
			$(this.listBox).append(li);
		}
		
		var a = $("<a>",{
			"html" : "不限",
			"href" : this.SetATag.setUrl(this.url,"mile","")
		});
		var li = $("<li>",{"html" : a});
		
		$(this.listBox).append(li);
	};
	
	var CarControlList = function(inputEle) {
		this.init(inputEle);
	};

	CarControlList.prototype = new DropDownList();
	CarControlList.prototype.setList = function() {
		var html;
		
		for (var i=0; i<3; i++) {
			if (i==0) {
				html = "自动";
			} else if(i==1) {
				html = "手动";
			}else {
				html = "不限";
			}
			
			var a = $("<a>",{
				"href": this.SetATag.setUrl(this.url,"control",html),
				"html": html
			});
			
			var li = $("<li>",{"html":a});
			$(this.listBox).append(li);
		}
	};
		
	var StartTimePlate = new TimePlate(plateStart);
	var EndTimePlate = new TimePlate(plateEnd);
	var CarMile = new CarMileList(carMileEle);
	var CarControl = new CarControlList(controlEle);
	var BrandList = new SetBrandList();
	var SelectSlug = new DropDownList();
	
	function setPlateYear() {
		var $endYear = $("#plate-end-time .end-time"),
			$startYear = $("#plate-start-time .start-time"),
			$endList = $("#plate-end-time .end-time").parent().find("div"),
			$startList = $("#plate-start-time .start-time").parent().find("div");
			
		var myDate = new Date();
		var thisYear = myDate.getFullYear();
		var end = thisYear-15;
		var setTag = new SetGetParameter();
		var endYear = $("#plate-end-time .end-time").val();
		var startYear = $("#plate-start-time .start-time").val();
		var currentUrl = window.location.href;
		
		startYear = startYear === "" ? end : startYear;
		
		for (var i=endYear-1; i>=end; i--) {
			var a = $("<a>",{
				"html" : i+"年",
				"href" : setTag.setUrl(currentUrl,"year",i+"-"+endYear)
			});
			
			var li = $("<li>",{ "html":a });
			$startList.append(li);
		}
		
		for (var i=thisYear; i>startYear; i--) {
			var a = $("<a>",{
				"html" : i+"年",
				"href" : setTag.setUrl(currentUrl,"year",startYear+"-"+i)
			});
			
			var li = $("<li>",{ "html":a });
			$endList.append(li);
		}
	}
	
	setPlateYear();
		
	CarMile.setList(1,8,2);
	CarControl.setList();
	
	SelectSlug.init("#select-slug",".slug-list dl");
	
	BrandList.init(".brand-list","/meta-data/brand/",function(){});
	
	$("#select-brand-btn").click(function(){
		$(".brand-list").toggle("fast",function(){
			var type = $(this).css("display");
			if (type == "block") {
				$(".select-brand-list").addClass("select-brand-list-focus").
				css("border-bottom","1px solid #006599");
			} else {
				$(".select-brand-list").removeClass("select-brand-list-focus").
				css("border-bottom","1px solid #ddd");
			}
		});
	});
	
	$(".brand-list").mouseleave(function(){
		$(this).hide("fast");
		
		$(".select-brand-list").removeClass("select-brand-list-focus").
		css("border-bottom","1px solid #ddd");
	});
	
	
	$("input[name='start_price']").focus(function(){		
		$(".input-price-bg").show();
	});
	
	$("input[name='end_price']").focus(function(){	
		$(".input-price-bg").show();
	});
	
	
	$(".input-price-bg").mouseleave(function(){
		$(this).hide();
	});
	
	layerScroll(170,function(){
		$(".filter-field-bar").show();
	},function(){
		$(".filter-field-bar").hide();
	});
	
	//加入对比
	$(".add-contrast").click(function(){
		var carId = $(this).parents(".car-bar").attr("id");
		carCompare(carId);
	});
	
	$(".contrast-mark").click(function(){
		var carId = $(this).parents(".car-bar").attr("id");
		carCompare(carId);
	});
	
	function carCompare(carId) {
		var $mark = $("#"+carId).find(".contrast-mark"),
			flag = $mark.css("display"),
			compare = new Compare();
		
		flag == "none" ? $mark.show() && compare.add(carId)
			: $mark.hide() && compare.del(carId);;
	}
	
	
	
	$("#custom-price").click(function(){
		var minPrice = $("input[name='start_price']").val(),
			maxPrice = $("input[name='end_price']").val(),
			thisUrl = window.location.href;
		
		var jumpUrl = new SetGetParameter();
		jumpLink = jumpUrl.setUrl(thisUrl, "price", minPrice+"-"+maxPrice);
		
		window.location.href = jumpLink;
	});
	
	$(".car-img").flexslider({
		animation: "slide",
		slideshow: false,
	});
	
	$(".scrollLoading").scrollLoading();
});
