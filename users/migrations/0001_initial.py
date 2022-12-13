# Generated by Django 4.1.3 on 2022-12-13 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=100)),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to='users')),
                ('like', models.BooleanField(default=False)),
                ('select_books', models.ManyToManyField(related_name='book_user', to='articles.book')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
