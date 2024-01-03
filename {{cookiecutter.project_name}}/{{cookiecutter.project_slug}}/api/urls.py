from django.urls import path, include

urlpatterns = [
    # path('blog/', include(('{{cookiecutter.project_slug}}.blog.urls', 'blog')))
    path('users/', include(('{{cookiecutter.project_slug}}.users.urls', 'users'))),
    path('auth/', include(('{{cookiecutter.project_slug}}.authentication.urls', 'auth'))),
]
]
