from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_season_trailer_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='subtitle',
            field=models.TextField(blank=True),
        ),
    ]
