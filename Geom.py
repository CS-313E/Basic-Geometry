#  File: Geom.py

#  Description: Describe varying aspects of a point and line (i.e slope, intercepts, and intersections)

#  Student Name: Jadesola Jaiyesimi

#  Student UT EID: jaj3847  

#  Course Name: CS 313E

#  Unique Number: 50295

#  Date Created: February 10th, 2020

#  Date Last Modified: February 14th, 2020

import math

class Point (object):
  # constructor with default values
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y

  # get distance to other which is another Point object
    def dist (self, other):
        return math.hypot (self.x - other.x, self.y - other.y)

  # create a string representation of a Point (x, y)
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # test for equality between two points
    def __eq__ (self, other):
        tol = 1.0e-6
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Line (object):
  # line is defined by two Point objects p1 and p2
  # constructor assign default values if user does not define
  # the coordinates of p1 and p2 or the two points are the same
    def __init__ (self, p1_x = 0, p1_y = 0, p2_x = 1, p2_y = 1):
        self.p1_x = p1_x
        self.p1_y = p1_y
        self.p2_x = p2_x
        self.p2_y = p2_y
        if (self.p1_x == self.p2_x) and (self.p1_y == self.p2_y):
            self.p1 = Point(0,0)
            self.p2 = Point(1,1)
        else:
            self.p1 = Point(p1_x,p1_y)
            self.p2 = Point(p2_x,p2_y)

  # returns True if the line is parallel to the x axis 
  # and False otherwise
    def is_parallel_x (self):
        return (self.p1_y == self.p2_y)

  # returns True if the line is parallel to the y axis
  # and False otherwise
    def is_parallel_y (self):
        return (self.p1_x == self.p2_x)

  # determine slope for the line
  # return float ('inf') if line is parallel to the y-axis
    def slope (self):
        if self.is_parallel_y:
            return float('inf')
        else:
            return (self.p1_y - self.p2_y) / (self.p1_x - self.p2_x)

  # determine the y-intercept of the line
  # return None if line is parallel to the y axis
    def y_intercept (self):
        y_int = -1*((self.p1_x * self.slope()) - self.p1_y) #solve for b in y = mx+b
        return y_int

  # determine the x-intercept of the line
  # return None if line is parallel to the x axis
    def x_intercept (self):
        x_int = -(self.p1_y) / self.slope() #make y = 0 and solve for x
        return x_int

  # returns True if line is parallel to other and False otherwise
    def is_parallel (self, other):
        return(self.slope() == other.slope())

  # returns True if line is perpendicular to other and False otherwise
    def is_perpendicular (self, other):
        return(self.slope() * other.slope() == -1 )

  # returns True if Point p is on the line or an extension of it
  # and False otherwise
    def is_on_line (self, p):
        return (self.slope() * (p2_x) + self.y_intercept() == (p.p1_y))
  
  # determine the perpendicular distance of Point p to the line
  # return 0 if p is on the line
    def perp_dist (self, p):
        dist = abs((p.y + (self.slope() * p.x)+ self.y_intercept() ) / math.sqrt(self.slope() **2 +self.y_intercept() **2)
        #Perpendicular Distance from a Point to a Line equation
        return dist

  # returns a Point object which is the intersection point of line
  # and other or None if they are parallel
    def intersection_point (self, other):
        if (other.slope() - self.slope()) == 0:
            return None
        else:
            #Cramers Rule for Intersection
            y = (self.y_intercept() * other.slope()) - (other.y_intercept() * self.slope())/(other.slope() - self.slope())
            x = (self.y_intercept() - other.y_intercept()) / (other.slope() - self.slope())
            return x,y

  # return True if two points are on the same side of the line
  # and neither points are on the line
  # return False if one or both points are on the line 
    def on_same_side (self, p1, p2):
        x = p1.y - (self.slope() * p1.x)
        y = p2.y - (self.slope() * p2.x)
        return ((x > self.y_intercept() and (y > self.y_intercept())) or ((x < self.y_intercept()) and (y < self.y_intercept())))
      
  # string representation of the line - one of three cases
  # y = c if parallel to the x axis
  # x = c if parallel to the y axis
  # y = m * x + b
    def __str__ (self):
        return('y = '+ str(self.slope()) + ' * x + ' +str(self.y_intercept()))
        if self.y_intercept() > 0:
            str_intercept = '+ ' + str(int(self.y_intercept()))
        else:
            str_intercept = str(int(self.y_intercept()))
        if self.slope() == 1:
            str_slope = ''
        else:
            str_slope = str(int(self.slope()))
      
        if self.is_parallel_x():
            return 'y = ' + str_intercept
        elif self.is_parallel_y():
            return 'x = '+ str_intercept
        else:
            return 'y = ' + str_slope + 'x ' + str_intercept

def main():
    infile = open('geom.txt', 'r')    # open file "geom.txt" for reading
    line = infile.readline()    # read the coordinates of the first Point P
    line_split_P = line.split()
    pointp_x = float(line_split_P[0])
    pointp_y = float(line_split_P[1])

    point_q = infile.readline()    # read the coordinates of the second Point Q
    line_split_Q = point_q.split()
    pointq_x = float(line_split_Q[0])
    pointq_y = float(line_split_Q[1])

    print()
    p = Point(pointp_x,pointp_y)
    q = Point(pointq_x,pointq_y)
    print('Coordinates of P:',pointp_x,',',pointp_y)    # print the coordinates of points P and Q
    print('Coordinates of Q:',pointq_x,',',pointq_y)
    print('Distance between P and Q:', format(p.dist(q),".2f"))    # print distance between P and Q
   
    print()
    line_class = Line(pointp_x,pointp_y,pointq_x,pointq_y)
    print('Slope of PQ:',line_class.slope())    # print the slope of the line PQ
    print('Y-Intercept of PQ:',line_class.y_intercept())# print the y-intercept of the line PQ
    print('X-Intercept of PQ:',line_class.x_intercept())# print the x-intercept of the line PQ
    
    print()
    point_a = infile.readline()
    line_split_A = point_a.split()  # read the coordinates of the third Point A
    pointa_x = float(line_split_A[0])
    pointa_y = float(line_split_A[1])
    
    point_b = infile.readline()
    line_split_B = point_b.split()  # read the coordinates of the fourth Point B
    pointb_x = float(line_split_B[0])
    pointb_y = float(line_split_B[1])
    AB = Line(pointa_x,pointa_y,pointb_x,pointb_y)
    PQ = Line(pointp_x,pointp_y,pointq_x,pointq_y)
    print('Line AB:',AB.__str__()) # print the string representation of the line AB

    if AB.is_parallel(PQ):
        print('PQ is parallel to AB')
    else:
        print('PQ is not parallel to AB')
    # print if the lines PQ and AB are parallel or not
    if AB.is_perpendicular(PQ):
        print('PQ is perpendicular to AB')  
    else:
        print('PQ is not perpendicular to AB')
    # print if the lines PQ and AB (or extensions) are perpendicular or not
    if AB.is_parallel(PQ) == False:
        print('Intersection point of PQ and AB: ',AB.intersection_point(PQ))
        # print coordinates of the intersection point of PQ and AB if not parallel

    point_g = infile.readline() # read the coordinates of the fifth Point G
    line_split_G = point_g.split()
    pointg_x = float(line_split_G[0])
    pointg_y = float(line_split_G[1])

    point_h = infile.readline() # read the coordinates of the sixth Point H
    line_split_H = point_h.split()
    pointh_x = float(line_split_H[0])
    pointh_y = float(line_split_H[1])

    H = Point(pointh_x,pointh_y)
    G = Point(pointg_x,pointg_y)

    print(PQ.perp_dist(G))
    
    if PQ.on_same_side(G,H):
        print('G and H are on the same side of PQ')
    else: 
        print('G and H are not on the same side of PQ')
     # print if the the points G and H are on the same side of PQ
    if AB.on_same_side(G,H):
        print('G and H are on the same side of AB')
    else:
        print('G and H are not on the same side of AB')
    # print if the the points G and H are on the same side of AB

    infile.close()  # close file "geom.txt"

if __name__ == "__main__":
  main()