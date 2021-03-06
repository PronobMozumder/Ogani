# Generated by Django 3.0.7 on 2020-06-20 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0006_remove_product_posted_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='siteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteName', models.CharField(max_length=200)),
                ('siteLogo', models.ImageField(upload_to='logo')),
                ('Address', models.CharField(max_length=500)),
                ('helpLine', models.CharField(max_length=200)),
                ('topNotice', models.CharField(max_length=500)),
                ('fbLink', models.CharField(max_length=200)),
                ('twiterLink', models.CharField(max_length=200)),
                ('LinkedinLink', models.CharField(max_length=200)),
                ('supportTime', models.IntegerField()),
                ('supportHour', models.IntegerField()),
                ('siteDescription', models.CharField(max_length=500)),
                ('aboutUs', models.CharField(max_length=500)),
                ('privacyPolicy', models.CharField(max_length=800)),
                ('deliveryInfomation', models.CharField(max_length=800)),
            ],
        ),
    ]
