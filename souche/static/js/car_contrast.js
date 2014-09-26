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
		$(".item .first-title").css({
			"position":"fixed",
			"top":"0",
			"z-index":"999",
			"text-indent":"0",
			"padding":"0 5px",
			"windth":"238.5px"
		});
		$(".main-title .first-title").css({
			"position":"fixed",
			"top":"0",
			"text-indent":"2%"
		});
	},function(){
		$(".item .first-title").css({
			"position":"static",
			"text-indent":"2%"
		});
		$(".main-title .first-title").css({
			"position":"static",
			"text-indent":"20%",
			"windth":"248.5px"
		});
	});
	
	var setMain = function(){
		var itemTotal = $(".base-info .item").length,
			itemWidth = $(".base-info .item").width();
			
		$(".main").width(itemWidth*itemTotal+188);
	}();
	
	
	//删除基本信息相同项目
	$("#irreducible-list").click(function(){
		if ($(this).attr("name") !== "true") {
			irreducible();
			$(this).attr("name","true");
			$(".mark").show();
		} else {
			$(".base-info").find("li").show();
			$(this).attr("name","false");
			$(".mark").hide();
		}
	});
	
	function irreducible() {
		var $baseItem = $(".base-info .item"),
			$baseItemLI = $(".base-info .item").find("li"),
			$baseTitle = $(".base-info .main-title").find("li"),
			$baseUl = $(".base-info").find("ul");
		
		var baseLiLength =  $baseTitle.length,
			itemLength = $(".base-info .item").length,
			baseUlLength = $(".base-info").find("ul").length;
			
			
		for (var i=0; i<baseLiLength; i++) {
			var matchCount = 0;
			
			for (var j=0; j<itemLength-1; j++) {
				
				var thisItem = $baseItem.eq(j).find("li"),
					nextItem = $baseItem.eq(j+1).find("li");
					
				if (thisItem.eq(i).text() === nextItem.eq(i).text()) {
					if (thisItem.eq(i).find("img").attr("alt") !== '') {
						if (thisItem.eq(i).find("img").attr("alt") === nextItem.eq(i).find("img").attr("alt")) {
							matchCount++;
						}
					} else {
						matchCount++;
					}
				}
			}
			
			if (matchCount === itemLength-1) {
				for (var k=0; k<baseUlLength; k++) {
					$baseUl.eq(k).find("li").eq(i).hide();
				}
			}
		}
	}
});
