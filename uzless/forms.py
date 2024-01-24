from django import forms
from .models import PrinterModel, ContractorModel


class Printer_Insert_Form(forms.ModelForm):
    class Meta:
        model = PrinterModel
        exclude = ["printerId", "printerQueueId"]


class Printer_Delete_Form(forms.ModelForm):
    class Meta:
        model = PrinterModel
        exclude = ["name", "printerTypeId", "printStateId", "printerQueueId"]


class Contractor_Insert_Form(forms.ModelForm):
    class Meta:
        model = ContractorModel
        exclude = ["contractorId"]
