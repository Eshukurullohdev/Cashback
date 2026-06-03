from django.urls import path
from .views import dashboard_view, splash_view
from django.views.generic import TemplateView
urlpatterns = [

    # 🔥 SPLASH
    path('', splash_view, name='splash'),

    # 🏠 DASHBOARD
    path('dashboard/', dashboard_view, name='dashboard'),
        path(
        "manifest.json",
        TemplateView.as_view(
            template_name="manifest.json",
            content_type="application/json"
        ),
    ),
]