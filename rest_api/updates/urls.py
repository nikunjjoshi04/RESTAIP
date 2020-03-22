from django.urls import path
from .views import update_model_detail_view, JsonCBV, JsonCBV2, SerializedDetailView, \
    SerializedListView, SerializedDetailView2, MySerializedDetailView, MySerializedListView

app_name = 'updates'
urlpatterns = [
    path('update_detail_view/', update_model_detail_view, name='update_detail_view'),
    path('class/', JsonCBV.as_view(), name='class'),
    path('class2/', JsonCBV2.as_view(), name='class2'),
    path('serialized/detail_view/', SerializedDetailView.as_view(), name='serialized_detail_view'),
    path('serialized/detail_view2/', SerializedDetailView2.as_view(), name='serialized_detail_view2'),
    path('serialized/list_view/', SerializedListView.as_view(), name='serialized_list_view'),

    path('my/serialized/list_view/', MySerializedListView.as_view(), name='my_serialized_list_view'),
    path('my/serialized/detail_view/', MySerializedDetailView.as_view(), name='my_serialized_detail_view2'),

    
]
