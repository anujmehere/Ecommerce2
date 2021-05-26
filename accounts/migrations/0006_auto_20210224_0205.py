# Generated by Django 3.1.7 on 2021-02-23 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210224_0145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='wish_num',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='wish_product',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='wish_id',
            field=models.AutoField(default='999', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='wish_prod',
            field=models.CharField(default='ads123', max_length=250, unique=True),
        ),
    ]