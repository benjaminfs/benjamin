# coding:utf-8
from django.shortcuts import render_to_response
# from buluojianshe.models import Benjamin
from article.models import Article
# from django.contrib.auth.models import User
from django.template import RequestContext
# from django.core.paginator import Paginator
# from comment.models import Comment
# from utils.paginator import paginate_queryset


def article_list(request, fs_id=0):
    fs_id = int(fs_id)
    articles = Article.objects.all().order_by("-last_update_timestamp")
    return render_to_response("article_list.html",
                                                 {"articles": articles},
                                                 context_instance=RequestContext(request)
)
