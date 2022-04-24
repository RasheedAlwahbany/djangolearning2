from sqlite3 import Cursor
from django.apps import AppConfig
from django.db import connection
from django.db.models.signals import post_migrate

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    
    def post_migrate(self,*args,**kwargs):
        sql_statment="""
        
        select * from core.Course
        """
        cursor=connection.cursor()
        cursor.execute(sql_statment)
    def ready(self):
        # this ready function its run after runserver
        # this post_migrate run after migrate
        post_migrate.connect(self.post_migrate,sender=self)
        
