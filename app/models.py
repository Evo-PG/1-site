from django.db import models

# модель автор
class Author(models.Model):
    user_name = models.CharField(max_length=100)
    about_myself = models.TextField(max_length=1000)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

# модкль категорий
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# модель пост
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    images = models.ImageField(upload_to='media/article_img')
    video = models.FileField(upload_to='media/article_video')
    media = models.FileField(upload_to='media/article_audio')
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

