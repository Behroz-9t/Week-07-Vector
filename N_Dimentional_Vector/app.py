from N_dimentional_vector import Vector 

class App:
    def run(self):
        
        V1=Vector(3,4,5) #--> instantiation and creating objects.
        V2=Vector(3,4,1)

        V=V1+V2 #--> adding V1 and V2 in V as result
        print("Addition of V1 and V2:" ,V)

        print("Are V1 and V2 equal:" ,V1==V2) #--> Checking if V1 and V2 are equal (false)

        R=V1@V2 #--> Dot product calculation and using @ as it is built-in sign for dot product.
        print("Dot product of V1 and V2:" ,R)

        S=V1.cross(V2) #--> Cross product calculation
        print("Cross product of V1 and V2:" ,S)

        V3=V2.clone() #--> cloning V2 as V3  
        print("Cloned V2 as V3: ",V3)

        V3[2]=9 #--> changed V3 3rd value 
        print("Value of V3",V3) 
        print("Original V2",V2)