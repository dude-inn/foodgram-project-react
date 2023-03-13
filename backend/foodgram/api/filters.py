from django_filters.rest_framework import (AllValuesMultipleFilter,
                                           BooleanFilter, CharFilter,
                                           FilterSet, NumberFilter)
from recipe.models import Ingredient, Recipe


class IngredientFilter(FilterSet):
    """
    Фильтрсет для ингредиентов.
    Отбирает по вхождению текста в начало названия.
    """
    name = CharFilter(lookup_expr='istartswith')

    class Meta:
        model = Ingredient
        fields = ('name', )


class RecipeFilter(FilterSet):
    """
    Фильтрсет для рецептов.
    Отборы по:
    - в избранном у текущего пользователя;
    - в корзине у текущего пользователя;
    - автор;
    - множественный фильтр по наличию тегов.
    """
    is_favorited = BooleanFilter(
        method='get_is_favorited',
    )
    is_in_shopping_cart = BooleanFilter(
        method='get_is_in_shopping_cart',
    )
    author = NumberFilter(
        field_name='author__id',
        lookup_expr='exact'
    )
    tags = AllValuesMultipleFilter(
        field_name='tags__slug',
        null_value=True,
    )

    def get_is_favorited(self, queryset, name, value):
        """Функция фильтра по наличию в избранном у текущего пользователя"""
        if value:
            return Recipe.objects.filter(favorite=self.request.user)
        return Recipe.objects.all()

    def get_is_in_shopping_cart(self, queryset, name, value):
        """Функция фильтра по наличию в корзине у текущего пользователя"""
        if value:
            return Recipe.objects.filter(shopping_cart=self.request.user)
        return Recipe.objects.all()

    class Meta:
        model = Recipe
        fields = (
            'is_favorited',
            'is_in_shopping_cart',
            'author',
            'tags'
        )
