from django.db import models
from common.models import CommonModel


class Board(CommonModel):    
    writer = models.ForeignKey("users.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=140,default="")
    content = models.TextField(default="")
    like_users = models.ManyToManyField(
        "users.User",
        related_name="like_boards"
    )
    
    def count_comments(board):
        return board.comments.count() + board.nested_comments.count()
    ## photo 모델 추가 
    def count_likes(board):
        return board.like_users.count()
    
    def __str__(self):
        return self.title
    
# Create your models here.
class Comment(CommonModel):
    writer = models.ForeignKey("users.User", on_delete=models.CASCADE)
    board = models.ForeignKey(
        "boards.Board", 
        on_delete=models.CASCADE,
        related_name="comments"
    )
    content = models.TextField(default="")
    comment_index = models.IntegerField()
    
    
    def __str__(self):
        return self.content[:5]
    
    
class Nested_Comment(CommonModel):
    writer = models.ForeignKey("users.User", on_delete=models.CASCADE)
    comment = models.ForeignKey(
        "boards.Comment",
        on_delete=models.CASCADE,
        related_name="nested_comments"
    )
    board = models.ForeignKey(
        "boards.Board", 
        on_delete=models.CASCADE,
        related_name="nested_comments"
    )
    content = models.TextField(default="")
    nested_comment_index = models.IntegerField()
    
    ## photo 모델 추가 
    
    def __str__(self):
        return self.content[:5]
    
    
