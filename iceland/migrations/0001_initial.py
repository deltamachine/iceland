# Generated by Django 2.0.1 on 2020-05-31 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clustering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_short', models.IntegerField(blank=True, null=True)),
                ('id_mask', models.IntegerField(blank=True, null=True)),
                ('id_cluster', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'clustering',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NgramFull',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_text', models.IntegerField(blank=True, null=True)),
                ('id_sent', models.IntegerField(blank=True, null=True)),
                ('word_start', models.IntegerField(blank=True, null=True)),
                ('word_end', models.IntegerField(blank=True, null=True)),
                ('full_text', models.TextField(blank=True, null=True)),
                ('short_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ngram_full',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NgramShort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_text', models.TextField(blank=True, null=True)),
                ('id_pos_mask', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ngram_short',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PosMask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mask', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pos_mask',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sentences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_text', models.IntegerField(blank=True, null=True)),
                ('sent_idx', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sentences',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'texts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_sentence', models.IntegerField(blank=True, null=True)),
                ('word_idx', models.IntegerField(blank=True, null=True)),
                ('form', models.TextField(blank=True, null=True)),
                ('lemma', models.TextField(blank=True, null=True)),
                ('gram', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'words',
                'managed': False,
            },
        ),
    ]
