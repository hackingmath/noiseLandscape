'''Landscape using Perlin noise
works!'''

def setup():
    size(600,600,P3D)
    
def draw():
    background(0)
    landscape()

z = 0.0
def landscape():
    land = [] #matrix of point for landscape
    #add empty rows:
    for i in range(1000):
        land.append([])
    w = 10
    h = 10
    translate(-700,500,300)
    rotateX(-2.0)
    elevation = 500
    ampl = 10
    for i in range(200):
        for j in range(200):
            land[i].append(noise(float(i)/ampl, float(j)/ampl, z)*elevation)
    for x in range(199):
        for y in range(199):
            #translate(-50,-50)
            beginShape(QUADS)
            elevation = land[x][y]
            if elevation <150:
                fill(255) #make the mountaintops white
            else:
                fill(0,255-elevation/2.0,0)
            #strokeWeight(0.5)
            #stroke(0)
            noStroke()
            vertex(x*w,y*h,land[x][y])
            vertex((x+1)*w,y*h,land[x+1][y])
            vertex((x+1)*w,(y+1)*h,land[x+1][y+1])
            vertex(x*w,(y+1)*h,land[x][y+1]) 
            endShape()    