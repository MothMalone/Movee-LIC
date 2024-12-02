from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0012_alter_actor_films_alter_genre_movies_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
