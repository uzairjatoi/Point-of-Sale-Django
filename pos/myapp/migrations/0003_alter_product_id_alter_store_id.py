# Generated by Django 4.2 on 2023-05-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_delete_expense_delete_expensecategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='store',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
