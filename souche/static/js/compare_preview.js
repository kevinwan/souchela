$(function(){
	$(".delete-compare").click(function(){
		var carId = $(this).parents(".contrast-box").attr("id");
		delCompare(carId);
		location.reload(true);
	});
});