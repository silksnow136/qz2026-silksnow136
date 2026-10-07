from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from .models import Article, Attachment

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.views = F('views') + 1
    article.save(update_fields=['views'])   # 这里是实例，不是 QuerySet，用不了 update()
    article.refresh_from_db()
    return render(request, 'articles/detail.html', {'article': article})
    # 为什么 article.views += 1; article.save() 在并发下会丢更新：多个请求对应到数据库都是对同一列进行绝对的赋值。

def upload_attachment(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.attachments = request.FILES['attachment']
        article.save()
        return render(request, 'articles/detail.html', {'article': article})
    redirect('articles:article_detail', pk=article.pk)

def delete_attachment(request, pk, attachment_id):
    article = get_object_or_404(Article, pk=pk)
    attachment = get_object_or_404(Attachment, pk=attachment_id)
    if request.method == 'POST':
        attachment.delete()
        return render(request, 'articles/detail.html', {'article': article})
    redirect('articles:article_detail', pk=article.pk)