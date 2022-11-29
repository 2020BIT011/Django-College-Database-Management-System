# Generated by Django 4.1 on 2022-11-23 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Student', '0005_rename_reg_no_admission_details_registration_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher_Name', models.CharField(max_length=30)),
                ('Teacher_id', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('Education', models.CharField(max_length=50)),
                ('Experience', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='media/img')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
