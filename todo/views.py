from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
    try:
        if request.method == 'POST':
            form = ListForm(request.POST or None)

            if form.is_valid() :
            # if request.POST :
                form.save()
                all_items = List.objects.all
                messages.success(request,("Item has been added to List"))
                return render(request, 'index.html', {'all_items': all_items})

        else:
            all_items = List.objects.all
            return render(request,'index.html',{'all_items':all_items})
    except Exception as ex:
        print("[ishan-app] exception wile post api withexcp as {}".format(ex))
        all_items = List.objects.all
        return render(request, 'index.html', {'all_items': all_items})


def about(request):
    return render(request,'about.html',{})

def delete(request,list_id):
     item = List.objects.get(pk=list_id)
     item.delete()
     messages.success(request, ("Item has been deleted"))
     return redirect('home')
