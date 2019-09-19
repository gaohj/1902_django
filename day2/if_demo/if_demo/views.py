from django.shortcuts import render


def index(request):
    # context = {
    #     'age':16
    # }
    context = {
        'hero':[
            '林彪',
            '乔丹',
            'c罗'
        ]
    }

    return render(request,'index.html',context=context)