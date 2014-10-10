$(function(){	
	(function(){
		var compare = new Compare();
		
		$(".delete-compare").click(function(){
			var carId = $(this).parents(".contrast-box").attr("id");			
			compare.del(carId);
			location.reload();
			setParentCheck(carId);
		});
		
		$("#empty-compare").click(function(){
			compare.empty();
			location.reload();
			$(window.parent.document).find(".contrast-mark").hide();
		});
	})();
});