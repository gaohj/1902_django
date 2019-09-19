from django.shortcuts import render


def index(request):
    context = {
        'books':[
            '任性的弱点',
            'python从入门到放弃',
            'python深入浅出',
            'mysql从删库到跑路',
        ],
        'persons':{
            'username':'琼',
            'age':18,
            'contry':'china',
        },
        'bookes':[
            {
               'name':'三国演义',
                'author':'罗贯中',
                'price':12.34
            },
            {
                'name': '水浒传',
                'author': '施耐庵',
                'price': 34.56
            },
            {
                'name': '西游记',
                'author': '吴承恩',
                'price': 56.78
            },
            {
                'name': '红楼梦',
                'author': '曹雪芹',
                'price': 89.10
            }
        ],
        'comments':[
            'asdf',
            'asdfadsf'
        ]
    }
    return render(request,'index.html',context=context)