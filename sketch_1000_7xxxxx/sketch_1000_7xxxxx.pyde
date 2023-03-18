a=500
b=500
g=500
d=600
f=400
h=500
r=475
y=350
napr="niz"
def setup():
    size(1000,1000)
    frameRate(60)
def draw():
    global a,b,g,d,r,y,f,h
    clear()
    ellipse(b,a,200,200)
    ellipse(d,g,100,300)
    ellipse(f,h,100,300)
    rect(r,y,50,300)
    if keyPressed:
        if key == "s":
           a+=1
    if keyPressed:
        if key == "w":
           a-=1      
    if keyPressed:
        if key == "d":
           b+=1
    if keyPressed:
        if key == "a":
           b-=1 
           #             
        if key == "s":
           g+=1
    if keyPressed:
        if key == "w":
           g-=1      
    if keyPressed:
        if key == "d":
           d+=1
    if keyPressed:
        if key == "a":
           d-=1            
    

    
    
        
    
    
