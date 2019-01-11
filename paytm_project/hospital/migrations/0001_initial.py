# Generated by Django 2.1.5 on 2019-01-10 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=150)),
                ('address', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('available', models.BooleanField(blank=True)),
                ('phoneno', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dob', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='doctors/')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField(max_length=150)),
                ('long', models.DecimalField(decimal_places=20, max_digits=50)),
                ('lat', models.DecimalField(decimal_places=20, max_digits=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'hospital',
                'verbose_name_plural': 'hospitals',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='hospital.Hospital'),
        ),
        migrations.AlterIndexTogether(
            name='doctor',
            index_together={('id', 'slug')},
        ),
    ]
