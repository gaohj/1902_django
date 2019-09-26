from django.http import HttpResponse,StreamingHttpResponse
from django.template import loader
import csv

def index(request):
    #告诉浏览器 这是一个csv文件 不是 html文件了
    response = HttpResponse(content_type="text/csv")
    #添加head头   告诉浏览器如何去处理这个文件
    #attachment表明这是个附件 不需要展示  而是作为附件下载
    #附件的名字为 1902.csv
    response['Content-Disposition'] = "attachment;filename=1902.csv"
    #使用csv 文件的writer方法  将相应的数据写入到 reponse中
    writer = csv.writer(response)
    writer.writerow(['username','age','height']) #设置表头
    writer.writerow(['kangbazi','18','180cm']) #数据行
    return response

def template_csv_view(request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = "attachment;filename=1902.csv"
    context = {
        'rows':[
            ['username','age'],
            ['kangbazi','20'],
            ['binbin','16'],
            ['qiongqiong','15'],
        ]
    }

    template = loader.get_template('kangbazi.txt')
    csv_template = template.render(context)
    response.content = csv_template
    return response
class Echo:
    #可执行的写操作类，以后调用csv.writer的时候 会执行这个方法
    def write(self,value):
        return value

def large_csv_view(request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = "attachment;filename=large.csv"
    # buffer = Echo()
    writer = csv.writer(response)
    for row in range(0,1000000):
        writer.writerow(['Row {}'.format(row),'{}'.format(row)])
    return response


def streaming_csv_view(request):
    rows = (["p {}".format(x), str(x)] for x in range(1000000))
    buffer = Echo()
    writer = csv.writer(buffer)
    response = StreamingHttpResponse((writer.writerow(row) for row in rows),content_type="text/csv")
    response['Content-Disposition'] = "attachment;filename=large.csv"
    return response

def streaming1_csv_view(request):
    response = StreamingHttpResponse(content_type="text/csv")
    response['Content-Disposition'] = "attachment;filename=large.csv"
    rows = ("p{},{}\n".format(x,x) for x in range(0,1000000))
    response.streaming_content = rows
    return response