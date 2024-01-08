print ('Минимальная сумма инвестиций:')
MIA = int (input () )
print ('Сколько внёс Майкл:')
Michael = int (input () )
print ('Сколько внёс Иван:')
Ivan = int (input () )
if (Michael >= MIA) and (Ivan >= MIA):
    print (2)
elif (Michael >= MIA) or (Ivan >= MIA):
    if Michael >= MIA:
        print ('Mike')
    else:
        print ('Ivan')
elif Michael + Ivan >= MIA:
    print (1)
else:
    print (0)