from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home_logged_in', views.home_logged_in, name='home_logged_in'),

    # group
    path('groups/', views.groups, name='groups'),

    # library
    path('library/', views.library_index, name='library'),
    path('library_01/', views.library_index_01, name='library_01'),
    path('library_02/', views.library_index_02, name='library_02'),
    path('library_03/', views.library_index_03, name='library_03'),
    path('library_demo_search/', views.library_index_demo_search, name='library_demo_search'),
    path('members/<int:pk>/', views.library_index_demo, name='library_demo'),
    path('dog/<int:pk>/', views.dog_detail_demo, name='library_demo'),

    # signup
    path('accounts/signup/', views.signup, name='signup'),

    # link
    path('links/create/', views.LinkCreate.as_view(), name='links_create'),
    path('links/<int:pk>/update/', views.LinkUpdate.as_view(), name='links_update'),
    path('links/<int:pk>/delete/', views.LinkDelete.as_view(), name='links_delete'),

     # items
    path('items/create/', views.ItemCreate.as_view(), name='items_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),

    # themes
    path('themes/create/', views.ThemeCreate.as_view(), name='themes_create'),
    path('themes/<int:pk>/update/', views.ThemeUpdate.as_view(), name='themes_update'),

    # event
    path('event/', views.event, name='event'),


    # wishlist
    path('wishlist_user/', views.wishlist_user, name='wishlist_user'),

] 