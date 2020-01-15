# Generated by Django 3.0.1 on 2020-01-15 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prueba', '0007_auto_20200113_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship_creator_set', to=settings.AUTH_USER_MODEL)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Owned',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waifu_owner_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='amigos',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='inventario',
        ),
        migrations.RemoveField(
            model_name='waifus',
            name='ident',
        ),
        migrations.AddField(
            model_name='waifus',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='waifus',
            name='waifu_card',
            field=models.ImageField(null=True, upload_to='waifus'),
        ),
        migrations.DeleteModel(
            name='Friends',
        ),
        migrations.AddField(
            model_name='owned',
            name='waifu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waifu_set', to='prueba.Waifus'),
        ),
    ]
