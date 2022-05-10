from typing import List

from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.responses import codes_2xx
from ninja.security import django_auth

from books.models import Book, Chapter
from books.schemas.books import BookListOut, BookIn, BookOut
from books.schemas.chapters import ChapterOut, ChapterIn

book_api = Router()
_BOOK_TG = ['Books']
_CHAPTER_TG = ['Chapters']


@book_api.get("/books", tags=_BOOK_TG, response=List[BookListOut])
def get_list_of_all_books(_):
    return Book.objects.all()


@book_api.get("/books/{pk}", tags=_BOOK_TG, response=BookOut)
def get_book(_, pk: int):
    return get_object_or_404(Book, pk=pk)


@book_api.post("/books", tags=_BOOK_TG, response={codes_2xx: BookListOut, 409: dict}, auth=django_auth)
def add_book(_, payload: BookIn):
    try:
        book = Book.objects.create(**payload.dict())
        return book
    except IntegrityError as e:
        return 409, {"message": str(e)}


@book_api.get("/chapters/{pk}", tags=_CHAPTER_TG, response=ChapterOut)
def get_chapter(_, pk: int):
    return get_object_or_404(Chapter, pk=pk)


@book_api.post("/chapters/", tags=_CHAPTER_TG, response={codes_2xx: ChapterOut, 409: dict}, auth=django_auth)
def add_chapter(_, payload: ChapterIn):
    book = get_object_or_404(Book, id=payload.book)
    try:
        chapter = Chapter.objects.create(
            chapter_number=payload.chapter_number,
            title=payload.title,
            content=payload.content,
            book=book
        )
        return 200, chapter
    except IntegrityError as e:
        return 409, {"message": str(e)}
