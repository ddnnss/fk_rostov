from django.shortcuts import render
from stadium.models import *
from match.models import *
def show_sector(request,match_id,sector_slug):
    match = Match.objects.get(id=match_id)
    sector = Sector.objects.get(name_slug=sector_slug)
    # print(sector)
    rows = Row.objects.filter(sector=sector)
    # print(rows)
    sector_map=[]

    for row in rows:
        row_map=[]
        seats = Place.objects.filter(row=row)
        for seat in seats:
            # print(seats)
            try:
                price = Price.objects.get(match=match, place=seat).price
            except:
                price = 0

            row_map.append({'row': row.number,'seat':seat.number,'price':price, 'selected':0})
        sector_map.append(row_map)
    print(sector_map)
    return render(request, 'cp/show_sector.html', locals())

