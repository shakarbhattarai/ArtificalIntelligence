import pydot
graph = pydot.Dot(graph_type='graph')
class Problem:
        """
   The program is capable of solving missionary cannibals problem for not just 3/3 but any valid number beyond that.
   
   The program uses pydot for plotting the tree. Please install pydot from the site: https://pypi.python.org/pypi/pydot below.

   All the states that have already been acheived are not displayed in the tree, making it more efficeient.
   
   The state [3,3,0] represents 3 missionaries, 3 cannibals, and 0 represents the position of the boat. 0 for the left and 1 for the right        
   
        """
        def __init__(self,a,b):
               
               
                self.goalstate=[0,0,1]
                self.possible=[ [1,1],[0,1],[1,0],[0,2],[2,0]]
                self.a=a
                self.b=b
                self.attained=[]
                
        def performaction(self,state):
                children=[]
                
                self.attained.append(state) # Append all the states that have already been attained so that a loop is not formed.
                    
                init=state
                init_number=state[2]
                for action in self.possible:
                      
                       
                        if init_number==0:   # The boat is on the left side, so substract the action values from the state the system is in. Also change the boat to 1.
                                number=1
                                
                                temp=[x-y for x,y in zip(init[:2], action)]
                                
                                temp.append(number)     
                                
                        else:
                                number=0
                                temp=[x+y for x,y in zip(init[:2], action)] # Since the boat is on the right side, some M/C are added to the state on the left. Act accordingly.
                                
                                temp.append(number)
                        
                        right_miss=self.a-temp[0]
                        right_can=self.b-temp[1]
                       
                        if (temp[1]<=temp[0] or temp[0]==0) and (temp[0]<=self.a and temp[0]>=0 and temp[1]<=self.b and temp[1]>=0 and (right_can<=right_miss or right_miss==0) and temp not in self.attained):
                                print temp       
                                state=temp
                              
                                
                                children.append(state)
                                
                                
                                  
                print init,children  
                print "***************************","\n"
                
                for child in children:
                         edge = pydot.Edge(''.join(str(e) for e in init), ''.join(str(e) for e in child)) #Perform a DFS by looking for all the possible states of each child.
                         graph.add_edge(edge)
                
                         if child==self.goalstate:
                                        print "terminated"
                                        return
                         self.performaction(child)      
                    
def main():
	
        a=input ("Enter the number of missionaries")
        b= input ("Enter hte number of cannibals")
        
        if (a<b):
                print ("The number of missionaries can't be less than the cannibals")
        else:
                pr=Problem(a,b)
                pr.performaction([a,b,0]) #[3,3,0] represents the initial state
                graph.write_png('example1_graph.png')
	
main()
                   
                
                     
                        
                       
                
                
                
                
                
                         
                        
