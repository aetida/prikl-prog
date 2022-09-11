a = int(input())

x = a//100000
a = a - x*100000
z = a//10000
a = a - z*10000
c = a//1000
a = a - c*1000
v = a//100
a = a - v*100
b = a//10
a = a - b*10
n = a//1 

hundred = ['сто ','двести ','триста ', 'четыреста ','пятьсот ','шестьсот ','семьсот ','восемьсот ','девятьсот ']
dozens = ['десять ','одиннадцать ','двенадцать ','тринадцать ','четырнадцать ','пятнадцать ','шестнадцать ','семнадцать ','восемнадцать ','девятнадцать ', 'двадцать ','тридцать ','сорок ','пятьдесят ','шестдесят ','семдесят ','восемдесят ','девяносто ',''] 
thousands = ['','тысяча ', 'тысячи ','тысяч ']
unit = ['один','два','три','четыре','пять','шесть','семь','восемь','девять','одна']
rubl = ['рубль','рубля','рублей']

if x != 0:
	s = hundred[x-1]
else:
	s = thousands[0]

if z != 0:
	if z == 1:
		if c == 0:
			d = dozens[0]
			f = thousands[0]
		else:
			d = dozens[c]
			f = thousands[0]
	else:
		d = dozens[z+8]
		if c != 0:
			f = unit[c-1]
		else:
			f=thousands[0]
else:
	d = thousands[0]
	if c != 0:
		if c == 1:
			f=unit[9]
		else:
			f = unit[c-1]
	else:
		f=thousands[0]

if x!=0 or z!=0 or c!=0:
	if z == 1 or (c!=2 and c!=3 and c!=4 ):
		m = thousands[3]
	else:
		pass
	if z!=1 and c ==1:
		m=thousands[1]
	else:
		pass
	if z!=1 and (c==2 or c==3 or c==4):
		m=thousands[2]
	else:
		pass
	if x!=0 and z==0 and c==0:
		m=thousands[3]
	else:
		pass
	if x!=0 and c ==0:
		m=thousands[3]
	else:
		pass
else:
	m=thousands[0]

if v != 0:
	g = hundred[v-1]
else:
	g = thousands[0]

if b != 0:
	if b == 1:
		if n == 0:
			h = dozens[0]
			j = thousands[0]
		else:
			h = dozens[n]
			j = thousands[0]
	else:
		h = dozens[z+8]
		if n != 0:
			j = unit[n-1]
		else:
			j=thousands[0]
else:
	h = thousands[0]
	if n != 0:
		j = unit[c-1]
	else:
		j=thousands[0]

if n == 1:
	if b!=1:
		r=rubl[0]
	else:
		r=rubl[2]
else:
	pass

if n == 2 or n == 3 or n ==4:
	if b!=1:
		r=rubl[0]
	else:
		r = rubl[1]
else:
	pass

if n > 4 or n == 0:
	r = rubl[2]
else:
	pass

print(str(s)+str(d)+str(f)+str(m)+str(g)+str(h)+str(j)+str(r))

input()