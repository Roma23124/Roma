a=350
b=400
g=0
napr="niz"
def setup():
    size(1000,1000)
    frameRate(60)
    rectMode(CENTER)
def draw():
    global a,b,g
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
 
