from django.conf.urls import url

urlpatterns = [
    url(r'^list/(?P<article_id>\d+)', "article.views.article_list", name="article_list"),
    url(r'^create/(?P<article_id>\d+)', "article.views.article_create", name="article_create"),
    url(r'^detail/(?P<article_id>\d+)', "article.views.article_detail", name="article_detail"),
]
