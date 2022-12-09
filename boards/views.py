from . models import *
from . import serializers
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.response import Response
from common.paginations import ListPagination
from rest_framework.exceptions import NotFound, NotAuthenticated, PermissionDenied
from medias.serializers import PhotoSerializer
from rest_framework.permissions import IsAuthenticated


class Boards(APIView, ListPagination):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        all_boards = Board.objects.all()
        
        serializer = serializers.BoardListSerializer(
            self.paginate(all_boards,request),
            many=True,
            context={"request":request}
        )
        
        return Response({
            "page": self.paginated_info(),
            "content": serializer.data,
        })

    def post(self, request):
        serializer = serializers.BoardDetailSerializer(data=request.data)
        if serializer.is_valid():
            board = serializer.save(
                writer=request.user
            )
            serializer= serializers.BoardDetailSerializer(board)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)        
        
class BoardDetail(APIView):
    def get_object(self, pk):
        try:
            return Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        board = self.get_object(pk)
        serializer = serializers.BoardDetailSerializer(
            board,
            context={"request":request}
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        board = self.get_object(pk)
        
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if board.writer != request.user:
            raise PermissionDenied
        
        serializer = serializers.BoardDetailSerializer(
            board,
            data=request.data,
            partial=True
        )
        
        if serializer.is_valid():
            updated_board = serializer.save()
            return Response(
                serializers.BoardDetailSerializer(updated_board).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        board = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if board.writer != request.user:
            raise PermissionDenied
        board.delete()
        return Response(status=HTTP_204_NO_CONTENT)
        
class Comments(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        all_comments = Comment.objects.all()
        serializer = CommentSerializer(all_comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save()
            return Response(
                CommentSerializer(comment).data
            )
        else:
            return Response(serializer.errors)

class NestedComments(APIView):
    def get(self, request):
        all_nested_comments = Nested_Comment.objects.all()
        serializer = NestedCommentSerializer(all_nested_comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NestedCommentSerializer(data=request.data)
        if serializer.is_valid():
            nested_comment = serializer.save()
            return Response(
                NestedCommentSerializer(nested_comment).data
            )
        else:
            return Response(serializer.errors)


class BoardDetailComments(APIView, ListPagination):

    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        board = self.get_object(pk)
        comments = board.comments.all()
        serializer = serializers.CommentSerializer(
            self.paginate(comments, request),
            many=True,
        )
        
        return Response({
            "page": self.paginated_info(),
            "content": serializer.data,
        })
    

class BoardPhotos(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            raise NotFound
    
    def post(self, request, pk):
        board = self.get_object(pk)

        if request.user != board.writer:
            raise PermissionDenied
        
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save(board=board)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

def make_error(request):
    division_by_zero = 1/0
        