# Generated by Django 2.1.2 on 2018-11-29 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umarket', '0011_auto_20181129_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(default='static/images/chick.jpg', upload_to='umarket/static/images'),
        ),
    ]
