import matplotlib.pyplot as plt, numpy as np

fig = plt.figure(figsize=(4,3))
t = np.linspace(0,2*np.pi)
plt.plot(t,np.sin(t),'o--')
plt.savefig('image.png',dpi=300)
plt.savefig('image.pdf')
plt.savefig('image.eps')