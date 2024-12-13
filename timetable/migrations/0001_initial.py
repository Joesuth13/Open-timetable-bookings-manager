# Generated by Django 5.1.4 on 2024-12-13 23:57

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age_group_min', models.IntegerField()),
                ('age_group_max', models.IntegerField(default=99)),
                ('duration', models.IntegerField(choices=[(15, '15 Minutes'), (30, '30 Minutes'), (45, '45 Minutes'), (60, '1 Hour'), (75, '1 Hour 15 Minutes'), (90, '1 Hour 30 Minutes'), (105, '1 Hour 45 Minutes'), (120, '2 Hours'), (135, '2 Hours 15 Minutes'), (150, '2 Hours 30 Minutes'), (165, '2 Hours 45 Minutes'), (180, '3 Hours'), (195, '3 Hours 15 Minutes'), (210, '3 Hours 30 Minutes'), (225, '3 Hours 45 Minutes'), (240, '4 Hours'), (255, '4 Hours 15 Minutes'), (270, '4 Hours 30 Minutes'), (285, '4 Hours 45 Minutes'), (300, '5 Hours')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('defaultCapacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('emergency_contact', models.CharField(max_length=15)),
                ('is_member', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Additional_info', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=False)),
                ('selected_days', models.JSONField(default=list, help_text="Store selected days of the week as a JSON array (e.g., ['MON', 'TUE'])")),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('full_name', models.CharField(max_length=200)),
                ('contact_number', models.CharField(max_length=12)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('ParticipantID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable.participant')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_or_member', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClassInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_date', models.DateTimeField()),
                ('start_time', models.DateTimeField()),
                ('finish_time', models.DateTimeField()),
                ('Capacity', models.IntegerField(verbose_name=0)),
                ('attendees', models.ManyToManyField(to='timetable.booking')),
                ('class_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.classtype')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='instanceID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.classinstance'),
        ),
        migrations.AddField(
            model_name='booking',
            name='participantID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.participant'),
        ),
    ]
