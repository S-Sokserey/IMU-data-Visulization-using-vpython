from vpython import *
from time import *
import numpy as np
import math
import serial 
ad = serial.Serial('com6',115200)
sleep(1)



scene.range=5
toRad = 2*np.pi/360
toDeg = 1/toRad
scene.forward=vector(-1,-1,-1)

scene.width=600
scene.height=600

xarrow=arrow(length=4, shaftwidth=.15, color=color.red,axis=vector(1,0,0),pos=vector(0,1,0))
yarrow=arrow(length=4, shaftwidth=.15, color=color.blue,axis=vector(0,1,0),pos=vector(0,1,0))
zarrow=arrow(length=4, shaftwidth=.15, color=color.green,axis=vector(0,0,1),pos=vector(0,1,0))

frontArrow=arrow(length=7,shaftwidth=.1,color=color.purple,axis=vector(1,0,0),pos=vector(0,1,0))
upArrow=arrow(length=7,shaftwidth=.1,color=color.magenta,axis=vector(0,1,0),pos=vector(0,1,0))
sideArrow=arrow(length=7,shaftwidth=.1,color=color.orange,axis=vector(0,0,1),pos=vector(0,1,0))

support = cylinder(length=6,radius=1.4,height=5,color=color.white,axis=vector(0,1,0),pos=vector(0,-6,0))
lsupport = box(length=6,width=6,height=.1,pos=vector(0,-6,0))
square = sphere(radius=1,color=color.blue)
lsupport = box(length=4,width=4,height=.2,pos=vector(0,1,0))
myObj = compound([square,lsupport])

while (True):
    while (ad.inWaiting()==0):
        pass
    dataPacket=ad.readline()
    dataPacket=str(dataPacket,'utf-8')
    splitPacket=dataPacket.split(",")
    roll=float(splitPacket[1])*(-toRad)
    pitch=float(splitPacket[0])*(toRad)
    yaw=float(splitPacket[2])*toRad+np.pi
    #print("Roll=",roll*toDeg," Pitch=",pitch*toDeg,"Yaw=",yaw*toDeg)
    rate(50)
    k=vector(cos(yaw)*cos(pitch), sin(pitch),sin(yaw)*cos(pitch))
    y=vector(0,1,0)
    s=cross(k,y)
    v=cross(s,k)
    vrot=v*cos(roll)+cross(k,v)*sin(roll)
 
    frontArrow.axis=k
    sideArrow.axis=cross(k,vrot)
    upArrow.axis=vrot
    myObj.axis=k
    myObj.up=vrot
    sideArrow.length=6
    frontArrow.length=6
    upArrow.length=6
        
