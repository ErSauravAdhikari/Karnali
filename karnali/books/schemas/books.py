from typing import List

from ninja import Schema


class BookListOutChapterList(Schema):
    id: int
    chapter_number: int
    title: str


class BookListOut(Schema):
    id: int
    author: str
    title: str
    cover: str


class BookOut(Schema):
    title: str
    author: str
    cover: str
    chapters: List[BookListOutChapterList]


class BookIn(Schema):
    title: str
    author: str
    cover: str
