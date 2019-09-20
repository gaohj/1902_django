from django import template
from datetime import datetime
#创建模板库对象
register = template.Library()

@register.filter('my_greet')
def greet(value,word):
    return word+value
@register.filter
def time_since(value):
    if not isinstance(value,datetime):
        return value
    now = datetime.now()
    timestamp = (now-value).total_seconds()
    if timestamp<60:
        return "%s 秒前" % int(timestamp)
    elif timestamp>=60 and timestamp < 60*60:
        minutes = int(timestamp/60)
        return "%s分钟前 " % minutes
    elif timestamp>=60*60 and timestamp < 60*60*24:
        hours = int(timestamp/60/60)
        return "%s小时前 " % hours
    elif timestamp>=60*60*24 and timestamp < 60*60*24*30:
        days = int(timestamp/60/60/24)
        return "%s小时前 " % days
    else:
        return value.strftime("%Y/%m/%d %H/%M/%s")