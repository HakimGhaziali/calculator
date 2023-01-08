from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm
from .models import Post
# Create your views here.


def post_list(request):

        if request.method == "POST":
            form = MyForm(request.POST)

            if form.is_valid():

                x = form.cleaned_data['part_number']
                d2 = form.cleaned_data['today_dollar']
                x = Post.objects.get(partnumber=x)
                p2 = ((int(d2)) * int((x.past_price)))/int((x.past_dollar))

            #x = Post.objects.get(partnumber= request.POST.part_number)
            #print(x)
            context = {'p2': int(p2) , 'x': x , 'd2': d2 }

            return render(request , 'blog/post_result.html' , context )
            #return HttpResponse("gheymat jadid {} nesbat be dollar {} , kasani ke daran: {} ".format(int(p2) , x.past_dollar , x.body))   

        if request.method == "GET":
            
            form = MyForm()

            context = {'form': form }
            return render(request, 'blog/post_list.html', context)



    