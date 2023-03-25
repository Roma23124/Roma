a=100
y=100
g=100
f=500
def setup():
    size(1000,1000)
    frameRate(10)
def draw():
    global a,y,g,f
    fill(random(255),random(255),random(255))
    strokeWeight(random(255))
    for i in range(10):
        ellipse(500,f,y,y)
        y=y-1
    for i in range(10):
        ellipse(200,f,a,a)
        a=a-1
    for i in range(10):
        ellipse(800,f,g,g)
        g=g-1
    if keyPressed:
        if key == "k":
           f=f+10 
        
       
       
    

        
