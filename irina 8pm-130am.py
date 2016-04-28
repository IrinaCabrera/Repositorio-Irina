
def suma(x,y):
	suma=x+y
	print "la suma es",suma
			
	
def resta(x,y):
	resta=x-y
	print "la resta es",resta
			
	
def mult(x,y):
	mult=x*y
	print "la multiplicacion es",mult
    		
	
def div(x,y):
	div=x/y
	print "la division es",div
			
control=1
while (control==1):
	x= float(input("coloque el primer numero:"))
	y= float(input("coloque el segundo numero:"))
	opcion=int(input("coloque la operacion que desea realizar:" 
    "\n""1) suma" 
    "\n""2) resta"
    "\n""3) multiplicacion"
    "\n""4) division"))
	if (opcion==1):
		suma (x,y)
	if (opcion==2):
		resta (x,y)
	if (opcion==3):
		mult (x,y)
	if (opcion==4):
		div (x,y)
	control=int(input("desea seguir operando?"
	"\n""1)si""\n""2)no"))
else: 
	print "adios mundo cruel"
