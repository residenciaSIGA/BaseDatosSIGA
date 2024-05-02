from django.db import models

# Create your models here.

class TipoDoc(models.Model):
    idTipoDoc = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length = 100)

class Institucion(models.Model):
    idIns = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 100)
    direccion = models.CharField(max_length = 100)

class Departamento(models.Model):
    idDep = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 100)

class Puesto(models.Model):
    idPue = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 100)

class Usuario(models.Model):
    idUsu = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 100)
    pssword = models.CharField(max_length = 100)
    correo_e = models.CharField(max_length = 100)
    puesto = models.ForeignKey('Puesto', on_delete=models.CASCADE)

class Documento(models.Model):
    idDoc = models.AutoField(primary_key=True)
    folio = models.IntegerField()
    fecha_emi = models.DateField()
    fecha_rec = models.DateField()
    ins_rem = models.ForeignKey('Institucion', on_delete=models.CASCADE, related_name='ins_rem')
    dep_rem = models.ForeignKey('Departamento', on_delete=models.CASCADE, related_name='dep_rem')
    usu_rem = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='usu_rem')
    ins_des = models.ForeignKey('Institucion', on_delete=models.CASCADE, related_name='ins_des')
    dep_des = models.ForeignKey('Departamento', on_delete=models.CASCADE, related_name='dep_des')
    usu_des = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='usu_des')
    pdf_doc = models.FileField(upload_to='documentos/')


