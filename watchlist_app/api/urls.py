
from django.urls import path,include
from watchlist_app.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream',views.StreamPlatformVS,basename='streamplatform')
urlpatterns = [
    path('',views.WatchListAV.as_view(),name='movie_list'),
    path('<int:pk>/',views.WatchDetailAV.as_view(),name='movie_detail'),
    path('newlist/',views.WatchListGV.as_view(),name='watchlist'),
    
    path('',include(router.urls)),
    # path('stream/',views.StreamPlatformAV.as_view(),name='stream_list'),
    # path('stream/<int:pk>/',views.StreamPlatformDetailAV.as_view(),name='stream_detail'),
    
    path('<int:pk>/reviews/create/',views.ReviewCreate.as_view(),name='review-create'),
    path('<int:pk>/reviews/',views.ReviewList.as_view(),name='review-list'),
    path('review/<int:pk>/',views.ReviewDetail.as_view(),name='review-detail'),
    
    # path('reviews/<str:username>/',views.UserReview.as_view(),name='user-review'),
    path('user-reviews/',views.UserReview.as_view(),name='user-review'),#this is for individual username,eg:-localhost://?username=admin. The things after ? need not to be mentioned

]