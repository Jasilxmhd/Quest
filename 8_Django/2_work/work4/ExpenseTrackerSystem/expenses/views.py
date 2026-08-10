from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Category
from .forms import CategoryForm


def category_list(request):
    categories = Category.objects.all().order_by('-created_at')
    return render(request, 'category_list.html', {'categories': categories})


def category_create(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('category_list')

    else:

        form = CategoryForm()

    return render(request,'category_form.html',
        {
            'form': form,
            'title': 'Add Category'
        }
    )


def category_update(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    category = get_object_or_404(Category,id=id)

    if request.method == 'POST':

        form = CategoryForm(request.POST,instance=category)

        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)

    return render(request,'category_form.html',
        {
            'form': form,
            'title': 'Update Category'
        }
    )


def category_delete(request, id):

    if not request.user.is_authenticated:

        return redirect('login')

    category = get_object_or_404(Category,id=id)

    if request.method == 'POST':
        category.delete()
        return redirect('category_list')

    return render(request,'category_delete.html',
        {
            'category': category
        }
    )