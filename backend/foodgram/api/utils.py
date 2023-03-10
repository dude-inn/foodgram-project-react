import os
from datetime import datetime as dt

from django.conf import settings
from django.http.response import HttpResponse
from fpdf import FPDF
from recipe.models import IngredientAmount


def recipe_amount_ingredients_set(recipe, ingredients):
    """
    Создаёт объект IngredientAmount связывающий объекты Recipe и
    Ingredient с указанием количества ("amount") конкретного ингридиента.
    """
    for ingredient in ingredients:
        IngredientAmount.objects.get_or_create(
            recipe=recipe,
            ingredients=ingredient['ingredient'],
            amount=ingredient['amount'],
        )


def prepare_file(user, ingredients, filename='shopping_list.pdf'):
    """
    Формирует объект типа HttpResponse, содержащий файл формата *.pdf со
    списком и количеством ингредиентов, которые нужно купить.
    """
    filename = 'shopping_list.pdf'
    create_time = dt.now().strftime('%d.%m.%Y %H:%M')
    pdf = FPDF()
    font_dir = os.path.join(
        settings.BASE_DIR,
        'import_data'
    )
    pdf.add_font('arial', style='', fname=f'{font_dir}/arial.ttf', uni=True)
    pdf.add_page()
    pdf.set_font('arial', size=13)
    pdf.cell(200, 10, txt=f'Список покупок пользователя: {user.first_name}', ln=1, align="C")
    pdf.cell(200, 10, txt=f'{create_time}', ln=1, align='C')
    table_header = ['Ингредиент', 'Количество', 'Единицы измерения']
    line_height = pdf.font_size * 2.5
    col_width = pdf.epw / 3

    for item in table_header:
        pdf.multi_cell(
            col_width, line_height, txt=item, border=1, ln=3,
            max_line_height=pdf.font_size
        )
    pdf.ln(line_height)

    for item in ingredients:
        pdf.multi_cell(
            col_width, line_height, txt=item['ingredient'], border=1, ln=3,
            max_line_height=pdf.font_size)
        pdf.multi_cell(
            col_width, line_height, txt=str(item['sum_amount']), border=1, ln=3,
            max_line_height=pdf.font_size)
        pdf.multi_cell(
            col_width, line_height, txt=item['measure'], border=1, ln=3,
            max_line_height=pdf.font_size)
        pdf.ln(line_height)

    pdf.cell(200, 10, txt='Сформировано в продуктовом помощнике Foodgram', ln=1, align="C")
    pdf.output(filename)

    response = HttpResponse(bytes(pdf.output()), content_type='application/pdf; charset=utf-8')
    response['Content-Disposition'] = f'attachment; filename={filename}'

    return response
