import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# sion = input("Enter stable io name: ")
# Es = input("Enter its energy in Mev/u: ")
# n_s = input("Enter the numebr of simulated primaries: ")
# uion = input("Enter unstable isotope name: ")
# Eu = input("Enter its energy in Mev/u: ")
# n_u = input("Enter the numebr of simulated primaries: ")
# #
sion='Li7'
uion='Li8'
# sion='C12'
# uion='C9'
directory1 = "/home/angela/Desktop/SFRTGate/data/GDRT/ctc35/" + sion + "/"
directory2 = "/home/angela/Desktop/SFRTGate/data/GDRT/ctc35/" + uion + "/"
z=(np.arange(0, 100) *1)

def plotPDD( profile,bin_z, res_z,sion,uion,n_s,n_u,Es,Eu):
    zp_s = np.load(directory1 + profile+"peak_" + sion + ".npy")
    zv_s = np.load(directory1 + profile+"valley_" + sion + ".npy")
    zp_u = np.load(directory2 + profile+"peak_" + uion + ".npy")
    zv_u = np.load(directory2 + profile+"valley_" + uion + ".npy")

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle(
    " Depth dose profile GRT :$E_{stable}$= %s MeV/u, $E_{unstable}$= %s MeV/u "
    % (Es, Eu),
    fontsize=24,
    )
    ax1.plot(
        (np.arange(0, bin_z) * res_z),
        (zp_s/n_s)*(10**6),
        ".",
        color=sns.color_palette("Paired")[1],
        markersize=9,
        label="%s: $D_{peak}$"%(sion),
    )
    ax1.plot(
            (np.arange(0, bin_z) * res_z),
            (zp_u/n_u)*(10**6),
            ".",
            color=sns.color_palette("Paired")[2],
            markersize=9,
            label="%s: $D_{peak}$"%(uion),
    )

    ax2.plot(
        (np.arange(0, bin_z) * res_z),
        (zv_s/n_s)*(10**6),
        ".",
        color=sns.color_palette("Paired")[1],
        markersize=9,
        label="%s: $D_{valley}$"%(sion),
    )
    ax2.plot(
            (np.arange(0, bin_z) * res_z),
            (zv_u/n_u)*(10**6),
            ".",
            color=sns.color_palette("Paired")[2],
            markersize=9,
            label="%s: $D_{valley}$"%(uion),
    )
    ax1.legend(title= '', title_fontsize=18, fontsize=18, loc=3, markerscale=3)
    # plt.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax1.tick_params(axis="x", which="major", labelsize=22)
    ax1.tick_params(axis="y", which="major", labelsize=22)
    ax1.set_xlabel("Depth z[mm]", fontsize=22)
    ax1.set_ylabel("Dose/#primaries [uGy]", fontsize=22)
    ax2.legend(title='', title_fontsize=18, fontsize=18, loc=3, markerscale=3)
    ax2.tick_params(axis="x", which="major", labelsize=22)
    ax2.tick_params(axis="y", which="major", labelsize=22)
    ax2.set_xlabel("Depth z[mm]", fontsize=22)


def plot(profile,sion,uion,electron,proton,positron,n_s,n_u,Es,Eu):
    zp_s = np.load(directory1 + profile+"peak_" + sion + ".npy")
    zv_s = np.load(directory1 + profile +"valley_" + sion + ".npy")
    zp_u = np.load(directory2 + profile+"peak_" + uion + ".npy")
    zv_u = np.load(directory2 + profile+"valley_" + uion + ".npy")
    zp_sprimaries = np.load(directory1 + profile+"peak_" + sion + "_primaries.npy")
    zv_sprimaries = np.load(directory1 + profile+"valley_" + sion + "_primaries.npy")
    zp_uprimaries = np.load(directory2 + profile+"peak_" + uion + "_primaries.npy")
    zv_uprimaries = np.load(directory2 + profile+"valley_" + uion + "_primaries.npy")
    zp_salpha = np.load(directory1 + profile+"peak_" + sion + "_alpha.npy")
    zv_salpha = np.load(directory1 + profile+"valley_" + sion + "_alpha.npy")
    zp_ualpha = np.load(directory2 + profile+"peak_" + uion + "_alpha.npy")
    zv_ualpha = np.load(directory2 + profile+"valley_" + uion + "_alpha.npy")

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    if profile=="zprofile":
        fig.suptitle("Depth dose profile GRT", fontsize=22)

        ax1.plot(
        z,
        zp_s/n_s,
        ".-",
        color=sns.color_palette("Paired")[1],
        markersize=9,
        label="$D_{peak}$" ,
        )
        ax1.plot(
        z,
        zp_sprimaries/n_s,
        ".-",
        color=sns.color_palette("Paired")[0],
        markersize=9,
        label="$D_{peak,primaries}$" ,
        )
        ax1.plot(
        z,
        zp_salpha/n_s,
        ".-",
        color=sns.color_palette("Paired")[4],
        markersize=9,
        label="$D_{peak,alpha}$" ,
        )
        ax2.plot(
        z,
        zp_u/n_u,
        ".-",
        color=sns.color_palette("Paired")[1],
        markersize=9,
        label="$D_{peak}$" ,
        )
        ax2.plot(z,
        zp_uprimaries/n_u,".-",color=sns.color_palette("Paired")[0],
        markersize=9,
        label=" $D_{peak,primaries}$" ,
        )

        ax2.plot(z,zp_ualpha/93421652,".-",color=sns.color_palette("Paired")[4],
        markersize=9,
        label=" $D_{peak,alpha}$" ,
        )
        ax3.plot(
        z,
        zv_s/n_s,
        ".-",
        color=sns.color_palette("Paired")[1],
        markersize=9,
        label="$D_{valley}$" ,
        )
        ax3.plot(
        z,
        zv_sprimaries/n_s,
        ".-",
        color=sns.color_palette("Paired")[0],
        markersize=9,
        label="$D_{valley,primaries}$" ,
        )
        ax3.plot(
        z,
        zv_salpha/n_s,
        ".-",
        color=sns.color_palette("Paired")[4],
        markersize=9,
        label="$D_{valley,alpha}$" ,
        )
        ax4.plot(
        z,
        zv_u/n_u,
        ".-",
        color=sns.color_palette("Paired")[1],
        markersize=9,
        label="$D_{valley}$" ,
        )
        ax4.plot(z,
        zv_uprimaries/n_u,".-",color=sns.color_palette("Paired")[0],
        markersize=9,
        label=" $D_{valley,primaries}$" ,
        )

        ax4.plot(z,zv_ualpha/n_u,".-",color=sns.color_palette("Paired")[4],
        markersize=9,
        label=" $D_{valley,alpha}$" ,
        )
        ax3.set_ylabel(" Dose/#primaries [Gy] ", fontsize=18)
        ax1.set_ylabel(" Dose/#primaries [Gy] ", fontsize=18)
        if electron==True:
            zp_selectron=np.load(directory1+profile+'peak_'+sion+'_electron.npy')
            zv_selectron=np.load(directory1+profile+'valley_'+sion+'_electron.npy')
            zp_uelectron=np.load(directory2+profile+'peak_'+uion+'_electron.npy')
            zv_uelectron=np.load(directory2+profile+'valley_'+uion+'_electron.npy')
            ax1.plot(
            z,
            zp_selectron/n_s,
            ".-",
            color=sns.color_palette("Paired")[9],
            markersize=9,
            label="$D_{peak,electron}$" ,
            )
            ax2.plot(
                z,
                zp_uelectron/n_u,
                ".-",
                color=sns.color_palette("Paired")[9],
                markersize=9,
                label="$D_{peak,electron}$" ,
                )
            ax3.plot(
                z,
                zv_selectron/n_s,
                ".-",
                color=sns.color_palette("Paired")[9],
                markersize=9,
                label="$D_{valley,electron}$" ,
            )
            ax4.plot(
                z,
                zv_uelectron/n_u,
                ".-",
                color=sns.color_palette("Paired")[9],
                markersize=9,
                label="$D_{valley,electron}$" ,
                )

        if proton==True:
            zp_sproton=np.load(directory1+profile+'peak_'+sion+'_proton.npy')
            zv_sproton=np.load(directory1+profile+'valley_'+sion+'_proton.npy')
            zp_uproton=np.load(directory2+profile+'peak_'+uion+'_proton.npy')
            zv_uproton=np.load(directory2+profile+'valley_'+uion+'_proton.npy')
            ax2.plot(
            z,
            zp_uproton/n_u,
            ".-",
            color=sns.color_palette("Paired")[7],
            markersize=9,
            label=" $D_{peak,proton}$" ,
            )
            ax1.plot(
            z,
            zp_sproton/n_s,
            ".-",
            color=sns.color_palette("Paired")[7],
            markersize=9,
            label=" $D_{peak,proton}$" ,
            )
            ax3.plot(
            z,
            zv_uproton/n_u,
            ".-",
            color=sns.color_palette("Paired")[7],
            markersize=9,
            label=" $D_{valley,proton}$" ,
            )
            ax4.plot(
            z,
            zv_sproton/n_s,
            ".-",
            color=sns.color_palette("Paired")[7],
            markersize=9,
            label=" $D_{valley,proton}$" ,
            )
        if positron==True:
            zp_spositron=np.load(directory1+profile+'peak_'+sion+'_positron.npy')
            zv_spositron=np.load(directory1+profile+'valley_'+sion+'_positron.npy')
            zp_upositron=np.load(directory2+profile+'peak_'+uion+'_positron.npy')
            zv_upositron=np.load(directory2+profile+'valley_'+uion+'_positron.npy')
            ax1.plot(
            z,
            zp_spositron/n_s,
            ".-",
            color=sns.color_palette("Paired")[10],
            markersize=9,
            label=" $D_{peak,positron}$" ,
            )
            ax2.plot(
            z,
            zp_upositron/n_u,
            ".-",
            color=sns.color_palette("Paired")[10],
            markersize=9,
            label="$D_{peak,positron}$" ,
            )
            ax3.plot(
            z,
            zv_spositron/n_s,
            ".-",
            color=sns.color_palette("Paired")[10],
            markersize=9,
            label=" $D_{valley,positron}$" ,
            )
            ax4.plot(
            z,
            zv_upositron/n_u,
            ".-",
            color=sns.color_palette("Paired")[10],
            markersize=9,
            label="$D_{valley,positron}$" ,
            )

    if profile=="LET":
        fig.suptitle("LET depth profile GRT", fontsize=22)
        ax1.plot(
        z,
        zp_s/n_s,
        ".-",
        color=sns.color_palette("Paired")[1],
        markersize=9,
        label="$LET_{peak}$" ,
        )
        ax1.plot(
        z,
        zp_sprimaries/n_s,
        ".-",
        color=sns.color_palette("Paired")[0],
        markersize=9,
        label="$LET_{peak,primaries}$" ,
        )
        ax1.plot(
        z,
        zp_salpha/n_s,
        ".-",
        color=sns.color_palette("Paired")[4],
        markersize=9,
        label="$LET_{peak,alpha}$" ,
        )
        ax2.plot(
        z,
        zp_u/n_u,
        ".-",
        color=sns.color_palette("Paired")[1],
        markersize=9,
        label="$LET_{peak}$" ,
        )
        ax2.plot(z,
        zp_uprimaries/n_u,".-",color=sns.color_palette("Paired")[0],
        markersize=9,
        label=" $LET_{peak,primaries}$" ,
        )

        ax2.plot(z,zp_ualpha/93421652,".-",color=sns.color_palette("Paired")[4],
        markersize=9,
        label=" $LET_{peak,alpha}$" ,
        )
        ax3.plot(
        z,
        zv_s/n_s,
        ".-",
        color=sns.color_palette("Paired")[1],
        markersize=9,
        label="$LET_{valley}$" ,
        )
        ax3.plot(
        z,
        zv_sprimaries/n_s,
        ".-",
        color=sns.color_palette("Paired")[0],
        markersize=9,
        label="$LET_{valley,primaries}$" ,
        )
        ax3.plot(
        z,
        zv_salpha/n_s,
        ".-",
        color=sns.color_palette("Paired")[4],
        markersize=9,
        label="$LET_{valley,alpha}$" ,
        )
        ax4.plot(
        z,
        zv_u/n_u,
        ".-",
        color=sns.color_palette("Paired")[1],
        markersize=9,
        label="$LET_{valley}$" ,
        )
        ax4.plot(z,
        zv_uprimaries/n_u,".-",color=sns.color_palette("Paired")[0],
        markersize=9,
        label=" $LET_{valley,primaries}$" ,
        )

        ax4.plot(z,zv_ualpha/n_u,".-",color=sns.color_palette("Paired")[4],
        markersize=9,
        label=" $LET_{valley,alpha}$" ,
        )
        ax3.set_ylabel(" LET/#primaries [KeV/um] ", fontsize=18)
        ax1.set_ylabel(" LET/#primaries [KeV/um] ", fontsize=18)
        if electron==True:
            zp_selectron=np.load(directory1+profile+'peak_'+sion+'_electron.npy')
            zv_selectron=np.load(directory1+profile+'valley_'+sion+'_electron.npy')
            zp_uelectron=np.load(directory2+profile+'peak_'+uion+'_electron.npy')
            zv_uelectron=np.load(directory2+profile+'valley_'+uion+'_electron.npy')
            ax1.plot(
            z,
            zp_selectron/n_s,
            ".-",
            color=sns.color_palette("Paired")[9],
            markersize=9,
            label="$LET_{peak,electron}$" ,
            )
            ax2.plot(
                z,
                zp_uelectron/n_u,
                ".-",
                color=sns.color_palette("Paired")[9],
                markersize=9,
                label="$LET_{peak,electron}$" ,
                )
            ax3.plot(
                z,
                zv_selectron/n_s,
                ".-",
                color=sns.color_palette("Paired")[9],
                markersize=9,
                label="$LET_{valley,electron}$" ,
            )
            ax4.plot(
                z,
                zv_uelectron/n_u,
                ".-",
                color=sns.color_palette("Paired")[9],
                markersize=9,
                label="$LET_{valley,electron}$" ,
                )
        if proton==True:
            zp_sproton=np.load(directory1+profile+'peak_'+sion+'_proton.npy')
            zv_sproton=np.load(directory1+profile+'valley_'+sion+'_proton.npy')
            zp_uproton=np.load(directory2+profile+'peak_'+uion+'_proton.npy')
            zv_uproton=np.load(directory2+profile+'valley_'+uion+'_proton.npy')
            ax2.plot(
            z,
            zp_uproton/n_u,
            ".-",
            color=sns.color_palette("Paired")[7],
            markersize=9,
            label=" $LET_{peak,proton}$" ,
            )
            ax1.plot(
            z,
            zp_sproton/n_s,
            ".-",
            color=sns.color_palette("Paired")[7],
            markersize=9,
            label=" $LET_{peak,proton}$" ,
            )
            ax3.plot(
            z,
            zv_uproton/n_u,
            ".-",
            color=sns.color_palette("Paired")[7],
            markersize=9,
            label=" $LET_{valley,proton}$" ,
            )
            ax4.plot(
            z,
            zv_sproton/n_s,
            ".-",
            color=sns.color_palette("Paired")[7],
            markersize=9,
            label=" $LET_{valley,proton}$" ,
            )
        if positron==True:
            zp_spositron=np.load(directory1+profile+'peak_'+sion+'_positron.npy')
            zv_spositron=np.load(directory1+profile+'valley_'+sion+'_positron.npy')
            zp_upositron=np.load(directory2+profile+'peak_'+uion+'_positron.npy')
            zv_upositron=np.load(directory2+profile+'valley_'+uion+'_positron.npy')
            ax1.plot(
            z,
            zp_spositron/n_s,
            ".-",
            color=sns.color_palette("Paired")[10],
            markersize=9,
            label=" $LET_{peak,positron}$" ,
            )
            ax2.plot(
            z,
            zp_upositron/n_u,
            ".-",
            color=sns.color_palette("Paired")[10],
            markersize=9,
            label="$LET_{peak,positron}$" ,
            )
            ax3.plot(
            z,
            zv_spositron/n_s,
            ".-",
            color=sns.color_palette("Paired")[10],
            markersize=9,
            label=" $LET_{valley,positron}$" ,
            )
            ax4.plot(
            z,
            zv_upositron/n_u,
            ".-",
            color=sns.color_palette("Paired")[10],
            markersize=9,
            label="$LET_{valley,positron}$" ,
            )











    ax2.legend(title="%s: E=%sMeV/u" % (uion,Eu),title_fontsize=16,
            fontsize=16,loc=2,
            markerscale=3,)
    ax4.legend(title="%s: E=%sMeV/u" % (uion,Eu),title_fontsize=16,fontsize=16,
            loc=2,
            markerscale=3,)
    ax3.legend(title="%s: E=%sMeV/u" % (sion,Es),title_fontsize=16,fontsize=16,
            loc=2,
            markerscale=3,)

    ax1.legend(title="%s: E=%sMeV/u" % (sion,Es),title_fontsize=16,fontsize=16,
            loc=2,
            markerscale=3,)
    ax1.tick_params(axis="x", which="major", labelsize=18)
    ax1.tick_params(axis="y", which="major", labelsize=18)
    #ax1.set_xlabel("Depth z[mm]", fontsize=18)
    ax3.tick_params(axis="x", which="major", labelsize=18)
    ax3.tick_params(axis="y", which="major", labelsize=18)
    ax3.set_xlabel("Depth z[mm]", fontsize=18)

    # plt.yscale('log')
    # plt.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax4.tick_params(axis="x", which="major", labelsize=18)
    ax4.tick_params(axis="y", which="major", labelsize=18)
    ax2.tick_params(axis="x", which="major", labelsize=18)
    ax2.tick_params(axis="y", which="major", labelsize=18)
    ax4.set_xlabel("Depth z[mm]", fontsize=18)
    #ax2.set_ylabel("Relative Dose ", fontsize=18)
    return
###########################################################################











#
# plotPDD("zprofile",100,1,'C12','C9',93331032,93464832,'190','222')
# plot("zprofile",sion,uion,True,True,True,93331032,93464832,'190','222')
#
# plot("LET",sion,uion,False,True,True,93661784,93700632,'190','222')


# plotPDD("zprofile",100,1,'Li7','Li8',93742558,93413065,'115','107')
plot("zprofile",sion,uion,True,False,True,93742558,93413065,'115','107')
plot("LET",sion,uion,False,False,False, 93857352,93764280,'115','107')

plt.show()
