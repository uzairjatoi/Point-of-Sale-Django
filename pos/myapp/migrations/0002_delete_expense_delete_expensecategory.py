# Generated by Django 4.2 on 2023-05-04 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Expense',
        ),
        migrations.DeleteModel(
            name='ExpenseCategory',
        ),
    ]