from django.db import models


class BotUsers(models.Model):
    user_id = models.IntegerField(verbose_name='vk_id пользователя')
    name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия пользователя')
    group_name = models.CharField(max_length=40, verbose_name='Название группы')
    faculty = models.ForeignKey('FacultiesULSTU', on_delete=models.PROTECT, default=1)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'bot_users'
        ordering = ['id']

    def __str__(self):
        return self.name


class BotSchedulePictures(models.Model):
    group_name = models.CharField(max_length=40, verbose_name='Название группы')
    picture_weekend_1 = models.CharField(max_length=50, verbose_name='Расписание на 1 неделю')
    picture_weekend_2 = models.CharField(max_length=50, verbose_name='Расписание на 2 неделю')

    class Meta:
        verbose_name = 'Расписание на неделю'
        verbose_name_plural = 'Таблица расписаний на неделю'
        db_table = 'bot_schedule_pictures'
        ordering = ['id']

    def __str__(self):
        return self.group_name


class BotScheduleUlSTU(models.Model):
    group_name = models.CharField(max_length=40, verbose_name='Название группы')
    today = models.TextField(verbose_name='Расписание на сегодня')
    tomorrow = models.TextField(verbose_name='Расписание на завтра')

    class Meta:
        verbose_name = 'Расписание на 2 дня'
        verbose_name_plural = 'Таблица расписаний на 2 дня'
        db_table = 'bot_schedule_text'
        ordering = ['id']

    def __str__(self):
        return self.group_name


class FacultiesULSTU(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Назание факультета')

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'
        db_table = 'faculty_ulstu'

    def __str__(self):
        return self.title


