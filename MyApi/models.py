from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user/{0}'.format(filename)


class ShowTodo(models.Model):
    Image = models.ImageField(upload_to=user_directory_path)
    SignatureImage = models.ImageField(upload_to=user_directory_path)
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    DoItCheck = models.BooleanField(default=False)
    UserCreated = models.ForeignKey(User, on_delete=models.CASCADE)
    On_Created = models.DateTimeField(auto_now_add=True)
    On_Updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title

    class Meta :
        ordering = ['On_Created']
