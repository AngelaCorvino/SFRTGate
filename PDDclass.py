from sys import argv
import seaborn as sns

import scipy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class profileplotter:
    """Analize """
    def __init__(self,sion,Es,uion,Eu):
        """ Initialization of class"""
        self.sion = sion
        self.uion= uion
        self.Es= Es
        self.Eu=Eu

        (self.d
        )=self.readdata()

    def readdata(self):
        directory1 = "/home/angela/Desktop/SFRTGate/data/GDRT/ctc35/" + self.sion + "/"
        directory2 = "/home/angela/Desktop/SFRTGate/data/GDRT/ctc35/" + self.uion + "/"

        particle=['primaries','alpha','proton','electron','positron']
        d={}
        for pname in particle:
            d["zp_s{}".format(pname)] = np.load(directory1 + "zprofilepeak_" + self.sion +pname+".npy")
            d["zv_s{}".format(pname)]=np.load(directory1 + "zprofilepeak_" + self.sion + pname +".npy")
            d["zp_u{}".format(pname)]=np.load(directory2 + "zprofilepeak_" + self.uion + pname+".npy")
            d["zv_u{}".format(pname)] = np.load(directory2 + "zprofilevalley_" + self.uion + pname+".npy")

        d["zp_s"] = np.load(directory1 + "zprofilepeak_" + self.sion +".npy")
        d["zv_s"] = np.load(directory1 + "zprofilevalley_" + self.sion + ".npy")
        d["zp_u"] = np.load(directory2 + "zprofilepeak_" + self.uion + ".npy")
        d["zv_u"] = np.load(directory2 + "zprofilevalley_" + self.uion + ".npy")
        print(d.keys())
        return d

    def plotPVDR(self,norm):
        nz=100
        res_z=1
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle(
            " Depth dose profile GRT :$E_{stable}$= %s MeV/u, $E_{unstable}$= %s MeV/u "
            % (self.Es, self.Eu),
            fontsize=24,
        )
        if norm== True:
            zp_s=d["zp_s"]/d["zp_s"].max()
            zp_u=d["zp_u"]/d["zp_u"].max()
            zv_s=d["zv_s"]/d["zv_s"].max()
            zv_u=d["zv_u"]/d["zv_u"].max()
        ax1.plot(
            (np.arange(0, nz) * res_z),
            zp_s,
            ".",
            color=sns.color_palette("Paired")[2],
            markersize=9,
            label="%s: $D_{peak}$"%(self.sion),
        )
        ax1.plot(
            (np.arange(0, nz) * res_z),
            zp_u,
            ".",
            color=sns.color_palette("Paired")[1],
            markersize=9,
            label="%s: $D_{peak}$"%(self.uion),
        )
        ax2.plot(
            (np.arange(0, nz) * res_z),
            zv_s,
            ".",
            color=sns.color_palette("Paired")[2],
            markersize=9,
            label="%s: $D_{valley}$"%(self.sion),
        )
        ax2.plot(
            (np.arange(0, nz) * res_z),
            zv_u,
            ".",
            color=sns.color_palette("Paired")[1],
            markersize=9,
            label="%s: $D_{valley}$"%(self.uion),
        )
        plt.show()


if __name__ == '__main__':
    sion = input("Enter stable io name: ")
    Es = input("Enter its energy in Mev/u: ")
    uion = input("Enter unstable isotope name: ")
    Eu = input("Enter its energy in Mev/u: ")

    a=profileplotter(sion,Es,uion,Eu)
    #data.zprofile()
    d=a.readdata()
    print(d["zp_s"])
    a.plotPVDR(True)
