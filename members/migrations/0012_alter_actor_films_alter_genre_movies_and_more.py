from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_genre_actor_movie_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='films',
            field=models.ManyToManyField(blank=True, related_name='actor_list', to='members.movie'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='movies',
            field=models.ManyToManyField(blank=True, related_name='genre_list', to='members.movie'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, related_name='movie_list', to='members.genre'),
        ),
    ]