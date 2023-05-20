a=350
b=400
g=0
napr="niz"
h=0
k=0
g=0
y=100
n=100
def setup():
    size(1000,1000)
    frameRate(60)
    rectMode(CENTER)
def draw():
    global a,b,g,h,k,y,n
    clear()
    push()
    translate(a,b)
    rotate(radians(g))
    fill(50,255,0)
    rect(0,0,100,150)
    fill(96,96,96)
    ellipse(-50,0,50,150)
    ellipse(50,0,50,150)
    fill(0,153,0)
    rect(0,-70,25,150)
    rect(0,h,25,50)
    if k==1:
        h=h-20
    pop()
    push()
    text(y,200,200)
    ellipse(430,800,n,n)
    
    y=y-0.1
    if y<=0:
        n=0
        ellipse(300,300,100,100)
        y=100
      
    pop()
    
    if keyPressed:
        if key == "d":
           a+=1
        if key == "a":
           a-=1     
        if key == "s":
           b+=1
        if key == "w":
           b-=1 
        if key == "q":
           g=g+1
        if key == "e":
           g=g-1   
        if key == "r":
           h=0 
           k=0    
                 
def mouseClicked(): 
    global g,b,a,h,k
    k=1
       
