from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_movie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='movie',
            name='image_src',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='source',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
