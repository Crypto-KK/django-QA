# Generated by Django 2.1.9 on 2019-07-06 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models
import taggit.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('uuid_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', markdownx.models.MarkdownxField(verbose_name='内容')),
                ('is_answer', models.BooleanField(default=False, verbose_name='是否被接受')),
            ],
            options={
                'verbose_name': '回答',
                'verbose_name_plural': '回答',
                'ordering': ('-is_answer', '-created_at'),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='标题')),
                ('content', markdownx.models.MarkdownxField(verbose_name='内容')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, verbose_name='url别名')),
                ('status', models.CharField(choices=[('O', 'OPEN'), ('C', 'Close'), ('D', 'Draft')], default='O', max_length=1, verbose_name='问题状态')),
                ('has_answer', models.BooleanField(default=False, verbose_name='接受回答')),
                ('tags', taggit.managers.TaggableManager(help_text='多个标签，使用,隔开', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='q_author', to=settings.AUTH_USER_MODEL, verbose_name='提问者')),
            ],
            options={
                'verbose_name': '问题',
                'verbose_name_plural': '问题',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('uuid_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.BooleanField(default=True, verbose_name='赞同或者反对')),
                ('object_id', models.CharField(max_length=255)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_on', to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qa_vote', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '投票',
                'verbose_name_plural': '投票',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='qa.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('user', 'content_type', 'object_id')},
        ),
        migrations.AlterIndexTogether(
            name='vote',
            index_together={('content_type', 'object_id')},
        ),
    ]
