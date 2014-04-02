# coding: utf-8
from lib_app.models import Book
from lib_app.forms import Book_Edit_Form
from django.template import RequestContext 
from django.views.generic import ListView,DetailView
from django.shortcuts import render_to_response


class BookListView(ListView):
    model = Book
    template_name='book_list.html'
    context_object_name = 'book_list'

class BookDetailView(DetailView): 
    model = Book
    template_name='book_detail.html'
    context_object_name = 'book_detail'

def book_edit(request,book_id):
    edit_book=Book.objects.get(id=book_id)
    all_is_right = ''
    if request.method == 'POST':    
        form=Book_Edit_Form(request.POST)
        if form.is_valid():
            fcd = form.cleaned_data
            edit_book.title=fcd['title']
            edit_book.author=fcd['author']                         
            edit_book.save()
            all_is_right =u"Вы успешно отредактировали информацию о книге "+"\""+edit_book.title+"\""            
            #form=Book_Edit_Form()
    else:
        form=Book_Edit_Form(initial={'title':edit_book.title})
     
    return render_to_response('book_edit.html',{'form':form,'all_is_right': all_is_right,'book_title':edit_book.title}, 
                                       context_instance=RequestContext(request) )
