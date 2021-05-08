# Generated by Django 3.2.2 on 2021-05-08 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Answer', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('desc', models.TextField(help_text='Poll description', max_length=100)),
                ('received_answers', models.JSONField(blank=True, default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Question', max_length=64)),
                ('type', models.IntegerField(choices=[(0, 'Text Answer'), (1, 'One Answer'), (2, 'Multi Answers')])),
                ('answers', models.ManyToManyField(blank=True, null=True, related_name='questions', to='polls_app.Answers')),
                ('polls', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to='polls_app.polls')),
            ],
        ),
    ]
