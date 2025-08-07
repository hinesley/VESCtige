import json

#from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import RideUploadForm
from .models import Ride


class RideListCreateView(View):
    queryset = Ride.objects.all()
    #serializer_class = RideSerializer

    def get(self, request):
        return HttpResponse(self.queryset.values_list())

    # def post(self, request):
    #     pass


# def upload_json(request):
#     if request.method == "POST":
#         form = RideUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = json.load(request.FILES['file'])
#
#             project = Project.objects.create(
#                 name=data["name"],
#                 description=data.get("description", "")
#             )
#
#             return redirect("success_url")
#     else:
#         form = RideUploadForm()
#
#     return render(request, "upload.html", {"form": form})
#
