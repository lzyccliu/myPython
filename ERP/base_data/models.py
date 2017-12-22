from django.db import models

# Create your models here.

class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32,unique=True)
    
class UserInfo(models.Model):
    username = models.CharField(max_length=32,blank=True,verbose_name='用户名')
    password = models.CharField(max_length=60,help_text='pwd')
    email = models.EmailField()
    # default=1 表示默认属于哪个部门，django在数据库中将user_group存取字段为user_group_id，实际上user_group为UserGroup的对象封装了(uid,caption,ctime,uptime)
    user_group = models.ForeignKey("UserGroup",to_field='uid', default=1)

