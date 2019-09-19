from django.urls import converters,register_converter
class CategoryConverter(object):
    regex = r'\w+|(\w+\+\w+)+'

    #将url /article/python+go+ruby  变成  ['article','python','go']
    def to_python(self,value):
        result = value.split("+")
        return result
    #reverse 反转获取url 需要将 列表 转成 python+go+ruby
    def to_url(self,value):
        if isinstance(value,list):
            result = "+".join(value)
            return result
        else:
            raise RuntimeError("reverse转化url的时候，参数必须为列表")

register_converter(CategoryConverter,'cate')
