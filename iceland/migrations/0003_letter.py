# Generated by Django 2.0.1 on 2020-05-31 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iceland', '0002_sentence_text_word'),
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'letters',
                'managed': False,
            },
        ),
    ]
