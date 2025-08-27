class Vector:
     
 #Represention of vector in multidimensional space.
 
    def __init__ (self,*n): #--> Here *n takes the input as tuple()
    
        self.coords=list(n) #--> The coords stores the n in the form of list.
        
            

    def __len__ (self): #--> this dunder function returns the length of the vector
        return len(self.coords)
   
    
    def __getitem__ (self, i): #--> this function (gets) every item in respected index of the tuple
  
        return self.coords[i]
    
    def __setitem__ (self, i,val): #--> this function (sets) every item on the respected index of the tuple

        self.coords[i]=val

    def __add__ (self,other): #--> this function adds the two vectors. Operator overloading for "+"

        if len(self) != len(other): #--> checks if the two adding vectors are of same length
            raise ValueError("The dimensions of both vectors must be equal!")
        
        result=Vector(*([0]*len(self))) #--> initializes result with Vector instantiation. Here if the vector is intantiated in app and not given co ordinates then they are initally 0. first "*" sign is for the answer in every respected index of the tuple such as [0],[1],... and second "*" sign is for multiplication with the length of the vector

        for i in range(len(self)): #--> loop running from 0 to length of vector - 1
            result[i]=self[i]+other[i] #--> adds number present at ith index of self and other and stores it in ith index of result.
        return result


    def __eq__ (self,other): #--> For checking the equality of the vector.(Dunder method /function)

        return self.coords==other.coords
    

    def __str__ (self): #--> for string reresentation of the vector when object is called
    
        return f"Vector {self.coords} and size is {len(self)}" 


    def __matmul__(self, other):  #--> Dunder function for dot product
        
        if len(self) != len(other): #--> again check length or dimensions of the vector
            raise ValueError("The dimensions of both vectors must be equal!")
        
        results=0 #--> initialized result as 0
        for i in range(len(self)):
            results +=(self[i] * other[i]) #--> summition of multiplication of ith index's number of self and other .
        return results
    
    def cross(self, other):  #-->  Cross product function
        
        if len(self) and len(other) !=3: #--> As the primary cross product happens between 3x3 vector
            raise ValueError("Order incorrect!") 
        i = self[1] * other[2] - self[2] * other[1] 

        j = self[2] * other[0] - self[0] * other[2]

        k = self[0] * other[1] - self[1] * other[0]

        return Vector(i, j, k)
    

    def clone(self): #--> for cloning of the vector .It creates the deep copy.
        return Vector(*self) #--> Here "*" sign is again returningevery number on different or every index. Its abscence will cause the answer or coords to be stored in first index only and the rest will be empty such as: [(1,3,2),0,0]--> here 1,3,2 are stored in 0th idex. 
            









