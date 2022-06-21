from unicodedata import name
from django.urls import path
from cars import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.VehicleListView.as_view(), name="vehicle_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)