function print(info) {
	var isIE6= !!window.ActiveXObject&&!window.XMLHttpRequest;
	
	if (!isIE6) {
		console.log(info);
	}
}