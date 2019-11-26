BROKER_URL = 'redis://localhost:6379/1'

CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'

CELERY_IMPORTS = (
'apps.task1',
'apps.task2',
'apps.beat_task',
)

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = False
CELERY_TASK_ANNOTATIONS = {'apps.task1.add': {'rate_limit': '10/s'}}
CELERY_TASK_PUBLISH_RETRY = True


from datetime import timedelta
from celery.schedules import crontab
CELERYBEAT_SCHEDULE = {
    'my_beat':{
        'task':'apps.beat_task.beat_test',
        'schedule':timedelta(seconds=5),
        # 'schedule':crontab(minute='57',hour='20'),
        # 'schedule':crontab(hour='*/3'),
        'args':(2,6),
        'kwargs':{'name':'hallen_41'},
        # 'options':{
        #     'queue':'beat_task',
        #     'routing_key':'beat_task'
        # }
        # 'relative':False
    },

    'spider_task':{
            'task':'apps.sina_spider_task.get_spider',
            'schedule':timedelta(minutes=10),
            'options':{
                'queue':'spider_queue',
                'routing_key':'spider_queue'
            }

        }

}