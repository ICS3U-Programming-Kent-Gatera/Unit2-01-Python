#!/usr/bin/env python3
# Created By: Kent Gatera
# Date: 09.21.22
# This program calculates the area and circumference of a circle.
# with the radius of 15 mm

import math

rad = 15
Circumference = math.pi * rad * 2
Area = math.pi * rad ** 2

print("The circumference is {} cm". format(Circumference))
print("The area is {} cm^2". format(Area))
