# Generated by Django 3.2.6 on 2021-08-17 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='유저 아이디')),
                ('user_pwd', models.CharField(max_length=20, verbose_name='유저 비밀번호')),
                ('user_name', models.CharField(max_length=20, verbose_name='유저 이름')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='계정생성시간')),
            ],
            options={
                'verbose_name': '개인 사용자',
                'verbose_name_plural': '개인 사용자',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='wastedata',
            fields=[
                ('data_id', models.AutoField(primary_key=True, serialize=False)),
                ('base_date', models.DateTimeField()),
                ('city', models.CharField(max_length=10, verbose_name='city')),
                ('emd_nm', models.CharField(max_length=10, verbose_name='town name')),
                ('area_cd', models.CharField(max_length=20, verbose_name='area code')),
                ('em_cnt', models.IntegerField(verbose_name='cnt')),
                ('em_g', models.IntegerField(verbose_name='g')),
                ('pay_amt', models.IntegerField(verbose_name='pay amount')),
            ],
            options={
                'verbose_name': 'food waste data',
                'verbose_name_plural': 'food waste data',
                'db_table': 'wastedata',
            },
        ),
        migrations.CreateModel(
            name='worker',
            fields=[
                ('worker_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='유저 아이디')),
                ('worker_pwd', models.CharField(max_length=20, verbose_name='유저 비밀번호')),
                ('worker_name', models.CharField(max_length=20, verbose_name='유저 이름')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='계정생성시간')),
            ],
            options={
                'verbose_name': 'worker 사용자',
                'verbose_name_plural': 'worker 사용자',
                'db_table': 'worker',
            },
        ),
    ]
