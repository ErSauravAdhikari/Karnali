from django.urls import path
from ninja import NinjaAPI

from auth.api import auth_api
from auth.views import redirect_to_docs
from books.api.route import book_api

api = NinjaAPI(csrf=True)
api.add_router('auth/', auth_api)
api.add_router('', book_api)

urlpatterns = [
    path("api/", api.urls, name="api"),
    path("", redirect_to_docs, name="index"),
]