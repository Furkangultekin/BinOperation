from django.urls import path, include
from .views import AddBinView, GetBinView, AddOperationView, GetOperationView, AddBinOperationView,GetBinOperationView,GetCollectionFreq

urlpatterns = [
    path('add_bin', AddBinView.as_view()),
    path('get_bin', GetBinView.as_view()),
    path('add_operation', AddOperationView.as_view()),
    path('get_operation', GetOperationView.as_view()),
    path('add_bin_ops', AddBinOperationView.as_view()),
    path('get_bin_ops', GetBinOperationView.as_view()),
    path('get_col_freq', GetCollectionFreq.as_view()),
]