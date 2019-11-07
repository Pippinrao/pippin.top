from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import Note, Category, Tag
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


class Edit(View):
    def get(self, request, id):
        note = Note.objects.get(id=id)
        categories = Category.objects.all()
        tags = note.tag.all()
        context = {
            'note': note,
            'title': note.title,
            'body': note.body,
            'category': note.category.title,
            'categories': categories,
            'tags': tags,
        }
        return render(request, "note/edit.html", context)

    def post(self, request, id):
        note = Note.objects.get(id=id)
        title = request.POST.get("title")
        body = request.POST.get("body")
        category = request.POST.get("category")
        categories = Category.objects.all()
        context_error = {
            'title': title,
            'body': body,
            'category': category,
            'categories': categories,
        }
        if not title:
            context_error["title_empty"] = True
            return render(request, "note/create.html", context_error)
        this_cat = Category.objects.get(title=category)
        note.title = title
        note.body = body
        note.category = this_cat
        note.save()
        note.body = markdown.markdown(note.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                      ])
        context = {
            'note': note,
        }
        return render(request, 'note/detail.html', context)


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

    def post(self, request, id):
        pass


class Delete(View):
    def get(self, request, id):
        note = Note.objects.get(id=id)
        note.delete()
        notes = Note.objects.all()
        context = {
            "notes": notes,
        }
        return render(request, "note/list.html", context)

    def post(self, request, id):
        pass


class Add_something(View):
    def get(self):
        pass

    def post(self, request, id):
        note = Note.objects.get(id=id)
        flag = request.POST.get('flag')
        title = request.POST.get("title")
        if flag and title:
            if flag == 'category':
                category = Category.objects.filter(title=title)
                if not category:
                    category = Category.objects.create(title=title)
                note.category = category
            elif flag == 'tag':
                tag = Tag.objects.filter(title=title)
                if not tag:
                    tag = Tag.objects.create(title=title)
                note.tag.add(tag)
        return redirect('/edit/'+str(id)+'/')


class Rm_something(View):
    def get(self):
        pass

    def post(self, request, id):
        note = Note.objects.get(id=id)
        tag_id = request.POST.get("tag_id")
        tag = Tag.objects.get(id=int(tag_id))
        note.tag.remove(tag)
        return redirect('/edit/'+str(id)+'/')