# Generated by Django 4.0.5 on 2022-06-07 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_description_question_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]