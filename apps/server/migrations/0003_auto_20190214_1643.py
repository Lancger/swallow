# Generated by Django 2.1 on 2019-02-14 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_remove_server_asset_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nic',
            options={'ordering': ['id'], 'verbose_name': '网卡', 'verbose_name_plural': '网卡'},
        ),
        migrations.AlterModelOptions(
            name='server',
            options={'ordering': ['id'], 'verbose_name': '服务器', 'verbose_name_plural': '服务器'},
        ),
        migrations.AlterModelOptions(
            name='serverip',
            options={'ordering': ['id'], 'verbose_name': 'IP地址', 'verbose_name_plural': 'IP地址'},
        ),
    ]
