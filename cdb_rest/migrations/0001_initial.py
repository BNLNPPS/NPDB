# Generated by Django 3.2.9 on 2022-11-23 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalTag',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_column='name', max_length=80, unique=True)),
                ('description', models.CharField(db_column='description', max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_column='created')),
                ('updated', models.DateTimeField(auto_now=True, db_column='updated')),
            ],
            options={
                'db_table': 'GlobalTag',
            },
        ),
        migrations.CreateModel(
            name='GlobalTagStatus',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_column='name', max_length=80, unique=True)),
                ('description', models.CharField(db_column='description', max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_column='created')),
            ],
            options={
                'db_table': 'GlobalTagStatus',
            },
        ),
        migrations.CreateModel(
            name='PayloadListIdSequence',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'db_table': 'PayloadListIdSequence',
            },
        ),
        migrations.CreateModel(
            name='PayloadType',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_column='name', max_length=80, unique=True)),
                ('description', models.CharField(db_column='description', max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_column='created')),
            ],
            options={
                'db_table': 'PayloadType',
            },
        ),
        migrations.CreateModel(
            name='PayloadList',
            fields=[
                ('id', models.BigIntegerField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_column='name', max_length=255, unique=True)),
                ('description', models.CharField(db_column='description', max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_column='created')),
                ('updated', models.DateTimeField(auto_now=True, db_column='updated')),
                ('global_tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payload_lists', to='cdb_rest.globaltag')),
                ('payload_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdb_rest.payloadtype')),
            ],
            options={
                'db_table': 'PayloadList',
            },
        ),
        migrations.CreateModel(
            name='PayloadIOV',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('payload_url', models.CharField(db_column='payload_url', max_length=255)),
                ('checksum', models.CharField(db_column='checksum', max_length=255)),
                ('major_iov', models.BigIntegerField(db_column='major_iov')),
                ('minor_iov', models.BigIntegerField(db_column='minor_iov')),
                ('major_iov_end', models.BigIntegerField(db_column='major_iov_end')),
                ('minor_iov_end', models.BigIntegerField(db_column='minor_iov_end')),
                ('description', models.CharField(db_column='description', max_length=255, null=True)),
                ('inserted', models.DateTimeField(auto_now_add=True, db_column='created')),
                ('updated', models.DateTimeField(auto_now=True, db_column='updated')),
                ('payload_list', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payload_iov', to='cdb_rest.payloadlist')),
            ],
            options={
                'db_table': 'PayloadIOV',
            },
        ),
        migrations.AddField(
            model_name='globaltag',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdb_rest.globaltagstatus'),
        ),
        migrations.AddIndex(
            model_name='payloadiov',
            index=models.Index(fields=['major_iov', 'minor_iov'], name='PayloadIOV_major_i_be996d_idx'),
        ),
    ]
