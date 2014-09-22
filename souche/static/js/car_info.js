$(function(){
	//估值接口调用
	var evalURL = $("#eval-api").val();
	var evalData = {
		brand: $("#brand").val(),
		model: $("#model").val(),
		d_model: $("#detail-model").val(),
		volume: $("#volume").val(),
		year: $("#year").val(),
		month: $("#month").val(),
		mile: $("#mile").val(),
		color: $("#color").val(),
		city: $("#city").val(),
		condition: $("#condition").val(),
		intent: "buy"
	};
	
	var getEvaluationPrice = function() {};
	//请求成功
	var updateEvaluationPrice = function(evalPrice, evalReportURL) {
		var evalPriceMin = parseFloat(evalPrice*0.975/10000).toFixed(1),
			evalPriceMax = parseFloat(evalPrice*1.025/10000).toFixed(1),
			evalPriceRangeStr = "￥"+evalPriceMin+"万-"+"￥"+evalPriceMax+"万";
		var carPrice = $("#car-price").text(),
			$listPrice = $("#list-price"),
			evalPriceRange = evalPriceMax - evalPriceMin,
			width = 215,
			widthRate = width / evalPriceRange,
			leftPosition = 0;
		var $evalPriceRange = $("#eval-range"),
			$evalPriceRangeReport = $("#eval-range-report"),
			$evaDiagramLoad = $("#evalua-load-in-diagram");
		
		carPrice = parseFloat(carPrice);
		//概述信息估值结果操作
		$evalPriceRange.text(evalPriceRangeStr).attr("href", evalReportURL);
		
		$("#load-in-info").fadeOut("normal",function(){
			$evalPriceRangeReport.text(evalPriceRangeStr);
			$(".evaluate-price").fadeIn("normal");
		});
		//价格趋势图操作
		leftPosition = (carPrice - evalPriceMin) * widthRate;
		if (leftPosition < -40) {
			leftPosition = -40;
		} else if (leftPosition > 255) {
			leftPosition = 255;
		}
		$evaDiagramLoad.hide();
		$("#diagram-bg").attr("class","diagram");
		$listPrice.animate({"margin-left":leftPosition});
	};
	//请求失败
	var evalError = function() {
		var $evalPriceRangeReport = $(".evaluate-price"),
			$evaDiagramLoad = $("#evalua-load-in-diagram"),
			$loadInInfo = $("#load-in-info");
			
			$loadInInfo.find("img").hide();
			$evaDiagramLoad.hide();
	};
	$.ajax({
		url: evalURL,
		dataType: "jsonp",
		data: evalData,
		jsonpCallback: "getEvaluationPrice",
		success: function(response){
			if (response.status === "success") {
				var evalPrice = response.deal_price;
				var evalReportURL = response.url;
				updateEvaluationPrice(evalPrice, evalReportURL);
			} else {
				evalError();
			}
		},
		error: function() {
			evalError();
		}
	});
	
	//悬浮导航
	layerScroll(900,function(){
		$(".base-info .nav").css({
			"position": "fixed",
			"top":0,
			"z-index":"999"
		});
		},function(){
			$(".base-info .nav").css({
				"position": "static",
				"top":0
			});
		}
	);
	
	$(".base-info .nav").find("li").click(function(){
		var contentEle = $(this).find("a").attr("href");
		
		$(this).parent().find("li").removeClass("focus");
		$(this).addClass("focus");
		
		$(contentEle).css("padding-top","50px");
	});
	
	//加入对比
	$("#select-contrast").find("span").click(function(){
		carCompare();
	});
	
	$("#contrast-mark").click(function(){
		carCompare();
	});
	
	function carCompare() {
		var $mark = $("#contrast-mark"),
			flag = $mark.css("display"),
			carId = $(".main").attr("id");
		
		flag=="none" ? $mark.show() : $mark.hide();
		flag=="none" ? addCompare(carId) : delCompare(carId);
	}
	
	//Tip
	var Transfer = new Tip("#transfer","#transfer-tip");
	var Mandatory = new Tip("#mandatory","#mandatory-tip");
	var Business = new Tip("#business","#business-tip");
	
	Transfer.selfClosing();
	Mandatory.selfClosing();
	Business.selfClosing();
});
