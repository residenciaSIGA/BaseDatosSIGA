# Generated by Django 5.0.4 on 2024-04-29 02:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_tipodoc_id_tipo_doc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_dep', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id_ins', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id_pue', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usu', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('pssword', models.CharField(max_length=100)),
                ('correo_e', models.CharField(max_length=100)),
                ('puesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.puesto')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id_doc', models.AutoField(primary_key=True, serialize=False)),
                ('folio', models.IntegerField()),
                ('fecha_emi', models.DateField()),
                ('fecha_rec', models.DateField()),
                ('pdf_doc', models.FileField(upload_to='documentos/')),
                ('dep_des', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dep_des', to='api.departamento')),
                ('dep_rem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dep_rem', to='api.departamento')),
                ('ins_des', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ins_des', to='api.institucion')),
                ('ins_rem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ins_rem', to='api.institucion')),
                ('usu_des', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usu_des', to='api.usuario')),
                ('usu_rem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usu_rem', to='api.usuario')),
            ],
        ),
    ]
