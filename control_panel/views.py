import json
from django.http import JsonResponse
from django.shortcuts import render
from stadium.models import *
from match.models import *
def show_sector(request,match_id,sector_slug):
    cpShowSector=True
    match = Match.objects.get(id=match_id).id
    sector = Sector.objects.get(name_slug=sector_slug).name_slug
    sector_name = Sector.objects.get(name_slug=sector_slug).name
    return render(request, 'cp/show_sector.html', locals())

def get_sector(request):
    body = json.loads(request.body)
    print(body)
    match = Match.objects.get(id=body['match'])
    sector = Sector.objects.get(name_slug=body['sector'])
    # print(sector)
    rows = Row.objects.filter(sector=sector)
    # print(rows)
    sector_map = []
    for row in rows:
        row_map = []
        seats = Place.objects.filter(row=row)
        for seat in seats:
            # print(seats)
            try:
                price = Price.objects.get(match=match, place=seat).price
            except:
                price = 0
            row_map.append({'row': row.number, 'seat': seat.number, 'price': price, 'selected': 0})
        sector_map.append(row_map)
    print(sector_map)
    return JsonResponse(sector_map, safe=False)

def save_sector(request):
    body = json.loads(request.body)
    sector_slug = body['sector']
    match_id = body['match']
    rows = body['rows']

    for row in rows:
        # print (len(row))
        for i in range(0,len(row)):
            # print(row[i])
            cur_row=int(row[i]['row'])
            cur_seat=int(row[i]['seat'])
            cur_price=int(row[i]['price'])
            tempSector = Sector.objects.get(name_slug=sector_slug)
            tempRow = Row.objects.get(sector=tempSector, number=cur_row)
            tempSeat = Place.objects.get(row=tempRow, number=cur_seat)
            if cur_price > 0:
                tempPrice,created = Price.objects.get_or_create(match_id=match_id,place=tempSeat,defaults={'price':cur_price})
                if not created:
                    print('price found')
                    tempPrice.price = cur_price
                    tempPrice.save()
            else:
                Price.objects.get(match_id=match_id,place=tempSeat).delete()


    return JsonResponse({'result':'ok'}, safe=False)
