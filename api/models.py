from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = RichTextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        ordering = ['created']

    @property
    def categories(self):
        return Category.objects.filter(post_id=self.id)

    def __str__(self):
        return self.title

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return 'POST : '+str(self.post)+' By '+str(self.owner)+' Comment : '+self.body

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    posts = models.ManyToManyField('Post', related_name='categories', blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    email = models.EmailField(max_length=100, null=True)
    subject = models.CharField(max_length=255, blank=False, default='')
    message = models.CharField(max_length=500, blank=False, default='')