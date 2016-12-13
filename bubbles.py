
from picture import *
""" Thia program recursively draws bubbles on a size by size canvas, given a depth d."""
def circle(pic,x,y,r):
  """ First, the thickness of the circles is set to zero. The circle fill-in color is set to blue.
  This function draws a circle with a given radius r, and center points (x,y)"""
  
    pic.setPenWidth(0)
    pic.setFillColor(0,0,255)
    pic.drawCircleFill(x,y,r)
    pic.display()
    
   
def bubbles(pic,x,y,d,r):
  """if the depth is less than 1, do nothing.
  Otherwise, draw the bubbles recursively, with depths always decreasing by 1."""
  
    if d > 1:
        bubbles(pic,x-r,y-r,d-1,r/2)
       
        bubbles(pic,x-r,y+r,d-1,r/2)
        
        bubbles(pic,x+r,y-r,d-1,r/2)
        
        bubbles(pic,x+r,y+r,d-1,r/2)
        circle(pic,x,y,r)
    else:
        return circle(pic,x,y,r)
        
def main():

    print("Welcome to my Bubble Fractal Image.")
    size = eval(input("Enter the size of the canvas: "))
    d = eval(input("Enter the depth: "))
    r = size//4
    x = size//2
    y = size//2
    
    bubbles(pic, x,y,d,r)
 
main()
 
