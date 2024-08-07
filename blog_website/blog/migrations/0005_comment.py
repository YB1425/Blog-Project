# Generated by Django 4.2.14 on 2024-07-13 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_posttable_post_publish_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.posttable')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.usertable')),
            ],
        ),
    ]
