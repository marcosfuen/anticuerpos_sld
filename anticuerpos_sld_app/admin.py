from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from .models import Provincia, Municipio, AreaSalud, Paciente, Condicion, TipoMuestra, LabEnvio, ProcedenciaMuestra, TipoTest, ClasificacionPaciente, Resultado

# Register your models here.

class PacienteResource(resources.ModelResource):
    # provincia_name = fields.Field(column_name='Provincia',attribute='provincia',widget=ForeignKeyWidget(Provincia, 'nombre'))
    # municipio_name = fields.Field(column_name='Municipios',attribute='municipio',widget=ForeignKeyWidget(Municipio, 'nombre'))
    # tipoTest_name = fields.Field(column_name='Tipo Test',attribute='tipoTest',widget=ForeignKeyWidget(TipoTest, 'nombre'))
    # areaSalud_name = fields.Field(column_name='Nombre Área de Salud',attribute='areaSalud',widget=ForeignKeyWidget(AreaSalud, 'nombre'))
    # condicion_name = fields.Field(column_name='Condición',attribute='condicion',widget=ForeignKeyWidget(Condicion, 'nombre'))
    # tipoMuestra_name = fields.Field(column_name='Tipo de muestra',attribute='tipoMuestra',widget=ForeignKeyWidget(TipoMuestra, 'nombre'))
    # labEnvio_name = fields.Field(column_name='Laboratorio de envío',attribute='labEnvio',widget=ForeignKeyWidget(LabEnvio, 'nombre'))
    # procMuestra_name = fields.Field(column_name='Procedencia de muestra',attribute='procMuestra',widget=ForeignKeyWidget(ProcedenciaMuestra, 'nombre'))
    # resultado_name = fields.Field(column_name='Resultado',attribute='resultado',widget=ForeignKeyWidget(Resultado, 'nombre'))
    # clasificacion_name = fields.Field(column_name='Clasificación Paciente',attribute='clasificacionPaciente',widget=ForeignKeyWidget(ClasificacionPaciente, 'nombre'))
    
    # def before_import(self, dataset, using_transactions, dry_run, **kwargs):
    #     for row in dataset:
    #         is_exist_clasificacion = ClasificacionPaciente.objects.filter(nombre__iexact=row[24]).exists()
    #         if not is_exist_clasificacion:
    #             ClasificacionPaciente.objects.create(nombre=row[24])
    #         is_exist_resultado = Resultado.objects.filter(nombre__iexact=row[22]).exists()
    #         if not is_exist_resultado:
    #             Resultado.objects.create(nombre=row[22])
    #         is_exist_procMuestra = ProcedenciaMuestra.objects.filter(nombre__iexact=row[19]).exists()
    #         if not is_exist_procMuestra:
    #             ProcedenciaMuestra.objects.create(nombre=row[19])
    #         is_exist_labEnvio = LabEnvio.objects.filter(nombre__iexact=row[20]).exists()
    #         if not is_exist_labEnvio:
    #             LabEnvio.objects.create(nombre=row[20])
    #         is_exist_tipoMuestra = TipoMuestra.objects.filter(nombre__iexact=row[18]).exists()
    #         if not is_exist_tipoMuestra:
    #             TipoMuestra.objects.create(nombre=row[18])
    #         is_exist_condicion = Condicion.objects.filter(nombre__iexact=row[14]).exists()
    #         if not is_exist_condicion:
    #             Condicion.objects.create(nombre=row[14])
    #         is_exist_provincia = Provincia.objects.filter(nombre__iexact=row[13]).exists()
    #         if not is_exist_provincia:
    #             Provincia.objects.create(nombre=row[13])
    #         is_exist_municipio = Municipio.objects.filter(nombre__iexact=row[12]).exists()
    #         if not is_exist_municipio:
    #             provincia = Provincia.objects.get(nombre__iexact=row[13])
    #             Municipio.objects.create(nombre=row[12], provincia=provincia)
    #         is_exist_tipo_test = TipoTest.objects.filter(nombre__iexact=row[5]).exists()
    #         if not is_exist_tipo_test:
    #             TipoTest.objects.create(nombre=row[5])
    #         is_exist_area_salud = AreaSalud.objects.filter(nombre__iexact=row[11]).exists()
    #         if not is_exist_area_salud:
    #             municipio = Municipio.objects.get(nombre__iexact=row[12])
    #             AreaSalud.objects.create(nombre=row[11], municipio=municipio)

    #     return super(self.__class__, self).before_import(dataset, using_transactions, dry_run, **kwargs)
    # def before_import(self, dataset, using_transactions, dry_run, **kwargs):
    #     for row in dataset.dict:
    #         is_exist_clasificacion = ClasificacionPaciente.objects.filter(nombre__iexact=row['Clasificación Paciente']).exists()
    #         if not is_exist_clasificacion:
    #             ClasificacionPaciente.objects.create(nombre=row['Clasificación Paciente'])
    #         is_exist_resultado = Resultado.objects.filter(nombre__iexact=row['Resultado']).exists()
    #         if not is_exist_resultado:
    #             Resultado.objects.create(nombre=row['Resultado'])
    #         is_exist_procMuestra = ProcedenciaMuestra.objects.filter(nombre__iexact=row['Procedencia de muestra']).exists()
    #         if not is_exist_procMuestra:
    #             ProcedenciaMuestra.objects.create(nombre=row['Procedencia de muestra'])
    #         is_exist_labEnvio = LabEnvio.objects.filter(nombre__iexact=row['Laboratorio de envío']).exists()
    #         if not is_exist_labEnvio:
    #             LabEnvio.objects.create(nombre=row['Laboratorio de envío'])
    #         is_exist_tipoMuestra = TipoMuestra.objects.filter(nombre__iexact=row['Tipo de muestra']).exists()
    #         if not is_exist_tipoMuestra:
    #             TipoMuestra.objects.create(nombre=row['Tipo de muestra'])
    #         is_exist_condicion = Condicion.objects.filter(nombre__iexact=row['Condición']).exists()
    #         if not is_exist_condicion:
    #             Condicion.objects.create(nombre=row['Condición'])
    #         is_exist_provincia = Provincia.objects.filter(nombre__iexact=row['Provincia']).exists()
    #         if not is_exist_provincia:
    #             Provincia.objects.create(nombre=row['Provincia'])
    #         is_exist_municipio = Municipio.objects.filter(nombre__iexact=row['Municipios']).exists()
    #         if not is_exist_municipio:
    #             Municipio.objects.create(nombre=row['Municipios'])
    #         is_exist_tipo_test = TipoTest.objects.filter(nombre__iexact=row['Tipo Test']).exists()
    #         if not is_exist_tipo_test:
    #             TipoTest.objects.create(nombre=row['Tipo Test'])
    #         is_exist_area_salud = AreaSalud.objects.filter(nombre__iexact=row['Nombre Área de Salud']).exists()
    #         if not is_exist_area_salud:
    #             AreaSalud.objects.create(nombre=row['Nombre Área de Salud'])

    #     return super(self.__class__, self).before_import(dataset, using_transactions, dry_run, **kwargs)

    @classmethod
    def field_from_django_field(self, field_name, django_field, readonly):
        """
        Returns a Resource Field instance for the given Django model field.
        """
        FieldWidget = self.widget_from_django_field(django_field)
        widget_kwargs = self.widget_kwargs_for_field(field_name)
        field = fields.Field(attribute=field_name, column_name=django_field.verbose_name,
                widget=FieldWidget(**widget_kwargs), readonly=readonly)
        return field
    class Meta:
        model = Paciente
        fields = ('id', 'noCorridas', 'codigo', 'idSuma', 'idLab', 'tipoTest__nombre', 'nombresApellidos', 'edad', 'sexo', 'carIdentidad',
                     'direccion', 'areaSalud__nombre', 'municipio__nombre', 'provincia__nombre', 'condicion__nombre',
                     'paisProcedencia', 'fis', 'fecha', 'tipoMuestra__nombre', 'procMuestra__nombre',
                     'labEnvio__nombre', 'fechaEnvio', 'resultado__nombre', 'fechaRecibido', 'clasificacionPaciente__nombre', 'hiperArt', 'diabetis', 'cardioIs', 'renalCro', 'cancer', 'epoc', 'obesidad', 'insuCard', 'otras', 'observacion')
        export_order = ('id', 'noCorridas', 'codigo', 'idSuma', 'idLab', 'tipoTest__nombre', 'nombresApellidos', 'edad', 'sexo', 'carIdentidad',
                     'direccion', 'areaSalud__nombre', 'municipio__nombre', 'provincia__nombre', 'condicion__nombre',
                     'paisProcedencia', 'fis', 'fecha', 'tipoMuestra__nombre', 'procMuestra__nombre',
                     'labEnvio__nombre', 'fechaEnvio', 'resultado__nombre', 'fechaRecibido', 'clasificacionPaciente__nombre', 'observacion', 'hiperArt', 'diabetis', 'cardioIs', 'renalCro', 'cancer', 'epoc', 'obesidad', 'insuCard', 'otras', )
class ProvinciaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
class MunicipioAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class AreaSaludAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class CondicionAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class TipoTestAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
class TipoMuestraAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
class LabEnvioAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class ProcedenciaMuestraAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class ClasificacionPacienteAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class ResultadoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class PacienteAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PacienteResource
    list_filter = ('tipoTest__nombre','areaSalud__nombre', 'fis', 'resultado')
    list_display = ('noCorridas', 'codigo', 'idSuma', 'idLab', 'tipoTest', 'nombresApellidos', 'edad', 'sexo', 'carIdentidad',
                    'direccion', 'areaSalud', 'municipio', 'provincia', 'condicion',
                    'paisProcedencia', 'fis', 'fecha', 'tipoMuestra', 'procMuestra',
                    'labEnvio', 'fechaEnvio', 'resultado', 'clasificacionPaciente', 'fechaRecibido', 'hiperArt', 'diabetis', 'cardioIs', 'renalCro', 'cancer', 'epoc', 'obesidad', 'insuCard', 'otras','observacion')
    list_display_links = ('carIdentidad',)
    fields = (('noCorridas', 'codigo', 'idSuma', 'idLab', 'tipoTest'), ('nombresApellidos', 'edad', 'sexo', 'carIdentidad'),
              'direccion', ('provincia', 'municipio', 'areaSalud', 'condicion'),
              'paisProcedencia', ('fis', 'fecha'), ('tipoMuestra', 'procMuestra',
                                  'labEnvio'), ('fechaEnvio', 'fechaRecibido'), ('hiperArt', 'diabetis', 'cardioIs', 'renalCro', 'cancer', 'epoc', 'obesidad', 'insuCard', 'otras'), ('resultado', 'clasificacionPaciente'), 'observacion')
    search_fields = ['noCorridas', 'codigo', 'idSuma', 'idLab', 'tipoTest__nombre', 'nombresApellidos', 'edad', 'sexo', 'carIdentidad',
                     'direccion', 'areaSalud__nombre', 'municipio__nombre', 'provincia__nombre', 'condicion__nombre',
                     'paisProcedencia', 'fis', 'fecha', 'tipoMuestra__nombre', 'procMuestra__nombre',
                     'labEnvio__nombre', 'fechaEnvio', 'resultado__nombre', 'clasificacionPaciente__nombre', 'fechaRecibido', 'observacion']
    autocomplete_fields = ['provincia', 'municipio', 'areaSalud', 'condicion', 'tipoMuestra', 'tipoTest', 'labEnvio', 'procMuestra', 'clasificacionPaciente', 'resultado']
    list_editable = ['hiperArt', 'diabetis', 'cardioIs', 'renalCro', 'cancer', 'epoc', 'obesidad', 'insuCard', 'otras']
    # fields = (('cm', 'idProv'), ('nombresApellidos',
    #           'edad', 'sexo', 'carIdentidad'), 'direccion', ('areaSalud', 'municipio', 'provincia', 'condicion', 'paisProcedencia', 'fis'))
    # fields = ('cm', 'idProv', 'nombresApellidos', 'edad', 'sexo', 'carIdentidad', 'direccion',
    #           'areaSalud', 'municipio', 'provincia', 'condicion', 'paisProcedencia', 'fis')

admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(AreaSalud, AreaSaludAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Condicion, CondicionAdmin)
admin.site.register(TipoMuestra, TipoMuestraAdmin)
admin.site.register(TipoTest, TipoTestAdmin)
admin.site.register(LabEnvio, LabEnvioAdmin)
admin.site.register(ProcedenciaMuestra, ProcedenciaMuestraAdmin)
admin.site.register(ClasificacionPaciente, ClasificacionPacienteAdmin)
admin.site.register(Resultado, ResultadoAdmin)

admin.site.site_header = 'Diagnóstico'
admin.site.site_title = 'Diagnóstico'
admin.site.site_url = '/accounts/profile/'
