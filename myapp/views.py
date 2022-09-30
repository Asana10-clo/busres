from django.shortcuts import render
# from django.http import HttpResponse

from .services import search

def index(request):
    context = {}

    if request.method == 'POST':
        from_source = request.POST.get('from')
        to_dest = request.POST.get('to')
        departure_date = request.POST.get('departure')
        return_date = request.POST.get('return')
        passengers = request.POST.get('passengers')

        query_results = search(
            from_source,
            to_dest,
            departure_date,
            return_date,
            passengers
        )

        if query_results:
            return render(request, 'result.html', locals())
        else:
            context["error"] = "Sorry no results"
            return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')

