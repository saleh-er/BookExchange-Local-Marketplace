from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from books import models
from django.contrib.auth.decorators import login_required
def book_list(request):
    query = request.GET.get('q')
    if query:
        # This searches for the query in the title OR the author
        books = Book.objects.filter(
            models.Q(title__icontains=query) | models.Q(author__icontains=query)
        ).order_by('-created_at')
    else:
        books = Book.objects.all().order_by('-created_at')
    
    return render(request, 'books/book_list.html', {'books': books})
@login_required
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.seller = request.user # Links the book to the logged-in user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    # Security check: only the seller can delete it
    if request.user == book.seller:
        book.delete()
    return redirect('book_list')