/*
 *弹出层基类
 */
function Layer() { }

Layer.prototype.init = function(onBtn,closeBtn,layerName)  {
    this.onBtn = onBtn;
    this.closeBtn = closeBtn;
    this.layerName = layerName;
}

Layer.prototype.show = function(){
    $(this.layerName).show();
}

Layer.prototype.hide = function(){   
    $(this.layerName).hide();
}

Layer.prototype.event = function(){}

/*
 *弹出层实现类声明
 */
function Tip() {};
function PopWindow() {};

/*
 *弹窗类
 */

PopWindow.prototype = new Layer();

PopWindow.prototype.event = function(modal) {
    $(this.onBtn).click(function(){
        this.show();
        return modal ? '' : $(modal).show() ;
    });
    
    $(this.closeBtn).click(function(){
        this.hide();
        return modal ? '' : $(modal).hide() ;
    });
}

/*
 *提示弹出层
 */

Tip.prototype = new Layer();

Tip.prototype.event = function(isStay) {
    if (isStay) {
        this.onBtn.hover(function(){
            this.show();
        },function(){
            this.hide();
        });
    } else {
        this.OnBtn.mousemove(function(){
            this.show();
        });
        
        this.closeBtn.click(function(){
            this.hide();
        });
    }
}


/*
 *下拉框
 */


function DropDownList () {};

DropDownList.prototype.init = function(inputEle) {
    this.inputEle = inputEle;
    
    var listContent = $("<div>",{
        "class"    : "list-box",
        "width"    : $(this.inputEle).width(),
    });
    $(this.inputEle).parent().append(listContent);
    this.listBox = $(this.inputEle).parent().find("div");
    
    this._event(this.inputEle,this.listBox);
}

DropDownList.prototype._event = function(btn,box) {
    $(btn).click(function(){
        //alert($(btn).parent().find("div").width());
        $(box).show();
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