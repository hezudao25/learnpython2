# Generated by Django 2.1.7 on 2019-05-10 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='areainfo',
            options={'verbose_name': '地区', 'verbose_name_plural': '地区'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '会员', 'verbose_name_plural': '会员'},
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='pic',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='book'),
        ),
        migrations.AlterField(
            model_name='areainfo',
            name='aparent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booktest.AreaInfo', verbose_name='父类'),
        ),
        migrations.AlterField(
            model_name='areainfo',
            name='atitle',
            field=models.CharField(max_length=20, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='add_time',
            field=models.DateField(auto_now=True, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='areas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booktest.AreaInfo', verbose_name='地区'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gener',
            field=models.CharField(choices=[('N', '保密'), ('M', '男'), ('N', '女')], default='N', max_length=1, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=124, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='remark',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=20, unique=True, verbose_name='用户名'),
        ),
    ]