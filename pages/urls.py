# from django.urls import path
# from  .views import homePageView
# # from . import views

# urlpatters=[
#     path('',  homePageView, name='home'),
# ]


from django.urls import path
from .views import homePageView
urlpatterns = [
path('', homePageView, name='home'),
]
