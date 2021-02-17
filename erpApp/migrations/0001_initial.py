# Generated by Django 3.1.6 on 2021-02-15 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stockItem',
            fields=[
                ('stockCode', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('stockItem', models.CharField(max_length=100)),
                ('currentBalance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transDate', models.DateField()),
                ('quantity', models.IntegerField()),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erpApp.stockitem')),
            ],
        ),
    ]