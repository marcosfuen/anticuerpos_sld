from django.urls import path
from .views import profile, usuariosPosotivoTestRapido, usuariosPosotivoKit, usuariosPosotivoPCR, buscarPorTest, todosUsuariosPosotivo, usuariosPosotivoSUMA, usuariosPosotivoAreaSalud
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/testrapido_positivo', usuariosPosotivoTestRapido, name='testrapido'),
    path('accounts/profile/kit_positivo', usuariosPosotivoKit, name='kit'),
    path('accounts/profile/pcr_positivo', usuariosPosotivoPCR, name='pcr'), 
    path('accounts/profile/buscar_por_test/', buscarPorTest, name='buscarPorTest'),
    path('accounts/profile/todos_positivos/', todosUsuariosPosotivo, name='todos_positivos'),
    path('accounts/profile/suma_positivos/', usuariosPosotivoSUMA, name='suma_positivos'),
    path('accounts/profile/area_salud_positivos/', usuariosPosotivoAreaSalud, name='area_salud_positivos'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
