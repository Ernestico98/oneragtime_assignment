# Generated by Django 4.0.3 on 2022-03-07 23:28

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_amount', models.FloatField(validators=[api.models.Investment.validate_investment_amount])),
                ('fee_percentage', models.FloatField(default=0, validators=[api.models.Investment.validate_fee_percentage])),
                ('investment_date', models.DateField(auto_now_add=True)),
                ('up_front_payed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investments', to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_type', models.CharField(max_length=30)),
                ('status', models.CharField(default='validated', max_length=20)),
                ('bill_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills', to='api.user')),
            ],
        ),
    ]
