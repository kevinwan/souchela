$(function(){
    var plateStart =  "#plate-start-time .start-time";
    var plateEnd = "#plate-end-time .end-time";
    var carMileEle = "#car-mile";
    var volumeEle = "#car-volume";
    
    //上牌时间下拉框生成
    var TimePlate = function(inputEle) {        
        this.init(inputEle);
    };
    
    TimePlate.prototype = new DropDownList();
    
    TimePlate.prototype.setList = function(url, type) {
        var date = new Date(),
            thisYear = date.getFullYear();
            //lastYear = !type && !$("#plate-start-time .start-time").val() ? thisYear - 15: $("#plate-start-time .start-time").val();
        if (type !== "end" || $("#plate-start-time .start-time").val()==="") {
            lastYear = thisYear - 15;
        } else {
            lastYear = $("#plate-start-time .start-time").val();
        }
        
        for (var year=thisYear; year>=lastYear; year--) {
            var li = $("<li>",{"html":year});
            $(this.listBox).append(li);
        }
        
        var li = $("<li>",{"html":"不限"});
        $(this.listBox).append(li);
    };
    
    //里程
    var CarMileList = function(inputEle) {
        this.init(inputEle);
    };
    
    CarMileList.prototype = new DropDownList();
    
    CarMileList.prototype.setList = function(start,end,step) {
        step = step ? step : 1;
        for (var i=start; i<=end; i+=step) {
            var li = $("<li>",{ "html" : i+"万公里内" });
            $(this.listBox).append(li);
        }
        
        var li = $("<li>",{"html":"不限"});
        $(this.listBox).append(li);
    };
    
    var CarVolumeList = function(inputEle) {
        this.init(inputEle);
    };
    
    CarVolumeList.prototype = new DropDownList();
    CarVolumeList.prototype.setList = function() {
        var html;
        
        for (var i=0; i<2; i++) {
            if (i) {
                html = "自动";
            } else {
                html = "手动";
            }
            
            var li = $("<li>",{ "html" : html });
            $(this.listBox).append(li);
        }
        
        
        var li = $("<li>",{ "html" : "不限" });
        $(this.listBox).append(li);
    }
    
        
    var StartTimePlate = new TimePlate(plateStart);
    var EndTimePlate = new TimePlate(plateEnd);
    var CarMile = new CarMileList(carMileEle);
    var CarVolume = new CarVolumeList(volumeEle);
    
    StartTimePlate.setList("#","start");
    StartTimePlate.select();
    
    EndTimePlate.setList("#","end");
    EndTimePlate.select();
    
    CarMile.setList(1,8,2);
    CarMile.select();
    
    CarVolume.setList();
    CarMile.select();
});
