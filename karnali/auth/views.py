from django.shortcuts import redirect
from django.urls import reverse


def redirect_to_docs(request):
    return redirect(reverse("api-1.0.0:openapi-swagger"))
