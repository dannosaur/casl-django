# Generated by Django 2.1 on 2022-04-25 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CASLPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(help_text='Subject', max_length=128)),
                ('action', models.TextField(help_text='Action', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='UserPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='Created date')),
                ('permission', models.ForeignKey(help_text='Permission', on_delete=django.db.models.deletion.CASCADE, to='casl_django.CASLPermission')),
                ('user', models.ForeignKey(help_text='User', on_delete=django.db.models.deletion.CASCADE, related_name='casl_permissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='caslpermission',
            unique_together={('subject', 'action')},
        ),
        migrations.AlterUniqueTogether(
            name='userpermission',
            unique_together={('permission', 'user')},
        ),
    ]
