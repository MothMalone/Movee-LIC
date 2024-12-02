from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_member_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='source1',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
