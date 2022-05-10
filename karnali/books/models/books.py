from django.db import models


# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    cover = models.URLField()

    class Meta:
        unique_together = [['author', 'title']]

    @staticmethod
    def chapters(self):
        return self.chapters.all()

    def __str__(self):
        return self.title + " by " + self.author


class Chapter(models.Model):
    chapter_number = models.IntegerField()
    book = models.ForeignKey(Book, related_name='chapters', on_delete=models.CASCADE)
    content = models.TextField()
    title = models.CharField(max_length=255)

    class Meta:
        unique_together = (('chapter_number', 'book'))

    def __str__(self):
        return f"{self.book.title} - {self.chapter_number}"
