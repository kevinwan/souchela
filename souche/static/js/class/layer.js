/*
 *弹出层基类
 */
function Layer(onBtn,closeBtn,layerName) {
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

Layer.prototype.event = function(){};

/*
 *弹出层实现类声明
 */
function Tip() {};
function PopWindow() {};

/*
 *弹窗类
 */

PopWindow.prototype = new Layer();

PopWindow.prototype.event = function(modal=false) {
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

Tip.prototyp.event = function(isStay=true) {
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