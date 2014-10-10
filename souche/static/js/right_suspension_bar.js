$(function(){
	$("#compare").click(function(){
		$("#sidebar-window").fadeIn();
		$(this).css({
			"border-right" : "none",
			"background" : "#fff"
		});
		$(".blank-leaving").show();
		
		refreshFrame("#compare-list");
	});
	
	$("#right-sidebar-closed").click(function(){
		$("#sidebar-window").hide();
		compareHide();
	});
	
	var siderbar = (function(){
		var offest = $(window).height()/2,
			$goTopBtn = $("#go-top");
		
		layerScroll(offest,function(){
			$goTopBtn.show();
		},function(){
			$goTopBtn.hide();
		});
			
		$goTopBtn.click(function(){
			scrollPage(0);
		});
	})();
	
	$("#suspension-bar").mouseleave(function(){
		$("#sidebar-window").hide();
		compareHide();
	});
	
	var compareHide = function() {
		$("#compare").css({
			"border-right" : "1px solid #E5E5E5",
			"background" : "#FAF8F9"
		});
		
		$(".blank-leaving").hide();
	};
});