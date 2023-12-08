from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'detail.html', {'book': book})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # breakpoint()
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
        return render(request, 'edit.html', {'form': form})

def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
        return render(request, 'edit.html', {'form': form})
    
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()

    return redirect('book_list')

def book_delete_batch(request):
    if request.method == "POST":
        if request.POST.getlist('ids', False):
            ids = request.POST.getlist('ids')
            books = Book.objects.filter(id__in=ids)
            books.delete()

    return redirect('book_list')
