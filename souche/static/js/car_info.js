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
			$evalPriceRangeReport = $("#eval-range-report");
		carPrice = parseFloat(carPrice);

		$evalPriceRange.text(evalPriceRangeStr).attr("href", evalReportURL);
		$evalPriceRangeReport.text(evalPriceRangeStr);

		leftPosition = (carPrice - evalPriceMin) * widthRate;
		if (leftPosition < -40) {
			leftPosition = -40;
		} else if (leftPosition > 255) {
			leftPosition = 255;
		}
		$listPrice.css("margin-left", leftPosition);
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
				console.log(response.message);
			}
		},
		error: function() {
			console.log("request evaluation failed!");
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
	
	$("#select-contrast").find("span").click(function(){
		var $mark = $("#contrast-mark"),
			flag = $mark.css("display");
			
		flag=="none" ? $mark.show() : $mark.hide();
	});
	
	$("#contrast-mark").click(function(){
		var flag = $(this).css("display");
		flag=="none" ? $(this).show() : $(this).hide();
	});
	
	var Transfer = new Tip("#transfer","#transfer-tip");
	var Mandatory = new Tip("#mandatory","#mandatory-tip");
	var Business = new Tip("#business","#business-tip");
	
	Transfer.selfClosing();
	Mandatory.selfClosing();
	Business.selfClosing();
});
