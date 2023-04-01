a=200
x=200
g=900


def setup():
    size(1000,1000)
    frameRate(3)
def draw():
    y=1900

    
    
    while y!=0:
      
       ellipse(500,500,y,y)
       y-=0.5
def mouseClicked():
     stroke(random(255),random(255),random(255))
       
       
    

        
