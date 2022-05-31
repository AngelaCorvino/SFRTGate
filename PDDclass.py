from sys import argv
import seaborn as sns

import scipy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from readcsv import read_data

LET, RBE = read_data("/home/angela/Desktop/SFRTGate/", "RBE10vsLET.csv")


class Profileplotter:
    """Class reading and plotting  data
    Parameters
    ----------
    sion : string-like
        The name of the stable isotope to be passed to the Profileplotter.
    Es : string-like
        The energy of the stable isotope beam to be passed to the Profileplotter.
    uion : string-like
        The name of the unstable isotope to be passed to the Profileplotter.
    Eu : string-like
        The energy of the unstable isotope beam to be passed to the Profileplotter.
    """

    def __init__(self, sion, Es, uion, Eu, ctc):

        """Initialization of class"""
        nz = 100
        res_z = 1
        self.z = np.arange(0, nz) * res_z
        self.sion = sion
        self.uion = uion
        self.Es = Es
        self.Eu = Eu
        self.ctc = ctc

        (self.dose, self.let) = self.read_npy()

    def read_npy(self):
        """
        Read data and create a dictionary
        """

        directory1 = (
            "/home/angela/Desktop/SFRTGate/data/GDRT/ctc"
            + self.ctc
            + "/"
            + self.sion
            + "/"
        )
        directory2 = (
            "/home/angela/Desktop/SFRTGate/data/GDRT/ctc"
            + self.ctc
            + "/"
            + self.uion
            + "/"
        )

        particle = ["primaries", "alpha", "proton", "electron", "positron"]
        dose = {}
        let = {}
        for pname in particle:
            dose["zp_s{}".format(pname)] = np.load(
                directory1 + "zprofilepeak_" + self.sion + "_" + pname + ".npy"
            )
            dose["zv_s{}".format(pname)] = np.load(
                directory1 + "zprofilevalley_" + self.sion + "_" + pname + ".npy"
            )
            dose["zp_u{}".format(pname)] = np.load(
                directory2 + "zprofilepeak_" + self.uion + "_" + pname + ".npy"
            )
            dose["zv_u{}".format(pname)] = np.load(
                directory2 + "zprofilevalley_" + self.uion + "_" + pname + ".npy"
            )
            let["LETp_s{}".format(pname)] = np.load(
                directory1 + "LETpeak_" + self.sion + "_" + pname + ".npy"
            )
            let["LETv_s{}".format(pname)] = np.load(
                directory1 + "LETvalley_" + self.sion + "_" + pname + ".npy"
            )
            let["LETp_u{}".format(pname)] = np.load(
                directory2 + "LETpeak_" + self.uion + "_" + pname + ".npy"
            )
            let["LETv_u{}".format(pname)] = np.load(
                directory2 + "LETvalley_" + self.uion + "_" + pname + ".npy"
            )

        dose["zp_s"] = np.load(directory1 + "zprofilepeak_" + self.sion + ".npy")
        dose["zv_s"] = np.load(directory1 + "zprofilevalley_" + self.sion + ".npy")
        dose["zp_u"] = np.load(directory2 + "zprofilepeak_" + self.uion + ".npy")
        dose["zv_u"] = np.load(directory2 + "zprofilevalley_" + self.uion + ".npy")
        let["LETp_s"] = np.load(directory1 + "LETpeak_" + self.sion + ".npy")
        let["LETv_s"] = np.load(directory1 + "LETvalley_" + self.sion + ".npy")
        let["LETp_u"] = np.load(directory2 + "LETpeak_" + self.uion + ".npy")
        let["LETv_u"] = np.load(directory2 + "LETvalley_" + self.uion + ".npy")
        print(dose.keys())
        return dose, let

    def plotPVDR(self, norm_RBE):
        """
        Plot the Peak To Valley Dose Ratio
        """
        if norm_RBE==True:
            self.dose["zp_s"] *= np.interp(self.let["LETp_s"], LET, RBE)
            self.dose["zp_u"] *= np.interp(self.let["LETp_u"], LET, RBE)
            self.dose["zv_s"] *= np.interp(self.let["LETv_s"], LET, RBE)
            self.dose["zv_u"] *= np.interp(self.let["LETv_u"], LET, RBE)
            plt.ylabel("PVDR RBE weighted ", fontsize=22)
        else:
            plt.ylabel("PVDR  ", fontsize=22)

        plt.plot(
            self.z,
            self.dose['zp_s'] / self.dose['zv_s'],
            ".",
            color=sns.color_palette("Paired")[2],
            markersize=9,
            label="%s: $D_{peak}$/$D_{valley}$" % (sion),
        )
        plt.plot(
            self.z,
            self.dose['zp_u'] / self.dose['zv_u'],
            ".",
            color=sns.color_palette("Paired")[1],
            markersize=9,
            label="$%s:D_{peak}/D_{valley}$" % (uion),
        )
        plt.axvspan(60, 80, facecolor="yellow", alpha=0.3, label="Tumor region ")
        plt.legend(
            title="bw= 600μm x 600 μm, ctc= {} mm ".format(ctc),
            title_fontsize=18,
            fontsize=18,
            loc=3,
            markerscale=3,
        )
        plt.title("Depth dose profile GRT", fontsize=24)
        plt.yscale("log")
        plt.tick_params(axis="x", which="major", labelsize=22)
        plt.tick_params(axis="y", which="major", labelsize=22)
        plt.xlabel("Depth z [mm]", fontsize=22)



    def plotPDD(self, norm, norm_RBE):
        """
        Plot the depth dose profile
        """
        nz = 100
        res_z = 1
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle(
            " Depth dose profile GRT",  # ":$E_{stable}$= %s MeV/u, $E_{unstable}$= %s MeV/u "% (Es, Eu),
            fontsize=24,
        )
        # for k,profile in self.dose.items():
        if norm == True:
            self.dose["zp_s"] /= self.dose["zp_s"].max()
            self.dose["zp_u"] /= self.dose["zp_u"].max()
            self.dose["zv_s"] /= self.dose["zv_s"].max()
            self.dose["zv_u"] /= self.dose["zv_u"].max()
            ax1.set_ylabel("Relative Dose", fontsize=22)
        elif norm_RBE == True:
            self.dose["zp_s"]  *= np.interp(self.let["LETp_s"], LET, RBE)
            self.dose["zp_u"]  *= np.interp(self.let["LETp_u"], LET, RBE)
            self.dose["zv_s"]  *= np.interp(self.let["LETv_s"], LET, RBE)
            self.dose["zv_u"]  *= np.interp(self.let["LETv_u"], LET, RBE)
            # self.dose["zp_s"] /= self.dose["zp_s"].max()
            # self.dose["zp_u"] /= self.dose["zp_u"].max()
            # self.dose["zv_s"] /= self.dose["zv_s"].max()
            # self.dose["zv_u"] /= self.dose["zv_u"].max()
            ax1.set_ylabel("Biological Dose (D x RBE)", fontsize=22)

        ax1.plot(
            self.z,
            self.dose["zp_s"],
            ".",
            color=sns.color_palette("Paired")[2],
            markersize=9,
            label="%s" % (self.sion),
        )
        ax1.plot(
            self.z,
            self.dose["zp_u"],
            ".",
            color=sns.color_palette("Paired")[1],
            markersize=9,
            label="%s" % (self.uion),
        )
        ax2.plot(
            self.z,
            self.dose["zv_s"],
            ".",
            color=sns.color_palette("Paired")[2],
            markersize=9,
            label="%s" % (self.sion),
        )
        ax2.plot(
            self.z,
            self.dose["zv_u"],
            ".",
            color=sns.color_palette("Paired")[1],
            markersize=9,
            label="%s" % (self.uion),
        )
        ax1.axvspan(60, 80, facecolor="yellow", alpha=0.3, label="Tumor region ")
        ax2.axvspan(60, 80, facecolor="yellow", alpha=0.3, label="Tumor region ")
        ax1.legend(
            title="peak, ctc={} mm".format(self.ctc),
            title_fontsize=18,
            fontsize=18,
            loc=3,
            markerscale=3,
        )
        ax1.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
        ax1.tick_params(axis="x", which="major", labelsize=22)
        ax1.tick_params(axis="y", which="major", labelsize=22)
        ax1.set_xlabel("Depth z [mm]", fontsize=22)
        ax2.legend(
            title="Valley, ctc={} mm".format(self.ctc),
            title_fontsize=18,
            fontsize=18,
            loc=3,
            markerscale=3,
        )
        ax2.tick_params(axis="x", which="major", labelsize=22)
        ax2.tick_params(axis="y", which="major", labelsize=22)
        ax2.set_xlabel("Depth z [mm]", fontsize=22)
        ax2.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
        plt.show()

    def plotparticlePDD(self, norm, log, electron, proton, positron):
        """
        Plot the depth dose profile
        """

        if norm == True:
            normp_s = 1 / self.dose["zp_s"].max()
            normp_u = 1 / self.dose["zp_u"].max()

        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
        fig.suptitle("Depth dose profile GRT", fontsize=22)
        ax1.plot(
            self.z,
            self.dose["zp_s"] * normp_s,
            "--",
            color=sns.color_palette("Paired")[1],
            markersize=9,
            label="total dose",
        )
        ax1.plot(
            self.z,
            self.dose["zp_sprimaries"] * normp_s,
            ".-",
            color=sns.color_palette("Paired")[0],
            markersize=9,
            label="primaries",
        )
        ax1.plot(
            self.z,
            self.dose["zp_salpha"] * normp_s,
            ".-",
            color=sns.color_palette("Paired")[4],
            markersize=9,
            label="alpha",
        )
        ax2.plot(
            self.z,
            self.dose["zp_u"] * normp_u,
            "--",
            color=sns.color_palette("Paired")[1],
            markersize=9,
            label="total dose",
        )
        ax2.plot(
            self.z,
            self.dose["zp_uprimaries"] * normp_u,
            ".-",
            color=sns.color_palette("Paired")[0],
            markersize=9,
            label="primaries",
        )
        ax2.plot(
            self.z,
            self.dose["zp_ualpha"] * normp_u,
            ".-",
            color=sns.color_palette("Paired")[4],
            markersize=9,
            label="alpha",
        )
        ax3.plot(
            self.z,
            self.dose["zv_s"] * normp_s,
            "--",
            color=sns.color_palette("Paired")[1],
            markersize=9,
            label="total dose",
        )
        ax3.plot(
            self.z,
            self.dose["zv_sprimaries"] * normp_s,
            ".-",
            color=sns.color_palette("Paired")[0],
            markersize=9,
            label="primaries",
        )
        ax3.plot(
            self.z,
            self.dose["zv_salpha"] * normp_s,
            ".-",
            color=sns.color_palette("Paired")[4],
            markersize=9,
            label="alpha",
        )
        ax4.plot(
            self.z,
            self.dose["zv_u"] * normp_u,
            "--",
            color=sns.color_palette("Paired")[1],
            markersize=9,
            label="total dose",
        )
        ax4.plot(
            self.z,
            self.dose["zv_uprimaries"] * normp_u,
            ".-",
            color=sns.color_palette("Paired")[0],
            markersize=9,
            label=" primaries",
        )
        ax4.plot(
            self.z,
            self.dose["zv_ualpha"] * normp_u,
            ".-",
            color=sns.color_palette("Paired")[4],
            markersize=9,
            label=" alpha",
        )

        if electron == True:
            ax1.plot(
                self.z,
                self.dose["zp_selectron"] * normp_s,
                ".-",
                color=sns.color_palette("Paired")[9],
                markersize=9,
                label="electron",
            )
            ax2.plot(
                self.z,
                self.dose["zp_uelectron"] * normp_u,
                ".-",
                color=sns.color_palette("Paired")[9],
                markersize=9,
                label="electron",
            )
            ax3.plot(
                self.z,
                self.dose["zv_selectron"] * normp_s,
                ".-",
                color=sns.color_palette("Paired")[9],
                markersize=9,
                label="electron",
            )
            ax4.plot(
                self.z,
                self.dose["zv_uelectron"] * normp_u,
                ".-",
                color=sns.color_palette("Paired")[9],
                markersize=9,
                label="electron",
            )
        if proton == True:
            ax2.plot(
                self.z,
                self.dose["zp_uproton"] * normp_u,
                ".-",
                color=sns.color_palette("Paired")[7],
                markersize=9,
                label=" proton",
            )
            ax1.plot(
                self.z,
                self.dose["zp_sproton"] * normp_s,
                ".-",
                color=sns.color_palette("Paired")[7],
                markersize=9,
                label=" proton",
            )
            ax3.plot(
                self.z,
                self.dose["zv_uproton"] * normp_u,
                ".-",
                color=sns.color_palette("Paired")[7],
                markersize=9,
                label=" proton",
            )
            ax4.plot(
                self.z,
                self.dose["zv_sproton"] * normp_s,
                ".-",
                color=sns.color_palette("Paired")[7],
                markersize=9,
                label=" proton",
            )
        if positron == True:
            ax1.plot(
                self.z,
                self.dose["zp_spositron"] * normp_s,
                ".-",
                color=sns.color_palette("Paired")[10],
                markersize=9,
                label=" positron",
            )
            ax2.plot(
                self.z,
                self.dose["zp_upositron"] * normp_u,
                ".-",
                color=sns.color_palette("Paired")[10],
                markersize=9,
                label="positron",
            )
            ax3.plot(
                self.z,
                self.dose["zv_spositron"] * normp_s,
                ".-",
                color=sns.color_palette("Paired")[10],
                markersize=9,
                label=" positron",
            )
            ax4.plot(
                self.z,
                self.dose["zv_upositron"] * normp_u,
                ".-",
                color=sns.color_palette("Paired")[10],
                markersize=9,
                label="positron",
            )
        if log == True:
            ax1.set_yscale("log")
            ax2.set_yscale("log")
            ax3.set_yscale("log")
            ax4.set_yscale("log")
            ax3.set_ylim([0, 1])
            ax4.set_ylim([0, 1])
        ax2.legend(
            title="Peak",
            title_fontsize=16,
            fontsize=16,
            loc=2,
            markerscale=3,
        )
        ax4.legend(
            title="Valley",
            title_fontsize=16,
            fontsize=16,
            loc=2,
            markerscale=3,
        )
        ax3.legend(
            title="Valley",
            title_fontsize=16,
            fontsize=16,
            loc=2,
            markerscale=3,
        )
        ax1.legend(
            title="Peak",
            title_fontsize=16,
            fontsize=16,
            loc=2,
            markerscale=3,
        )
        ax4.text(50, 1, "%s: E= %s MeV/u" % (uion, Eu), fontsize=18)
        ax3.text(50, 1, "%s: E= %s MeV/u" % (sion, Es), fontsize=18)
        ax2.text(45, 3, "%s: E= %s MeV/u" % (uion, Eu), fontsize=18)
        ax1.text(45, 3, "%s: E= %s MeV/u" % (sion, Es), fontsize=18)
        ax1.tick_params(axis="x", which="major", labelsize=18)
        ax1.tick_params(axis="y", which="major", labelsize=18)
        # ax1.set_xlabel("Depth z [mm]", fontsize=18)
        ax1.set_ylabel("Relative Dose ", fontsize=18)
        ax3.tick_params(axis="x", which="major", labelsize=18)
        ax3.tick_params(axis="y", which="major", labelsize=18)
        ax3.set_xlabel("Depth z [mm]", fontsize=18)
        ax3.set_ylabel("Relative Dose ", fontsize=18)
        ax1.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
        ax2.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
        ax3.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
        ax4.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
        ax4.tick_params(axis="x", which="major", labelsize=18)
        ax4.tick_params(axis="y", which="major", labelsize=18)
        ax2.tick_params(axis="x", which="major", labelsize=18)
        ax2.tick_params(axis="y", which="major", labelsize=18)
        ax4.set_xlabel("Depth z [mm]", fontsize=18)
        plt.show()

    def plotparticleLET(self, electron, proton, positron):
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
        fig.suptitle(
            "$LET_{d}$ depth profile GRT",  # \n $E_{stable}=%s [MeV/u], E_{unstable}=%s [MeV/u] $" % (Es, Eu),
            fontsize=24,
        )
        ax1.plot(
            self.z,
            self.let["LETp_s"],
            "--",
            color=sns.color_palette("Paired")[1],
            markersize=9,
            label="total LET",
        )
        ax1.plot(
            self.z,
            self.let["LETp_sprimaries"],
            ".-",
            color=sns.color_palette("Paired")[0],
            markersize=9,
            label="primaries",
        )
        ax1.plot(
            self.z,
            self.let["LETp_salpha"],
            ".-",
            color=sns.color_palette("Paired")[4],
            markersize=9,
            label="alpha",
        )
        ax2.plot(
            self.z,
            self.let["LETp_u"],
            "--",
            color=sns.color_palette("Paired")[1],
            markersize=9,
            label="total LET",
        )
        ax2.plot(
            self.z,
            self.let["LETp_uprimaries"],
            ".-",
            color=sns.color_palette("Paired")[0],
            markersize=9,
            label="primaries",
        )
        ax2.plot(
            self.z,
            self.let["LETp_ualpha"],
            ".-",
            color=sns.color_palette("Paired")[4],
            markersize=9,
            label="alpha",
        )
        ax3.plot(
            self.z,
            self.let["LETv_s"],
            "--",
            color=sns.color_palette("Paired")[1],
            markersize=9,
            label="total LET",
        )
        ax3.plot(
            self.z,
            self.let["LETv_sprimaries"],
            ".-",
            color=sns.color_palette("Paired")[0],
            markersize=9,
            label="primaries",
        )
        ax3.plot(
            self.z,
            self.let["LETv_salpha"],
            ".-",
            color=sns.color_palette("Paired")[4],
            markersize=9,
            label="alpha",
        )
        ax4.plot(
            self.z,
            self.let["LETv_u"],
            "--",
            color=sns.color_palette("Paired")[1],
            markersize=9,
            label="total LET ",
        )
        ax4.plot(
            self.z,
            self.let["LETv_uprimaries"],
            ".-",
            color=sns.color_palette("Paired")[0],
            markersize=9,
            label="primaries",
        )
        ax4.plot(
            self.z,
            self.let["LETv_ualpha"],
            ".-",
            color=sns.color_palette("Paired")[4],
            markersize=9,
            label="alpha",
        )
        if electron == True:
            ax1.plot(
                self.z,
                self.let["LETp_selectron"],
                ".-",
                color=sns.color_palette("Paired")[9],
                markersize=9,
                label="electron",
            )
            ax2.plot(
                self.z,
                self.let["LETp_uelectron"],
                ".-",
                color=sns.color_palette("Paired")[9],
                markersize=9,
                label="electron",
            )
            ax3.plot(
                self.z,
                self.let["LETv_selectron"],
                ".-",
                color=sns.color_palette("Paired")[9],
                markersize=9,
                label="electron",
            )
            ax4.plot(
                self.z,
                self.let["LETv_uelectron"],
                ".-",
                color=sns.color_palette("Paired")[9],
                markersize=9,
                label="electron",
            )
        if proton == True:
            ax2.plot(
                self.z,
                self.let["LETp_uproton"],
                ".-",
                color=sns.color_palette("Paired")[7],
                markersize=9,
                label="proton",
            )
            ax1.plot(
                self.z,
                self.let["LETp_sproton"],
                ".-",
                color=sns.color_palette("Paired")[7],
                markersize=9,
                label="proton",
            )
            ax3.plot(
                self.z,
                self.let["LETv_uproton"],
                ".-",
                color=sns.color_palette("Paired")[7],
                markersize=9,
                label="proton",
            )
            ax4.plot(
                self.z,
                self.let["LETv_sproton"],
                ".-",
                color=sns.color_palette("Paired")[7],
                markersize=9,
                label="proton",
            )
        if positron == True:
            ax1.plot(
                self.z,
                self.let["LETp_spositron"],
                ".-",
                color=sns.color_palette("Paired")[10],
                markersize=9,
                label="positron",
            )
            ax2.plot(
                self.z,
                self.let["LETp_upositron"],
                ".-",
                color=sns.color_palette("Paired")[10],
                markersize=9,
                label="positron",
            )
            ax3.plot(
                self.z,
                self.let["LETv_spositron"],
                ".-",
                color=sns.color_palette("Paired")[10],
                markersize=9,
                label="positron",
            )
            ax4.plot(
                self.z,
                self.let["LETv_upositron"],
                ".-",
                color=sns.color_palette("Paired")[10],
                markersize=9,
                label="positron",
            )

        ax2.legend(
            title="Peak",
            title_fontsize=16,
            fontsize=16,
            loc=2,
            markerscale=3,
        )
        ax4.legend(
            title="Valley",
            title_fontsize=16,
            fontsize=16,
            loc=2,
            markerscale=3,
        )
        ax4.text(45, 20, "%s: E=%s MeV/u" % (uion, Eu), fontsize=18)
        ax3.text(45, 20, "%s: E=%s MeV/u" % (sion, Es), fontsize=18)
        ax2.text(45, 50, "%s: E=%s MeV/u" % (uion, Eu), fontsize=18)
        ax1.text(45, 50, "%s: E=%s MeV/u" % (sion, Es), fontsize=18)
        ax2.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
        ax3.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
        ax4.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
        ax4.tick_params(axis="x", which="major", labelsize=18)
        ax4.tick_params(axis="y", which="major", labelsize=18)
        ax2.tick_params(axis="x", which="major", labelsize=18)
        ax2.tick_params(axis="y", which="major", labelsize=18)
        ax4.set_xlabel("Depth z [mm]", fontsize=18)
        ax3.legend(
            title="Valley",
            title_fontsize=16,
            fontsize=16,
            loc=2,
            markerscale=3,
        )
        ax1.legend(
            title="Peak",
            title_fontsize=16,
            fontsize=16,
            loc=2,
            markerscale=3,
        )
        ax1.set_ylabel("LET [keV/um]", fontsize=22)
        ax1.set_ylim([0, self.let["LETp_sprimaries"].max()])
        ax2.set_ylim([0, self.let["LETp_uprimaries"].max()])
        ax3.set_ylim(
            [0, max(self.let["LETv_s"].max(), self.let["LETv_sprimaries"].max())]
        )
        ax4.set_ylim(
            [0, max(self.let["LETv_u"].max(), self.let["LETv_uprimaries"].max())]
        )
        ax1.tick_params(axis="x", which="major", labelsize=18)
        ax1.tick_params(axis="y", which="major", labelsize=18)
        # ax1.set_xlabel("Depth z [mm]", fontsize=18)
        ax1.set_ylabel("LET [keV/um]", fontsize=18)
        ax3.tick_params(axis="x", which="major", labelsize=18)
        ax3.tick_params(axis="y", which="major", labelsize=18)
        ax3.set_xlabel("Depth z [mm]", fontsize=18)
        ax3.set_ylabel("LET [keV/um]", fontsize=18)
        ax1.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
        ax2.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
        ax3.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
        ax4.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
        ax4.tick_params(axis="x", which="major", labelsize=18)
        ax4.tick_params(axis="y", which="major", labelsize=18)
        ax2.tick_params(axis="x", which="major", labelsize=18)
        ax2.tick_params(axis="y", which="major", labelsize=18)
        ax4.set_xlabel("Depth z [mm]", fontsize=18)
        plt.show()

    def plotparticlecontribution(self, particle):
        """
        Plot the contribution a particular species to the total dose 
        """

        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle(
            "DDP GRT: %s contribution" % (particle),
            fontsize=22,
        )

        ax1.plot(
            self.z,
            (self.dose["zp_s{}".format(particle)] / self.dose["zp_s"]) * 100,
            ".",
            color=sns.color_palette("Paired")[3],
            markersize=9,
            label="%s: $D_{peak,%s}$/$D_{peak}$" % (self.sion, particle),
        )
        ax1.plot(
            self.z,
            (self.dose["zp_u{}".format(particle)] / self.dose["zp_u"]) * 100,
            ".",
            color=sns.color_palette("Paired")[1],
            markersize=9,
            label="%s: $D_{peak,%s}$/$D_{peak}$" % (self.uion, particle),
        )

        ax2.plot(
            self.z,
            (self.dose["zv_s{}".format(particle)] / self.dose["zv_s"]) * 100,
            ".",
            color=sns.color_palette("Paired")[3],
            markersize=9,
            label="%s: $D_{valley,%s}$/$D_{valley}$" % (self.sion, particle),
        )
        ax2.plot(
            self.z,
            (self.dose["zv_u{}".format(particle)] / self.dose["zv_u"]) * 100,
            ".",
            color=sns.color_palette("Paired")[1],
            markersize=9,
            label="%s: $D_{valley,%s}$/$D_{valley}$" % (self.uion, particle),
        )

        ax2.axvspan(60, 80, facecolor="yellow", alpha=0.3, label="Tumor region ")
        ax1.axvspan(60, 80, facecolor="yellow", alpha=0.3, label="Tumor region ")
        ax1.legend(title="", title_fontsize=18, fontsize=18, loc=1, markerscale=3)
        ax1.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
        ax1.tick_params(axis="x", which="major", labelsize=22)
        ax1.tick_params(axis="y", which="major", labelsize=22)
        ax1.set_xlabel("Depth z [mm]", fontsize=22)
        ax1.set_ylabel("particle contribution[%] ", fontsize=22)
        ax2.legend(title="", title_fontsize=18, fontsize=18, loc=2, markerscale=3)
        ax2.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
        ax2.tick_params(axis="x", which="major", labelsize=22)
        ax2.tick_params(axis="y", which="major", labelsize=22)
        ax2.set_xlabel("Depth z [mm]", fontsize=22)
        plt.show()


if __name__ == "__main__":
    sion = input("Enter stable io name: ")
    Es = input("Enter its energy in Mev/u: ")
    uion = input("Enter unstable isotope name: ")
    Eu = input("Enter its energy in Mev/u: ")
    ctc = input("Center to center distance in 10^(-1) mm: ")

    a = Profileplotter(sion, Es, uion, Eu, ctc)
    # a.plotPVDR(True)
    # a.plotPDD(False, True)
    a.plotparticlePDD(True, True, True, True, True)
    # a.plotparticleLET(True, True, True)
    a.plotparticlecontribution('alpha')
