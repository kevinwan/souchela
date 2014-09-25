$(function(){
	//估值接口调用
	var evalURL = $("#eval-api").val();
	
	//请求成功
	var updateEvaluationPrice = function(element, evalPrice, evalReportURL) {
		var evalPriceMin = parseFloat(evalPrice*0.975/10000).toFixed(1),
			evalPriceMax = parseFloat(evalPrice*1.025/10000).toFixed(1),
			evalPriceRangeStr = "￥"+evalPriceMin+"万-"+"￥"+evalPriceMax+"万";
		//估值结果操作
		$(element).find(".eval-price").fadeOut("normal",function() {
			$(this).text(evalPriceRangeStr).attr("href", evalReportURL);
			$(element).find(".load-price").remove();
		});
	};
	//请求失败
	var evalError = function() {
		var $evalPriceRangeReport = $(".evaluate-price"),
			$evaDiagramLoad = $("#evalua-load-in-diagram"),
			$loadInInfo = $("#load-in-info");
			
			$loadInInfo.find("img").hide();
			$evaDiagramLoad.hide();
	};
	var $carData = $(".car-data");
	var evalData, element;
	var requestEvaluationPrice = function(element, evalURL, evalData) {
		$.ajax({
			url: evalURL,
			dataType: "jsonp",
			data: evalData,
			crossDomain: true,
			success: function(response){
				if (response.status === "success") {
					var evalPrice = response.deal_price;
					var evalReportURL = response.url;
					updateEvaluationPrice(element, evalPrice, evalReportURL);
				} else {
					evalError();
				}
			},
			error: function() {
				evalError();
			}
		});
	};
	for (var i=1; i<$carData.length+1; i++) {
		var elementStr = ".car-data.car" + i;
		element = $(elementStr);
		evalData = {
			brand: $(element).find("input[name='brand']").val(),
			model: $(element).find("input[name='model']").val(),
			d_model: $(element).find("input[name='detail-model']").val(),
			volume: $(element).find("input[name='volume']").val(),
			year: $(element).find("input[name='year']").val(),
			month: $(element).find("input[name='month']").val(),
			mile: $(element).find("input[name='mile']").val(),
			color: $(element).find("input[name='color']").val(),
			city: $(element).find("input[name='city']").val(),
			condition: $(element).find("input[name='condition']").val(),
			intent: "buy"
		};
		requestEvaluationPrice(elementStr, evalURL, evalData);
	}

	layerScroll("240",function(){
		$(".first-title").css({
			"position":"fixed",
			"top":"0",
			"z-index":"999",
			"text-indent":"2%"
		});
	},function(){
		$(".first-title").css({
			"position":"static",
			"text-indent":"20%"
		});
	});
	
	var setMain = function(){
		var itemTotal = $(".base-info .item").length,
			itemWidth = $(".base-info .item").width();
			
		$(".main").width(itemWidth*itemTotal+188);
	}();
	
});
