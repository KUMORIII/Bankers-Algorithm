from tabnanny import verbose
from django.db import models

# Create your models here.

class  Resource(models.Model):
    res_id = models.AutoField(primary_key=True, editable=False)
    res_name = models.CharField('资源名', max_length=15)
    total_num = models.IntegerField('资源上限', blank=False, null=False)
    available_num = models.IntegerField('可分配资源', blank=False, null=False)
    
    class Meta:
        managed = True
        verbose_name_plural='资源表'
        db_table = 'resource'
        
class Process(models.Model):
    pro_id = models.AutoField(primary_key=True, editable=False)
    pro_name = models.CharField('进程名', max_length=15)
    
    class Meta:
        managed = True
        verbose_name_plural='进程列表'
        db_table = 'process'
        
class Need(models.Model):
    need_id = models.AutoField(primary_key=True, editable=False)
    pro = models.ForeignKey(Process, models.DO_NOTHING, blank=False, null=False, verbose_name='进程')
    res = models.ForeignKey(Resource, models.DO_NOTHING, blank=False, null=False, verbose_name='资源')
    need_num = models.IntegerField('需求数', blank=False, null=False)
    
    class Meta:
        managed = True
        verbose_name_plural='需求矩阵'
        db_table = 'need'
        
class Allocation(models.Model):
    allo_id = models.AutoField(primary_key=True, editable=False)
    res = models.ForeignKey(Resource, models.DO_NOTHING, blank=False, null=False, verbose_name='资源')
    pro = models.ForeignKey(Process, models.DO_NOTHING, blank=False, null=False, verbose_name='进程')
    allo_num = models.IntegerField('已分配数', blank=False, null=False)
    hour = models.CharField('时', max_length=2)
    minute = models.CharField('分', max_length=2)
    second = models.CharField('秒', max_length=2)
    idx = models.CharField(max_length=1, editable=False)
    #time_left = models.CharField('剩余时间', max_length=20, blank=True, null=True)
    
    class Meta:
        managed = True
        verbose_name_plural='分配矩阵'
        db_table = 'allocation'

class Max(models.Model):
    max_id = models.AutoField(primary_key=True, editable=False)
    res = models.ForeignKey(Resource, models.DO_NOTHING, blank=False, null=False,verbose_name='资源')
    pro = models.ForeignKey(Process, models.DO_NOTHING, blank=False, null=False, verbose_name='进程')
    max_num = models.IntegerField('已分配数', blank=False, null=False)
    
    class Meta:
        managed = True
        verbose_name_plural = '最大需求矩阵'
        db_table = 'max'
    