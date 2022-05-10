# Generated by Django 3.1.4 on 2022-03-11 21:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ref', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medic',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='pesel',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='patient',
            name='postal_code',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='You must provide code in format DD-DDD', regex='^[0-9]{2}-[0-9]{3}')]),
        ),
    ]
