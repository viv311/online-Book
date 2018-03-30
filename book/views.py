from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Books,Auther

def index(request):
    all_books = Books.objects.all()
    context = {'all_books':all_books,}
    return render(request,'book/bookInfo.html',context)


def detail(request, book_id):
    try:
        book = Books.objects.get(pk=book_id)
    except Books.DoesNotExist:
        raise Http404("Book Does Not Exist")
    return render(request, 'book/bookDetails.html', {'book':book})
