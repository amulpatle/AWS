from django.shortcuts import render
from dal import autocomplete
from .models import Stock
from .forms import StockForm
from .utils import scrape_stock_data
# Create your views here.

def stocks(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock_id = request.POST.get('stock')
            # fetch the stock and symbol
            stock = Stock.objects.get(pk=stock_id)
            symbol = stock.Symbol
            
            exchange = stock.Exchange
            stock_response = scrape_stock_data(symbol,exchange)
            print('stock ================>>>>>>>>>',stock_response)
            
        else:
            print('Form is not valid')
    else:
        form = StockForm()
        context = {
            'form':form,
        }
        return render(request,'stockanalysis/stocks.html',context)


class StockAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Stock.objects.all()
        
        if self.q:
            print('entered keyword=>', self.q)
            qs = qs.filter(Name__istartswith=self.q)
            print('result==>', qs)

        return qs