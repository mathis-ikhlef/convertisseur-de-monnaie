from forex_python.converter import CurrencyRates
c = CurrencyRates(force_decimal=True)
devise_source = input("Quel devise souhaitez-vous convertir ?")
montant = input("Montant à convertir ?")
devise_dest =input("En quel devise ?")

result = ''
try:
    result = c.convert(devise_source, devise_dest, int(montant))
except(ValueError,IndexError):
    print("La conversion n'est pas possible.")
    exit()

print(result)
with open ('convertisseurdemonnaie' ,'a') as file :
    file.write(str(result) + '\n')