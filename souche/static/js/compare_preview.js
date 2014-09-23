$(function(){
	$(".delete-compare").click(function(){
		var carId = $(this).parents(".contrast-box").attr("id");
		var compare = new Compare();
		
		compare.del(carId);
	});
	
	$("#empty-compare").click(function(){
		var compare = new Compare();
		compare.empty();
	});
});