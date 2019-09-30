from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Note

# Create your views here.


class Home(View):
    def get(self, request):
        notes = Note.objects.all()
        context = {
            "notes": notes,
        }
        return render(request, "note/list.html", context)
