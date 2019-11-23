function News() {
    var self = this;
     self.progressGroup = $("#progress-group");
     self.progressBar = $(".progress-bar");
}
//ueditor 编辑器
News.prototype.initUEditor = function () {
    window.ue = UE.getEditor('editor',{
        'initialFrameHeight': 400, //初始化编辑器的高度
        'serverUrl': '/ueditor/upload/' //这里是 服务器响应的接口  也就是上面的 views.py
    });
};
News.prototype.ListenUploadFileEvent = function(){
    var uploadBtn = $('#thumbnail-btn');
    uploadBtn.change(function(){
        var file = uploadBtn[0].files[0];
        var formdata=new FormData();
        formdata.append("file",file);
        xfzajax.post({
            'url':'/cms/upload_file/',
            'data':formdata,
            'processData':false,
            'contentType':false,
            'success':function (result) {
                if(result['code']===200){
                    var url = result['data']['url']
                    var thumbnailInput = $('#thumbnail-form')
                    thumbnailInput.val(url);
                }
            }

        })
    });
}

News.prototype.ListenQiniuUploadFileEvent = function(){
     var self = this;
     var thumbnailBtn = $('#thumbnail-btn');
     thumbnailBtn.change(function (event) {
         var file = this.files[0];
         xfzajax.get({
             'url': '/cms/qntoken/',
             'success': function (result) {
                 var token = result['uptoken'];
                 var key = (new Date()).getTime() + '.' + file.name.split('.')[1];
                 var putExtra = {
                     fname: key,
                     params: {},
                     mimeType: ['image/png','video/x-ms-wmv','image/jpeg']
                 };
                 var config = {
                     useCdnDomain: true,
                     retryCount: 6,
                     region: qiniu.region.z0
                 };
                 var observable = qiniu.upload(file, key, token, putExtra,config);
                 observable.subscribe({
                     "next":self.updateUploadProgress,
                     "error":self.uploadErrorEvent,
                     "complete": self.complateUploadEvent
                 });
                 self.progressGroup.show();
             }
         });
     });
}
 News.prototype.updateUploadProgress = function (response) {
     var self = this;
     var total = response.total;
     var percent = total.percent;
     var percentText = percent.toFixed(0) + '%';
     var progressBar = $(".progress-bar");
     progressBar.css({"width":percentText});
     progressBar.text(percentText);
 };

 News.prototype.uploadErrorEvent = function (error) {
     window.messageBox.showError(error.message);
 };

 News.prototype.complateUploadEvent = function (response) {
     var self = this;
     var filename = response['key'];
     var domain = 'http://q1cpa1kbu.bkt.clouddn.com/';
     var thumbnailUrl = domain + filename;
     var thumbnailInput = $("#thumbnail-form");
     thumbnailInput.val(thumbnailUrl);
     var progressGroup = $("#progress-group");
     progressGroup.hide();
 };

News.prototype.ListenSubmitEvent = function(){
    var submitBtn = $('#submit-btn');
    submitBtn.click(function (event) {
        event.preventDefault();//阻止默认提交
        var btnAttr = $(this);
        var pk = btnAttr.attr('data-news-id')//获取到要修改的文章的id
        var title = $("input[name='title']").val();
        var category = $("select[name='category']").val();
        var desc = $("input[name='desc']").val();
        var thumbnail = $("input[name='thumbnail']").val();
        var content = window.ue.getContent();
        var url = '';
        if(pk){
            url = '/cms/edit_news/';
        }else{
            url = '/cms/write_news/';
        }
        xfzajax.post({
            'url':url,
            'data':{
                'title': title,
                'category': category,
                'desc': desc,
                'thumbnail': thumbnail,
                'content': content,
            },
            'success':function (result) {
                if(result['code'] === 200){
                    alert('发表成功');
                }
            }
        })


    })
}


News.prototype.run = function () {
    var self = this;
    // self.ListenUploadFileEvent();
    self.ListenQiniuUploadFileEvent();
    self.initUEditor();
    self.ListenSubmitEvent();
}

$(function () {
    var news = new News();
    news.run();
})