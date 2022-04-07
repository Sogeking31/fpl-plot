
file_name = 'fplrecord.txt'
with open (file_name, 'r') as f:
	lines = f.readlines()

oarank = lines[1]
gwrank = lines[3]
gwpoints = lines[5]
oapoints = lines[7]
tv = lines[9]
print(f"{oarank}\n{gwrank}\n{gwpoints}\n{oapoints}\n{tv}")

#plt.style.use('seaborn')
#fig, ax = plt.subplots()
#ax.plot(range(31), oarank, linewidth = 3)
#ax.set_title("FPL Rank", fontsize= 24)
#ax.set_xlabel("GW", fontsize=14)
#ax.set_ylabel("rank", fontsize = 14)
#a#x.tick_params(axis='both', labelsize= 14)
#plt.show()

#p#rint(tv)