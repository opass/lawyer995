from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed

from Case.models import Case
from Info.models import County

import json

def case_list_view(request):
    case_list = Case.objects.all()
    return render(request, "Case/case_list.html", {
        "case_list": case_list
    })


def add_case_view(request):
    if request.method == "POST":
        new_case = request.POST
        Case.objects.create(
            clientName=new_case.get("clientName"),
            clientPhone=new_case.get("clientPhone"),
            arrestedReason=new_case.get("arrestedReason"),
            placeCounty=County.objects.get(id=new_case.get("placeCounty")),
            status=Case.STATUS_UNDO
        )
        return HttpResponseRedirect('/case/list/')
    else:
        return render(request, "Case/add_case.html", {
            "county_list": County.objects.all()
        })


def accept_case(request):
    if request.method == "GET":
        lawyer_id = request.GET.get("lawyer_id")
        case_id = request.GET.get("case_id")
        try:
            case = Case.objects.get(id=case_id, lawyerAssigned__id=lawyer_id)
        except Case.DoesNotExist:
            return HttpResponseNotAllowed("not exist")

        if case.status == Case.STATUS_UNDO:
            case.status = Case.STATUS_DOING
            return HttpResponse("OK")
        else:
            return HttpResponseNotAllowed("fail")


def json_case_list(request):
    all_case = []
    for case in Case.objects.all():
        case = {
            "caseId": case.id,
            "clientName": case.clientName,
            "clientPhone": case.clientPhone,
            "arrestedReason": case.arrestedReason,
            "arrestedTime": int(case.arrestedTime.timestamp()),
            "placeDescription": case.placeDescription,
            "placeCounty": case.placeCounty.name,
            "status": case.status
        }
        all_case.append(case)
    return HttpResponse(json.dumps(all_case))