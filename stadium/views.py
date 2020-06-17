from django.shortcuts import render
from .models import *
def create_sectors(request):
    sectors=[
        {
        'name':417,
        'rows':
            {
                '1': 20,
                '2': 20,
                '3': 10,
                '4': 10,
                '5': 20,
                '6': 20,
             }

    },
        {
            'name': 418,
            'rows':
                {
                    '1': 10,
                    '2': 15,
                    '3': 10,
                    '4': 10,
                    '5': 20,
                    '6': 20,
                }

        },


    ]
    Sector.objects.all().delete()
    for sector in sectors:
        # print(sector['name'])

        new_sector = Sector.objects.create(name=sector['name'])
        seats = 0
        for row in sector['rows']:
            # print(row)
            # print(sector['rows'][row])
            new_row = Row.objects.create(number=row,sector=new_sector)
            seats += sector['rows'][row]
            for i in range(1,sector['rows'][row]+1):
                # print (i)
                Place.objects.create(row=new_row, number=i)
            new_sector.seats = seats
            new_sector.save()
        print('sector created: ',sector['name'])


def get_sector_info(request):
    match = Match.objects.get(id=1)
    sector = Sector.objects.get(name_slug='417')
    seats = sector
    price = Price.objects.filter(place__row__sector_id=sector.id, match=match)
    print(price)