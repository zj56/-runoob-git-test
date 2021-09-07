from matplotlib import pyplot as plt
x = range(1995,2010)
y = [0.32,0.32,0.32,0.32,0.33,0.33,0.34,0.37,0.37,0.37,0.37,0.39,0.41,0.42,0.44,]
plt.figure(figsize=(20,8),dpi=80)
plt.plot(x, y, 'o--', color='grey', alpha=0.3)
plt.step(x,y,where='post',label='post',color="orange")
_xtick_labels = [i for i in x]
plt.xticks(_xtick_labels)
for a,b in zip(x,y):
    plt.text(x=a,y=b,s=b)
plt.show()
