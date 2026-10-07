from django.db import models

class Member(models.Model):
    nickname = models.CharField(max_length=100, unique = True)
    join_date = models.DateField(auto_now_add=True)
    bio = models.TextField(blank=True, null=True)


    class Meta:
        ordering = ["-join_date", "nickname"]
        verbose_name = '会员'

    def __str__(self):
        return self.nickname

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='articles')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    views = models.PositiveIntegerField(default=0)

    class Status(models.TextChoices):
        DRAFT = ('draft', '草稿')
        PUBLISHED = ('published', '已发布')
        ARCHIVED = ('archived', '已归档')

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    class Meta:
        ordering = ["-update_at", "-create_at", "title"]
        verbose_name = '文章'

    def __str__(self):
        return self.title

class Attachment(models.Model):
    filename = models.CharField(max_length=100)
    file = models.FileField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='attachments')
    upload_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-upload_date"]
        verbose_name = '附件文件'

    def __str__(self):
        return self.filename

class AuditLog:
    timestamp = models.DateTimeField(auto_now_add=True)
    operator = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True, related_name='audit_logs')
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, blank=True, related_name='audit_logs')
    summary = models.JSONField(default=dict)

    class Operation(models.TextChoices):
            CREATE = ('create', '创建')
            UPDATE = ('update', '更新')
            PUBLISH = ('publish', '发布')
            ARCHIVE = ('archive', '归档')
            DELETE = ('delete', '删除')
    
    operation = models.CharField(
        max_length=20,
        choices=Operation.choices,
        default=Operation.CREATE
    )

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = '审计日志'

    def __str__(self):
        return f"{self.operation} - {self.timestamp}"
