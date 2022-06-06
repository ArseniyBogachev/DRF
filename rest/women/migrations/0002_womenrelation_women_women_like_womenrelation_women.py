# Generated by Django 4.0.3 on 2022-05-21 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WomenRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='women',
            name='women_like',
            field=models.ManyToManyField(through='women.WomenRelation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='womenrelation',
            name='women',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='women.women'),
        ),
    ]
