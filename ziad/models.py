from django.db import migrations, models
from django.conf import settings

class Migration(migrations.Migration):
    initial = True
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PharmacyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmacy_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('manager_phone', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
