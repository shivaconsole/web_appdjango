# Generated by Django 4.1 on 2022-09-28 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_alter_reportdb_refimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportdb',
            name='desc',
            field=models.CharField(choices=[('WARDROBE-GST@18%', 'Wardrobe-GST@18%'), ('FURNITURE-GST@18%', 'Furniture-GST@18%'), ('KITCHEN-GST@18%', 'Kitchen-GST@18%'), ('DOOR-GST@18%', 'Door-GST@18%'), ('VANITY-GST@18%', 'Vanity-GST@18%'), ('PANELLING-GST@18%', 'Panelling-GST@18%'), ('SERVICE-GST@18%', 'Service-GST@18%'), ('ADDITIONAL-GST@18%', 'Additional-GST@18%')], default=None, max_length=100, null=True),
        ),
    ]
