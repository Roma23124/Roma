elY=0
elX=500
napr="left"
def setup():
    size(1000,1000)
def draw():
    
    global elX,elY,napr
    ellipse(elX,elY,50,50)
    
    

    
    elY+=1
    if napr=="left":
        elX-=1
    if napr=="right":
        elX+=1
    if elY> 600:
        elY=0
    if elX==50:
        napr="right"
    if elX==550:
        napr="left"
    #if elX<x and elX>x+150 and     
    
    
    
       
                         
                  
                     
                        
                           
                              
                                 
                                    
                                       
                                          
                                                
