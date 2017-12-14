import turtle


def polygon(t, length, n):
	#t=turtle.Turtle()
	for i in range(n):
		t.fd(length)
		t.lt(360/n)
	turtle.mainloop()
	
def circle(t, r):
	n = 200
	lenth = 2*math.pi*r/n
	polygon(t, lenth, n)
    
def polygon_arc(t, length, n, angle):
	#t=turtle.Turtle()
    n1 = round((angle/360)*n)
    for i in range(n1):
        t.fd(length)
        t.lt(360/n)
    turtle.mainloop()
    
def arc(t, r, angle):
    n = 200
    lenth = 2*3.1415927*r/n
    polygon_arc(t, lenth, n, angle)
	
bob = turtle.Turtle()
#polygon(bob, 50, 15)
#circle(bob, 40)
arc(bob, 40, 270)

