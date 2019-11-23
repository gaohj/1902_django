function Comment() {

}

Comment.prototype.listenSubmitEvent = function(){
    var submitBtn = $('.submit-btn')
    var textarea = $("textarea[name='comment']")
    submitBtn.click(function () {
        var content = textarea.val();
        var news_id = submitBtn.attr('data-news-id')
        xfzajax.post({
            'url':'/news/public_comment/',
            'data':{
                'content':content,
                'news_id':news_id
            },
            'success':function (result) {
                if(result['code'] === 200){
                    var comment = result['data'];
                    var tpl = template('comment-item',{'comment':comment})
                    var commentList = $('.comment-list');
                    constructor.prepend(tpl)
                    window.messageBox.showSuccess('评论发表成功');
                    textarea.val('');//发表成功以后 输入框清空
                }else{
                    window.messageBox.showError(result['message']);
                }
            }
        })
    })
}

Comment.prototype.run =function () {

}

$(function () {
    var comment = new Comment();
    comment.run()
})