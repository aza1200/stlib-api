from .models import *
from rest_framework import serializers
from users.serializers import TinyUserSerializer
from medias.serializers import PhotoSerializer

class BoardListSerializer(serializers.ModelSerializer):
    
    writer = TinyUserSerializer(read_only=True)
    count_comments  = serializers.SerializerMethodField()
    is_writer = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only= True)
    
    class Meta:
        model = Board
        fields = (
            "id",
            "title",
            "created_at",
            "content",
            "writer",
            "count_comments",
            "is_writer",
            "like_count",
            "photos",
        )
    
    def get_like_count(self,board):
        return board.count_likes()
    
    def get_count_comments(self, board):
        return board.count_comments()

    def get_is_writer(self, board):
        request = self.context["request"]
        return board.writer == request.user

 

class NestedCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nested_Comment
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    nested_comments = NestedCommentSerializer(many=True, read_only=True, )
    # nested_comments=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model = Comment
        fields =  "__all__"

class BoardDetailSerializer(serializers.ModelSerializer):
    
    writer = TinyUserSerializer(read_only=True)
    count_comments  = serializers.SerializerMethodField()
    is_writer = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only= True)
    
    class Meta:
        model= Board
        fields = "__all__"    
    
    def get_count_comments(self, board):
        return board.count_comments()

    def get_is_writer(self, board):
        request = self.context["request"]
        return board.writer == request.user
        

    