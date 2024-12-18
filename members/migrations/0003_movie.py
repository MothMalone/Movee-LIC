from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_email_member_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('source', models.CharField(max_length=255)),
            ],
        ),
    ]
