from celery import Celery


app = Celery('test_celery1')

app.config_from_object('apps.celery_conf')