from django.http import HttpResponse,JsonResponse
import json
def index(request):
    response = HttpResponse('<h1>千锋大课堂</h1>',content_type="text/plain;charset=utf-8")
    #content_type
    #text/plain;charset=utf-8 纯文本
    #text/html;charset=utf-8   html文件 默认的
    #text/css;charset=utf-8  css文件
    #text/javascript;charset=utf-8 js文件
    #multipart/form-data 文件提交
    #application/json json传输
    #application/xml xml 文件
    response.status_code = 400
    response['X-Token'] = '1000phone' #设置请求头
    response.write('kangbazi')
    response.set_cookie('kangbazi','aaaaa')
    response.delete_cookie('kangbazi')
    return response

def json_view(request):
    person = [
        {
            'username':'binbinlaile',
            'password':'123abc',
            'age':18,

        },
        {
            'username': 'xiaobinbin',
            'password': 'abc123',
            'age': 20,
        }
    ]

    # person_str = json.dumps(person)
    # response = HttpResponse(person_str, content_type="application/json")
    # return response
    response = JsonResponse(person,safe=False)
    return response