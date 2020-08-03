from django.contrib import admin
from django.urls import path, include
import blog.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    # 
    # 추후 detail, create, delete 경로 추가!
    #
    # path('blog/update/<int:blog_id>/', blog.views.update, name="update"),

    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
