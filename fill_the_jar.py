import random

def  main():
   
    global a,b,c
    a=input("Enter the values for a i.e the capacity of first jar")
    b=input("Enter value for b i.e the capacity of second jar")
    c=input("Enter k, i.e the amount of water you wish to acheive")
    dict=[[0,0],]
    print dict[0][0]
    if (is_possible(a,b,c)):
        print ("Possible")
        tempa,tempb=0,0
        while True:
			
		
			choice=random.randrange(0,5,1)
			 
			if (choice==0):
				tempa,tempb=fillA(tempa,tempb)
			elif (choice==1):
				tempa,tempb=fillB(tempa,tempb)
			elif (choice==2):
				tempa,tempb=emptyA(tempa,tempb)
			elif (choice==3):
				tempa,tempb=emptyB(tempa,tempb)
			elif (choice==4):
				tempa,tempb=transfer_from_A(tempa,tempb)	
			else:
				tempa,tempb=transfer_from_B(tempa,tempb)			
			
			if [tempa,tempb] not in dict:
				print tempa,tempb
				dict.append([tempa,tempb])
         			if check(tempa,tempb) :
         				
         				return
         		
         		
         		 
         		
         			
         		
    else:
        print ("Not possible")
        return

def check(first,second):
	if (first==c or second==c or first+second==c):
		return True;
	return False;

def is_possible(a1,b1,c1):
	if (c1 % gcd(a1,b1)==0):
		return True
	return False
	
def gcd(a1,b1):
	if (a1%b1==0):
		return b1
	return gcd(b1,a1%b1)    


def emptyA(a1,b1):
	a1=0
	return a1,b1



def emptyB(a1,b1):
	b1=0
	return a1,b1



def transfer_from_A(tempA,tempB):
	
	transferrable=b-tempB
	if (transferrable>tempA):
		transferrable=tempA
	
	if (check_underflow(tempA-transferrable,tempB+transferrable) and check_overflow(tempA-transferrable,tempB+transferrable)):
		return tempA-transferrable,tempB+transferrable
	
	return tempA,tempB
	
def check_underflow(first,second):
	 
	if (first>=0 and second>=0):
		return True
	
	return False
def check_overflow(first,second):
	 
	if (first<=a and second<=b):
		return True
	
	return False


def transfer_from_B(tempA,tempB):
	 
	transferrable=a-tempA
	if (transferrable>tempB):
		transferrable=tempB
	
	if check_underflow(tempA+transferrable,tempB-transferrable) and check_overflow(tempA+transferrable,tempB-transferrable):
		
		return tempA+transferrable,tempB-transferrable
	 
	return tempA,tempB


def fillA(tempA,tempB):
	fillable=a-tempA
	if check_overflow(tempA+fillable,tempB):
		return tempA+fillable,tempB
	return tempA,tempB


def fillB(tempA,tempB):
	
	fillable=b-tempB
	if check_overflow(tempA,tempB+fillable):
		return tempA,tempB+fillable
	return tempA,tempB


a=b=c=0	
main()
    
