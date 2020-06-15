from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from staticPage.sitemaps import *
# from django.contrib.sitemaps.views import sitemap

# sitemaps = {
#     'static': StaticViewSitemap,
#     'TechniqueSitemap': TechniqueSitemap,
#     'TypeSitemap': TypeSitemap,
#     'SubSectionSitemap': SubSectionSitemap,
#     'SectionSitemap': SectionSitemap,
#     'OrdersSitemap': OrdersSitemap,
# }

admin.site.site_header = "ФК Ростов"
admin.site.site_title = "ФК Ростов - администрирование"
admin.site.index_title = "ФК Ростов - администрирование"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('news/', include('blog.urls')),
    path('cart/', include('cart.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
