from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse


# Create, Update, Retrieving, Deleting --> UpdateModel

class UpdateModelDetailAPIView(View):
    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id).serialize()
        return HttpResponse(obj, content_type='application/json')

    def post(self, request, *args, **kwargs):
        return HttpResponse({}, content_type='application/json')

    def put(self, request, *args, **kwargs):
        return HttpResponse({}, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        return HttpResponse({}, content_type='application/json')


class UpdateModelListAPIView(View):
    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all().serialize()
        return HttpResponse(qs, content_type='application/json')

