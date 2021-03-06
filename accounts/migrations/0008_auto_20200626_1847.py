# Generated by Django 3.0.6 on 2020-06-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200623_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='メールアドレス'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(upload_to='userimages/'),
        ),
    ]
