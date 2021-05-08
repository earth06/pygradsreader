from matplotlib.colors import LinearSegmentedColormap
import numpy as np
"""
ex)普通のカラーマップとして扱う
plt.contourf(xx,yy,....
    ,cmap=custom_colorbar.get_gscmap()...)

ex) 等高線とその色を手動で与える(カラーマップを使わないver)
plt.contourf(xx,yy,...
    levels=[0,0.1,0.5,1,3,5,10,15,20,30,50],
    colors=custom_colorbar.get_gscolors())

ex) 手動で決めた等高線に対して色を適当に割り振る
from matplotlib.colors import BoundaryNorm
levels=[0,0.1,0.5,1,3,5,10,15,20,30,50]
norm=BoundaryNorm(levels,ncolors=256)
plt.contourf(xx,yy,
    levels=levels,norm=norm,cmap=custom_colorbar.get_gscmap()...)

"""
def get_gscolors():
    gscolors=np.array([
        [160,0 ,200,1],#purple
        [130,0 ,220,1],#dark purple
        [30 ,60,255,1],#dark blue
        [0, 160,255,1],#medium blue
        [0, 200,200,1],#light blue
        [0, 210,140,1],#aqua
        [0,220,0,1],   #green
        [160,230,50,1],#yellow/green
        [230,220,50,1],#yellow
        [230,175,45,1],#dark yellow
        [240,130,40,1],#orange
        [250,60,60,1], #red
        [240,0,130,1]  #magenta
        ],dtype=np.float32)
    gscolors[:,:3]/=256 #RGBを0-1の範囲に変換
    return gscolors

def get_jmacolors():
    jmacolors=np.array([
        [242,242,242,1],#white
        [160,210,255,1],#white blue
        [33 ,140,255,1],#lightblue
        [0  ,65 ,255,1],#blue
        [250,245,0,1],#yellow
        [255,153,0,1],#orange
        [255,40,0,1],#red
        [180,0,104,1]#magenta
    ],dtype=np.float32)
    jmacolors[:,:3] /=256
    return jmacolors
def get_jwacolors():
    jwacolors=np.array([
        [0,255,253,1],#aqua
        [0,0,226,1],#blue
        [28,150,0,1],#green
        [254,255,5,1],#yellow
        [254,255,5,1],#orange
        [253,3,242,1],#pink
        [255,0,0],#red
    ],dtype=np.float32)

def get_jmalevels():
    return [0,1,5,10,20,30,50,80]

def get_jwalevels():
    return [0,1,5,10,15,25,30,50]

def get_gscmap():
    gscolors=get_gscolors()
    gscmap=LinearSegmentedColormap.from_list("gscmap",colors=gscolors)
    return gscmap

def get_jmacmap():
    jmacolors=get_jmacolors()
    jmacmap=LinearSegmentedColormap.from_list("jmacmap",colors=jmacolors)
    return jmacmap

def get_jwacmap():
    jwacolors=get_jwacolors()
    jwacmap=LinearSegmentedColormap.from_list("jwacmap",colors=jwacolors)
    return jwacmap

def make_cmap(colors,cname="custom"):
    cmap=LinearSegmentedColormap.from_list(cname,colors=colors)
    return cmap