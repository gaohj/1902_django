
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
    self.smsCaptcha = $('.sms-captcha-btn');
}

Auth.prototype.run = function(){
    var self = this
    self.listenShowHideEvent();
    self.listenSwitchEvent();
    self.ListenSigninEvent();
    self.listenSmsCaptchaEvent();
    self.ListenImageCaptchaEvent();
    self.ListenSignupEvent();
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
                    messageBox.showSuccess('登录成功')
                }else{
                    messageBox.showError('登录失败')
                }
            },
            'fail':function (error) {
                console.log(error)
            }
        })
    })



}

//监听短信发送事件
Auth.prototype.listenSmsCaptchaEvent = function(){
    var self = this;
    var smsCaptcha = self.smsCaptcha
    var telephoneInput = $(".signup-group input[name='telephone']")
    smsCaptcha.click(function () {
        var telephone = telephoneInput.val()
        if(!telephone){
            alert('请输入手机号码')
        }else{
          xfzajax.get({
            'url':'/account/sms_captcha/',
            'data':{
                'telephone':telephone
            },
            'success':function (result) {
                if(result['code'] == 200){
                    self.smsSuccessEvent()
                }else{
                    alert('失败')
                }
            },
            'fail':function (error) {
                console.log(error)
            }
        })
        }

    })
}

//发送短信按钮 点击一次以后禁止点击 并倒计时 然后恢复点击 
Auth.prototype.smsSuccessEvent = function(){
    var self = this;
    messageBox.showError("短信验证码发送成功")
    self.smsCaptcha.addClass('disabled');
    var count  = 10
    self.smsCaptcha.unbind('click');
    var timer = setInterval(function () {
        self.smsCaptcha.text(count+'秒');
        count -= 1
        if(count<=0){
            clearInterval(timer);
            self.smsCaptcha.removeClass('disabled');
            self.smsCaptcha.text('发送验证码');
            self.listenSmsCaptchaEvent();
        }
    },1000)
    
}


//图形验证码事件  
Auth.prototype.ListenImageCaptchaEvent = function(){
    var imgCaptcha = $('.img-captcha')
    imgCaptcha.click(function () {
        imgCaptcha.attr("src","/account/img_captcha/"+"?random="+Math.random())
    })
}

//监听注册事件

Auth.prototype.ListenSignupEvent =function(){
    var self = this;
    var signupGroup = $('.signup-group');
    var submitBtn = signupGroup.find(".submit-btn")
    //获取登录的区域
    //获取三个输入框  现在只是定位到输入框
    var telephoneInput = signupGroup.find("input[name='telephone']")
    var usernameInput = signupGroup.find("input[name='username']")
    var imgCaptchaInput = signupGroup.find("input[name='img_captcha']")
    var smsCaptchaInput = signupGroup.find("input[name='sms_captcha']")
    var password1Input = signupGroup.find("input[name='password1']")
    var password2Input = signupGroup.find("input[name='password2']")

    submitBtn.click(function (event) {
        event.preventDefault();//阻止默认提交事件
        //获取输入框输入的内容
        var telephone = telephoneInput.val();
        var password1 = password1Input.val();
        var password2 = password2Input.val();
        var username = usernameInput.val();
        var img_captcha = imgCaptchaInput.val();
        var sms_captcha = smsCaptchaInput.val();
        xfzajax.post({
            'url':'/account/register/',
            'data':{
                'telephone':telephone,
                'password1':password1,
                'password2':password2,
                'username':username,
                'img_captcha':img_captcha,
                'sms_captcha':sms_captcha,
            },
            'success':function (result) {
                if(result['code'] == 200){
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