from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import models
from .models import stockItem,transaction
from datetime import date
 
message = ""
message1 = ""
# Create your views here.

def stockEntryPage(request):
   
    if request.method=="POST" and 'createStockBtn' in request.POST:

        stockCode = request.POST.get('stockCode')
        stockName = request.POST.get('stockItem')
        balance = 10
        stock = stockItem(stockCode=stockCode,stockItem=stockName,currentBalance=0)
        stock.save()
        message="Stock saved !"
        message1=""

    elif request.method=="POST" and 'saveTransactionBtn' in request.POST:

        message = ""
        id = request.POST.get('stockName')
        qty=1
        ops = ""
        date1 = date.today()

        try:
            qty = (int) (request.POST.get('qty'))
            date1 = request.POST.get('date')
            ops = request.POST.get('ops')
            stock = stockItem.objects.get(stockCode=id)
        
        except:
            message1 = "Nothing to save !"
                   
        if(ops=="Receipt"):
            rate =(int) (request.POST.get('rate'))
            amount = rate * qty

                                 
            try:
                stock = stockItem.objects.get(stockCode=id)
                stockBalance = stock.currentBalance +qty
                stock.currentBalance = stockBalance
                stock.save()
                trans = transaction(stockID=id,transDate=date1,quantity=qty,rate = rate,amount=amount,ops=ops,stockBalanceAsOnDate=qty)
                trans.save()
                message1 = "Stock Receipt noted successfully!"
            except:
                message1 = "Please enter all fields correctly !"

        elif(ops=="Issue"):

            stock = stockItem.objects.get(stockCode=id)
            if(stock.currentBalance<qty):
                message1 = "Current stock level is less than the ordered quantity !"
            
            else:
                transactions = transaction.objects.all().filter(stockID=id).exclude(ops="Issue" , stockBalanceAsOnDate=0 )
                transactions = transactions.order_by('transDate')
                i = 0
                while(qty>0):

                    if(transactions[i].stockBalanceAsOnDate>=qty):
                        stock = stockItem.objects.get(stockCode=id)
                        stockBalance = stock.currentBalance - qty
                        stock.currentBalance = stockBalance
                        stock.save()
                        rate = transactions[i].rate
                        amount = transactions[i].rate * qty
                        stockBalanceAsOnDate = transactions[i].stockBalanceAsOnDate - qty
                        trans = transaction(stockID=id,transDate=date1,quantity=qty,rate = rate,amount=amount,ops=ops,stockBalanceAsOnDate=stockBalanceAsOnDate)
                        trans.save()
                        message1 = "Stock issued successfully !"
                        break
                    
                    elif(transactions[i].stockBalanceAsOnDate>0):
                        stock = stockItem.objects.get(stockCode=id)
                        stockBalance = stock.currentBalance - transactions[i].stockBalanceAsOnDate
                        stock.currentBalance = stockBalance
                        stock.save()
                        rate = transactions[i].rate
                        amount = transactions[i].rate * transactions[i].stockBalanceAsOnDate
                        trans = transaction(stockID=id,transDate=date1,quantity=transactions[i].stockBalanceAsOnDate,rate = rate,amount=amount,ops=ops,stockBalanceAsOnDate=0)
                        trans.save()
  
                    qty = qty - transactions[i].stockBalanceAsOnDate        
                    i = i + 1
                    
        
    else:
         message=""
         message1=""

    
    stocks = stockItem.objects.all
    return render(request,'erpApp/index.html',{'stocks':stocks,'message':message,'message1':message1})

def showReport(request):
    trans = []

    stocks = stockItem.objects.all()

    for stock in stocks:
        transAct = transaction.objects.all().order_by('transDate')
        trans.append(transAct)

    return render(request,'erpApp/report.html',{'stocks':stocks,'trans':transAct})