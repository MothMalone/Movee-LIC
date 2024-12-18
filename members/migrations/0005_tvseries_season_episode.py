from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_rename_name_movie_title_movie_image_src_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TVSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('genre', models.CharField(blank=True, max_length=100)),
                ('seasons', models.PositiveIntegerField(default=1)),
                ('episodes', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('thumbnail', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('title', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('thumbnail', models.TextField(blank=True)),
                ('episodes', models.PositiveIntegerField(default=1)),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='season_list', to='members.tvseries')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('duration', models.PositiveIntegerField(blank=True, help_text='Duration in minutes', null=True)),
                ('source', models.TextField(blank=True)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episode_list', to='members.season')),
            ],
        ),
    ]
