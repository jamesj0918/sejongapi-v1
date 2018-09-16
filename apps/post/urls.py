from django.urls import path, include

from .views import ArticleListCreateAPIView, ArticleRetrieveUpdateDeleteCommentCreateAPIView, CommentUpdateDeleteAPIView, CommentListAPIView

urlpatterns = [
    path('channels/<int:channel_pk>/posts/', ArticleListCreateAPIView.as_view()),
    path('channels/<int:channel_pk>/posts/<int:article_pk>/', ArticleRetrieveUpdateDeleteCommentCreateAPIView.as_view()),
    path('channels/<int:channel_pk>/posts/<int:article_pk>/comments/', CommentListAPIView.as_view()),
    path('channels/<int:channel_pk>/posts/<int:article_pk>/comments/<int:comment_pk>/', CommentUpdateDeleteAPIView.as_view()),
]