from django.http import response
import challenges
from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

dict_month = {
    "january": "Eat",
    "february": "Walk",
    "march": "Learn",
    "april": "Eat",
    "may": "Walk",
    "june": "Learn",
    "july": "Eat",
    "august": "Walk",
    "september": "Eat",
    "october": "Walk",
    "november": "Learn",
    "december": None

}

def index(request):

    list_items = ""
    months = list(dict_month.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })
    '''   for month in months:
        capitalized_moth = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_moth}</a></li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data) '''

def monthly_chalanges_by_number(request, month):
    my_key = list(dict_month.keys())
    response_text = my_key[month - 1]
    path_response = reverse("month_challenge", args=[response_text])
    return HttpResponseRedirect(path_response)
    

def monthly_chalanges(request, month):
    text = None
    try:
        text = dict_month[month]

        #response_data = render_to_string("challenges/challenge.html")
    except:
        raise Http404()
    #return HttpResponse(response_data)
    return render(request, "challenges/challenge.html", {
        "tekst": text,
        "tekst_month": month
    })
  

