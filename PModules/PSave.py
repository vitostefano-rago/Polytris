AH = 30
AW = 25

def ExportData(bw, sc, st, sh, sn, posx, posy, posr):
	f = ""
	for cnt in range(len(bw)):
		f += ";"
		for cntt in range(len(bw[cnt])):
			f += str(bw[cnt][cntt])
			f += ","
		f += "\n"
	
	f += "score  "
	f += str(sc)
	f += "\n"
	f += "blockno  "
	f += str(st)
	f += "\n"
	f += "shape  "
	f += str(sh)
	f += "\n"
	f += "next  "
	f += str(sn)
	f += "\n"
	f += "posx  "
	f += str(posx)
	f += "\n"
	f += "posy  "
	f += str(posy)
	f += "\n"
	f += "posr  "
	f += str(posr)
	f += "\n"
	f += "checksum  "
	f += str(CalculateCrc(bw, sc, st, sh, sn, posx, posy, posr))
	f += "\n"
	
	with open("Savedgamestatus.txt", "w") as g:
		g.write(f)

def CalculateCrc(bw, sc, st, sh, sn, posx, posy, posr):
	crc = 0
	
	for cnt in range (len(bw)):
		lrc = 0
		for cntt in range(len(bw[cnt])):
			if bw[cnt][cntt] != 0:
				lrc += 2 ** cntt
			crc = crc ^ lrc
	
	crc = crc ^ sc
	crc = crc ^ st
	crc = crc ^ sh
	crc = crc ^ sn
	crc = crc ^ posx
	crc = crc ^ posy
	crc = crc ^ posr
	
	return crc

def ImportData():
	global AH
	global AW
	
	try:
		with open("Savedgamestatus.txt", "r") as f:
			cntnt = f.readlines()
		
		wsm = [[0 for _ in range(AW + 3)] for _ in range(AH + 5)]
		
		for cnt in range(AH + 5):
			tl = cntnt[cnt]
			for cntt in range(AW + 3):
				tv = tl[(len(tl) - tl[::-1].index(";")):tl.index(",")]
				tl = tl.replace(",",";",1)
				if tv != "0":
					wsm[cnt][cntt] = tv
		
		for cnt in range(len(cntnt)):
			if "score" in cntnt[cnt]:
				sc = int(cntnt[cnt][6:])
			if "blockno" in cntnt[cnt]:
				st = int(cntnt[cnt][8:])
			if "shape" in cntnt[cnt]:
				sh = int(cntnt[cnt][6:])
			if "next" in cntnt[cnt]:
				sn = int(cntnt[cnt][5:])
			if "posx" in cntnt[cnt]:
				posx = int(cntnt[cnt][5:])
			if "posy" in cntnt[cnt]:
				posy = int(cntnt[cnt][5:])
			if "posr" in cntnt[cnt]:
				posr = int(cntnt[cnt][5:])
			if "checksum" in cntnt[cnt]:
				chcksm = int(cntnt[cnt][9:])
		
		return chcksm ==  CalculateCrc(wsm, sc, st, sh, sn, posx, posy, posr), wsm, sc, st, sh, sn, posx, posy, posr
	
	except:
		return False, 0,0,0,0,0,0,0,0