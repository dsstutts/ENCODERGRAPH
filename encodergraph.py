# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 14:29:38 2016
Tested using Python 3.51

This code draws a rotary encoder mask for use 
with optical interrupters to measure rotation speed
or position.

# Author: D. S. Stutts
# Associate Professor of Mechanical Engineering
# 282 Toomey Hall
# 400 W. 13th St.
# Rolla, MO 65409-0050
# Email: stutts@mst.edu

The three input parameters are specified in the INPUTS
section below.

Copyright (c) 2016 encodergraph.py)

S&T and the University of Missouri Board of Curators
license to you the right to use, modify, copy, and distribute this
code subject to the MIT license:

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.



THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

The authors kindly request that any publications benefitting from the use
of this software include the following citation:

@Misc{encodergraph-,
author =   {Stutts, Daniel. S.},
title = {{encodergraph.py}: {Plots rotary optical encoder masks on transparencies}},
howpublished = {/url{https://github.com/dsstutts/ENCODERGRAPH.git}},
year = {2016}}

 #
 # LANGUAGE:  Python 3.5
 #_____________________________________

"""

import math
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
#INPUTS:
r = 1# radius
size = 5# figure size in inches
N = 64# Number of encoder lines
res = 72# Number of dots per inch
# End of INPUTS
dtheta = 2*math.pi/N # Angular increment
ang = 0.# Initialize angle
fig = plt.figure(figsize=(size,size), dpi=res)
plt.axis('equal')
plt.axis('off')
ax = fig.add_subplot(111)
# Loop over the number of encoder lines
while ang < 2*math.pi-dtheta:
    b1x = r*math.cos(ang)
    b1y = r*math.sin(ang)
    b2x = r*math.cos(ang+dtheta)
    b2y = math.sin(ang+dtheta)
    ang = ang+dtheta
    w1x = r*math.cos(ang)
    w1y = r*math.sin(ang)
    w2x = r*math.cos(ang+dtheta)
    w2y = math.sin(ang+dtheta)
    ang = ang+dtheta
    vertsb = [(0.0,0.0),(b1x,b1y),(b2x,b2y),(0.0,0.0)]
    vertsw = [(0.0,0.0),(w1x,w1y),(w2x,w2y),(0.0,0.0)]
    codes = [Path.MOVETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY,
        ]
    pathb = Path(vertsb, codes)
    pathw = Path(vertsw, codes)
    patchb = patches.PathPatch(pathb, facecolor='black', lw=0)
    ax.add_patch(patchb)
    patchw = patches.PathPatch(pathw, facecolor='white', lw=0)
    ax.add_patch(patchw)
    
verts1 = [(0.0,-0.02),(0.0,0.02),(-0.02, 0.0), (0.02,0.0)]
codes1 = [Path.MOVETO,Path.LINETO,Path.MOVETO,Path.LINETO]
path1 = Path(verts1, codes1)
patch1 = patches.PathPatch(path1, color='black', lw=1)

circle1 = patches.Circle((0.,0.),  radius=0.1, color='white', ec='black',fill=True)
circle2 = patches.Circle((0.,0.),  radius=0.25, color='black', fill=False)
circle3 = patches.Circle((0.,0.),  radius=0.5, color='black', fill=False)
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)
ax.add_patch(patch1)
    
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
plt.show()
figname = 'encoder'+str(N)+".eps"
fig.savefig(figname, format='eps', dpi=res)
