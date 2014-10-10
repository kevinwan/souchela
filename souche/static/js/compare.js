function Compare(iframeName) {
	this.iframeName = iframeName;
	this.csrfValue = $.cookie("csrftoken");
}

Compare.prototype.add = function(carId) {
	var carData = this.setData(carId);
	this.post("/car/contrast/add/",carData);
};

Compare.prototype.del = function(carId) {
	var carData = this.setData(carId);
	this.post("/car/contrast/delete/",carData);
};

Compare.prototype.empty = function() {
	var carData = this.setData();
	this.post("/car/contrast/empty/",carData);
};

Compare.prototype.setData = function(carId) {
	var carJsonData = {
		csrfmiddlewaretoken: this.csrfValue
	};
	
	if (typeof carId !== "undefined") {
		carJsonData['car_id'] = carId;
	}
	
	return carJsonData;
};

Compare.prototype.post = function(postUrl,postData) {	
	$.ajax({
		url: postUrl,
		type: 'post',
		dataType: "json",
		data: postData,
		success: function(response) {
		}
	});
};

function refreshFrame(frameElement) {
	$(frameElement).attr("src", $(frameElement).attr("src"));
}

function setParentCheck(ele) {
	$(window.parent.document).find("#"+ele).find(".contrast-mark").hide();
}