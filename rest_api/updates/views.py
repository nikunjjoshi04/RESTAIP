import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Update
from django.views.generic import View
from rest_api.mixins import JsonCBVMixin
from django.core.serializers import serialize

# Create your views here.


# def update_model_detail_view(request):
#     data = {
#         'count': 1000,
#         'content': 'Some new content'
#
#     }
#     json_data = json.dumps(data)
#     return HttpResponse(json_data, content_type='application/json')


def update_model_detail_view(request):
    data = {
        'count': 1000,
        'content': 'Some new content'

    }
    return JsonResponse(data)


class JsonCBV(View):

    def get(self, request, *args, **kwargs):
        data = {
            'count': 1000,
            'content': 'Some new content'
        }
        return JsonResponse(data)


class JsonCBV2(JsonCBVMixin, View):

    def get(self, request, *args, **kwargs):
        data = {
            'count': 1000,
            'content': 'Some new content'
        }
        return self.render_to_json_response(data)


class SerializedDetailView(View):

    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = {
            'user': obj.user.username,
            'content': obj.content
        }
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')


class SerializedDetailView2(JsonCBVMixin, View):

    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):

    def get(self, request, *args, **kwargs):
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')


class MySerializedDetailView(JsonCBVMixin, View):

    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1).serialize()
        return HttpResponse(obj, content_type='application/json')


class MySerializedListView(View):

    def get(self, request, *args, **kwargs):
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')

