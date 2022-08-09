dia = float(input("dia do seu nascimanto: "))
mes = str(input("qual seu mes de nascimento: "))
ano = float(input("qual seu ano de nascimento: "))

if mes == "1" or mes == "01":
    mesreal = "janero"
    print("{:.0f}/{}/{:.0f}".format(dia,mesreal,ano))
elif mes == "2" or mes == "02":
    mesreal = "fevereiro"
    print("{:.0f}/{}/{:.0f}".format(dia,mesreal,ano))
elif mes == "3" or mes == "03":
    mesreal = "março"
    print("{:.0f}/{}/{:.0f}".format(dia,mesreal,ano))
elif mes == "4" or mes == "04":
    mesreal = "abril"
    print("{:.0f}/{}/{:.0f}".format(dia,mesreal,ano))
elif mes == "5" or mes == "05":
    mesreal = "maio"
    print("{:.0f}/{}/{:.0f}".format(dia,mesreal,ano))
elif mes == "6" or mes == "06":
    mesreal = "junho"
    print("{:.0f}/{}/{:.0f}".format(dia,mesreal,ano))
elif mes == "7" or mes == "07":
    mesreal = "julho"
    print("{:.0f}/{}/{:.0f}".format(dia,mesreal,ano))
elif mes == "8" or mes == "08":
    mesreal = "agosto"
    print("{:.0f}/{}/{:.0f}".format(dia,mesreal,ano))
elif mes == "9" or mes == "09":
    mesreal = "setembro"
    print("{:.0f}/{}/{:.0f}".format(dia,mesreal,ano))
elif mes == "10":
    mesreal = "outubro"
    print("{:.0f}/{}/{:.0f}".format(dia,mesreal,ano))
elif mes == "11":
    mesreal = "novembro"
    print("{:.0f}/{}/{:.0f}".format(dia,mesreal,ano))
elif mes == "12":
    mesreal = "dezembro"
    print("{:.0f}/{}/{:.0f}".format(dia,mesreal,ano))
else:
    print("{:.0f}/{}/{:.0f}".format(dia,mes,ano))

