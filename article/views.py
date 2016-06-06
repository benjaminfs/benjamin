# coding:utf-8
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
# from buluojianshe.models import Benjamin
from models import Article
from django.contrib import messages
# from django.contrib.auth.models import User
from django.template import RequestContext
from django.core.urlresolvers import reverse
# from django.core.paginator import Paginator
# from comment.models import Comment
from utils.paginator import paginate_queryset


def article_list(request, article_id):
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)
    page_no = int(request.GET.get("page_no", "1"))
    articles = Article.objects.all().order_by("-last_update_timestamp")

    object_list, pagination_data = paginate_queryset(articles, page_no, cnt_per_page=1)
    return render_to_response("article_list.html",
                                                 {"articles": object_list,
                                                  "article": article,
                                                  "pagination": pagination_data},
                                                 context_instance=RequestContext(request))


# 创建文章
# @login_required
def article_create(request, article_id):
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)
    if request.method == "GET":
        return render_to_response("article_create.html", {"artcle": article}, context_instance=RequestContext(request))
    elif request.method == "POST":
        title = request.POST['title'].strip()
        content = request.POST["content"].strip()
        if not title or not content:
            messages.add_message(request, messages.ERROR, u"标题与内容均不能为空")
            return render_to_response("article_create.html", {'"buluojianshe": block,' "title": title, "content": content}, context_instance=RequestContext(request))
# owner = User.objects.all()[0]
# owner=request.user
            new_article = Article(article=article, owner=request.user, title=title, content=content)
            new_article.save()
            messages.add_message(request, messages.INFO, u"文章发表成功")
            return redirect(reverse("article_list", args=[article.id]))


def article_detail(request, article_id):
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)
    # page_no = int(request.GET.get("comment_page_no", "1"))
    # comments = Comment.objects.filter(article=article, status=0)
    # comments, pagination_data = paginate_queryset(comments, page_no, cnt_per_page=5)
    return render_to_response("article_detail.html",
                             {"article": article},
                             context_instance=RequestContext(request))
