from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.db.models import Avg, Count

from blog.models import Post
from .models import Apartment, Villa, Land


def main(request):

    if request.method == "GET":
        query_result = _get_real_estate_data(request)

    if request.method == "POST":
        return _contact_us(request)

    # Get latest 3 posts in blog app.
    latest_blogs = Post.objects.all().order_by("-date")[:3]

    return render(
        request,
        "main/roof.html",
        context={
            "form_defaults": request.GET,
            "query_result": query_result,
            "blog": latest_blogs,
        },
    )


def _get_real_estate_data(request):
    days = request.GET.get("days")
    if days:
        s_time = datetime.now() - timedelta(days=int(days))
    category = request.GET.get("category")
    city = request.GET.get("city")
    district = request.GET.get("district")

    filters = _make_filters(request, category)

    match category:
        case "Apartment":
            base = Apartment.objects.filter(ad_date__gte=s_time, city=city)

            city_result = base.exclude(price_per_msquare=-404).aggregate(
                count=Count("id"), avg_price=Avg("price_per_msquare")
            )
            district_result = (
                base.filter(district__contains=district)
                .exclude(price_per_msquare=-404)
                .aggregate(
                    count=Count("id"), avg_price=Avg("price_per_msquare")
                )
            )
            filtered_result = (
                base.filter(district__contains=district, **filters)
                .exclude(price_per_msquare=-404)
                .aggregate(
                    count=Count("id"), avg_price=Avg("price_per_msquare")
                )
            )

        case "Villa":
            base = Villa.objects.filter(ad_date__gte=s_time, city=city)

            city_result = base.exclude(price_per_msquare=-404).aggregate(
                count=Count("id"), avg_price=Avg("price_per_msquare")
            )
            district_result = (
                base.filter(district__contains=district)
                .exclude(price_per_msquare=-404)
                .aggregate(
                    count=Count("id"), avg_price=Avg("price_per_msquare")
                )
            )
            filtered_result = (
                base.filter(district__contains=district, **filters)
                .exclude(price_per_msquare=-404)
                .aggregate(
                    count=Count("id"), avg_price=Avg("price_per_msquare")
                )
            )

        case "Land":
            base = Land.objects.filter(ad_date__gte=s_time, city=city)

            city_result = base.exclude(price_per_msquare=-404).aggregate(
                count=Count("id"), avg_price=Avg("price_per_msquare")
            )
            district_result = (
                base.filter(district__contains=district)
                .exclude(price_per_msquare=-404)
                .aggregate(
                    count=Count("id"), avg_price=Avg("price_per_msquare")
                )
            )
            filtered_result = {"count": 0, "avg_price": 0}

        case _:
            return {}

    city_result = {
        key: value if value is not None else 0
        for key, value in city_result.items()
    }
    district_result = {
        key: value if value is not None else 0
        for key, value in district_result.items()
    }
    filtered_result = {
        key: value if value is not None else 0
        for key, value in filtered_result.items()
    }
    return {
        "days": days,
        "category": category,
        "fa_category": _fa_category(category),
        "city": _fa_city(city),
        "district": district,
        "city_result": {
            "count": city_result["count"],
            "avg": int(city_result["avg_price"] // 1000000),
        },
        "district_result": {
            "count": district_result["count"],
            "avg": int(district_result["avg_price"] // 1000000),
        },
        "filtered_result": {
            "count": filtered_result["count"],
            "avg": int(filtered_result["avg_price"] // 1000000),
        },
    }


def _make_filters(request, category):
    match category:
        case "Apartment":
            filters = {}
            if floor_number := request.GET.get("apr_floor_number"):
                filters["floor_number"] = floor_number
            if total_floors := request.GET.get("apr_total_floors"):
                filters["total_floors"] = total_floors
            if production_year := request.GET.get("apr_production_year"):
                filters["production_year__gte"] = production_year
            if rooms := request.GET.get("apr_rooms"):
                filters["rooms__gte"] = rooms
            if request.GET.get("apr_elevator"):
                filters["elevator"] = 1
            if request.GET.get("apr_parking"):
                filters["parking"] = 1
            if request.GET.get("apr_storeroom"):
                filters["storeroom"] = 1

            return filters

        case "Villa":
            filters = {}
            if production_year := request.GET.get("villa_production_year"):
                filters["production_year__gte"] = production_year
            if rooms := request.GET.get("villa_rooms"):
                filters["rooms__gte"] = rooms
            if request.GET.get("villa_balcony"):
                filters["balcony"] = 1
            if request.GET.get("apr_parking"):
                filters["parking"] = 1
            if request.GET.get("apr_storeroom"):
                filters["storeroom"] = 1

            return filters

        case _:
            return {}


def _fa_category(category):
    return {
        "Apartment": "فروش آپارتمان",
        "Villa": "فروش ویلایی",
        "Land": "فروش زمین",
    }.get(category)


def _fa_city(city):
    return {
        "tehran": "تهران",
        "karaj": "کرج",
        "mashhad": "مشهدی",
        "isfahan": "اصفهان",
        "tabriz": "تبریز",
        "shiraz": "شیراز",
        "ahvaz": "اهواز",
        "qom": "قم",
        "kermanshah": "کرمانشاه",
    }.get(city)


def _contact_us(request):

    subject = request.POST.get("subject")
    email = request.POST.get("email")
    name = request.POST.get("f_name") + " " + request.POST.get("l_name")
    message = request.POST.get("text-msg")

    send_mail(
        subject=subject,
        message=f"Email:\n\t{email}\n\nName:\n\t{name}\n\nMessage:\n\t{message}",
        from_email="HelloWorld@sameagle.ir",
        recipient_list=["samadtnd@gmail.com"],
        fail_silently=False,
    )

    return redirect("contact_success")


def contact_success(request):
    return render(request, "main/contact_success.html")


def services(request):
    return render(request, "main/services.html")


def about(request):
    return render(request, "main/about.html")


def sources(request):
    return render(request, "main/sources.html")
