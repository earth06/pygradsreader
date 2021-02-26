import numpy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import re
import glob
class Grads():
    """
    grads形式のデータをnumpy配列に変換するクラス
    """
    @classmethod
    def read_ctlfile(cls,ctlfile):
        ctl={}
        for line in f:
            info=re.split(" +",line.rstrip("\r\n"))
            ctl[info[0]]=info[1:]
    
    def __init__(self,x,y,z,t):
        self.x=x
        self.y=y
        self.z=z
        self.t=t
        self.num=x*y*z*t
        self.struct=np.dtype([("arr",f"<{self.num}f")])
    
    def read_grads(self,file):
        """
        Parameters
        ------------
        file : str
            grads binary filepath
        
        Retunrs
        -------------
        data : numpy.ndarray
            reshaped array of reading data 
        """
        with open(file) as f:
            chunk=np.fromfile(f,dtype=self.struct,count=self.t)
        data=chunk[0]["arr"].reshape((self.z,self.y, self.x))
        return data
    
    def read_multi_grads(self,files):
        t_all=len(files)
        alldata=np.zeros((t_all, self.z, self.y, self.x))

        for t,file in enumerate(files):
            tmp=self.read_grads(file)
            alldata[t,:,:,:]=tmp
            del tmp
        return alldata