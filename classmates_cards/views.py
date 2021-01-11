from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from classmates_cards.models import CardModel, ClassmateData
from classmates_cards.forms import CardsForm


def GetOutput(request, current_id, *args, **kwargs):
    try:
        data = ClassmateData.objects.get(id=current_id)
    except Exception as e:
        print(e)
        return render(request, "error.html")
    else:
        return render(request, "sent-page.html", {
            'data': data
        })


class MainView(View):
    @staticmethod
    def get(request):
        return render(request, "index.html", {
            "form": CardsForm
        })

    @staticmethod
    def post(request, *args, **kwargs):
        if request.method == "POST":
            apl_form = CardsForm(request.POST)

            if apl_form.is_valid():
                CardModel.objects.create(
                    number=apl_form.cleaned_data.get('number'),
                    email=apl_form.cleaned_data.get('email'),
                )
                return redirect(f'classmate/{CardModel.objects.all().last().number}')
        return render(request, "index.html", {'form': CardsForm})

