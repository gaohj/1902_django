
//
// // 点击登录按钮，弹出模态对话框
// $(function () {
//     $("#btn").click(function () {
//         $(".mask-wrapper").show();
//     });
//
//     $(".close-btn").click(function () {
//         $(".mask-wrapper").hide();
//     });
// });
//
//
// $(function () {
//     $(".switch").click(function () {
//         var scrollWrapper = $(".scroll-wrapper");
//         var currentLeft = scrollWrapper.css("left");
//         currentLeft = parseInt(currentLeft);
//         if(currentLeft < 0){
//             scrollWrapper.animate({"left":'0'});
//         }else{
//             scrollWrapper.animate({"left":"-400px"});
//         }
//     });
// });

//类以及初始化完成  专门用来操作登录注册的
function Auth() {
    var self = this; //多个地方用到this
    self.maskWrapper = $('.mask-wrapper'); //获取整个模态框
    self.scrollWrapper = $('.scroll-wrapper');
}

Auth.prototype.run = function(){
    var self = this
    self.listenShowHideEvent();
}


//给类写方法  让它做什么
Auth.prototype.showEvent = function () {
    var self = this
    self.maskWrapper.show()
    alert(888)
}


Auth.prototype.hideEvent = function () {
    var self = this
    self.maskWrapper.hide()
    alert(666)
}

Auth.prototype.listenShowHideEvent = function(){
    var self = this
    var signinbtn = $('.signin-btn')
    var signupbtn = $('.signup-btn')
    var closebtn = $('.close-btn')
    signinbtn.click(function () {
        self.showEvent()
    })

    signupbtn.click(function () {
        self.showEvent()
    })

    closebtn.click(function () {
        self.hideEvent()
    })
}


//实例化对象
$(function () {
    var auth = new Auth();
    auth.run() //通过run调用类方法
})