presu= int(input("coloque el monto a repartir ente las areas del hospital:"))
odon=40
trau=30
pedi=30
pors1=(presu*odon)/100
pors2=(presu*trau)/100
pors3=(presu*pedi)/100
print("el monto que les tocara a cada area sera de: odontologia %i,traumatologia %i, pediatria %i")%(pors1,pors2,pors3)