from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q, Sum, F
from .models import Paciente, TipoTest, AreaSalud
import datetime
# Create your views here.


@login_required(login_url='/')
def profile(request):
    ahora = datetime.datetime.utcnow()
    hace5Dias = ahora - datetime.timedelta(days=5)
    municipiosPositivos = []
    areasSaludLabel = []
    positivosData = []
    areasSaludNegativosLabel = []
    negativosData = []
    countUser = User.objects.count()
    municipioPositivos = Paciente.objects.values('municipio__nombre').annotate(
        Count('municipio')).exclude(resultado__nombre='Negativo').order_by()
    areaSaludPositivos = Paciente.objects.values('areaSalud__nombre').annotate(
        Count('areaSalud')).exclude(resultado__nombre='Negativo').order_by()
    areaSaludNegativos = Paciente.objects.values('areaSalud__nombre').annotate(
        Count('areaSalud')).exclude(resultado__nombre='Positivo').order_by()
    countTestRapido = Paciente.objects.filter(tipoTest__nombre='Test Rápido').exclude(resultado__nombre='Negativo').count()
    countSuma = Paciente.objects.filter(tipoTest__nombre='SUMA').exclude(resultado__nombre='Negativo').count()
    countPCR = Paciente.objects.filter(tipoTest__nombre='PCR').exclude(resultado__nombre='Negativo').count()
    countWaiTail = Paciente.objects.filter(tipoTest__nombre='WaiTai').exclude(resultado__nombre='Negativo').count()
    allPositivoAnticuerpo = Paciente.objects.exclude(resultado__nombre='Negativo').count()
    cantidadPCR = Paciente.objects.filter(fecha=hace5Dias).exclude(resultado__nombre='Negativo').count()
    # areaSaludPositivosDate = Anticuerpos.objects.values(
    #     'areaSalud__nombre', 'fecha').annotate(Count('resultado')).exclude(resultado='negativo').order_by()
    # areaSaludPositivos = Anticuerpos.objects.annotate(label=F(
    #     'areaSalud__nombre'), value=Count('resultado')).values('label', 'value').exclude(resultado='negativo').order_by()
    for a in municipioPositivos:
        municipiosPositivos.append({'label': a['municipio__nombre'],
                                    'value': a['municipio__count']})
    # for b in areaSaludPositivos:
    #     positivosData.append({'label': b['areaSalud__nombre'],
    #                           'value': b['areaSalud__count']})
    for b in areaSaludPositivos:
        areasSaludLabel.append(b['areaSalud__nombre'])
        positivosData.append(b['areaSalud__count'])
    # for c in areaSaludNegativos:
    #     areasSaludNegativosLabel.append(c['areaSalud__nombre'])
    #     negativosData.append(c['areaSalud__count'])

    context = {
        'municipiosPositivos': municipiosPositivos,
        'areasSaludLabel': areasSaludLabel,
        'positivosData': positivosData,
        'areasSaludNegativosLabel': areasSaludNegativosLabel,
        'negativosData': negativosData,
        'countTestRapido': countTestRapido,
        'countSuma': countSuma,
        'countPCR': countPCR,
        'countWaiTail': countWaiTail,
        'allPositivoAnticuerpo': allPositivoAnticuerpo,
        'countUser': countUser,
        'cantidadPCR': cantidadPCR,


    }
    return render(request, 'profile.html', context)


@login_required(login_url='/')
def usuariosPosotivoTestRapido(request):
    allTipoTest = TipoTest.objects.all()
    testRapidoPositivos = Paciente.objects.values('tipoTest__nombre').annotate(
        Count('tipoTest')).exclude(resultado__nombre='Negativo').order_by()
    testRapidoNegativos = Paciente.objects.values('tipoTest__nombre').annotate(
        Count('tipoTest')).exclude(resultado__nombre='Positivo').order_by()
    allAnticuerpos = Paciente.objects.filter(tipoTest__nombre='Test Rápido').exclude(resultado__nombre='Negativo')
    # allAnticuerpos = Anticuerpos.objects.filter(
    #     career=query).values_list('tipoTest', 'cm', 'idProv', 'nombresApellidos', 'edad', 'sexo', 'carIdentidad',
    #                               'direccion', 'areaSalud', 'municipio', 'provincia', 'condicion',
    #                               'paisProcedencia', 'fis', 'fecha', 'tipoMuestra', 'procMuestra',
    #                               'labEnvio', 'fechaEnvio', 'resultado', 'fechaRecibido', 'observacion')
    context = {
        'allAnticuerpos': allAnticuerpos,
        'testRapidoPositivos': testRapidoPositivos,
        'testRapidoNegativos': testRapidoPositivos,
        'allTipoTest': allTipoTest,
    }
    return render(request, 'testrapido_positivo.html', context)


@login_required(login_url='/')
def usuariosPosotivoKit(request):
    kitPositivos = Paciente.objects.filter(tipoTest__nombre='WaiTai').exclude(resultado__nombre='Negativo')
    context = {
        'kitPositivos': kitPositivos
    }
    return render(request, 'kit_positivo.html', context)


@login_required(login_url='/')
def usuariosPosotivoPCR(request):
    pcrPositivo = Paciente.objects.filter(tipoTest__nombre='PCR').exclude(resultado__nombre='Negativo')
    context = {
        'pcrPositivo': pcrPositivo,
    }
    return render(request, 'pcr_positivo.html', context)

@login_required(login_url='/')
def usuariosPosotivoSUMA(request):
    sumaPositivo = Paciente.objects.filter(tipoTest__nombre='SUMA').exclude(resultado__nombre='Negativo')
    context = {
        'sumaPositivo': sumaPositivo,
    }
    return render(request, 'suma_positivo.html', context)

@login_required(login_url='/')
def usuariosPosotivoAreaSalud(request):
    query = request.GET.get('test', '')
    allAreaSalud = AreaSalud.objects.all()
    allPositivoAreaSalud = Paciente.objects.filter(
        areaSalud__nombre=query).values_list('noCorridas', 'codigo', 'idSuma', 'idLab', 'tipoTest', 'nombresApellidos', 'edad', 'sexo', 'carIdentidad',
                                            'direccion', 'areaSalud__nombre', 'municipio__nombre', 'provincia__nombre', 'condicion__nombre',
                                            'paisProcedencia', 'fis', 'fecha', 'tipoMuestra__nombre', 'procMuestra__nombre',
                                            'labEnvio__nombre', 'fechaEnvio', 'resultado__nombre', 'fechaRecibido', 'observacion').exclude(resultado__nombre='Negativo')
    context = {
        'allPositivoAreaSalud': allPositivoAreaSalud,
        'allAreaSalud': allAreaSalud,
    }
    return render(request, 'area_salud_positivos.html', context)


@login_required(login_url='/')
def todosUsuariosPosotivo(request):
    allPacientes = Paciente.objects.all()
    allResultados = Paciente.objects.distinct().values_list('resultado', flat=True).order_by('resultado')
    allPositivos = Paciente.objects.all().exclude(resultado__nombre='Negativo')
    if request.method == 'POST':
        ci = request.POST['ci']
        # resultado = request.POST['resultado']
        # print(resultado)
        initDate = request.POST['initDate']
        endDate = request.POST['endDate']
        if ci:
            allPacientes = allPacientes.filter(carIdentidad__contains=ci)
        # if resultado:
        #     allPacientes = allPacientes.filter(resultado=resultado)
        #     print(allPacientes)
        currentCont = []
        if initDate:
            ec = None
            if ci:
                for a in allPacientes:
                    ec = Paciente.objects.filter(
                        Q(fechaRecibido__gte=initDate, carIdentidad__contains=ci))
            if ec == None:
                ec = Paciente.objects.filter(fechaRecibido__gte=initDate)
            if len(ec) > 0:
                for l in ec:
                    currentCont.append(l)
            allPacientes = currentCont
        currentCont = []
        if endDate:
            ec = None
            if ci:
                for a in allPacientes:
                    ec = Paciente.objects.filter(
                        Q(fechaRecibido__lte=endDate, carIdentidad__contains=ci))
            if ec == None:
                ec = Paciente.objects.filter(fechaRecibido__lte=endDate)

            if len(ec) > 0:
                for l in ec:
                    currentCont.append(l)
            allPacientes = currentCont

        currentCont = []
        if initDate and endDate:
            ec = None
            if ci:
                for a in allPacientes:
                    ec = Paciente.objects.filter(
                        Q(fechaRecibido__range=(initDate, endDate), carIdentidad__contains=ci))
            if ec == None:
                ec = Paciente.objects.filter(Q(fechaRecibido__range=(initDate, endDate)))
            if len(ec) > 0:
                for l in ec:
                    currentCont.append(l)
            allPacientes = currentCont
    context = {
        'allPositivos': allPositivos,
        'allResultados': allResultados,
        'allPacientes': allPacientes,
    }
    return render(request, 'all_positivos.html', context)


@login_required(login_url='/')
def buscarPorTest(request):
    ahora = datetime.datetime.utcnow()
    hace5Dias = ahora - datetime.timedelta(days=5)
    query = request.GET.get('test', '')
    allTipoTest = TipoTest.objects.all()
    allAnticuerpos = Paciente.objects.filter(
        tipoTest__nombre=query).filter(fecha=hace5Dias).values_list('noCorridas', 'codigo', 'idSuma', 'idLab', 'tipoTest', 'nombresApellidos', 'edad', 'sexo', 'carIdentidad',
                                            'direccion', 'areaSalud__nombre', 'municipio__nombre', 'provincia__nombre', 'condicion__nombre',
                                            'paisProcedencia', 'fis', 'fecha', 'tipoMuestra__nombre', 'procMuestra__nombre',
                                            'labEnvio__nombre', 'fechaEnvio', 'resultado__nombre', 'fechaRecibido', 'observacion').exclude(resultado__nombre='Negativo')
    context = {
        'allAnticuerpos': allAnticuerpos,
        'allTipoTest': allTipoTest,
    }
    return render(request, 'pendientes_pcr.html', context)
