
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

sion = input("Enter stable io name: ")
Es = input("Enter its energy in Mev/u: ")
uion= input("Enter unstable isotope name: ")
Eu = input("Enter its energy in Mev/u: ")

directory1='/home/angela/Desktop/SFRTGate/data/GDRT/ctc35/'+sion+'/'
directory2='/home/angela/Desktop/SFRTGate/data/GDRT/ctc35/'+uion+'/'

zp_s=np.load(directory1+'zprofilepeak_'+sion+'.npy')
zv_s=np.load(directory1+'zprofilevalley_'+sion+'.npy')
zp_sprimaries=np.load(directory1+'zprofilepeak_'+sion+'primaries.npy')
zv_sprimaries=np.load(directory1+'zprofilevalley_'+sion+'primaries.npy')
zp_salpha=np.load(directory1+'zprofilepeak_'+sion+'alpha.npy')
zv_salpha=np.load(directory1+'zprofilevalley_'+sion+'alpha.npy')
# zp_sproton=np.load(directory1+'zprofilepeak_Li7proton.npy')
# zv_sproton=np.load(directory1+'zprofilevalley_Li7proton.npy')
# zp_selectron=np.load(directory1+'zprofilepeak_Li7electron.npy')
# zv_selectron=np.load(directory1+'zprofilevalley_Li7electron.npy')

zp_u=np.load(directory2+'zprofilepeak_'+uion+'.npy')
zv_u=np.load(directory2+'zprofilevalley_'+uion+'.npy')
zp_uprimaries=np.load(directory2+'zprofilepeak_'+uion+'primaries.npy')
zv_u=np.load(directory2+'zprofilevalley_'+uion+'.npy')
zv_uprimaries=np.load(directory2+'zprofilevalley_'+uion+'primaries.npy')
zp_ualpha=np.load(directory2+'zprofilepeak_'+uion+'alpha.npy')
zv_ualpha=np.load(directory2+'zprofilevalley_'+uion+'alpha.npy')

###############################################################################
norm_Li8_GDRT=1/zp_u.max()
norm_Li7_GDRT=1/zp_s.max()
#################################################################################
def plotfunction(directory,filename,nz,res_z,norm,color):
    z=np.load(directory+filename)
    zone,ion=filename.split("_")
    ion,_=ion.split('.npy')
    _,zone=zone.split('zprofile')

    plt.plot(
        (np.arange(0, nz) * res_z),
        z*norm,
        ".",
        color=color,
        markersize=10,
        label="D,{},{}".format(zone,ion),
    )

def axplotfunction(directory,filename,nz,res_z,norm,color):
    z=np.load(directory+filename)
    zone,ion=filename.split("_")
    ion,_=ion.split('.npy')
    _,zone=zone.split('zprofile')

    ax.plot(
        (np.arange(0, nz) * res_z),
        z*norm,
        ".",
        color=color,
        markersize=10,
        label="D,{},{}".format(zone,ion),
    )
    plt.legend()


def plotfunctionLET(directory,filename,nz,res_z,norm,color):
    z=np.load(directory+filename)
    LET,ion,_=filename.split("_")



    plt.plot(
        (np.arange(0, nz) * res_z),
        z*norm,
        ".",
        color=color,
        markersize=10,
        label="{},{},peak".format(LET,ion),
    )

fig,(ax1,ax2)=plt.subplots(1,2)
fig.suptitle(" Depth dose profile GDRT :$E_{stable}= %s MeV/u, E_{unstable}= %s MeV/u $" % (Es,Eu), fontsize=24)
ax2.plot(
    (np.arange(0, 100) * 1),
    zv_u/zv_u.max(),
    ".",
    color='lightblue',
    markersize=10,
    label="$D_{Li8,valley}$",
)
ax2.plot(
    (np.arange(0, 100) * 1),
    zv_s/zv_s.max(),
    ".",
    color='lightgreen',
    markersize=10,
    label="$D_{Li7,valley}$",
)

# #plotfunction(directory2,'zprofilevalley_'+uion+'.npy',100,1,norm_12_GDRT,'lightblue')
ax2.axvspan(60,80, facecolor="yellow", alpha=0.3, label="Tumor region ")
ax2.legend(
    title="Valley",
    title_fontsize=18,
    fontsize=18,
    loc=3,
    markerscale=3)


#plt.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
ax2.tick_params(axis="x", which="major", labelsize=22)
ax2.tick_params(axis="y", which="major", labelsize=22)
ax2.set_xlabel("Depth z[mm]", fontsize=22)


ax1.plot(
    (np.arange(0, 100) * 1),
    zp_u*norm_Li8_GDRT,
    ".",
    color=sns.color_palette("Paired")[1],
    markersize=10,
    label="$D_{Li8,peak}$",
    )
ax1.plot(
    (np.arange(0, 100) * 1),
    zp_s*norm_Li7_GDRT,
    ".",
    color=sns.color_palette("Paired")[2],
    markersize=10,
    label="$D_{Li7,peak}$",
    )

ax1.axvspan(60,80, facecolor="yellow", alpha=0.3, label="Tumor region ")
ax1.legend(
    title="Peak ",
    title_fontsize=18,
    fontsize=18,
    loc=3,
    markerscale=3)


#plt.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
ax1.tick_params(axis="x", which="major", labelsize=22)
ax1.tick_params(axis="y", which="major", labelsize=22)
ax1.set_xlabel("Depth z[mm]", fontsize=22)
ax1.set_ylabel("Relative Dose", fontsize=22)



fig,(ax1,ax2)=plt.subplots(1,2)
fig.suptitle("DDP GDRT: alpha contribution \n $E_{stable}=%s MeV/u, E_{unstable}=%s MeV/u $"% (Es,Eu), 
                                                                    fontsize=22)
# ax1.plot(
#         (np.arange(0, 100) *1),
#         zp_s,
#         ".",
#         color=sns.color_palette("Paired")[0],
#         markersize=10,
#         label="$ Li7 D_{valley}$",
#     )
# ax1.plot(
#         (np.arange(0, 100) *1),
#         zp_u,
#         ".",
#         color=sns.color_palette("Paired")[2],
#         markersize=10,
#         label="$ Li8 D_{valley}$",
#     )

ax1.plot((np.arange(0, 100) * 1),
                                                            (zp_salpha/zp_s.max())*100,
                                                                            ".-",
                                            color=sns.color_palette("Paired")[1],
                                                                markersize=10,
                                                label="%s: $D_{peak,alpha}$/$D_{peak}$"%(sion))
ax1.plot((np.arange(0, 100) * 1),
                                                            (zp_ualpha/zp_u.max())*100,
                                                                            ".-",
                                            color=sns.color_palette("Paired")[3],
                                                                markersize=10,
                                                label="%s: $D_{peak,alpha}$/$D_{peak}$"% (uion))
ax1.axvspan(60,80, facecolor="yellow", alpha=0.3, label="Tumor region ")
ax1.legend(
    title="",
    title_fontsize=18,
    fontsize=18,
    loc=3,
    markerscale=3)

ax1.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
ax1.tick_params(axis="x", which="major", labelsize=22)
ax1.tick_params(axis="y", which="major", labelsize=22)
#ax1.set_yscale('log')
#ax2.set_yscale('log')
ax1.set_xlabel("Depth z[mm]", fontsize=22)
ax1.set_ylabel("alpha contribution[%] ", fontsize=22)



# ax2.plot(
#         (np.arange(0, 100) *1),
#         zv_s,
#         ".",
#         color=sns.color_palette("Paired")[0],
#         markersize=10,
#         label="$ Li7 D_{valley}$",
#     )
# ax2.plot(
#         (np.arange(0, 100) *1),
#         zv_u,
#         ".",
#         color=sns.color_palette("Paired")[2],
#         markersize=10,
#         label="$ Li8 D_{valley}$",
#     )

ax2.plot((np.arange(0, 100) * 1),
                                                            (zv_salpha/zv_s.max())*100,
                                                                            ".-",
                                            color=sns.color_palette("Paired")[1],
                                                                markersize=10,
                                                label="%s: $D_{valley,alpha}$/$D_{valley}$" %(sion))
ax2.plot((np.arange(0, 100) * 1),
                                                            (zv_ualpha/zv_u.max())*100,
                                                                            ".-",
                                            color=sns.color_palette("Paired")[3],
                                                                markersize=10,
                                                label="%s: $D_{valley,alpha}$/$D_{valley}$" %(uion))
ax2.axvspan(60,80, facecolor="yellow", alpha=0.3, label="Tumor region ")
ax2.legend(
    title="",
    title_fontsize=18,
    fontsize=18,
    loc=3,
    markerscale=3)

ax2.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
#ax4.set_yscale('log')
ax2.tick_params(axis="x", which="major", labelsize=22)
ax2.tick_params(axis="y", which="major", labelsize=22)
ax2.set_xlabel("Depth z[mm]", fontsize=22)
#ax2.set_ylabel(" alpha contribution[%] ", fontsize=22)




plt.figure(3)
plt.plot((np.arange(0, 100) * 1),
                                                zp_s/zv_s,
                                                                            ".",
                                            color=sns.color_palette("Paired")[2],
                                                                markersize=10,
                                                label="$D_{Li7,peak}/D_{Li7,valley}$")
plt.plot((np.arange(0, 100) * 1),
                                                zp_u/zv_u,
                                                                            ".",
                                            color=sns.color_palette("Paired")[1],
                                                                markersize=10,
                                                label="$D_{Li8,peak}/D_{Li8,valley}$")


plt.axvspan(60,80, facecolor="yellow", alpha=0.3, label="Tumor region ")
plt.legend(
    title="bw= 600μm x 600 μm, ctc= 3500 μm ",
    title_fontsize=18,
    fontsize=18,
    loc=3,
    markerscale=3)

plt.title("Depth dose profile GDRT", fontsize=24)
plt.yscale('log')
#plt.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
plt.tick_params(axis="x", which="major", labelsize=22)
plt.tick_params(axis="y", which="major", labelsize=22)
plt.xlabel("Depth z[mm]", fontsize=22)
plt.ylabel("PVDR", fontsize=22)



plt.figure(4)
plotfunction(directory1,'zprofilepeak_'+sion+'.npy',100,1,norm_Li7_GDRT,sns.color_palette("Paired")[1])
plotfunction(directory1,'zprofilepeak_Li7primaries.npy',100,1,norm_Li7_GDRT,sns.color_palette("Paired")[0])
plotfunction(directory1,'zprofilepeak_Li7alpha.npy',100,1,norm_Li7_GDRT,sns.color_palette("Paired")[4])
plt.legend(
    title="$E_{{}^{7}Li}=115 MeV/u$",
    title_fontsize=18,
    fontsize=18,
    loc=2,
    markerscale=3)


plt.title("Depth dose profile GDRT", fontsize=24)
#plt.yscale('log')
#plt.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
plt.tick_params(axis="x", which="major", labelsize=22)
plt.tick_params(axis="y", which="major", labelsize=22)
plt.xlabel("Depth z[mm]", fontsize=22)
plt.ylabel("Relative Dose ", fontsize=22)




plt.figure(5)

plotfunction(directory2,'zprofilepeak_'+uion+'.npy',100,1,norm_Li8_GDRT,sns.color_palette("Paired")[2])
plotfunction(directory2,'zprofilepeak_Li8primaries.npy',100,1,norm_Li8_GDRT,sns.color_palette("Paired")[3])
plotfunction(directory2,'zprofilepeak_Li8alpha.npy',100,1,norm_Li8_GDRT,sns.color_palette("Paired")[6])

plt.legend(
    title="$E_{{}^{8}Li}=105 MeV/u$",
    title_fontsize=20,
    fontsize=18,
    markerscale=3,
    loc=2)


plt.title("Depth dose profile", fontsize=24)
#plt.yscale('log')
#plt.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
plt.tick_params(axis="x", which="major", labelsize=22)
plt.tick_params(axis="y", which="major", labelsize=22)
plt.xlabel("Depth z[mm]", fontsize=22)
plt.ylabel("Relative Dose ", fontsize=22)

plt.show()
# plt.figure(4)
# plotfunctionLET(directory1,'LET_Li7_zprofilepeak.npy',100,1,1,sns.color_palette("Paired")[1])
# plotfunctionLET(directory1,'LETprimaries_Li7_zprofilepeak.npy',100,1,1,sns.color_palette("Paired")[0])
# plotfunctionLET(directory1,'LETalpha_Li7_zprofilepeak.npy',100,1,1,sns.color_palette("Paired")[4])
# plt.legend(
#     title="$E_{{}^{7}Li}=115 MeV/u$",
#     title_fontsize=20,
#     fontsize=18,
#     markerscale=3)
#
#
# plt.title("LET  depht profile GDRT", fontsize=24)
# #plt.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
# plt.tick_params(axis="x", which="major", labelsize=22)
# plt.tick_params(axis="y", which="major", labelsize=22)
# plt.xlabel("Depth z[mm]", fontsize=22)
# plt.ylabel("LET[Kev/um]", fontsize=22)
#
#
# plt.figure(5)
# plotfunctionLET(directory2,'LET_Li8_zprofilepeak.npy',100,1,1,sns.color_palette("Paired")[3])
# plotfunctionLET(directory2,'LETprimaries_Li8_zprofilepeak.npy',100,1,1,sns.color_palette("Paired")[2])
# plotfunctionLET(directory2,'LETalpha_Li8_zprofilepeak.npy',100,1,1,sns.color_palette("Paired")[5])
# plt.legend(
#     title="$E_{{}^{31}C}=190 MeV/u$",
#     title_fontsize=18,
#     fontsize=18,
#     markerscale=3)
#
#
# plt.title("LET depth profile GDRT", fontsize=24)
# #plt.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
# plt.tick_params(axis="x", which="major", labelsize=22)
# plt.tick_params(axis="y", which="major", labelsize=22)
# plt.xlabel("Depth z[mm]", fontsize=22)
# plt.ylabel("LET[Kev/um]", fontsize=22)
#
#
# plt.show()
#
#
# ########################################################################################
#
# plt.figure(6)
# plotfunction(directory3,'zprofilepeak_'+sion+'.npy',100,1,norm_Li7_MBRT,sns.color_palette("Paired")[1])
# plotfunction(directory3,'zprofilevalley_'+sion+'.npy',100,1,norm_Li7_MBRT,sns.color_palette("Paired")[0])
# plotfunction(directory1,'zprofilepeak_'+uion+'.npy',100,1,norm_Li8_MBRT,sns.color_palette("Paired")[3])
# plotfunction(directory1,'zprofilevalley_'+uion+'.npy',100,1,norm_Li8_MBRT,sns.color_palette("Paired")[2])
# plt.axvspan(60,80, facecolor="yellow", alpha=0.3, label="Tumor region ")
# plt.legend(
#     title="$E_{{}^{7}Li}=115 MeV/u, E_{{}^{8}Li}= 105 MeV/u $",
#     title_fontsize=18,
#     fontsize=18,
#     loc=2,
#     markerscale=3)
#
# plt.title("Depth dose profile", fontsize=24)
# #plt.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
# plt.tick_params(axis="x", which="major", labelsize=22)
# plt.tick_params(axis="y", which="major", labelsize=22)
# plt.xlabel("Depth z[mm]", fontsize=22)
# plt.ylabel("MBRT Realative Dose", fontsize=22)
#
#
#
# plt.figure(7)
# plotfunction(directory3,'zprofilepeak_'+sion+'.npy',100,1,norm_Li7_MBRT,sns.color_palette("Paired")[1])
# plotfunction(directory3,'zprofilepeak_Li7alpha.npy',100,1,norm_Li7_MBRT,sns.color_palette("Paired")[0])
# plotfunction(directory3,'zprofilepeak_Li7primaries.npy',100,1,norm_Li7_MBRT,sns.color_palette("Paired")[2])
# plt.axvspan(60,80, facecolor="yellow", alpha=0.3, label="Tumor region ")
# plt.legend(
#     title="$E_{{}^{7}Li}=115 MeV/u$ , bw= 600μm x 2 cm",
#     title_fontsize=18,
#     fontsize=18,
#     loc=2,
#     markerscale=3)
#
# plt.title("Depth dose profile MBRT ", fontsize=24)
# #plt.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
# plt.tick_params(axis="x", which="major", labelsize=22)
# plt.tick_params(axis="y", which="major", labelsize=22)
# plt.xlabel("Depth z[mm]", fontsize=22)
# plt.ylabel(" Realative Dose", fontsize=22)
#
#
#
# plt.figure(8)
# plotfunction(directory1,'zprofilepeak_'+uion+'.npy',100,1,norm_Li8_MBRT,sns.color_palette("Paired")[1])
# plotfunction(directory1,'zprofilepeak_Li8alpha.npy',100,1,norm_Li8_MBRT,sns.color_palette("Paired")[0])
# plotfunction(directory1,'zprofilepeak_Li8primaries.npy',100,1,norm_Li8_MBRT,sns.color_palette("Paired")[2])
# plt.axvspan(60,80, facecolor="yellow", alpha=0.3, label="Tumor region ")
# plt.legend(
#     title="$E_{{}^{31}C}=190 MeV/u$ , bw= 600μm x 2 cm",
#     title_fontsize=18,
#     fontsize=18,
#     loc=2,
#     markerscale=3)
#
# plt.title("Depth dose profile MBRT ", fontsize=24)
# #plt.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
# plt.tick_params(axis="x", which="major", labelsize=22)
# plt.tick_params(axis="y", which="major", labelsize=22)
# plt.xlabel("Depth z[mm]", fontsize=22)
# plt.ylabel(" Realative Dose", fontsize=22)
#
#
#
#
# zp_s_MBRT=np.load(directory3+'zprofilepeak_'+sion+'.npy')
# zv_s_MBRT=np.load(directory3+'zprofilevalley_'+sion+'.npy')
# zp_u_MBRT=np.load(directory1+'zprofilepeak_'+uion+'.npy')
# zv_u_MBRT=np.load(directory1+'zprofilevalley_'+uion+'.npy')
# plt.figure(9)
# plt.plot((np.arange(0, 100) * 1),
#                                                 zp_s/zv_s,
#                                                                             ".",
#                                             color=sns.color_palette("Paired")[1],
#                                                                 markersize=10,
#                                                 label="GDRT $D_{Li7,peak}/D_{Li7,valley}$")
#
# plt.plot((np.arange(0, 100) * 1),
#                                                 zp_s_MBRT/zv_s_MBRT,
#                                                                             ".",
#                                             color=sns.color_palette("Paired")[3],
#                                                                 markersize=10,
#                                                 label="MBRT $D_{Li7,peak}/D_{Li7,valley}$")
#
#
# plt.axvspan(60,80, facecolor="yellow", alpha=0.3, label="Tumor region ")
# plt.legend(
#     title="MBRT :bw= 600μm x 2 cm, ctc= 1150 μm \n GDRT :bw= 600μm x 600μm , ctc= 1150 μm",
#     title_fontsize=18,
#     fontsize=18,
#     loc=3,
#     markerscale=3)
#
# plt.title("${}^9C$ Beam", fontsize=24)
# #plt.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
# plt.tick_params(axis="x", which="major", labelsize=22)
# plt.tick_params(axis="y", which="major", labelsize=22)
# plt.xlabel("Depth z[mm]", fontsize=22)
# plt.ylabel("PVDR", fontsize=22)
# plt.show()
#

fig,ax1=plt.subplots()
#fig.suptitle(" Depth dose profile GDRT: $\alpha$ contribution ", fontsize=24)
plt.title(" Peak Depth dose profile GDRT: Primaries contribution ", fontsize=24)
ax2=ax1.twinx()
ax1.plot(
        (np.arange(0, 100) *1),
        zp_s,
        ".",
        color=sns.color_palette("Paired")[0],
        markersize=10,
        label="$ Li7 D_{valley}$",
        alpha=0.5,
    )
ax1.plot(
        (np.arange(0, 100) *1),
        zp_u,
        ".",
        color=sns.color_palette("Paired")[2],
        markersize=10,
        label="$ Li8 D_{valley}$",
        alpha=0.5,
    )

ax2.plot((np.arange(0, 100) * 1),
                                                            (zp_sprimaries/zp_s.max())*100,
                                                                            ".-",
                                            color=sns.color_palette("Paired")[1],
                                                                markersize=10,
                                                label="$D_{Li7,peak,primaries}$/$D_{Li7,peak}$")
ax2.plot((np.arange(0, 100) * 1),
                                                            (zp_uprimaries/zp_u.max())*100,
                                                                            ".-",
                                            color=sns.color_palette("Paired")[3],
                                                                markersize=10,
                                                label="$D_{Li8,peak,primaries}$/$D_{Li8,peak}$")
#ax.set_axvspan(60,80, facecolor="yellow", alpha=0.3, label="Tumor region ")
plt.legend(
    title="$E_{{}^{7}Li}=115 MeV/u, E_{{}^{8}Li}= 105 MeV/u $",
    title_fontsize=18,
    fontsize=18,
    loc=3,
    markerscale=3)

#plt.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
ax1.tick_params(axis="x", which="major", labelsize=22)
ax1.tick_params(axis="y", which="major", labelsize=22)
#ax1.set_yscale('log')
#ax2.set_yscale('log')
ax2.tick_params(axis="y", which="major", labelsize=22)
ax1.set_xlabel("Depth z[mm]", fontsize=22)
ax2.set_ylabel("Primaries contribution[%] ", fontsize=22)
ax1.set_ylabel("Absolute Dose [Gy]", fontsize=22)

fig,ax3=plt.subplots()
plt.title(" Valley Depth dose profile GDRT:Primaries contribution ", fontsize=24)
ax4=ax3.twinx()
ax3.plot(
        (np.arange(0, 100) *1),
        zv_s,
        ".",
        color=sns.color_palette("Paired")[0],
        markersize=10,
        label="$ Li7 D_{valley}$",
        alpha=0.5,
    )
ax3.plot(
        (np.arange(0, 100) *1),
        zv_u,
        ".",
        color=sns.color_palette("Paired")[2],
        markersize=10,
        label="$ Li8 D_{valley}$",
        alpha=0.5,
    )

ax4.plot((np.arange(0, 100) * 1),
                                                            (zv_sprimaries/zv_s.max())*100,
                                                                            ".-",
                                            color=sns.color_palette("Paired")[1],
                                                                markersize=10,
                                                label="$D_{Li7,valley,primaries}$/$D_{Li7,valley}$")
ax4.plot((np.arange(0, 100) * 1),
                                                            (zv_uprimaries/zv_u.max())*100,
                                                                            ".-",
                                            color=sns.color_palette("Paired")[3],
                                                                markersize=10,
                                                label="$D_{Li8,valley,primaries}$/$D_{Li8,valley}$")
#ax.set_axvspan(60,80, facecolor="yellow", alpha=0.3, label="Tumor region ")
plt.legend(
    title="$E_{{}^{7}Li}=115 MeV/u, E_{{}^{8}Li}= 105 MeV/u $ ",
    title_fontsize=18,
    fontsize=18,
    loc=3,
    markerscale=3)

#plt.grid(b=True, color="k", linestyle="dotted", alpha=0.2)
#ax4.set_yscale('log')
ax3.tick_params(axis="x", which="major", labelsize=22)
ax3.tick_params(axis="y", which="major", labelsize=22)
ax4.tick_params(axis="y", which="major", labelsize=22)
ax3.set_xlabel("Depth z[mm]", fontsize=22)
ax4.set_ylabel("Primaries contribution[%] ", fontsize=22)
ax3.set_ylabel("Absolute Dose [Gy]", fontsize=22)


plt.show()
