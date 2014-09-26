$(function(){	
	(function(){
		var compare = new Compare();
		
		$(".delete-compare").click(function(){
			var carId = $(this).parents(".contrast-box").attr("id");			
			compare.del(carId);
		});
		
		$("#empty-compare").click(function(){
			compare.empty();
		});
	})();
});