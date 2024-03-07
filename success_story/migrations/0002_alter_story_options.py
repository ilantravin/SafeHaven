from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'verbose_name_plural': 'סיפורי הצלחה'},
        ),
    ]
