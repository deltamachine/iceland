# Generated by Django 2.0.1 on 2020-05-31 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iceland', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_idx', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'sentences',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'texts',
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_idx', models.IntegerField(blank=True, null=True)),
                ('form', models.TextField(blank=True, null=True)),
                ('lemma', models.TextField(blank=True, null=True)),
                ('gram', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'words',
            },
        ),
    ]
