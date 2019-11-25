BROKER_URL = 'redis://localhost:6379/1'

CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'

CELERY_IMPORTS = (
'apps.task1',
'apps.task2'
)

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = False
CELERY_TASK_ANNOTATIONS = {'apps.task1.add': {'rate_limit': '10/s'}}
CELERY_TASK_PUBLISH_RETRY = True