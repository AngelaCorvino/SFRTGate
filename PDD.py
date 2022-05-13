import seaborn as sns

import numpy as np
from matplotlib import pyplot as plt

from readcsv import read_data

############################################################################


sion = input("Enter stable io name: ")
Es = input("Enter its energy in Mev/u: ")
uion = input("Enter unstable isotope name: ")
Eu = input("Enter its energy in Mev/u: ")

directory1 = "/home/angela/Desktop/SFRTGate/data/GDRT/ctc18/" + sion + "/"
directory2 = "/home/angela/Desktop/SFRTGate/data/GDRT/ctc18/" + uion + "/"

ctc='1.8'

#################################################################################
z = np.arange(0, 100) * 1


def ax1plotfunction(directory,ctc, zone, ion, nz, res_z, color, norm, norm_RBE):
    LET, RBE = read_data("/home/angela/Desktop/SFRTGate/", "RBEvsLET.csv")
    letprofile = np.load(directory + "LET" + zone + "_" + ion + ".npy")
    print(letprofile)
    profile = np.load(directory + "zprofile" + zone + "_" + ion + ".npy")
    print(profile)
    if norm == True:
        profile = profile / profile.max()
        ax1.set_ylabel("Relative Dose", fontsize=22)
    elif norm_RBE == True and letprofile.min() > LET.min():
        rbe = np.interp(letprofile, LET, RBE)
        profile = (profile / profile.max()) * rbe
        ax1.set_ylabel("Biological Dose (D x RBE)", fontsize=22)

    ax1.plot(
        (np.arange(0, nz) * res_z),
        profile,
        ".",
        color=color,
        markersize=9,
        label="%s: $D_{%s}$" % (ion, zone),
    )

    ax1.legend(
        title="{}, ctc={}mm".format(zone,ctc), title_fontsize=18, fontsize=18, loc=3, markerscale=3
    )
    ax1.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax1.tick_params(axis="x", which="major", labelsize=22)
    ax1.tick_params(axis="y", which="major", labelsize=22)
    ax1.set_xlabel("Depth z[mm]", fontsize=22)

def ax2plotfunction(directory, ctc,prefix, zone, ion, nz, res_z, color, norm, norm_RBE):
    LET, RBE = read_data("/home/angela/Desktop/SFRTGate/", "RBEvsLET.csv")
    letprofile = np.load(directory + "LET" + zone + "_" + ion + ".npy")
    profile = np.load(directory + prefix + zone + "_" + ion + ".npy")
    if norm == True:
        profile = profile / profile.max()
    elif norm_RBE == True:
        rbe = np.interp(letprofile, LET, RBE)
        profile = (profile / profile.max()) * rbe
        # ax2.set_ylabel("Biological Dose (D x RBE)", fontsize=22)
    ax2.plot(
        (np.arange(0, nz) * res_z),
        profile,
        ".",
        color=color,
        markersize=9,
        label="%s: $D_{%s}$" % (ion, zone),
    )
    ax2.legend(
        title="{}, ctc={}mm".format(zone,ctc), title_fontsize=18, fontsize=18, loc=3, markerscale=3
    )
    ax2.tick_params(axis="x", which="major", labelsize=22)
    ax2.tick_params(axis="y", which="major", labelsize=22)
    ax2.set_xlabel("Depth z[mm]", fontsize=22)
    ax2.grid(b=True, color="k", linestyle="dotted", alpha=0.2)

###############################################################################

# def plotparticlecontribution(particle,Es,Eu,sion,uion):
#     zp_s = np.load(directory1 + "zprofilepeak_" + sion + ".npy")
#     zv_s = np.load(directory1 + "zprofilevalley_" + sion + ".npy")
#     zp_u = np.load(directory2 + "zprofilepeak_" + uion + ".npy")
#     zv_u = np.load(directory2 + "zprofilevalley_" + uion + ".npy")
#     zp_sparticle = np.load(directory1 + "zprofilepeak_" + sion + particle+".npy")
#     zv_sparticle = np.load(directory1 + "zprofilevalley_" + sion + particle+".npy")
#     zp_uparticle = np.load(directory2 + "zprofilepeak_" + uion + particle+".npy")
#     zv_uparticle = np.load(directory2 + "zprofilevalley_" + uion + particle+".npy")
#
#     fig, (ax1, ax2) = plt.subplots(1, 2)
#     fig.suptitle(
#     "DDP GRT: %s contribution \n $E_{stable}=%s MeV/u, E_{unstable}=%s MeV/u $"
#     % (particle,Es, Eu),
#     fontsize=22,
#     )
#
#     ax1.plot(z,
#     (zp_sparticle / zp_s) * 100,".-",
#     color=sns.color_palette("Paired")[3],
#     markersize=9,
#     label="%s: $D_{peak,%s}$/$D_{peak}$" % (sion,particle),
#     )
#     ax1.plot(z,
#     (zp_uparticle / zp_u) * 100,".-",
#     color=sns.color_palette("Paired")[1],
#     markersize=9,
#     label="%s: $D_{peak,%s}$/$D_{peak}$" % (uion,particle),
#     )
#
#     ax2.plot(z,
#     (zv_sparticle / zv_s) * 100,".-",
#     color=sns.color_palette("Paired")[3],
#     markersize=9,
#     label="%s: $D_{valley,%s}$/$D_{valley}$" % (sion,particle),
#     )
#     ax2.plot(z,
#     (zv_uparticle / zv_u) * 100,".-",
#     color=sns.color_palette("Paired")[1],
#     markersize=9,
#     label="%s: $D_{valley,%s}$/$D_{valley}$" % (uion,particle),
#     )
#     ax2.axvspan(60, 80, facecolor="yellow", alpha=0.3, label="Tumor region ")
#     ax1.axvspan(60, 80, facecolor="yellow", alpha=0.3, label="Tumor region ")
#     ax1.legend(title="", title_fontsize=18, fontsize=18, loc=3, markerscale=3)
#     ax1.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
#     ax1.tick_params(axis="x", which="major", labelsize=22)
#     ax1.tick_params(axis="y", which="major", labelsize=22)
#     ax1.set_xlabel("Depth z[mm]", fontsize=22)
#     ax1.set_ylabel("particle contribution[%] ", fontsize=22)
#     ax2.legend(title="", title_fontsize=18, fontsize=18, loc=3, markerscale=3)
#     ax2.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
#     ax2.tick_params(axis="x", which="major", labelsize=22)
#     ax2.tick_params(axis="y", which="major", labelsize=22)
#     ax2.set_xlabel("Depth z[mm]", fontsize=22)
#     # ax2.set_ylabel(" alpha contribution[%] ", fontsize=22)
#     return
#
#
# # plotparticlecontribution('electron',Es,Eu,sion,uion)
# # plotparticlecontribution('primaries',Es,Eu,sion,uion)
# # plotparticlecontribution('proton',Es,Eu,sion,uion)
# # plotparticlecontribution('alpha',Es,Eu,sion,uion)
#

# #
#
def plot(sion, uion, norm, log, electron, proton, positron):
    zp_s = np.load(directory1 + "zprofilepeak_" + sion + ".npy")
    zv_s = np.load(directory1 + "zprofilevalley_" + sion + ".npy")
    zp_u = np.load(directory2 + "zprofilepeak_" + uion + ".npy")
    zv_u = np.load(directory2 + "zprofilevalley_" + uion + ".npy")
    zp_sprimaries = np.load(directory1 + "zprofilepeak_" + sion + "_primaries.npy")
    zv_sprimaries = np.load(directory1 + "zprofilevalley_" + sion + "_primaries.npy")
    zp_uprimaries = np.load(directory2 + "zprofilepeak_" + uion + "_primaries.npy")
    zv_uprimaries = np.load(directory2 + "zprofilevalley_" + uion + "_primaries.npy")
    zp_salpha = np.load(directory1 + "zprofilepeak_" + sion + "_alpha.npy")
    zv_salpha = np.load(directory1 + "zprofilevalley_" + sion + "_alpha.npy")
    zp_ualpha = np.load(directory2 + "zprofilepeak_" + uion + "_alpha.npy")
    zv_ualpha = np.load(directory2 + "zprofilevalley_" + uion + "_alpha.npy")
    LETp_s = np.load(directory1 + "LETpeak_" + sion + ".npy")
    LETv_s = np.load(directory1 + "LETvalley_" + sion + ".npy")
    LETp_u = np.load(directory2 + "LETpeak_" + uion + ".npy")
    LETv_u = np.load(directory2 + "LETvalley_" + uion + ".npy")
    LETp_salpha = np.load(directory1 + "LETpeak_" + sion + "_alpha.npy")
    LETv_salpha = np.load(directory1 + "LETvalley_" + sion + "_alpha.npy")
    LETp_ualpha = np.load(directory2 + "LETpeak_" + uion + "_alpha.npy")
    LETv_ualpha = np.load(directory2 + "LETvalley_" + uion + "_alpha.npy")
    LETp_sprimaries = np.load(directory1 + "LETpeak_" + sion + "_primaries.npy")
    LETv_sprimaries = np.load(directory1 + "LETvalley_" + sion + "_primaries.npy")
    LETp_uprimaries = np.load(directory2 + "LETpeak_" + uion + "_primaries.npy")
    LETv_uprimaries = np.load(directory2 + "LETvalley_" + uion + "_primaries.npy")

#
    if norm == True:
        normp_s = 1 / zp_s.max()
        normp_u = 1 / zp_u.max()

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle("Depth dose profile GRT", fontsize=22)
    ax1.plot(
        z,
        zp_s * normp_s,
        ".-",
        color=sns.color_palette("Paired")[1],
        markersize=9,
        label="$D_{peak}$",
    )
    ax1.plot(
        z,
        zp_sprimaries * normp_s,
        ".-",
        color=sns.color_palette("Paired")[0],
        markersize=9,
        label="$D_{peak,primaries}$",
    )
    ax1.plot(
        z,
        zp_salpha * normp_s,
        ".-",
        color=sns.color_palette("Paired")[4],
        markersize=9,
        label="$D_{peak,alpha}$",
    )
    ax2.plot(
        z,
        zp_u * normp_u,
        ".-",
        color=sns.color_palette("Paired")[1],
        markersize=9,
        label="$D_{peak}$",
    )
    ax2.plot(
        z,
        zp_uprimaries * normp_u,
        ".-",
        color=sns.color_palette("Paired")[0],
        markersize=9,
        label=" $D_{peak,primaries}$",
    )
    ax2.plot(
        z,
        zp_ualpha * normp_u,
        ".-",
        color=sns.color_palette("Paired")[4],
        markersize=9,
        label=" $D_{peak,alpha}$",
    )
    ax3.plot(
        z,
        zv_s / zp_s.max(),
        ".-",
        color=sns.color_palette("Paired")[1],
        markersize=9,
        label="$D_{valley}$",
    )
    ax3.plot(
        z,
        zv_sprimaries * normp_s,
        ".-",
        color=sns.color_palette("Paired")[0],
        markersize=9,
        label="$D_{valley,primaries}$",
    )
    ax3.plot(
        z,
        zv_salpha * normp_s,
        ".-",
        color=sns.color_palette("Paired")[4],
        markersize=9,
        label="$D_{valley,alpha}$",
    )
    ax4.plot(
        z,
        zv_u * normp_u,
        ".-",
        color=sns.color_palette("Paired")[1],
        markersize=9,
        label="$D_{valley}$",
    )
    ax4.plot(
        z,
        zv_uprimaries * normp_u,
        ".-",
        color=sns.color_palette("Paired")[0],
        markersize=9,
        label=" $D_{valley,primaries}$",
    )
    ax4.plot(
        z,
        zv_ualpha * normp_u,
        ".-",
        color=sns.color_palette("Paired")[4],
        markersize=9,
        label=" $D_{valley,alpha}$",
    )

    if electron == True:
        zp_selectron = np.load(directory1 + "zprofilepeak_" + sion + "_electron.npy")
        zv_selectron = np.load(directory1 + "zprofilevalley_" + sion + "_electron.npy")
        zp_uelectron = np.load(directory2 + "zprofilepeak_" + uion + "_electron.npy")
        zv_uelectron = np.load(directory2 + "zprofilevalley_" + uion + "_electron.npy")
        ax1.plot(
            z,
            zp_selectron * normp_s,
            ".-",
            color=sns.color_palette("Paired")[9],
            markersize=9,
            label="$D_{peak,electron}$",
        )
        ax2.plot(
            z,
            zp_uelectron * normp_u,
            ".-",
            color=sns.color_palette("Paired")[9],
            markersize=9,
            label="$D_{peak,electron}$",
        )
        ax3.plot(
            z,
            zv_selectron * normp_s,
            ".-",
            color=sns.color_palette("Paired")[9],
            markersize=9,
            label="$D_{valley,electron}$",
        )
        ax4.plot(
            z,
            zv_uelectron * normp_u,
            ".-",
            color=sns.color_palette("Paired")[9],
            markersize=9,
            label="$D_{valley,electron}$",
        )
    if proton == True:
        zp_sproton = np.load(directory1 + "zprofilepeak_" + sion + "_proton.npy")
        zv_sproton = np.load(directory1 + "zprofilevalley_" + sion + "_proton.npy")
        zp_uproton = np.load(directory2 + "zprofilepeak_" + uion + "_proton.npy")
        zv_uproton = np.load(directory2 + "zprofilevalley_" + uion + "_proton.npy")
        ax2.plot(
            z,
            zp_uproton * normp_u,
            ".-",
            color=sns.color_palette("Paired")[7],
            markersize=9,
            label=" $D_{peak,proton}$",
        )
        ax1.plot(
            z,
            zp_sproton * normp_s,
            ".-",
            color=sns.color_palette("Paired")[7],
            markersize=9,
            label=" $D_{peak,proton}$",
        )
        ax3.plot(
            z,
            zv_uproton * normp_u,
            ".-",
            color=sns.color_palette("Paired")[7],
            markersize=9,
            label=" $D_{valley,proton}$",
        )
        ax4.plot(
            z,
            zv_sproton * normp_s,
            ".-",
            color=sns.color_palette("Paired")[7],
            markersize=9,
            label=" $D_{valley,proton}$",
        )
    if positron == True:
        zp_spositron = np.load(directory1 + "zprofilepeak_" + sion + "_positron.npy")
        zv_spositron = np.load(directory1 + "zprofilevalley_" + sion + "_positron.npy")
        zp_upositron = np.load(directory2 + "zprofilepeak_" + uion + "_positron.npy")
        zv_upositron = np.load(directory2 + "zprofilevalley_" + uion + "_positron.npy")
        ax1.plot(
            z,
            zp_spositron * normp_s,
            ".-",
            color=sns.color_palette("Paired")[10],
            markersize=9,
            label=" $D_{peak,positron}$",
        )
        ax2.plot(
            z,
            zp_upositron * normp_u,
            ".-",
            color=sns.color_palette("Paired")[10],
            markersize=9,
            label="$D_{peak,positron}$",
        )
        ax3.plot(
            z,
            zv_spositron * normp_s,
            ".-",
            color=sns.color_palette("Paired")[10],
            markersize=9,
            label=" $D_{valley,positron}$",
        )
        ax4.plot(
            z,
            zv_upositron * normp_u,
            ".-",
            color=sns.color_palette("Paired")[10],
            markersize=9,
            label="$D_{valley,positron}$",
        )
    if log == True:
        ax1.set_yscale("log")
        ax2.set_yscale("log")
        ax3.set_yscale("log")
        ax4.set_yscale("log")
        ax3.set_ylim([0, 1])
        ax4.set_ylim([0, 1])
    ax2.legend(
        title="%s: E=%sMeV/u" % (uion, Eu),
        title_fontsize=16,
        fontsize=16,
        loc=2,
        markerscale=3,
    )
    ax4.legend(
        title="%s: E=%sMeV/u" % (uion, Eu),
        title_fontsize=16,
        fontsize=16,
        loc=2,
        markerscale=3,
    )
    ax3.legend(
        title="%s: E=%sMeV/u" % (sion, Es),
        title_fontsize=16,
        fontsize=16,
        loc=2,
        markerscale=3,
    )
    ax1.legend(
        title="%s: E=%sMeV/u" % (sion, Es),
        title_fontsize=16,
        fontsize=16,
        loc=2,
        markerscale=3,
    )
    ax1.tick_params(axis="x", which="major", labelsize=18)
    ax1.tick_params(axis="y", which="major", labelsize=18)
    # ax1.set_xlabel("Depth z[mm]", fontsize=18)
    ax1.set_ylabel("Relative Dose ", fontsize=18)
    ax3.tick_params(axis="x", which="major", labelsize=18)
    ax3.tick_params(axis="y", which="major", labelsize=18)
    ax3.set_xlabel("Depth z[mm]", fontsize=18)
    ax3.set_ylabel("Relative Dose ", fontsize=18)
    ax1.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax2.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax3.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax4.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax4.tick_params(axis="x", which="major", labelsize=18)
    ax4.tick_params(axis="y", which="major", labelsize=18)
    ax2.tick_params(axis="x", which="major", labelsize=18)
    ax2.tick_params(axis="y", which="major", labelsize=18)
    ax4.set_xlabel("Depth z[mm]", fontsize=18)
    plt.show()

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle(
        "LET profile  GRT \n $E_{stable}=%s MeV/u, E_{unstable}=%s MeV/u $" % (Es, Eu),
        fontsize=22,
    )
    ax1.plot(
        z,
        LETp_s,
        ".-",
        color=sns.color_palette("Paired")[1],
        markersize=9,
        label="$LET_{peak}$",
    )
    ax1.plot(
        z,
        LETp_sprimaries,
        ".-",
        color=sns.color_palette("Paired")[0],
        markersize=9,
        label="$LET_{peak,primaries}$",
    )
    ax1.plot(
        z,
        LETp_salpha,
        ".-",
        color=sns.color_palette("Paired")[4],
        markersize=9,
        label="$LET_{peak,alpha}$",
    )
    ax2.plot(
        z,
        LETp_u,
        ".-",
        color=sns.color_palette("Paired")[1],
        markersize=9,
        label="$LET_{peak}$",
    )
    ax2.plot(
        z,
        LETp_uprimaries,
        ".-",
        color=sns.color_palette("Paired")[0],
        markersize=9,
        label=" $LET_{peak,primaries}$",
    )
    ax2.plot(
        z,
        LETp_ualpha,
        ".-",
        color=sns.color_palette("Paired")[4],
        markersize=9,
        label=" $LET_{peak,alpha}$",
    )
    ax3.plot(
        z,
        LETv_s,
        ".-",
        color=sns.color_palette("Paired")[1],
        markersize=9,
        label="$LET_{valley}$",
    )
    ax3.plot(
        z,
        LETv_sprimaries,
        ".-",
        color=sns.color_palette("Paired")[0],
        markersize=9,
        label="$LET_{valley,primaries}$",
    )
    ax3.plot(
        z,
        LETv_salpha,
        ".-",
        color=sns.color_palette("Paired")[4],
        markersize=9,
        label="$LET_{valley,alpha}$",
    )
    ax4.plot(
        z,
        LETv_u,
        ".-",
        color=sns.color_palette("Paired")[1],
        markersize=9,
        label="$LET_{valley}$",
    )
    ax4.plot(
        z,
        LETv_uprimaries,
        ".-",
        color=sns.color_palette("Paired")[0],
        markersize=9,
        label=" $LET_{valley,primaries}$",
    )
    ax4.plot(
        z,
        LETv_ualpha,
        ".-",
        color=sns.color_palette("Paired")[4],
        markersize=9,
        label=" $LET_{valley,alpha}$",
    )

    if electron == True:
        LETp_selectron = np.load(directory1 + "LETpeak_" + sion + "_electron.npy")
        LETv_selectron = np.load(directory1 + "LETvalley_" + sion + "_electron.npy")
        LETp_uelectron = np.load(directory2 + "LETpeak_" + uion + "_electron.npy")
        LETv_uelectron = np.load(directory2 + "LETvalley_" + uion + "_electron.npy")
        ax1.plot(
            z,
            LETp_selectron,
            ".-",
            color=sns.color_palette("Paired")[9],
            markersize=9,
            label="$LET_{peak,electron}$",
        )
        ax2.plot(
            z,
            LETp_uelectron,
            ".-",
            color=sns.color_palette("Paired")[9],
            markersize=9,
            label="$LET_{peak,electron}$",
        )
        ax3.plot(
            z,
            LETv_selectron,
            ".-",
            color=sns.color_palette("Paired")[9],
            markersize=9,
            label="$LET_{valley,electron}$",
        )
        ax4.plot(
            z,
            LETv_uelectron,
            ".-",
            color=sns.color_palette("Paired")[9],
            markersize=9,
            label="$LET_{valley,electron}$",
        )
    if proton == True:
        LETp_sproton = np.load(directory1 + "LETpeak_" + sion + "_proton.npy")
        LETv_sproton = np.load(directory1 + "LETvalley_" + sion + "_proton.npy")
        LETp_uproton = np.load(directory2 + "LETpeak_" + uion + "_proton.npy")
        LETv_uproton = np.load(directory2 + "LETvalley_" + uion + "_proton.npy")
        ax2.plot(
            z,
            LETp_uproton,
            ".-",
            color=sns.color_palette("Paired")[7],
            markersize=9,
            label=" $LET_{peak,proton}$",
        )
        ax1.plot(
            z,
            LETp_sproton,
            ".-",
            color=sns.color_palette("Paired")[7],
            markersize=9,
            label=" $LET_{peak,proton}$",
        )
        ax3.plot(
            z,
            LETv_uproton,
            ".-",
            color=sns.color_palette("Paired")[7],
            markersize=9,
            label=" $LET_{valley,proton}$",
        )
        ax4.plot(
            z,
            LETv_sproton,
            ".-",
            color=sns.color_palette("Paired")[7],
            markersize=9,
            label=" $LET_{valley,proton}$",
        )
    if positron == True:
        LETp_spositron = np.load(directory1 + "LETpeak_" + sion + "_positron.npy")
        LETv_spositron = np.load(directory1 + "LETvalley_" + sion + "_positron.npy")
        LETp_upositron = np.load(directory2 + "LETpeak_" + uion + "_positron.npy")
        LETv_upositron = np.load(directory2 + "LETvalley_" + uion + "_positron.npy")
        ax1.plot(
            z,
            LETp_spositron * normp_s,
            ".-",
            color=sns.color_palette("Paired")[10],
            markersize=9,
            label=" $LET_{peak,positron}$",
        )
        ax2.plot(
            z,
            LETp_upositron * normp_u,
            ".-",
            color=sns.color_palette("Paired")[10],
            markersize=9,
            label="$LET_{peak,positron}$",
        )
        ax3.plot(
            z,
            LETv_spositron * normp_s,
            ".-",
            color=sns.color_palette("Paired")[10],
            markersize=9,
            label=" $LET_{valley,positron}$",
        )
        ax4.plot(
            z,
            LETv_upositron,
            ".-",
            color=sns.color_palette("Paired")[10],
            markersize=9,
            label="$LET_{valley,positron}$",
        )

    ax2.legend(
        title="%s: E=%sMeV/u" % (uion, Eu),
        title_fontsize=16,
        fontsize=16,
        loc=2,
        markerscale=3,
    )
    ax4.legend(
        title="%s: E=%sMeV/u" % (uion, Eu),
        title_fontsize=16,
        fontsize=16,
        loc=2,   markerscale=3,
        )
    ax2.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax3.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax4.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax4.tick_params(axis="x", which="major", labelsize=18)
    ax4.tick_params(axis="y", which="major", labelsize=18)
    ax2.tick_params(axis="x", which="major", labelsize=18)
    ax2.tick_params(axis="y", which="major", labelsize=18)
    ax4.set_xlabel("Depth z[mm]", fontsize=18)
    ax3.legend(
        title="%s: E=%sMeV/u" % (sion, Es),
        title_fontsize=16,
        fontsize=16,
        loc=2,
        markerscale=3,
    )
    ax1.legend(
        title="%s: E=%sMeV/u" % (sion, Es),
        title_fontsize=16,
        fontsize=16,
        loc=2,
        markerscale=3,
    )
    ax1.set_xlabel("Depth z[mm]", fontsize=22)
    ax2.set_xlabel("Depth z[mm]", fontsize=22)
    ax1.set_ylabel(" LET [KeV/um]", fontsize=22)
    ax1.set_ylim([0, 230])
    ax2.set_ylim([0, 230])
    ax3.set_ylim([0, 230])
    ax4.set_ylim([0, 230])
    ax1.tick_params(axis="x", which="major", labelsize=18)
    ax1.tick_params(axis="y", which="major", labelsize=18)
    # ax1.set_xlabel("Depth z[mm]", fontsize=18)
    ax1.set_ylabel("Relative Dose ", fontsize=18)
    ax3.tick_params(axis="x", which="major", labelsize=18)
    ax3.tick_params(axis="y", which="major", labelsize=18)
    ax3.set_xlabel("Depth z[mm]", fontsize=18)
    ax3.set_ylabel("LET [KeV/um]", fontsize=18)
    ax1.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax2.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax3.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax4.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax4.tick_params(axis="x", which="major", labelsize=18)
    ax4.tick_params(axis="y", which="major", labelsize=18)
    ax2.tick_params(axis="x", which="major", labelsize=18)
    ax2.tick_params(axis="y", which="major", labelsize=18)
    ax4.set_xlabel("Depth z[mm]", fontsize=18)

    return
##############################################################################
##################PLOTS
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle(
    " Depth dose profile GRT :$E_{stable}$= %s MeV/u, $E_{unstable}$= %s MeV/u "
    % (Es, Eu),
    fontsize=24,
)
ax1.axvspan(60, 80, facecolor="yellow", alpha=0.3, label="Tumor region ")
ax2.axvspan(60, 80, facecolor="yellow", alpha=0.3, label="Tumor region ")
ax2plotfunction(
    directory2,
    ctc,
    "zprofile",
    "valley",
    uion,
    100,
    1,
    sns.color_palette("Paired")[1],
    True,
    False,
)
ax2plotfunction(
    directory1,
    ctc,
    "zprofile",
    "valley",
    sion,
    100,
    1,
    sns.color_palette("Paired")[2],
    True,
    False,
)
ax1plotfunction(
    directory2,ctc, "peak", uion, 100, 1, sns.color_palette("Paired")[1], True, False
)
ax1plotfunction(
    directory1,ctc, "peak", sion, 100, 1, sns.color_palette("Paired")[2], True, False
)
plt.show()

plot(sion, uion, norm=True, log=True, electron=True, proton=True, positron=True)

plt.show()


plt.figure()
zp_s = np.load(directory1 + "zprofilepeak_" + sion + ".npy")
zv_s = np.load(directory1 + "zprofilevalley_" + sion + ".npy")
zp_u = np.load(directory2 + "zprofilepeak_" + uion + ".npy")
zv_u = np.load(directory2 + "zprofilevalley_" + uion + ".npy")
plt.plot(
    z,
    zp_s / zv_s,
    ".",
    color=sns.color_palette("Paired")[2],
    markersize=9,
    label="%s: $D_{peak}$/$D_{valley}$" % (sion),
)
plt.plot(
    z,
    zp_u / zv_u,
    ".",
    color=sns.color_palette("Paired")[1],
    markersize=9,
    label="$%s:D_{peak}/D_{valley}$" % (uion),
)
plt.axvspan(60, 80, facecolor="yellow", alpha=0.3, label="Tumor region ")
plt.legend(
    title="bw= 600μm x 600 μm, ctc= 1800 μm ",
    title_fontsize=18,
    fontsize=18,
    loc=3,
    markerscale=3,
)
plt.title("Depth dose profile GRT", fontsize=24)
plt.yscale("log")
# plt.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
plt.tick_params(axis="x", which="major", labelsize=22)
plt.tick_params(axis="y", which="major", labelsize=22)
plt.xlabel("Depth z[mm]", fontsize=22)
plt.ylabel("PVDR", fontsize=22)

plt.show()
