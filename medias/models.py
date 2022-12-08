from django.db import models
from common.models import CommonModel

# Create your models here.
class Photo(CommonModel):
    file = models.URLField()
    description = models.CharField(max_length=140)
    board = models.ForeignKey(
        "boards.Board",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos"
    )
    
    def __str__(self):
        return self.file

class Video(CommonModel):
    file = models.URLField()
    board = models.OneToOneField(
        "boards.Board",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="videos"
    )
    
    def __str__(self):
        return self.file
