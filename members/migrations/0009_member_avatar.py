from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_movie_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='avatar',
            field=models.URLField(blank=True),
        ),
    ]
