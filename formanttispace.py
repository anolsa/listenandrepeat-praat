>>> formantlist = ['589,985', '446,1801', '255,2218', '406,782', '312,597', '283,1567', '632,1310', '421,1288']
>>> f1list = []
>>> f2list = []
>>> for i in formantlist:
	f1, f2 = i.split(',')
	f1list.append(f1)
	f2list.append(f2)

	
>>> f1list = map(int, f1list)
>>> f2list = map(int, f2list)
>>> 
>>> f1low = min(f1list)
>>> f1high = max(f1list)
>>> f2low = min(f2list)
>>> f2high = max(f2list)
>>> 
>>> f1space = f1high - f1low
>>> f2space = f2high - f2low