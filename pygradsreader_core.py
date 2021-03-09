import numpy as np


def read_gs(file,x,y,z,t,na_value=-327.68):
    gsdtype=np.dtype([("arr",f"<{x*y*z}f")])
    with open(file,"br") as f:
        chunk=np.fromfile(f,dtype=gsdtype,count=t)
    arr= chunk[0]["arr"].reshape((z,y,x),order="C")
    arr=np.where(arr==na_value,np.nan,arr)
    arr=np.where(arr==255,np.nan,arr)
    return arr

#複数の変数が入ったgradsバイナリを読み込む
def read_mulit_gs(file,xmax,ymax,zmax,t,nvar,zdims=None,varnames=None,na_value=-327.68):
    #z次元が統一されていない
    if zdims is not None:
        if varnames is None:
            gsdtype=np.dtype([(f"var{i}",f"<{xmax*ymax*z}f") for i,z in zip(range(nvar),zdims)])
        else:
            gsdtype=np.dtype([(f"{varname}",f"<{xmax*ymax*z}f") for varname,z in zip(varnames,zdims)])
    #zがすべて同じ
    else:
        if varnames is None:
            gsdtype=np.dtype([(f"var{i}",f"<{xmax*ymax*zmax}f") for z in zdims])
        else:
            gsdtype=np.dtype([(f"{varname}",f"<{xmax*ymax*zmax}f") for varname in varnames])        
    with open(file,"br") as f:
        chunk=np.fromfile(f,dtype=gsdtype,count=t)
    return chunk[0]