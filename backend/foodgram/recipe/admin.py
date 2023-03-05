from django.contrib.admin import ModelAdmin, TabularInline, register
from django.utils.safestring import mark_safe

from .forms import TagForm
from .models import Ingredient, IngredientAmount, Recipe, Tag

EMPTY_VAL_PLACEHOLDER = 'Не указано'


@register(Ingredient)
class IngredientAdmin(ModelAdmin):
    """Класс настройки вида админки для ингредиентов."""
    list_display = ('name', 'measurement_unit')
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = EMPTY_VAL_PLACEHOLDER
    save_on_top = True


@register(IngredientAmount)
class IngredientAmountAdmin(ModelAdmin):
    """Класс настройки вида админки для количества ингредиентов."""
    pass


class IngredientInline(TabularInline):
    """Класс настройки виджета отображения количества ингредиентов."""
    model = IngredientAmount
    extra = 1


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    """Класс настройки вида админки для рецептов."""
    list_display = (
        'name',
        'author',
        'getimage',
        '_get_count_added_to_favorite'
    )
    fields = (
        ('image', ),
        ('name', 'author'),
        ('tags', 'cooking_time'),
        ('text', )
    )
    raw_id_fields = ('author', )
    list_filter = (
        'name',
        'author__username',
        'tags'
    )
    search_fields = ('name', 'author')
    save_on_top = True
    empty_value_display = EMPTY_VAL_PLACEHOLDER
    inlines = (IngredientInline, )

    def getimage(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="35"')

    getimage.short_description = 'Изображение'


@register(Tag)
class TagAdmin(ModelAdmin):
    """Класс настройки вида админки для тегов."""
    form = TagForm
    list_display = ('name', 'slug', 'color')
    fieldsets = (
        (
            None,
            {
                'fields': (('name', 'slug'), 'color')
            }
        ),
    )
    search_fields = ('name', )
    save_on_top = True
    empty_value_display = EMPTY_VAL_PLACEHOLDER
