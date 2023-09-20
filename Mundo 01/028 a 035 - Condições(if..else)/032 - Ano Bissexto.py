import calendar
import datetime

ano = int(input('Digite o ano: '))

if ano == 0:
    ano = datetime.date.today().year
if calendar.isleap(ano):
    print("O ano {} é bissexto".format(ano))
else:
    print("O ano {} não é bissexto".format(ano))

    
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#    print("O ano {} é BISSEXTO".format(ano))
#else:
#    print("O ano {} NÃO é BISSEXTO".format(ano))