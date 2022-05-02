import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

sion = input("Enter stable io name: ")
Es = input("Enter its energy in Mev/u: ")
uion = input("Enter unstable isotope name: ")
Eu = input("Enter its energy in Mev/u: ")

directory1 = "/home/angela/Desktop/SFRTGate/data/GDRT/ctc35/" + sion + "/"
directory2 = "/home/angela/Desktop/SFRTGate/data/GDRT/ctc35/" + uion + "/"

zp_s = np.load(directory1 + "zprofilepeak_" + sion + ".npy")
zv_s = np.load(directory1 + "zprofilevalley_" + sion + ".npy")
zp_sprimaries = np.load(directory1 + "zprofilepeak_" + sion + "primaries.npy")
zv_sprimaries = np.load(directory1 + "zprofilevalley_" + sion + "primaries.npy")
zp_salpha = np.load(directory1 + "zprofilepeak_" + sion + "alpha.npy")
zv_salpha = np.load(directory1 + "zprofilevalley_" + sion + "alpha.npy")
zp_LET_s = np.load(directory1 + "LETvalley_" + sion+".npy")

# zp_spositron=np.load(directory1+'zprofilepeak_'+sion+'positron.npy')
# zv_spositron=np.load(directory1+'zprofilevalley_'+sion+'positron.npy')

zp_u = np.load(directory2 + "zprofilepeak_" + uion + ".npy")
zv_u = np.load(directory2 + "zprofilevalley_" + uion + ".npy")
zp_uprimaries = np.load(directory2 + "zprofilepeak_" + uion + "primaries.npy")
zv_uprimaries = np.load(directory2 + "zprofilevalley_" + uion + "primaries.npy")
zp_ualpha = np.load(directory2 + "zprofilepeak_" + uion + "alpha.npy")
zv_ualpha = np.load(directory2 + "zprofilevalley_" + uion + "alpha.npy")
# zp_upositron=np.load(directory2+'zprofilepeak_'+uion+'positron.npy')
# zv_upositron=np.load(directory2+'zprofilevalley_'+uion+'positron.npy')
zp_LET_u = np.load(directory2 + "LETpeak_" + uion + ".npy")
zv_LET_u = np.load(directory2 + "LETvalley_" + uion + ".npy")

##############################################################################
#Data  normalization
# zp_u=zp_u/zp_u.max()
# zp_uparticle=zp_uparticle/zp_u.max()
# zp_ualpha=zp_ualpha/zp_u.max()
# zp_uproton=zp_uproton/zp_u.max()
# zp_uelectron=zp_uelectron/zp_u.max()
# zp_LET_u=zp_LET_u/zp_LET_u.max()
#
# zv_u=zv_u/zv_u.max()
# zv_uparticle=zv_uparticle/zv_u.max()
# zv_ualpha=zv_ualpha/zv_u.max()
# zv_uproton=zv_uproton/zv_u.max()
# zv_uelectron=zv_u/zv_uelectron.max()
# zv_LET_u=zv_LET_u/zv_LET_u.max()
#
#
# zp_s=zp_s/zp_s.max()
# zp_sparticle=zp_sparticle/zp_s.max()
# zp_salpha=zp_salpha/zp_s.max()
# # zp_sproton=zp_sproton/zp_s.max()
# # zp_selectron=zp_selectron/zp_s.max()
# zp_LET_s=zp_LET_s/zp_LET_s.max()
#
# zv_s=zv_s/zv_s.max()
# zv_sparticle=zv_sparticle/zv_s.max()
# zv_salpha=zv_salpha/zv_s.max()
# zv_sproton=zv_sproton/zv_s.max()
# zv_selectron=zv_selectron/zv_s.max()
# zv_LET_s=zv_LET_s/zv_LET_s.max()
###############################################################################
norm_u_GDRT = 1 / zp_u.max()
norm_s_GDRT = 1 / zp_s.max()

norm_uLET_GDRT = 1 / zp_LET_u.max()
norm_sLET_GDRT = 1 / zp_LET_s.max()

#################################################################################

#z=(np.arange(0, nz) * res_z)
z=(np.arange(0, 100) *1)


def plotfunction(directory, filename, nz, res_z, norm, color):
    z = np.load(directory + filename)
    zone, ion = filename.split("_")
    ion, _ = ion.split(".npy")
    _, zone = zone.split("zprofile")

    plt.plot(
        (np.arange(0, nz) * res_z),
        z * norm,
        ".",
        color=color,
        markersize=10,
        label="D,{},{}".format(zone, ion),
    )

def ax1plotfunction(directory, prefix,ion, nz, res_z, color,norm):
    profile=np.load(directory + prefix + ion + ".npy")
    _,zone=prefix.split('zprofile')
    zone,_=zone.split('_')
    if norm== True:
        profile=profile/profile.max()
    ax1.plot(
        (np.arange(0, nz) * res_z),
        profile,
        ".",
        color=color,
        markersize=10,
        label="%s: $D_{%s}$"%(ion,zone),
    )
    ax1.legend(title="{}".format(zone), title_fontsize=18, fontsize=18, loc=3, markerscale=3)
    # plt.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax1.tick_params(axis="x", which="major", labelsize=22)
    ax1.tick_params(axis="y", which="major", labelsize=22)
    ax1.set_xlabel("Depth z[mm]", fontsize=22)
    ax1.set_ylabel("Relative Dose", fontsize=22)

def ax2plotfunction(directory, prefix,ion, nz, res_z, color, norm):
    profile=np.load(directory + prefix + ion + ".npy")
    _,zone=prefix.split('zprofile')
    zone,_=zone.split('_')
    if norm== True:
        profile=profile/profile.max()
    ax2.plot(
        (np.arange(0, nz) * res_z),
        profile,
        ".",
        color=color,
        markersize=10,
        label="%s: $D_{%s}$"%(ion,zone),
    )
    ax2.legend(title="{}".format(zone), title_fontsize=18, fontsize=18, loc=3, markerscale=3)
    ax2.tick_params(axis="x", which="major", labelsize=22)
    ax2.tick_params(axis="y", which="major", labelsize=22)
    ax2.set_xlabel("Depth z[mm]", fontsize=22)


###############################################################################
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle(
    " Depth dose profile GRT :$E_{stable}$= %s MeV/u, $E_{unstable}$= %s MeV/u "
    % (Es, Eu),
    fontsize=24,
)
ax1.axvspan(60, 80, facecolor="yellow", alpha=0.3, label="Tumor region ")
ax2.axvspan(60, 80, facecolor="yellow", alpha=0.3, label="Tumor region ")
ax2plotfunction(directory2,"zprofilevalley_",uion,100,1,sns.color_palette("Paired")[1],True)
ax2plotfunction(directory1,"zprofilevalley_",sion,100,1,sns.color_palette("Paired")[2],True)
ax1plotfunction(directory2,"zprofilepeak_",uion,100,1,sns.color_palette("Paired")[1],True)
ax1plotfunction(directory1,"zprofilepeak_",sion,100,1,sns.color_palette("Paired")[2],True)
plt.show()



def plotparticlecontribution(particle,Es,Eu,sion,uion):
    zp_s = np.load(directory1 + "zprofilepeak_" + sion + ".npy")
    zv_s = np.load(directory1 + "zprofilevalley_" + sion + ".npy")
    zp_u = np.load(directory2 + "zprofilepeak_" + uion + ".npy")
    zv_u = np.load(directory2 + "zprofilevalley_" + uion + ".npy")
    zp_sparticle = np.load(directory1 + "zprofilepeak_" + sion + particle+".npy")
    zv_sparticle = np.load(directory1 + "zprofilevalley_" + sion + particle+".npy")
    zp_uparticle = np.load(directory2 + "zprofilepeak_" + uion + particle+".npy")
    zv_uparticle = np.load(directory2 + "zprofilevalley_" + uion + particle+".npy")

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle(
    "DDP GRT: %s contribution \n $E_{stable}=%s MeV/u, E_{unstable}=%s MeV/u $"
    % (particle,Es, Eu),
    fontsize=22,
    )

    ax1.plot(z,
    (zp_sparticle / zp_s) * 100,".-",
    color=sns.color_palette("Paired")[3],
    markersize=10,
    label="%s: $D_{peak,%s}$/$D_{peak}$" % (sion,particle),
    )
    ax1.plot(z,
    (zp_uparticle / zp_u) * 100,".-",
    color=sns.color_palette("Paired")[1],
    markersize=10,
    label="%s: $D_{peak,%s}$/$D_{peak}$" % (uion,particle),
    )

    ax2.plot(z,
    (zv_sparticle / zv_s) * 100,".-",
    color=sns.color_palette("Paired")[3],
    markersize=10,
    label="%s: $D_{valley,particle}$/$D_{valley}$" % (sion),
    )
    ax2.plot(z,
    (zv_uparticle / zv_u) * 100,".-",
    color=sns.color_palette("Paired")[1],
    markersize=10,
    label="%s: $D_{valley,particle}$/$D_{valley}$" % (uion),
    )
    ax2.axvspan(60, 80, facecolor="yellow", alpha=0.3, label="Tumor region ")
    ax1.axvspan(60, 80, facecolor="yellow", alpha=0.3, label="Tumor region ")

    ax1.legend(title="", title_fontsize=18, fontsize=18, loc=3, markerscale=3)
    ax1.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax1.tick_params(axis="x", which="major", labelsize=22)
    ax1.tick_params(axis="y", which="major", labelsize=22)

    ax1.set_xlabel("Depth z[mm]", fontsize=22)
    ax1.set_ylabel("particle contribution[%] ", fontsize=22)
    ax2.legend(title="", title_fontsize=18, fontsize=18, loc=3, markerscale=3)
    ax2.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    # ax4.set_yscale('log')
    ax2.tick_params(axis="x", which="major", labelsize=22)
    ax2.tick_params(axis="y", which="major", labelsize=22)
    ax2.set_xlabel("Depth z[mm]", fontsize=22)
    # ax2.set_ylabel(" alpha contribution[%] ", fontsize=22)
    return


plotparticlecontribution('alpha',Es,Eu,sion,uion)
plotparticlecontribution('primaries',Es,Eu,sion,uion)
plotparticlecontribution('electron',Es,Eu,sion,uion)

plt.figure(4)
plt.plot(
    z,
    zp_s / zv_s,
    ".",
    color=sns.color_palette("Paired")[2],
    markersize=10,
    label="%s: $D_{peak}$/$D_{valley}$" % (sion),
)
plt.plot(
    z,
    zp_u / zv_u,
    ".",
    color=sns.color_palette("Paired")[1],
    markersize=10,
    label="$%s:D_{peak}/D_{valley}$" % (uion),
)


plt.axvspan(60, 80, facecolor="yellow", alpha=0.3, label="Tumor region ")
plt.legend(
    title="bw= 600μm x 600 μm, ctc= 3500 μm ",
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






def plot(sion,uion,electron,proton):
    zp_s = np.load(directory1 + "zprofilepeak_" + sion + ".npy")
    zv_s = np.load(directory1 + "zprofilevalley_" + sion + ".npy")
    zp_u = np.load(directory2 + "zprofilepeak_" + uion + ".npy")
    zv_u = np.load(directory2 + "zprofilevalley_" + uion + ".npy")
    zp_sprimaries = np.load(directory1 + "zprofilepeak_" + sion + "primaries.npy")
    zv_sprimaries = np.load(directory1 + "zprofilevalley_" + sion + "primaries.npy")
    zp_uprimaries = np.load(directory2 + "zprofilepeak_" + uion + "primaries.npy")
    zv_uprimaries = np.load(directory2 + "zprofilevalley_" + uion + "primaries.npy")
    zp_salpha = np.load(directory1 + "zprofilepeak_" + sion + "alpha.npy")
    zv_salpha = np.load(directory1 + "zprofilevalley_" + sion + "alpha.npy")
    zp_ualpha = np.load(directory2 + "zprofilepeak_" + uion + "alpha.npy")
    zv_ualpha = np.load(directory2 + "zprofilevalley_" + uion + "alpha.npy")

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle("Depth dose profile GRT", fontsize=22)
    ax1.plot(
    z,
    zp_s/zp_s.max(),
    ".-",
    color=sns.color_palette("Paired")[1],
    markersize=10,
    label="$D_{peak}$" ,
    )
    ax1.plot(
    z,
    zp_sprimaries/zp_s.max(),
    ".-",
    color=sns.color_palette("Paired")[0],
    markersize=10,
    label="$D_{peak,primaries}$" ,
    )
    ax1.plot(
    z,
    zp_salpha/zp_s.max(),
    ".-",
    color=sns.color_palette("Paired")[4],
    markersize=10,
    label="$D_{peak,alpha}$" ,
    )
    ax2.plot(
        z,
        zp_u/zp_u.max(),
        ".-",
        color=sns.color_palette("Paired")[1],
        markersize=10,
        label="$D_{peak}$" ,
        )
    ax2.plot(z,
        zp_uprimaries/zp_u.max(),".-",color=sns.color_palette("Paired")[0],
        markersize=10,
        label=" $D_{peak,primaries}$" ,
        )

    ax2.plot(z,zp_ualpha/zp_u.max(),".-",color=sns.color_palette("Paired")[4],
        markersize=10,
        label=" $D_{peak,alpha}$" ,
        )
    ax3.plot(
    z,
    zv_s/zv_s.max(),
    ".-",
    color=sns.color_palette("Paired")[1],
    markersize=10,
    label="$D_{valley}$" ,
    )
    ax3.plot(
    z,
    zv_sprimaries/zv_s.max(),
    ".-",
    color=sns.color_palette("Paired")[0],
    markersize=10,
    label="$D_{valley,primaries}$" ,
    )
    ax3.plot(
    z,
    zv_salpha/zv_s.max(),
    ".-",
    color=sns.color_palette("Paired")[4],
    markersize=10,
    label="$D_{valley,alpha}$" ,
    )
    ax4.plot(
        z,
        zv_u/zv_u.max(),
        ".-",
        color=sns.color_palette("Paired")[1],
        markersize=10,
        label="$D_{valley}$" ,
        )
    ax4.plot(z,
        zv_uprimaries/zv_u.max(),".-",color=sns.color_palette("Paired")[0],
        markersize=10,
        label=" $D_{valley,primaries}$" ,
        )

    ax4.plot(z,zv_ualpha/zv_u.max(),".-",color=sns.color_palette("Paired")[4],
        markersize=10,
        label=" $D_{valley,alpha}$" ,
        )

    if electron==True:
        zp_selectron=np.load(directory1+'zprofilepeak_'+sion+'electron.npy')
        zv_selectron=np.load(directory1+'zprofilevalley_'+sion+'electron.npy')
        zp_uelectron=np.load(directory2+'zprofilepeak_'+uion+'electron.npy')
        zv_uelectron=np.load(directory2+'zprofilevalley_'+uion+'electron.npy')
        ax1.plot(
            z,
            zp_selectron/zp_s.max(),
            ".-",
            color=sns.color_palette("Paired")[9],
            markersize=10,
            label="$D_{peak,electron}$" ,
            )
        ax2.plot(
                z,
                zp_uelectron/zp_u.max(),
                ".-",
                color=sns.color_palette("Paired")[9],
                markersize=10,
                label="$D_{peak,electron}$" ,
                )
        ax3.plot(
            z,
            zv_selectron/zv_s.max(),
            ".-",
            color=sns.color_palette("Paired")[9],
            markersize=10,
            label="$D_{valley,electron}$" ,
            )
        ax4.plot(
                z,
                zv_uelectron/zv_u.max(),
                ".-",
                color=sns.color_palette("Paired")[9],
                markersize=10,
                label="$D_{valley,electron}$" ,
                )
    elif proton==True:
        zp_sproton=np.load(directory1+'zprofilepeak_'+sion+'proton.npy')
        zv_sproton=np.load(directory1+'zprofilevalley_'+sion+'proton.npy')
        zp_uproton=np.load(directory2+'zprofilepeak_'+uion+'proton.npy')
        zv_uproton=np.load(directory2+'zprofilevalley_'+uion+'proton.npy')
        ax2.plot(
            z,
            zp_uproton/zp_u.max(),
            ".-",
            color=sns.color_palette("Paired")[7],
            markersize=10,
            label=" $D_{peak,proton}$" ,
            )
        ax1.plot(
            z,
            zp_sproton/zp_s.max(),
            ".-",
            color=sns.color_palette("Paired")[7],
            markersize=10,
            label=" $D_{peak,proton}$" ,
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
    ax1.set_ylabel("Relative Dose ", fontsize=18)
    ax3.tick_params(axis="x", which="major", labelsize=18)
    ax3.tick_params(axis="y", which="major", labelsize=18)
    ax3.set_xlabel("Depth z[mm]", fontsize=18)
    ax3.set_ylabel("Relative Dose ", fontsize=18)
    # plt.yscale('log')
    # plt.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax4.tick_params(axis="x", which="major", labelsize=18)
    ax4.tick_params(axis="y", which="major", labelsize=18)
    ax2.tick_params(axis="x", which="major", labelsize=18)
    ax2.tick_params(axis="y", which="major", labelsize=18)
    ax4.set_xlabel("Depth z[mm]", fontsize=18)
    #ax2.set_ylabel("Relative Dose ", fontsize=18)
    return















#
# ax1.plot(
#     z,
#     zp_spositron/zp_s.max(),
#     ".-",
#     color=sns.color_palette("Paired")[9],
#     markersize=10,
#     label=" $D_{peak,positron}$" ,
#     )






# ax2.plot(
#     z,
#     zp_upositron/zp_u.max(),
#     ".-",
#     color=sns.color_palette("Paired")[9],
#     markersize=10,
#     label="$D_{peak,positron}$" ,
#     )
plot(sion,uion,True,False)
plt.show()
######################################################################
#LET PLOT plotfunction
def ax1plotLET(directory, prefix,ion,suffix, nz, res_z, color,norm):
    if suffix==None:
        profile=np.load(directory + prefix + ion +".npy")
        _,zone=prefix.split('LET')
        zone,_=zone.split('_')
        if norm== True:
            profile=profile/profile.max()
        ax1.plot(
            (np.arange(0, nz) * res_z),
            profile,
            ".",
            color=color,
            markersize=10,
            label="$LET_{%s}$"%(zone),
        )
    else:
        profile=np.load(directory + prefix + ion +'_'+suffix+".npy")
        _,zone=prefix.split('LET')
        zone,_=zone.split('_')
        if norm== True:
            profile=profile/profile.max()
        ax1.plot(
            (np.arange(0, nz) * res_z),
            profile,
            ".",
            color=color,
            markersize=10,
            label="%s: $LET_{%s}$"%(suffix,zone),
        )

    ax1.legend(title="%s"%(ion), title_fontsize=18, fontsize=18, loc=3, markerscale=3)
    ax1.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax1.tick_params(axis="x", which="major", labelsize=22)
    ax1.tick_params(axis="y", which="major", labelsize=22)

def ax2plotLET(directory, prefix,ion,suffix, nz, res_z, color,norm):
    if suffix==None:
        profile=np.load(directory + prefix + ion +".npy")
        _,zone=prefix.split('LET')
        zone,_=zone.split('_')
        if norm== True:
            profile=profile/profile.max()
        ax2.plot(
            (np.arange(0, nz) * res_z),
            profile,
            ".",
            color=color,
            markersize=10,
            label=" $LET_{%s}$"%(zone),
        )
    else:
        profile=np.load(directory + prefix + ion +'_'+ suffix+".npy")
        _,zone=prefix.split('LET')
        zone,_=zone.split('_')
        print(type(suffix))
        if norm== True:
            profile=profile/profile.max()
        ax2.plot(
            (np.arange(0, nz) * res_z),
            profile,
            ".",
            color=color,
            markersize=10,
            label="%s: $LET_{%s}$"%(suffix,zone),
        )

    ax2.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
    ax2.legend(title="{}".format(ion), title_fontsize=18, fontsize=18, loc=3, markerscale=3)
    ax2.tick_params(axis="x", which="major", labelsize=22)
    ax2.tick_params(axis="y", which="major", labelsize=22)

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("LET profile  GRT \n $E_{stable}=%s MeV/u, E_{unstable}=%s MeV/u $"% (Es, Eu),
fontsize=22,
)
ax1plotLET(directory1, "LETpeak_" ,sion ,'primaries',100,1,sns.color_palette("Paired")[0],False)
ax1plotLET(directory1, "LETpeak_" ,sion ,None,100,1,sns.color_palette("Paired")[1],False)
#ax1plotLET(directory1, "LETpeak_" ,sion ,"alpha",100,1,sns.color_palette("Paired")[4],False)
ax1plotLET(directory1, "LETpeak_" ,sion ,"proton",100,1,sns.color_palette("Paired")[5],False)


ax2plotLET(directory2, "LETpeak_" ,uion ,'primaries',100,1,sns.color_palette("Paired")[2],False)
ax2plotLET(directory2, "LETpeak_" ,uion ,None,100,1,sns.color_palette("Paired")[3],False)
#ax2plotLET(directory2, "LETpeak_" ,uion ,'alpha',100,1,sns.color_palette("Paired")[6],False)
ax2plotLET(directory2, "LETpeak_" ,uion ,'proton',100,1,sns.color_palette("Paired")[7],False)

ax1.set_xlabel("Depth z[mm]", fontsize=22)
ax2.set_xlabel("Depth z[mm]", fontsize=22)
ax1.set_ylabel(" LET [KeV/um]", fontsize=22)

plt.show()
