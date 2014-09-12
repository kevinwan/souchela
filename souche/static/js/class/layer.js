function SetBrandList() {};

SetBrandList.prototype = new SetGetParameter();

SetBrandList.prototype.init = function(listEle,requestUrl,successMethod) {
	this.ele = listEle;
	this.requestUrl = requestUrl;
	this.success = successMethod;
	
	this.getList(this.success);
};

SetBrandList.prototype.getList = function(successMethod) {
	var setUrl = this.setUrl;
	var ele = this.ele;
	var currentUrl = window.location.href;
	
	$.ajax({
		url: this.requestUrl,
		type: 'get',
		dataType : 'json',
		success : function(response) {
			if (response.status === 'success') {
				var tmp,
					data = response.data;

				for(var i in data) {
					if (tmp !== data[i].first_letter) {
						tmp = data[i].first_letter;
						$(ele).append("<dl></dl>");
						
						var letterLi = $("<dt>", {"class":"letter-"+data[i].first_letter , "html": tmp});
						$(ele).append(letterLi);
					
					}					
					
					var brandA = $("<a>" , {"href":setUrl(currentUrl,"brand",data[i].slug) , "html":data[i].name});
					var brandLi = $("<dd>" , {"html":brandA});
					$(ele).append(brandLi);
				
				}
				
				(successMethod)();
			}
		}
	});
};

function DropDownList () {};

DropDownList.prototype.init = function(inputEle,selectBox) {
	this.inputEle = inputEle;
	this.SetATag = new SetGetParameter();
	this.url = window.location.href;
	
	if(typeof selectBox === "undefined") {
		var listContent = $("<div>",{
			"class"    : "list-box",
			"width"    : $(this.inputEle).width(),
		});
		
		$(this.inputEle).parent().append(listContent);
		this.listBox = $(this.inputEle).parent().find("div");	
	} else {
		this.listBox = selectBox;
	}
	
	this._event(this.inputEle,this.listBox);
}

DropDownList.prototype._event = function(btn,box) {
	$(btn).click(function(){
		$(box).toggle();
	});    
};

DropDownList.prototype.select = function() {
	this._select(this.listBox,this.inputEle);
};

DropDownList.prototype._select = function(checkOption,inputEle) {
	$(checkOption).children().click(function(){
		var selectVal = $(this).text();
		$(inputEle).val(selectVal);
		$(checkOption).hide();
	});
}

function SetGetParameter() {};

SetGetParameter.prototype.setUrl = function(currentUrl,key,value) {
	var getPara = {},
		currentPara = currentUrl.split("?")[1],
		kv,
		length = 0,
		jumpUrl = "?";
	
	currentUrl = currentUrl.split("#")[0];
	
	if (currentPara) {
		currentPara = currentPara.split("&");
		
		for (var i in currentPara) {
			kv = currentPara[i].split("=");
			getPara[kv[0]] = kv[1] ? kv[1] : "";		
		}
	}
	
	getPara[key] = value;
	length = jsonLength(getPara);	
			
	for (var i in getPara) {
		length = --length<0 ? 0 : length;
		
		var andflag = !length ? "" : "&";
		jumpUrl+= i + "=" + getPara[i] + andflag;
	}
	
	return currentUrl.split("?")[0] + jumpUrl;
};

function jsonLength(jsonData) {
	var length = 0;
	
	if (Boolean(jsonData)) 
		for (var i in jsonData) length++;

	return length;
}