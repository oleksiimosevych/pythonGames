DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        #for SQLITE3
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #for MYSQL
        # 'ENGINE': 'django.db.backends.mysql',
        'USER':'111',
        'NAME':'111',
        'PASSWORD':'@@@111',
        'HOST':'111',
 
    }
}