from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    item_list=Item.objects.all()
    paginator = Paginator(item_list,6)
    page = request.GET.get('page')
    item_list = paginator.get_page(page)
    context = {
        'item_list':item_list,
    }
    return render(request,'food/index.html',context)

#Class View
class IndexClassView(ListView):
    model = Item;
    template_name = 'food/index.html'
    context_object_name='item_list'

def item(request):
    return HttpResponse("Item View")



def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request,'food/detail.html',context)
#Class View
class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'


@login_required
def create_item(request):
    form = ItemForm(request.POST or None )

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request,'food/item-form.html',{'form':form})
#Class view
class CreateItem(CreateView):
    model = Item;
    fields = ['item_name','item_desc','item_price','item_image']
    template_name='food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)



def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request,'food/item-form.html',{'form':form,'item':item})



def delete_item(request,id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('index')

    return render(request,'food/item-delete.html',{'item':item})
