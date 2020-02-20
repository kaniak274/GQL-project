from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include('gql.apps.gql.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
