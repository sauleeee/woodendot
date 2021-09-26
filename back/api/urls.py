from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from knox import views as knox_views
from .views.views_cbv import PostListAPIView, PostDetailAPIView, \
    Post1, Post2, Post3, Post4
from .views.views_fbv import product_detail, product_list, furniture_list, furniture_detail, \
    review_list,delete_order
from .views.views import product_furniture, product_review,OrderListGet,OrderListCreate,OrderListUpdate,OrderListDelete
from .views.authView import RegisterAPI,LoginAPI

urlpatterns = [
    path('login/', obtain_jwt_token),

    path('post/', PostListAPIView.as_view()),
    path('post/<int:pk>/', PostDetailAPIView.as_view()),
    path('post/post1', Post1.as_view()),
    path('post/post2', Post2.as_view()),
    path('post/post3', Post3.as_view()),
    path('post/post4', Post4.as_view()),

    path('product/', product_list),
    path('product/<int:product_id>/', product_detail),

    path('furniture/', furniture_list),
    path('furniture/<int:furniture_id>/', furniture_detail),
    path('product/<int:product_id>/furniture/', product_furniture),

    path('review/', review_list),
    path('product/<int:product_id>/review/', product_review),

    path('order/', OrderListGet.as_view()),
    path('order/create', OrderListCreate.as_view()),
    path('order/<int:pk>', OrderListUpdate.as_view()),
    path('order/<int:pk>/delete', OrderListDelete.as_view()),

    path('order_all_delete/',delete_order),

    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
]