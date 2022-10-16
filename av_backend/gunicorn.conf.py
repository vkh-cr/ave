import multiprocessing

wsgi_app = "av_backend.wsgi:application"

workers = multiprocessing.cpu_count() * 2 + 1
bind = "0.0.0.0:8000"

reload = False
preload_app = True

# user = "av"
# group = "av"

max_requests = 1000
max_requests_jitter = 100

accesslog = "-"
errorlog = "-"
