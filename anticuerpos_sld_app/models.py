from django.db import models

# Create your models here.
SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

RESULTADO_CHOICES = (
    ('negativo', 'Negativo'),
    ('positivo', 'Positivo'),
)

CONDICION_CHOICES = (
    ('confirmado evolutivo', 'Confirmado evolutivo'),
    ('contacto de caso confirmado', 'Contacto de caso confirmado'),
    ('contacto de caso positivo', 'Contacto de caso positivo'),
    ('contacto de caso positivo confirmado',
     'Contacto de caso positivo confirmado'),
    ('sospechoso', 'Sospechoso'),
    ('bronconeumonia', 'Bronconeumonia'),
    ('positivo', 'Positivo'),
    ('sintomas sugestivo de covid-19', 'sintomas sugestivo de Covid-19'),
    ('trabajador zona roja', 'Trabajador zona roja'),
    ('trabajador de centro aislamiento', 'trabajador de centro aislamiento'),
    ('viajero', 'Viajero'),
    ('viajero  interprovincial', 'Viajero interprovincial'),
    ('vigilancia', 'Vigilancia'),
)
FIS_CHOICES = (
    ('sintomatico', 'Sintomatico'),
    ('asintomatico', 'Asintomatico'),
    ('no lo recogen', 'No lo recogen'),
)


class Provincia(models.Model):
    nombre = models.CharField('Provincia', max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'anticuerpos_sld_provincias'
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        unique_together = ['nombre']


class Municipio(models.Model):
    nombre = models.CharField('Municipios', max_length=150)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'anticuerpos_sld_municipios'
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        unique_together = ['nombre']


class AreaSalud(models.Model):
    nombre = models.CharField('Nombre Área de Salud', max_length=150)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'anticuerpos_sld_area_salud'
        verbose_name = 'Área de Salud'
        verbose_name_plural = 'Área de Salud'
        unique_together = ['nombre']


class Condicion(models.Model):
    nombre = models.CharField('Condición', max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'anticuerpos_sld_condicion'
        verbose_name = 'Condición'
        verbose_name_plural = 'Condición'
        unique_together = ['nombre']
class TipoMuestra(models.Model):
    nombre = models.CharField('Tipo de muestra', max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'anticuerpos_sld_tipo_muestra'
        verbose_name = 'Tipo de muestra'
        verbose_name_plural = 'Tipo de muestras'
        unique_together = ['nombre']

class Resultado(models.Model):
    nombre = models.CharField('Resultado', max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'anticuerpos_sld_resultado'
        verbose_name = 'Resultado'
        verbose_name_plural = 'Resultados'
        unique_together = ['nombre']


class ProcedenciaMuestra(models.Model):
    nombre = models.CharField('Procedencia de muestra', max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'anticuerpos_sld_procedencia_muestra'
        verbose_name = 'Procedencia de muestra'
        verbose_name_plural = 'Procedencia de las muestras'
        unique_together = ['nombre']


class LabEnvio(models.Model):
    nombre = models.CharField('Laboratorio de envío', max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'anticuerpos_sld_lab_envio'
        verbose_name = 'Laboratorio de envío'
        verbose_name_plural = 'Laboratorio de envío'
        unique_together = ['nombre']


class TipoTest(models.Model):
    nombre = models.CharField('Tipo Test', max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'anticuerpos_sld_tipo_test'
        verbose_name = 'Tipo de Test'
        verbose_name_plural = 'Tipo de Test'
        unique_together = ['nombre']

class ClasificacionPaciente(models.Model):
    nombre = models.CharField('Clasificación Paciente', max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'anticuerpos_sld_clasificacion_paciente'
        verbose_name = 'Clasificación Paciente'
        verbose_name_plural = 'Clasificación Paciente'
        unique_together = ['nombre']


class Paciente(models.Model):
    noCorridas = models.CharField('No. Corrida', max_length=150, null=True, blank=True)
    codigo = models.CharField('Código', max_length=150, null=True, blank=True)
    idSuma = models.CharField('ID SUMA', max_length=150, null=True, blank=True)
    idLab = models.CharField('ID. Lab', max_length=150, null=True, blank=True)
    tipoTest = models.ForeignKey(
        TipoTest, verbose_name='Tipo de Test', on_delete=models.PROTECT, max_length=150, null=True, blank=True)
    nombresApellidos = models.CharField('Nombres y Apellidos', max_length=300, null=True, blank=True)
    edad = models.BigIntegerField('Edad', null=True, blank=True)
    sexo = models.CharField('Sexo', choices=SEXO_CHOICES, max_length=150, null=True, blank=True)
    carIdentidad = models.CharField(
        'C Identidad/Pasaporte', max_length=11, default=0)
    direccion = models.TextField('Dirección', max_length=500, null=True, blank=True)
    areaSalud = models.ForeignKey(
        AreaSalud, verbose_name='Área de salud', on_delete=models.PROTECT, max_length=150, null=True, blank=True)
    municipio = models.ForeignKey(
        Municipio, on_delete=models.PROTECT, max_length=150, null=True, blank=True)
    provincia = models.ForeignKey(
        Provincia, on_delete=models.PROTECT, max_length=150, null=True, blank=True)
    condicion = models.ForeignKey(
        Condicion, verbose_name='Condición', on_delete=models.PROTECT, max_length=150, null=True, blank=True)
    paisProcedencia = models.CharField(
        'País de Procedencia', max_length=150, null=True, blank=True)
    fis = models.DateField('Fecha inicio de sintomas', max_length=150, null=True, blank=True)
    fecha = models.DateField('Fecha toma de muestra', max_length=150, null=True, blank=True)
    tipoMuestra = models.ForeignKey(
        TipoMuestra, verbose_name='Tipo de muestra', on_delete=models.PROTECT, max_length=150, null=True, blank=True)
    procMuestra = models.ForeignKey(
        ProcedenciaMuestra, verbose_name='Procedencia de muestra', on_delete=models.PROTECT, max_length=150, null=True, blank=True)
    labEnvio = models.ForeignKey(
        LabEnvio, verbose_name='Laboratorio de envío', on_delete=models.PROTECT, max_length=150, null=True, blank=True)
    fechaEnvio = models.DateField('Fecha envío de la muestra', max_length=150, null=True, blank=True)
    resultado = models.ForeignKey(
        Resultado, verbose_name='Resultado', on_delete=models.PROTECT, max_length=150, null=True, blank=True)
    fechaRecibido = models.DateField('Fecha de recibido', max_length=150, null=True, blank=True)
    clasificacionPaciente = models.ForeignKey(
        ClasificacionPaciente, verbose_name='Clasificación Paciente', on_delete=models.PROTECT, max_length=150, null=True, blank=True)
    observacion = models.TextField(
        'Observaciones', max_length=5000, null=True, blank=True)
    hiperArt = models.BooleanField('Hipertensión Arterial', default=False)
    diabetis = models.BooleanField('Diabetes Mellitus', default=False)
    cardioIs = models.BooleanField('Cardiopatía Isquémica', default=False)
    renalCro = models.BooleanField('Enfermedad renal crónica', default=False)
    cancer = models.BooleanField('Cáncer', default=False)
    epoc = models.BooleanField('EPOC', default=False)
    obesidad = models.BooleanField('Obesidad', default=False)
    insuCard = models.BooleanField('Insuficiencia cardiaca', default=False)
    otras = models.BooleanField('Otras', default=False)

    def __str__(self):
        return self.carIdentidad

    class Meta:
        db_table = 'paciente_sld_datos'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        unique_together = ['tipoTest', 'carIdentidad', 'fis']
