$(function(){
	$("#compare").click(function(){
		$(".sidebar").animate({"height":"309px"});
		$("#sidebar-window").fadeIn();
		refreshFrame("#compare-list");
	});
	
	$("#right-sidebar-closed").click(function(){
		$("#sidebar-window").hide();
		$(".sidebar").height("124px");
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
		$(".sidebar").height("124px");
	});
});