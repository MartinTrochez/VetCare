# Generated by Django 4.2 on 2023-04-06 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('especie', models.CharField(max_length=255)),
                ('raza', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('edad', models.IntegerField(null='true')),
            ],
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico', models.TextField(max_length=255)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('peso', models.FloatField(blank=True, max_length=255, null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mascota', to='clientes.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('localidad', models.CharField(max_length=255)),
                ('provincia', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=10)),
                ('mascota', models.ManyToManyField(related_name='mascota_dueno', to='clientes.animal')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dueno', to='clientes.cliente'),
        ),
    ]
