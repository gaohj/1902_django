from django.http import HttpResponse
from django.shortcuts import render
from frontuser.models import FrontUser,UserExtension
from article.models import Article,Tag,Category
# Create your views here.

def one_to_many_view(request):
    # article = Article(title="钢铁是怎么练成的6",content="所谓的浪漫是指你负责浪我负责漫6")
    # users = FrontUser(username="xcxk")
    #
    # users.save()
    # article.author = users
    # article.save()
    # user = FrontUser.objects.first()
    # articles = user.article_set.all()
    # for article in articles:
    #     print(article)
    # article = Article.objects.filter(pk=2).first()
    # category = Category(name="欧美")
    # category.save()
    # article.category = category
    # article.save()
    # category = Category.objects.first()
    # articles = category.articles.all()
    # for article in articles:
    #     print(article)

    # category = Category.objects.first()
    # articles = category.article_set.all()
    # for article in articles:
    #     print(article)
    category = Category.objects.first()
    articles = Article(title="琼琼孑立",content="彬彬有礼")
    # articles.save() #肯定报错
    articles.author = FrontUser.objects.first()
    category.article_set.add(articles,bulk=False)

    #bulk=False 会先自动保存 aritcle  不需要等添加到category之后
    #article.category 是不能为空的  如果说没有分类  文章必须要在添加到category之后才能保存
    #容易陷入一个死循环
    #这时候bulk=False 可以解决这个问题 不用等 category.article_set.add 这一步
    # for article in articles:
    #     print(article)

    return HttpResponse("一对多添加数据成功")

def one_to_one_view(request):
    #先查到第一个用户
    # user = FrontUser.objects.first()
    # extension = UserExtension(cardid=123456789123456789)
    # extension.user = user
    # extension.save()
    # extension = UserExtension.objects.first()
    # print(extension.user) #<FrontUser:(id:1,username:xcxk)>
    # extension = UserExtension.objects.first()
    # print(extension.user)
    user = FrontUser.objects.first()
    print(user.extensions)
    return HttpResponse("一对一添加数据成功")

def many_to_many_view(request):
    # article = Article(title="钢铁是怎么样练成的",content="你负责浪我负责慢")
    # article.save()
    # tag = Tag(name="冷门")
    # tag.save()
    #
    # tag.articles.add(article) 这是 把ManyToManyField 写到 tag模型上

    # article = Article.objects.first()
    #
    # # tag = Tag(name="热门")
    # # tag.save()
    # # # article.tag_set.add(tag)#这是 把ManyToManyField 写到 Article模型上
    # # tag.articles.add(article)
    #
    # tags = article.tags.all()
    # for tag in tags:
    #     print(tag)

    tag = Tag.objects.get(pk=5)
    articles = tag.articles.all()
    for article in articles:
        print(article)
    return HttpResponse("多对多添加数据成功")




