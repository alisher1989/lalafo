from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import ProductForm
from webapp.models import Product


def products_view(request, *args, **kwargs):
    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(title__icontains=search_query)
    else:
        products = Product.objects.all()
    return render(request, 'products_view.html', context={
        'products': products
    })


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', context={
        'product': product
    })



def product_add_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'add.html', context={'form': form})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                balance=form.cleaned_data['balance'],
                cost=form.cleaned_data['cost'],
            )
            return redirect('product_view', pk=product.pk)
        else:
            return render(request, 'add.html', context={'form': form})


def product_edit_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(data={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'balance': product.balance,
            'cost': product.cost,
        })
        return render(request, 'edit.html', context={'form': form, 'product': product})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.balance = form.cleaned_data['balance']
            product.cost = form.cleaned_data['cost']
            product.save()
            return redirect('product_view', pk=product.pk)
        else:
            return render(request, 'edit.html', context={'form': form, 'product': product})



def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('product_view')