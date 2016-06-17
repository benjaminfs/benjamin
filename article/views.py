# coding:utf-8
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
# from buluojianshe.models import Benjamin
from article.models import Article
from django.template import RequestContext


def article_index(request):
    articles = Article.objects.all().order_by("-last_update_timestamp")
    return render_to_response("article_list.html",
                                                 {"articles": articles},
                                                 context_instance=RequestContext(request)
)


def article_create(request):
    # article_id = int(article_id)
    if request.method == "GET":
        return render_to_response("article_create.html",
                                                        {},
                                                        context_instance=RequestContext(request)
)
    else:
        title = request.POST["title"].strip()
        content = request.POST["content"].strip()
        if not title or not content:
            messages.add_message(request, messages.ERROR, u"标题与内容均不能为空")
            return render_to_response("article_create.html",
                                                           {"title": title, "content": content},
                                                           context_instance=RequestContext(request)
            )
    new_article = Article(owner=request.user, title=title, content=content)
    new_article.save()
    messages.add_message(request, messages.INFO, u"成功发表文章")
    return redirect(reverse("article_list"))
