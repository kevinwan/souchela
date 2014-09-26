$(function(){
	$("#header-show-wx-btn").hover(function(){
		$("#header-td-code").show();
	},function(){
		$("#header-td-code").hide();
	});
	
	$("#footer-wx-btn").hover(function(){
		$("#footer-td-code").show();
	},function(){
		$("#footer-td-code").hide();
	});
});