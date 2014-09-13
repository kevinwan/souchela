$(function(){
	var plateStart =  "#plate-start-time .start-time";
	var plateEnd = "#plate-end-time .end-time";
	var carMileEle = "#car-mile";
	var volumeEle = "#car-volume";
	
	//上牌时间下拉框生成
	var TimePlate = function(inputEle) {
		this.init(inputEle);
	};
	
	TimePlate.prototype = new DropDownList();
//	
	TimePlate.prototype.setList = function(type) {
		var date = new Date(),
			thisYear = date.getFullYear(),
			para = type=="end" ? "max-year" : "min-year";
			
		if (type !== "end" || $("#plate-start-time .start-time").val()==="") {
			lastYear = thisYear - 15;
		} else {
			lastYear = $("#plate-start-time .start-time").val();
		}
		
		for (var year=thisYear; year>=lastYear; year--) {
			var thisUrl = this.SetATag.setUrl(this.url,para,year);
			var a = $("<a>",{"html":year, "href":thisUrl });
			var li = $("<li>",{"html":a});
			$(this.listBox).append(li);
		}
		
		var li = $("<li>",{"html":"不限"});
		$(this.listBox).append(li);
	};
	
	//里程
	var CarMileList = function(inputEle) {
		this.init(inputEle);
	};
	
	CarMileList.prototype = new DropDownList();
	
	CarMileList.prototype.setList = function(start,end,step) {
		step = step ? step : 1;
		for (var i=start; i<=end; i+=step) {
			var a = $("<a>",{
				"html" : i+"万里",
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
	
	var CarVolumeList = function(inputEle) {
		this.init(inputEle);
	};

	CarVolumeList.prototype = new DropDownList();
	CarVolumeList.prototype.setList = function() {
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
				"href": this.SetATag.setUrl(this.url,"volume",html),
				"html": html
			});
			
			var li = $("<li>",{"html":a});
			$(this.listBox).append(li);
		}
	};

	var StartTimePlate = new TimePlate(plateStart);
	var EndTimePlate = new TimePlate(plateEnd);
	var CarMile = new CarMileList(carMileEle);
	var CarVolume = new CarVolumeList(volumeEle);
	var BrandList = new SetBrandList();
	var SelectSlug = new DropDownList();
	
	StartTimePlate.setList("start");
	EndTimePlate.setList("end");	
	CarMile.setList(1,8,2);
	CarVolume.setList();
	
	SelectSlug.init("#select-slug",".slug-list dl");
	
	BrandList.init(".brand-list","/meta-data/brand/",function(){});
	
	$("#select-brand-btn").click(function(){
		$(".brand-list").toggle("normal",function(){
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
	
	
	(function() {
		for (i=1; i<11; i++) {
			$($(".car-img")[i]).flexslider({
				animation: "slide",
			});
		}
	})();
});
