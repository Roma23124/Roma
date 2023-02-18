bg=0
a=0
b=0
def setup():
    size(1000,1000)
def draw():
    global a,b
    push()
    fill(b)
    rect(mouseX,mouseY,pmouseX,pmouseY)
    pop()
    rect(400,150,100,50)
    rect(600,150,100,50)
def mouseClicked():
    global bg,a,b
    if mouseX > 400 and mouseX <500 and mouseY >150 and mouseY < 200:
       a=a+1
    if mouseX > 600 and mouseX <700 and mouseY >150 and mouseY < 200:
       clear()
