from django.http import HttpResponse
from django.shortcuts import render, redirect
from .backendrequest.backendrequest import Backend_Request
from .service.viewservice import View_Service
from .forms import Printer_Insert_Form, Contractor_Insert_Form
from .models import PrinterModel

# Create your views here.


def indexView(request):
    return render(request, "uzless/index.html")


def printerView(request):
    endpoint = "printer/getAllPrinters/"
    module = "printer"
    table_headers = [
        "Id drukarki",
        "Nazwa",
        "Typ drukarki",
        "Kolejka drukarki",
        "Stan drukarki",
    ]
    desired_key_order = [
        "printerId",
        "name",
        "printerTypeId",
        "printerQueueId",
        "printStateId",
    ]
    subpage_title = "Drukarki"
    searchCriteria = {"id": "printerId", "name": "name"}
    insert_form = Printer_Insert_Form
    context = (
        View_Service()
        .prepareBasicPage(module, subpage_title)
        .prepareTableView(table_headers, endpoint)
        .sortKeysByOrder(desired_key_order)
        .prepareInsertForm(insert_form)
        .getContext()
    )
    # since there's no printerType or printerState i'll leave it like that 
    for entity in context["entities"]:
        if entity["printerTypeId"] == 1:
            entity["printerTypeId"] = "FDM"
        if entity["printStateId"] == 1:
            entity["printStateId"] = "Aktywna"
    return render(request, "uzless/viewtemplate.html", context)


def contractorView(request):
    endpoint = "contractor/getAllContractors/"
    table_headers = ["ID Klienta", "Klient", "Email", "Telefon", "NIP"]
    module = "contractor"
    subpage_title = "Klienci"
    form = Contractor_Insert_Form(request.POST)
    insert_form = Contractor_Insert_Form
    context = (
        View_Service()
        .prepareBasicPage(module, subpage_title)
        .prepareTableView(table_headers, endpoint)
        .prepareInsertForm(insert_form)
        .getContext()
    )
    return render(request, "uzless/viewtemplate.html", context)


"""
Long spoolId,
Long contractorId,
Long printerId,
Long filamentId,
Integer weightNetto,
Integer remainingWeight
"""


def spoolView(request):
    endpoint = "spool/getAllSpools/"
    table_headers = [
        "ID szpuli",
        "Klient",
        "Drukarka",
        "Filament",
        "Waga Netto",
        "Pozostała waga",
    ]
    module = "spool"
    subpage_title = "Szpule"
    form = Contractor_Insert_Form(request.POST)
    context = (
        View_Service()
        .prepareBasicPage(module, subpage_title)
        .prepareTableView(table_headers, endpoint)
        .concatDataFromOtherTable(
            "contractorId", "fullName", "contractor/getAllContractors/"
        )
        .concatDataFromOtherTable("printerId", "name", "printer/getAllPrinters/")
        .getContext()
    )
    return render(request, "uzless/viewtemplate.html", context)


def spoolInsertView(request):
    return HttpResponse("Jescze tu pusto")


def spoolDeleteView(request):
    return HttpResponse("Jescze tu pusto")


def contractorInsertView(request):
    if request.method == "POST":
        form = Contractor_Insert_Form(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data["fullName"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            nip = form.cleaned_data["nip"]
            formdata = {
                "fullName": full_name,
                "email": email,
                "phone": phone,
                "nip": nip,
            }
            Backend_Request.postDataToEndpoint(
                "contractor/insert/", data_to_send=formdata
            )
            return redirect(request.META.get("HTTP_REFERER", "/"))
    else:
        form = Contractor_Insert_Form()
    return render(request, "partials/insert.html", {"form": form})


def contractorDeleteView(request):
    if request.method == "POST":
        selected_entity = request.POST.get("selected_entity")
        formdata = {"id": selected_entity}
        Backend_Request.postDataToEndpoint("contractor/delete/", data_to_send=formdata)
        return redirect(request.META.get("HTTP_REFERER", "/"))
    else:
        form = Printer_Insert_Form()
    return render(request, "partials/insert.html", {"form": form})


"""
/printer/insert/
{
    "name": str,
    "printerTypeId": int,
    "stateId": int
}
"""


def printerInsertView(request):
    if request.method == "POST":
        form = Printer_Insert_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            printerTypeId = form.cleaned_data["printerTypeId"]
            stateId = form.cleaned_data["printStateId"]
            formdata = {
                "name": name,
                "printerTypeId": printerTypeId,
                "stateId": stateId,
            }
            Backend_Request.postDataToEndpoint("printer/insert/", data_to_send=formdata)
            return redirect(request.META.get("HTTP_REFERER", "/"))
    else:
        form = Printer_Insert_Form()
    return render(request, "partials/insert.html", {"form": form})


def printerDeleteView(request):
    if request.method == "POST":
        selected_entity = request.POST.get("selected_entity")
        formdata = {"id": selected_entity}
        print(formdata)
        Backend_Request.postDataToEndpoint("printer/delete/", data_to_send=formdata)
        return redirect(request.META.get("HTTP_REFERER", "/"))
    else:
        form = Printer_Insert_Form()
    return render(request, "partials/insert.html", {"form": form})
