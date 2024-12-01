from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_tvseries_season_episode'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='trailer_url',
            field=models.TextField(blank=True),
        ),
    ]
