from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_episode_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='subtitle',
            field=models.TextField(blank=True),
        ),
    ]
