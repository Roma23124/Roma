a=500
b=500
napr="niz"
def setup():
    size(1000,1000)
    frameRate(60)
def draw():
    global napr,a,b
    clear()
    ellipse(b,a,200,200)
    rect(400,400,100,100)
    rect(800,400,100,100)
    rect(600,600,100,100)
    rect(600,200,100,100)
    if napr == "a":
        b-=1
    if napr == "s":
        b+=1
    if napr =="w":
        a+=1
    if napr =="d":
        a-=1
def mouseClicked():
    global napr,a,b
    if mouseX > 400 and mouseX <500 and mouseY >400 and mouseY <500:
        napr="a"
    if mouseX > 800 and mouseX <900 and mouseY >400 and mouseY <500:
        napr="s"
    if mouseX > 600 and mouseX <700 and mouseY >600 and mouseY <700:
        napr="w"
    if mouseX > 600 and mouseX <700 and mouseY >200 and mouseY <300:
        napr="d"  

    

    
    
        
    
    
