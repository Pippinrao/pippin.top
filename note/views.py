from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import Note, Category
import markdown

# Create your views here.


class Home(View):
    def get(self, request):
        notes = Note.objects.all()
        context = {
            "notes": notes,
        }
        return render(request, "note/list.html", context)


class Create(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {
            'categories': categories,
        }
        return render(request, "note/create.html", context)

    def post(self, request):
        title = request.POST.get("title")
        body = request.POST.get("body")
        category = request.POST.get("category")
        categories = Category.objects.all()
        context = {
            'title': title,
            'body': body,
            'category': category,
            'categories': categories,
        }
        if not title:
            context["title_empty"] = True
            return render(request, "note/create.html", context)
        this_cat = Category.objects.get(title=category)
        new_note = Note.objects.create(
            author=request.user,
            title=title, body=body,
            category=this_cat
        )
        return redirect("/")


class Detail(View):
    def get(self, request, id):
        note = Note.objects.get(id=id)
        note.body = markdown.markdown(note.body,
                             extensions=[
                                 'markdown.extensions.extra',
                                 'markdown.extensions.codehilite',
                             ])
        context = {
            'note': note,
        }
        return render(request, 'note/detail.html', context)

    def post(self):
        pass
