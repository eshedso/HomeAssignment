# Generated by Django 4.1.7 on 2023-03-15 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='task1.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='favorite_color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='task1.color'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_senior',
            field=models.BooleanField(default=False),
        ),
    ]