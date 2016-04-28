presu= int(input("coloque el monto a repartir ente las areas del hospital:"))
odon=int(input("coloque el porsentaje del pesupuesto que le tocara a odontologia:"))
pors1=(presu*odon)/100
print("el monto que le tocara a odontolgia sera de:",pors1)
trau=int(input("coloque el porsentaje del presupuesto que le tocara a traumatologia:"))
pors2=(presu*trau)/100
print("el monto que le tocara a traumatologia sera de:",pors2)
pedi=int(input("coloque el porsentaje del presupuesto que le tocara a pediatria:"))
pors3=(presu*pedi)/100
print("el monto que le tocara a pediatria sera de:",pors3)
