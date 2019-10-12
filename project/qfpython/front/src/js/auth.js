
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
    self.listenSwitchEvent();
    self.ListenSigninEvent();
}


//给类写方法  让它做什么
Auth.prototype.showEvent = function () {
    var self = this
    self.maskWrapper.show()
}


Auth.prototype.hideEvent = function () {
    var self = this
    self.maskWrapper.hide()
}

Auth.prototype.listenShowHideEvent = function(){
    var self = this;
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

Auth.prototype.listenSwitchEvent = function(){
        var self = this;
        var switcher = $('.switch');
        switcher.click(function () {
            var currentLeft = self.scrollWrapper.css("left");
            currentLeft = parseInt(currentLeft);
            if(currentLeft < 0){
                self.scrollWrapper.animate({"left":'0'});
            }else{
                self.scrollWrapper.animate({"left":"-400px"});
            }
        })
}

Auth.prototype.ListenSigninEvent =function(){
    var self = this;
    var signinGroup = $('.signin-group');
    //获取登录的区域
    //获取三个输入框  现在只是定位到输入框
    var telephoneInput = signinGroup.find("input[name='telephone']")
    var passwordInput = signinGroup.find("input[name='password']")
    var rememberInput = signinGroup.find("input[name='remember']")
    var submitBtn = signinGroup.find(".submit-btn")
    submitBtn.click(function () {
        //获取输入框输入的内容
        var telephone = telephoneInput.val();
        var password = passwordInput.val();
        var remember = rememberInput.prop('checked');
        xfzajax.post({
            'url':'/account/login/',
            'data':{
                'telephone':telephone,
                'password':password,
                'remember':remember?1:0,
            },
            'success':function (result) {
                if(result['code'] == 200){
                    self.hideEvent()
                    window.location.reload()
                    alert('success')
                }else{
                    alert('失败')
                }
            },
            'fail':function (error) {
                console.log(error)
            }
        })
    })



}

//实例化对象
$(function () {
    var auth = new Auth();
    auth.run() //通过run调用类方法
})