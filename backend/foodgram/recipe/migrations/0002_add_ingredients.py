# Generated by Django 3.2.18 on 2023-03-04 02:16

import json

from django.db import migrations


def add_ingredients(apps, schema_editor):
    Ingredient = apps.get_model('recipe', 'Ingredient')
    with open(
            './data/ingredients.json',
            'r',
            encoding='utf-8'
    ) as json_file:
        for row in json.load(json_file):
            new_ingredient = Ingredient(
                name=row['name'],
                measurement_unit=row['measurement_unit']
            )
            new_ingredient.save()


def remove_ingredients(apps, schema_editor):
    Ingredient = apps.get_model('recipe', 'Ingredient')
    with open(
            './data/ingredients.json',
            'r',
            encoding='utf-8'
    ) as json_file:
        for row in json.load(json_file):
            Ingredient.objects.get(name=row['name']).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_ingredients,
            remove_ingredients
        )
    ]
