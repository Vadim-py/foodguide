from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Dish, Review
from .forms import ReviewForm


def home(request):
    categories = Category.objects.all()
    return render(request, 'menu/home.html', {'categories': categories})

def category_dishes(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    dishes = Dish.objects.filter(category=category)
    return render(request, 'menu/category_dishes.html', {'category': category, 'dishes': dishes})

def dish_detail(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    reviews = dish.reviews.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.dish = dish
            new_review.save()
            return redirect('dish_detail', dish_id=dish.id)
    else:
        form = ReviewForm()

    return render(request, 'menu/dish_detail.html', {
        'dish': dish,
        'reviews': reviews,
        'form': form
    })
