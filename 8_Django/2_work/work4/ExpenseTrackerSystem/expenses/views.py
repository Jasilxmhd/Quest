from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone

from .models import Category, Expense
from .forms import CategoryForm, ExpenseForm


@login_required(login_url='login')
def category_list(request):
    categories = Category.objects.all().order_by('-created_at')
    return render(request,'category_list.html',{'categories': categories })



@login_required(login_url='login')
def category_create(request):

    if request.method == 'POST':
        f = CategoryForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('category_list')
    else:
        f = CategoryForm()
    return render(request,'category_form.html',{'form': f,'title': 'Add Category'})



@login_required(login_url='login')
def category_update(request, id):
    data = Category.objects.get(id=id)

    if request.method == 'POST':

        form = CategoryForm(request.POST,instance=data)

        if form.is_valid():
            form.save()
            return redirect('category_list')

    else:
        form = CategoryForm(instance=data)

    return render( request, 'category_form.html', {'form': form,'title': 'Update Category'})






@login_required(login_url='login')
def category_delete(request, id):

    data = Category.objects.get(id=id)
    data.delete()

    return redirect('category_list')



@login_required(login_url='login')
def expense_list(request):

    expenses = Expense.objects.filter(user=request.user).select_related('category').order_by('-created_at')

    return render(request,'expense/expense_list.html',{'expenses': expenses})


@login_required(login_url='login')
def expense_create(request):

    if request.method == 'POST':
        f = ExpenseForm(request.POST)

        if f.is_valid():
            expense = f.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')

    else:
        f = ExpenseForm()
    return render(request,'expense/expense_form.html',{'form': f,'title': 'Add Expense'})




@login_required(login_url='login')
def expense_update(request, id):

    expense = get_object_or_404(Expense,id=id,user=request.user
)

    if request.method == 'POST':

        form = ExpenseForm(request.POST,instance=expense)

        if form.is_valid():
            form.save()
            return redirect('expense_list')

    else:
        form = ExpenseForm(instance=expense)

    return render(request,'expense/expense_form.html',{'form': form,'title': 'Update Expense'})



@login_required(login_url='login')
def expense_delete(request, id):

    expense = get_object_or_404(Expense,id=id,user=request.user)

    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')

    return render(request,'expense/expense_delete.html',{'expense': expense})




@login_required(login_url='login')
def dashboard(request):

    expenses = Expense.objects.filter(
        user=request.user
    )

    total_expenses = expenses.aggregate(
        total=Sum('amount')
    )['total'] or 0

    today = timezone.localdate()

    first_day = today.replace(day=1)

    if today.month == 12:
        next_month = today.replace(year=today.year + 1, month=1, day=1)
    else:
        next_month = today.replace(month=today.month + 1, day=1)

    current_month_expenses = expenses.filter(
        expense_date__gte=first_day,
        expense_date__lt=next_month
    ).aggregate(total=Sum('amount'))['total'] or 0


    total_categories = Category.objects.count()


    recent_expenses = expenses.order_by(
        '-created_at'
    )[:5]

    return render(request, 'dashboard.html', {
        'total_expenses': total_expenses,
        'current_month_expenses': current_month_expenses,
        'total_categories': total_categories,
        'recent_expenses': recent_expenses,
    })