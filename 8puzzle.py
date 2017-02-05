import random

list=[]
attained=[]
level=0
def main(lists):
    global list
    list=lists
    print lists
    
    while (True):
	    for j in range(3):
		          for k in range(3):
		                if (list[j][k]==""):
		                    
		                    shift(j,k)
		                    if (check()):
   		 		        return	
		                    print list
		                   
                            

def shift(row,col):
	   global list
	   choice=random.randrange(0,5,1)
	   #print choice
	   if (choice==0):
   
		    if (col>0):
			swap(row,col,row,col-1)
			
			check()
		   
	   
           if (choice==1):
		    if (row>0):
			swap(row,col,row-1,col)
			
			check()
		   
	    
           if (choice==2):
		    if (row<2):
			swap(row,col,row+1,col)
			
			check()
		   
	   
           else:
		    if (col<2):
			swap(row,col,row,col+1)
			
			check()
		    
        

def check():
    if (list==[[1,2,3],[4,5,6],[7,8,""]]):
                print(list)
                print("sakyo")    
                return True          


def swap(row,col,newrow,newcol):
    global list
    list[row][col],list[newrow][newcol]=list[newrow][newcol],list[row][col]
  

main([random.sample(range(1, 4), 3),random.sample(range(4, 7), 3),[7,"",8]])

