from django.shortcuts import render
from django.http import HttpResponse

from Info.models import County


def init_county(request):
    county_list = (
        (1, "臺北市"),
        (2, "新北市"),
        (3, "臺中市"),
        (4, "臺南市"),
        (5, "高雄市"),
        (6, "基隆市"),
        (7, "新竹市"),
        (8, "嘉義市"),
        (9, "桃園縣"),
        (10, "新竹縣"),
        (11, "苗栗縣"),
        (12, "彰化縣"),
        (13, "南投縣"),
        (14, "雲林縣"),
        (15, "嘉義縣"),
        (16, "屏東縣"),
        (17, "宜蘭縣"),
        (18, "花蓮縣"),
        (19, "臺東縣"),
        (20, "澎湖縣"),
        (21, "金門縣"),
        (22, "馬祖縣")
    )

    for county_id, county_name in county_list:
        County.objects.get_or_create(
            id=county_id,
            name=county_name
        )

    return HttpResponse("OK")