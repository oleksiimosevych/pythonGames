
DEBUG = True
#decomment for production
# DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        #for SQLITE3
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #for MYSQL
        # 'ENGINE': 'django.db.backends.mysql',
        'USER':'',
        'NAME':'',
        'PASSWORD':'',
        'HOST':'localhost',
 
    }
}