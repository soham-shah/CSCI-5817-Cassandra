import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

topology1 = pd.read_csv("topology1.csv")
topology2 = pd.read_csv("topology2.csv")
topology3 = pd.read_csv("topology3.csv")
topology4 = pd.read_csv("topology4.csv")
plt.figure(figsize=(5,8))
y = [topology1["Delay"],topology2["Delay"],topology4["Delay"],topology3["Delay"]]
plt.boxplot(y,0, '')
plt.title("Delay across various topologies")
plt.xlabel('Topology')
# plt.xticks([1,2,3,4],['1','2','3','4'])
plt.ylabel('Delay (ms)')
plt.tight_layout()
# plt.show()
plt.savefig("Delay.png")