from ninja import Schema


class ChapterOut(Schema):
    id: int
    chapter_number: int
    title: str
    content: str


class ChapterIn(Schema):
    chapter_number: int
    title: str
    content: str
    book: int
