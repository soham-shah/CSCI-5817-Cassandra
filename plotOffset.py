import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

topology1 = pd.read_csv("topology1.csv")
topology2 = pd.read_csv("topology2.csv")
topology3 = pd.read_csv("topology3.csv")
topology4 = pd.read_csv("topology4.csv")
plt.figure(figsize=(5,8))
y = [topology1["Offset"],topology2["Offset"],topology4["Offset"],topology3["Offset"]]
plt.boxplot(y,0, '')
plt.title("Offset across various topologies")
plt.xlabel('Topology')
plt.ylabel('Offset (ms)')
plt.tight_layout()
# plt.show()
plt.savefig("Offset.png")