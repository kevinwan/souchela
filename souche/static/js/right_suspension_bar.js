$(function(){
	$("#compare").click(function(){
		$("#sidebar-window").show("slow");
	});
	
	$("#right-sidebar-closed").click(function(){
		$("#sidebar-window").hide("normal");
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
});