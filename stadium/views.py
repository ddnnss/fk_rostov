from django.shortcuts import render
from .models import *
def s_417(request):
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
        for row in sector['rows']:
            # print(row)
            # print(sector['rows'][row])
            new_row = Row.objects.create(number=row,sector=new_sector)
            for i in range(1,sector['rows'][row]+1):
                # print (i)
                Place.objects.create(row=new_row,number=i)
        print('sector created: ',sector['name'])
