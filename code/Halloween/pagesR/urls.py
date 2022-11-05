from django.urls import path
from .views import peliculaPageView, peliculaPageDetail, peliculaPageCreate, peliculaPageUpdate, peliculaPageDelete


urlpatterns = [
    # ---------------------pelicula-------------
    path('pelicula', peliculaPageView.as_view(), name='pelicula'),
    path('pelicula/<int:pk>', peliculaPageDetail.as_view(), name='pelicula_detalle'),
    path('pelicula/nuevo', peliculaPageCreate.as_view(), name='pelicula_nuevo'),
    path('pelicula/<int:pk>/editar/',
         peliculaPageUpdate.as_view(), name='pelicula_editar'),
    path('pelicula/<int:pk>/eliminar/',
         peliculaPageDelete.as_view(), name='pelicula_eliminar'),
]
