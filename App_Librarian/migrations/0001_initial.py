# Generated by Django 3.2.23 on 2024-05-12 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=255)),
                ('authors', models.CharField(default=None, max_length=255, null=True)),
                ('genre', models.CharField(default='Unknown', max_length=100)),
                ('language', models.CharField(default=None, max_length=255)),
                ('publication_year', models.PositiveIntegerField(default=2022)),
                ('publisher', models.CharField(default='Unknown Publisher', max_length=255)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('description', models.TextField(default='')),
                ('cover_image', models.FileField(default='default_cover.jpg', upload_to='coverimages/')),
                ('pdf_file', models.FileField(default='default_pdf.pdf', upload_to='pdfs/')),
                ('no_of_copies_actual', models.IntegerField(default=None)),
                ('no_of_copies_current', models.IntegerField(default=None)),
            ],
            options={
                'db_table': 'Book_Data',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('publication_id', models.AutoField(primary_key=True, serialize=False)),
                ('publication_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('issued', 'Issued'), ('returned', 'Returned')], max_length=20)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Librarian.book_data')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
