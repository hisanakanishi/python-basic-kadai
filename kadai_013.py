def total_cult(amount,tax):
    rate = int(tax.strip('%'))
    total = amount + (amount*rate/100)
    
    print(total)
    
    

total_cult(2000,"10%")