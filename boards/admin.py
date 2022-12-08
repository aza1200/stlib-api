from django.contrib import admin
from .models import Board,Comment,Nested_Comment

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = (
        "writer","title","content"
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = ("writer","board","content","comment_index")
    
    readonly_fields = (
            "created_at",
            "updated_at",
        )


@admin.register(Nested_Comment)
class NestedCommentAdmin(admin.ModelAdmin):
    list_display = ("writer","comment","board","content","nested_comment_index")
    readonly_fields = (
            "created_at",
            "updated_at",
        )
