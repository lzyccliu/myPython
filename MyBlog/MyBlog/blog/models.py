from django.db import models

# Create your models here.
class BlogsPost(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     verbose_name='博客分类'
    #     verbose_name_plural = '博客分类'
    def __str__(self):
        return self.text

class BlogPostAdmin(models.Model):
    title = models.ForeignKey(BlogsPost,on_delete=models.CASCADE,)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     verbose_name = '博客文章'
    #     verbose_name_plural = '博客文章'
    def __str__(self):
        return self.text[:50] + "..."       # + self.date_added.strftime("%Y-%m-%d-%H")