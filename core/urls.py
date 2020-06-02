from django.conf.urls import url
from django.contrib import admin
from iceland.views import IndexView, ConstructionListView, ConstructionDetailView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^formulas/', ConstructionListView.as_view(), name='formulas'),
    url(r'^construction_(?P<pk>\d+)$', ConstructionDetailView.as_view(), name='construction'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
