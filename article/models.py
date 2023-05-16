from django.db import models
from django.utils.text import slugify

# from ckeditor.fields import RichTextField
# Create your models here.


class Article(models.Model):
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="Author"
    )
    title = models.CharField(max_length=50, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    article_image = models.FileField(
        blank=True, null=True, verbose_name="Article File or Image"
    )
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date",editable=False)

    slug = models.SlugField(
        verbose_name="Slug", max_length=150, unique=True, editable=False
    )

    def __str__(self):
        return self.title

    def get_slug(self):
        slug = slugify(
            self.title.replace("ı", "i")
            .replace("ə", "e")
            .replace("ü", "u")
            .replace("ö", "o")
        )
        unique = slug
        number = 1
        while Article.objects.filter(slug=unique).exists():
            unique = f"{slug} - {number}"
            number += 1
        return unique

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-created_date"]


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        related_name="comments",
        on_delete=models.CASCADE,
        verbose_name="Article",
    )
    comment_author = models.CharField(max_length=50, verbose_name="Name")
    comment_content = models.CharField(max_length=200, verbose_name="Comment")
    comment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ["-comment_date"]
