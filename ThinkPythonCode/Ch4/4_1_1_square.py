import turtle


def polygon(t, length, n):
	#t=turtle.Turtle()
	for i in range(n):
		t.fd(length)
		t.lt(360/n)
	turtle.mainloop()
	
def circle(t, r):
	n = 200
	lenth = 2*3.1415927*r/n
	polygon(t, lenth, n)
	
bob = turtle.Turtle()
#polygon(bob, 50, 15)
circle(bob, 40)

