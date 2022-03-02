from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)






urlpatterns = [
    path('all-events/',views.all_events,name='all_events'),
    path('add-event/',views.add_event,name='add-event'),
    path('add-club/',views.add_club,name='add-club'),
    path('all-clubs/',views.all_clubs,name='all-clubs'),
    path('edit-event/<str:id>/',views.edit_event,name='edit-event'),
    path('event-details/<str:id>/',views.event_details,name='event-details'),
    path('club-details/<str:id>/',views.club_details,name='club-details'),
    path('edit-club/<str:id>/',views.edit_club,name='edit-club'),
    path('add-contact/',views.add_contact,name='add-contact'),
    path('get-contacts/',views.get_contacts,name='get-contacts'),







    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-details/', views.api_details, name='api-details'),
]


