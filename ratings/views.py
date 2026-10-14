"""View-функции раздела отзывов: список отзывов и отдельный отзыв."""

from django.shortcuts import render

from reviews import find_review_by_id
from storage import load_catalog


def reviews(request):
    """Страница /reviews/: список отзывов из data/ratings.json."""
    _, _, _, reviews_list = load_catalog()
    context = {
        "reviews": reviews_list,
    }
    return render(request, "ratings/review_list.html", context)


def review_detail(request, review_id):
    """Страница /reviews/<id>/: отзыв со связанными игрой и пользователем."""
    _, _, _, reviews_list = load_catalog()
    review = find_review_by_id(reviews_list, review_id)
    context = {
        "review": review,
    }
    return render(
        request,
        "ratings/review_detail.html",
        context,
        status=404 if review is None else 200,
    )
