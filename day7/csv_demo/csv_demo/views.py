from django.http import HttpResponse
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

