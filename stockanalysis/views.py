from django.shortcuts import render,redirect
from dal import autocomplete
from .models import Stock
from .forms import StockForm
from .utils import scrape_stock_data
from django.contrib import messages
# Create your views here.

def stocks(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock_id = request.POST.get('stock')
            # fetch the stock and symbol
            stock = Stock.objects.get(pk=stock_id)
            symbol = stock.Symbol
            print("symbol ================>>>>>>>>>>>>>>>>",symbol)
            exchange = stock.Exchange
            print("exchange ================>>>>>>>>>>>>>>>>",exchange)
            stock_response = scrape_stock_data(symbol,exchange)
            print('stock ================>>>>>>>>>',stock_response)
            if stock_response:
                return redirect('stock')
            else:
                messages.error(request,f'Could not fetch the data for:{symbol}')
                return redirect('stocks')
            
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