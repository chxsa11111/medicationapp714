from django.db import models
from django.utils import timezone

# Create your models here.

#投薬記録
class TodoModel(models.Model):
    title = models.CharField('薬名', max_length=50)
    contents = models.TextField('詳細')
    img = models.ImageField('写真', upload_to='todo/picture/', blank=True, null=True)
    created_at = models.DateTimeField('作成日付', default=timezone.now)
    update_at = models.DateTimeField('編集日時',blank=True, null=True)
    duedate = models.DateTimeField('次回投薬', blank=True, null=True, default=timezone.now)
    
# class ImageUpload(models.Model):
#     img = models.ImageField('写真', upload_to='todo/picture/', blank=True, null=True)

#管理画面のobjectの表示をタイトルと一致して表示
    def __str__(self):
        return self.title
    
#予防接種記録
class VaccinationTodoModel(models.Model):
    title = models.CharField('予防接種名', max_length=50)
    contents = models.TextField('詳細')
    img = models.ImageField('写真', upload_to='todo/picture/', blank=True, null=True)
    created_at = models.DateTimeField('作成日付', default=timezone.now)
    update_at = models.DateTimeField('編集日時',blank=True, null=True)
    duedate = models.DateField('次回予定日',blank=True, null=True, default=timezone.now)

#管理画面のobjectの表示をタイトルと一致して表示
    def __str__(self):
        return self.title
    
