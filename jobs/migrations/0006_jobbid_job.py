# Generated by Django 2.2.1 on 2019-08-09 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_remove_jobbid_job_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobbid',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.Job'),
        ),
    ]