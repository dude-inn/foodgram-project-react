from django.contrib.auth.models import AbstractUser
from django.db.models import (CharField, CheckConstraint, EmailField,
                              ManyToManyField, Q)
from django.db.models.functions import Length
from django.utils.translation import gettext_lazy

from .validators import MinLengthValidator, RegexValidator

CharField.register_lookup(Length)


class FoodgramUser(AbstractUser):
    """
    Модель пользователя.
    """
    email = EmailField(
        verbose_name='Адрес электронной почты',
        help_text='Введите email',
        unique=True,
        max_length=254
    )
    username = CharField(
        verbose_name='Уникальный юзернейм',
        help_text='Введите username',
        unique=True,
        max_length=150,
        validators=(
            MinLengthValidator(min_length=3),
            RegexValidator(),
        )
    )
    first_name = CharField(
        verbose_name='Имя',
        help_text='Введите Имя',
        max_length=150
    )
    last_name = CharField(
        verbose_name='Фамилия',
        help_text='Введите Фамилию',
        max_length=150
    )
    password = CharField(
        verbose_name=gettext_lazy('password'),
        help_text='Введите пароль',
        max_length=150,
        validators=(
            MinLengthValidator(min_length=6),
        )
    )
    subscription = ManyToManyField(
        verbose_name='Подписка',
        related_name='followers',
        to='self',
        symmetrical=False
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username', 'email',)
        constraints = (
            CheckConstraint(
                check=Q(username__length__gte=3),
                name='Имя пользователя слишком короткое'
            ),
        )

    def __str__(self) -> str:
        return self.username
