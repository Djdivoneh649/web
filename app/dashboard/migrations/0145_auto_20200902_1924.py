# Generated by Django 2.2.4 on 2020-09-02 19:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0144_auto_20200902_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdirectory',
            name='rank_funder',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='activity_level',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='average_rating',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='bounty_earnings',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='bounty_work_start_orgs',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='bounty_work_submit_orgs',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='earnings_count',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='github_created_at',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='grant_contribution_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='hack_work_start_orgs',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='hack_work_submit_orgs',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='handle',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='join_date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='keywords',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='last_action_on',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='persona',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='reliability',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='verification_status',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdirectory',
            name='which_hacks_joined',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None),
        ),
    ]