from django.urls import path, include

urlpatterns = [
    path("auth/", include(("authentication.urls", "authentication"))),
    path("users/", include(("users.urls", "users"))),
    # path('common/', include(('common.urls', 'common'))),
    path("finances/", include(("finances.urls", "finances"))),
]
