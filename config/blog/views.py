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
                x = Post.objects.filter(partnumber=x).values()
                for i in x:
                    i['newprice'] = (int(d2) * int(i['past_price']))/int(i['past_dollar'])
                    int(i['past_price']) + 1000
       
            context = {'x': x}
            return render(request , 'blog/post_result.html' , context )

        if request.method == "GET":
            
            form = MyForm()
            context = {'form': form }
            return render(request, 'blog/post_list.html', context)



    