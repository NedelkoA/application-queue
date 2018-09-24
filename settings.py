# QUEUE_SERVER = {
#     'ENGINE': 'backends.redis',
#     'HOST': 'localhost',
#     'PORT': '5672',
# }

QUEUE_SERVER = {
    'ENGINE': 'backends.redis',
    'HOST': 'localhost',
    'PORT': '6379',
    'DB': 1,
}
