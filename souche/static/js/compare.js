function addCompare(carId) {
	var carData = {
		csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
		car_id : carId
	}
	
	print(carData);
	
	$.ajax({
		url:'/car/contrast/add/',
		type:'Post',
		dataType:'json',
		data:carData,
		success:function(response) {
			if (response.success) {
				print("Add");
			} else {
				print("Add");
			}
		},
		error:function(){
			print("Error");
		}
	});
	print("+"+carId);
	
	top.frames['car-compera'].location.reload();
}

function delCompare(carId) {
	var carData = {
		csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
		car_id : carId
	}
	
	$.ajax({
		url:'/car/contrast/delete/',
		type:'Post',
		dataType:'json',
		data:carData,
		success:function(response) {
			if (response.success) {
				print("Add");
			} else {
				print("Add");
			}
		},
		error:function(){
			print("Error");
		}
	});

	print("+"+carId);
	
	top.frames['car-compera'].location.reload();
}