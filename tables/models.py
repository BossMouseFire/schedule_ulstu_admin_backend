from django.db import models


class BotUsers(models.Model):
    user_id = models.IntegerField(verbose_name='vk_id пользователя')
    name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия пользователя')
    group_name = models.CharField(max_length=40, verbose_name='Название группы')

    class Meta:
        db_table = 'bot_users'
        ordering = ['id']


class BotSchedulePictures(models.Model):
    group_name = models.CharField(max_length=40, verbose_name='Название группы')
    picture_weekend_1 = models.CharField(max_length=50, verbose_name='Расписание на 1 неделю')
    picture_weekend_2 = models.CharField(max_length=50, verbose_name='Расписание на 2 неделю')

    class Meta:
        db_table = 'bot_schedule_pictures'


class BotScheduleUlSTU(models.Model):
    group_name = models.CharField(max_length=40, verbose_name='Название группы')
    today = models.TextField(verbose_name='Расписание на сегодня')
    tomorrow = models.TextField(verbose_name='Расписание на завтра')

    class Meta:
        db_table = 'bot_schedule_text'
        ordering = ['id']

