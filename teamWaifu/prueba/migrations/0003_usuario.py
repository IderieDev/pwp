# Generated by Django 2.2.4 on 2019-09-25 16:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0002_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30, verbose_name='Username')),
                ('correo', models.EmailField(max_length=60, verbose_name='Correo electrónico')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('favorito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario_requests_created', to='prueba.Item')),
                ('friends', models.ManyToManyField(blank=True, related_name='_usuario_friends_+', to='prueba.Usuario')),
                ('inventario', models.ManyToManyField(blank=True, to='prueba.Item')),
            ],
        ),
    ]
