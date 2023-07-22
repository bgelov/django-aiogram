from django.db import models


class User(models.Model):
    chat_id = models.IntegerField(unique=True, blank=False, verbose_name='ID')
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Фамилия')
    username = models.CharField(max_length=50, blank=True, null=True, verbose_name='Username')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    can_basta = models.BooleanField(default=False, verbose_name='/basta')
    can_ban = models.BooleanField(default=False, verbose_name='/ban*')
    can_ban_all = models.BooleanField(default=False, verbose_name='/banall*')
    can_mute = models.BooleanField(default=False, verbose_name='/mute*')
    can_mute_all = models.BooleanField(default=False, verbose_name='/muteall*')

    class Meta:
        verbose_name = 'администратора'
        verbose_name_plural = 'администраторы'

    def __str__(self):
        return f"{ self.first_name } { self.last_name }"


class Chat(models.Model):
    chat_id = models.CharField(max_length=255, unique=True, verbose_name='ID чата')
    title = models.CharField(blank=True, max_length=255, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    class Meta:
        verbose_name = 'чат'
        verbose_name_plural = 'чаты'

    def __str__(self):
        return self.title


class Member(models.Model):
    chat_id = models.IntegerField(unique=True, blank=False, verbose_name='ID')
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Фамилия')
    username = models.CharField(max_length=50, blank=True, null=True, verbose_name='Username')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    class Meta:
        verbose_name = 'участника'
        verbose_name_plural = 'участники'

    def __str__(self):
        return f"{ self.first_name } { self.last_name }"
