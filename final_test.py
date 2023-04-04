import pandas as pd 
from matplotlib import pyplot as plt
import csv 

stats=pd.read_csv('dict_stats_multi.csv', delimiter=',')
index=[]
nbr_agents=[]
p=[]
cout=[]
cout_r=[]
nbr_reel=[]
nbr_requetes_SMS=[]
nbr_requetes_call=[]
nbr_data_points=100
counter=0
for i in stats.index: 
    if counter<nbr_data_points:
        x=stats.loc[i]
        index.append(x[0])
        nbr_agents.append(x[1])
        p.append(x[2])
        cout.append(x[3])
        cout_r.append(x[4])
        nbr_reel.append(x[5])
        nbr_requetes_SMS.append(x[6])
        nbr_requetes_call.append(x[7])
        counter+=1

fig, [ax1, ax2] = plt.subplots(nrows=2,dpi=300)
plt.subplots_adjust(right=0.8)
color = 'black'
ax1.set_xlabel('Temps')
ax1.set_ylabel("Nombre d'agents", color=color)
ax1.plot(index, nbr_agents, color=color, label="Nombre d'agents sans temps d'attente")
ax1.plot(index, nbr_reel, color='red', linestyle='dashed', label="Nombre d'agents reel")
ax1.tick_params(axis='y', labelcolor=color)
ax1.locator_params(axis='x', nbins=10)
ax1.xaxis.set_major_locator(plt.MaxNLocator(10))
every_nth = 10
for n, label in enumerate(ax1.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'blue'
ax2.set_ylabel('Nombre de requêtes', color=color)  # we already handled the x-label with ax1
ax2.plot(index, nbr_requetes_call, color=color, label="Nombre d'appels par heure")
ax2.plot(index, nbr_requetes_SMS, color='green', label="Nombre de chat/SMS par heure")
ax2.tick_params(axis='y', labelcolor=color)



# for n, label in enumerate(ax2.xaxis.get_ticklabels()):
#     if n % every_nth != 0:
#         label.set_visible(False)
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()