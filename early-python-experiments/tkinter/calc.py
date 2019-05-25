#!/usr/bin/python
# calc.py 2008/02/09 GPL 
# david_goodall@mac.com

import math
radius = 1.0
degrees = 100.0
twopi = 3.141592535 * 2.0
radperdeg = 360.0 / twopi
radians = degrees / radperdeg
x =  math.cos( radians )
y =  math.sin( radians )
print "x,y is ",x,y
