# Generated by Django 5.0.3 on 2024-03-14 15:19

import recipes.validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_rename_avtive_recipes_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(max_length=50, validators=[recipes.validator.validate_unite_mesasure]),
        ),
    ]