# Generated by Django 4.1 on 2022-08-13 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_books_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
