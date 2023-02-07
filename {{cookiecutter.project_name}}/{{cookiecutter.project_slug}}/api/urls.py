from django.urls import path, include

urlpatterns = [
    path(
        'auth/', include(('embed.authentication.urls', 'authentication'))
    ),
    path('users/', include(('embed.users.urls', 'users'))),
    path('blog/', include(('embed.blog.urls', 'blog'))),
]
