import random

class Shapes:
	def __init__(self,blocklayout,turns,color):
		self.blocklayout = blocklayout
		self.turns = turns
		self.color = color
		self.allversions = self.CreateAllVersions()
		self.freespaceall = self.FreeSpaceAll()
	
	def CheckFreeSpace(self):
		#Cell 3, 3 is always full, free space is checked in relation to items
		#Order is: above, right, below, left
		freespace = [0,0,0,0]
		
		#Check above
		for cnt in range(0,3):
			freespace[0] += max(self.blocklayout[cnt])
		
		#Check right
		for cnt in range(4,7):
			for cntt in range(0,7):
				if self.blocklayout[cntt][cnt] == 1:
					freespace[1] += 1
					break
		
		#Check below
		for cnt in range(4,7):
			freespace[2] += max(self.blocklayout[cnt])
		
		#Check left
		for cnt in range(0,3):
			for cntt in range(0,7):
				if self.blocklayout[cntt][cnt] == 1:
					freespace[3] += 1
					break
		
		return freespace
	
	def Rotate(self,tbr):
		#Always rotate 90° to the right
		R = [[0 for _ in range(7)] for _ in range(7)]
		for cnt in range(7):
			for cntt in range(7):
				R[cnt][cntt] = tbr[6 - cntt][cnt]
		return R
	
	
	def CreateAllVersions(self):
		AV = []
		tmp = [[self.blocklayout[cnt][cntt] for cntt in range(7)] for cnt in range(7)]
		AV.append(tmp)
		for cnt in range(1,self.turns):
			tmp = self.Rotate(tmp)
			AV.append(tmp)
		return AV
	
	def FreeSpaceAll(self):
		fs = []
		fs.append(self.CheckFreeSpace())
		for cnt in range (1,self.turns):
			fs.append([fs[0][(4 - cnt) % 4], fs[0][(5 - cnt) % 4], fs[0][(6 - cnt) % 4], fs[0][(7 - cnt) % 4]])
		return fs
	
	def CurrRotation(self, cs):
		return(self.allversions[cs % self.turns])
	
	def CurrFree(self, cs):
		return(self.freespaceall[cs % self.turns])

allshapes = []

M = [[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

L = Shapes(M, trns, "orange")

allshapes.append(L)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

J = Shapes(M, trns, "blue")

allshapes.append(J)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,1,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 1

O = Shapes(M, trns, "yellow")

allshapes.append(O)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,1,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

T = Shapes(M, trns, "magenta")

allshapes.append(T)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 2

I = Shapes(M, trns, "cyan")

allshapes.append(I)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,1,1,0,0],
[0,0,1,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 2

S = Shapes(M, trns, "lime")

allshapes.append(S)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 2

Z = Shapes(M, trns, "red")

allshapes.append(Z)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 2

Id = Shapes(M, trns, "peru")
allshapes.append(Id)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 2

It = Shapes(M, trns, "chocolate")
allshapes.append(It)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Tt = Shapes(M, trns, "sienna")
allshapes.append(Tt)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0]]

trns = 2

Ip = Shapes(M, trns, "darkcyan")
allshapes.append(Ip)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,1,1,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Fp = Shapes(M, trns, "purple")
allshapes.append(Fp)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Fip = Shapes(M, trns, "indigo")
allshapes.append(Fip)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Lp = Shapes(M, trns, "darkorange")
allshapes.append(Lp)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Jp = Shapes(M, trns, "navy")
allshapes.append(Jp)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Pp = Shapes(M, trns, "gold")
allshapes.append(Pp)

M = [[0,0,0,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Pip = Shapes(M, trns, "khaki")
allshapes.append(Pip)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,1,1,1,0],
[0,0,1,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Sp = Shapes(M, trns, "green")
allshapes.append(Sp)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,1,1,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Sip = Shapes(M, trns, "crimson")
allshapes.append(Sip)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,1,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Tp = Shapes(M, trns, "deeppink")
allshapes.append(Tp)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,1,0,1,0,0],
[0,0,1,1,1,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Up = Shapes(M, trns, "olive")
allshapes.append(Up)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,1,1,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Vp = Shapes(M, trns, "darkolivegreen")
allshapes.append(Vp)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,1,0,0],
[0,0,0,1,1,0,0],
[0,0,1,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Wp = Shapes(M, trns, "olivedrab")
allshapes.append(Wp)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Xp = Shapes(M, trns, "mediumblue")
allshapes.append(Xp)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Yp = Shapes(M, trns, "forestgreen")
allshapes.append(Yp)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Yip = Shapes(M, trns, "lightgreen")
allshapes.append(Yip)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Zp = Shapes(M, trns, "goldenrod")
allshapes.append(Zp)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Zip = Shapes(M, trns, "darkgoldenrod")
allshapes.append(Zip)

M = [[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0]]

trns = 2

Ih = Shapes(M, trns, "turquoise")

allshapes.append(Ih)

M = [[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Lh = Shapes(M, trns, "orangered")
allshapes.append(Lh)


M = [[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Jh = Shapes(M, trns, "midnightblue")
allshapes.append(Jh)


M = [[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

LLh = Shapes(M, trns, "limegreen")
allshapes.append(LLh)


M = [[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

JJh = Shapes(M, trns, "seagreen")
allshapes.append(JJh)


M = [[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

TTh = Shapes(M, trns, "orchid")
allshapes.append(TTh)

M = [[0,0,0,0,1,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Sh = Shapes(M, trns, "greenyellow")
allshapes.append(Sh)


M = [[0,0,1,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Sih = Shapes(M, trns, "yellowgreen")
allshapes.append(Sih)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

S

Ph = Shapes(M, trns, "lightsalmon")
allshapes.append(Ph)


M = [[0,0,0,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Pih = Shapes(M, trns, "darksalmon")
allshapes.append(Pih)



M = [[0,0,0,0,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Fh = Shapes(M, trns, "darkorchid")
allshapes.append(Fh)


M = [[0,0,0,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Fih = Shapes(M, trns, "mediumorchid")
allshapes.append(Fih)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Uh = Shapes(M, trns, "royalblue")
allshapes.append(Uh)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Uih = Shapes(M, trns, "slateblue")
allshapes.append(Uih)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,1,1,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Vh = Shapes(M, trns, "darkslateblue")
allshapes.append(Vh)

M = [[0,0,0,0,0,0,0],
[0,1,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Vih = Shapes(M, trns, "mediumslateblue")
allshapes.append(Vih)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,1,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

VVh = Shapes(M, trns, "skyblue")
allshapes.append(VVh)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,1,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

VVih = Shapes(M, trns, "deepskyblue")
allshapes.append(VVih)


M = [[0,0,0,0,0,0,0],
[0,0,1,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Th = Shapes(M, trns, "sandybrown")
allshapes.append(Th)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,1,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Ah = Shapes(M, trns, "saddlebrown")
allshapes.append(Ah)

M = [[0,0,0,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Aih = Shapes(M, trns, "rosybrown")
allshapes.append(Aih)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

AAh = Shapes(M, trns, "maroon")
allshapes.append(AAh)

M = [[0,0,0,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

AAih = Shapes(M, trns, "firebrick")
allshapes.append(AAih)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 2

Zh = Shapes(M, trns, "tomato")
allshapes.append(Zh)

M = [[0,0,0,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 2

Zih = Shapes(M, trns, "indianred")
allshapes.append(Zih)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 2

Bh = Shapes(M, trns, "springgreen")
allshapes.append(Bh)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 2

Bih = Shapes(M, trns, "darkseagreen")
allshapes.append(Bih)

M = [[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Ch = Shapes(M, trns, "darkslategray")
allshapes.append(Ch)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,1,0,0],
[0,0,0,1,1,1,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Dh = Shapes(M, trns, "mediumspringgreen")
allshapes.append(Dh)

M = [[0,0,0,0,0,0,0],
[0,0,1,0,0,0,0],
[0,1,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Dih = Shapes(M, trns, "mediumaquamarine")
allshapes.append(Dih)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,1,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Eh = Shapes(M, trns, "darkkhaki")
allshapes.append(Eh)

M = [[0,0,0,0,0,0,0],
[0,0,1,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Eih = Shapes(M, trns, "palegreen")
allshapes.append(Eih)

M = [[0,0,0,0,1,0,0],
[0,0,0,0,1,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 2

Gh = Shapes(M, trns, "steelblue")
allshapes.append(Gh)


M = [[0,0,1,0,0,0,0],
[0,0,1,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 2

Gih = Shapes(M, trns, "burlywood")
allshapes.append(Gih)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,1,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 2

Hh = Shapes(M, trns, "peachpuff")
allshapes.append(Hh)


M = [[0,0,0,0,0,0,0],
[0,0,1,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 2

Hih = Shapes(M, trns, "navajowhite")
allshapes.append(Hih)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,1,1,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 2

Oh = Shapes(M, trns, "aquamarine")
allshapes.append(Oh)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,1,0,0],
[0,0,1,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Kh = Shapes(M, trns, "lightsteelblue")
allshapes.append(Kh)

M = [[0,0,0,0,0,0,0],
[0,0,1,0,0,0,0],
[0,0,1,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Kih = Shapes(M, trns, "papayawhip")
allshapes.append(Kih)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,1,1,1,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Nh = Shapes(M, trns, "mistyrose")
allshapes.append(Nh)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,1,1,1,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Nih = Shapes(M, trns, "tan")
allshapes.append(Nih)


M = [[0,0,0,0,0,0,0],
[0,0,0,0,1,0,0],
[0,0,0,1,1,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Rh = Shapes(M, trns, "mediumvioletred")
allshapes.append(Rh)

M = [[0,0,0,0,0,0,0],
[0,0,1,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Rih = Shapes(M, trns, "palevioletred")
allshapes.append(Rih)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,1,0],
[0,0,0,1,1,1,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Qh = Shapes(M, trns, "violet")
allshapes.append(Qh)

M = [[0,0,0,0,0,0,0],
[0,1,0,0,0,0,0],
[0,1,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

Qih = Shapes(M, trns, "hotpink")
allshapes.append(Qih)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,1,1,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

BBh = Shapes(M, trns, "pink")
allshapes.append(BBh)

M = [[0,0,0,0,0,0,0],
[0,1,1,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

BBih = Shapes(M, trns, "lightpink")
allshapes.append(BBih)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,1,1,1,0],
[0,0,0,1,0,1,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

CCh = Shapes(M, trns, "darkmagenta")
allshapes.append(CCh)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,1,1,1,0,0,0],
[0,1,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

CCih = Shapes(M, trns, "mediumpurple")
allshapes.append(CCih)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,1,0,1,0,0],
[0,0,1,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

DDh = Shapes(M, trns, "dodgerblue")
allshapes.append(DDh)


M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,1,0,0,0],
[0,0,1,1,0,0,0],
[0,0,1,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

EEh = Shapes(M, trns, "cornflowerblue")
allshapes.append(EEh)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,0,1,0,0],
[0,0,0,0,0,0,0]]

trns = 4

EEih = Shapes(M, trns, "powderblue")
allshapes.append(EEih)


M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,1,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,1,1,1,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

FFh = Shapes(M, trns, "darkturquoise")
allshapes.append(FFh)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,0,1,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

GGh = Shapes(M, trns, "mediumturquoise")
allshapes.append(GGh)

M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,1,0,0],
[0,0,1,1,1,0,0],
[0,0,1,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

HHh = Shapes(M, trns, "mediumseagreen")
allshapes.append(HHh)


M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,1,0,0,0,0,0],
[0,1,1,1,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 4

HHih = Shapes(M, trns, "chartreuse")
allshapes.append(HHih)


M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,1,0,0],
[0,0,0,1,1,0,0],
[0,0,1,1,0,0,0],
[0,0,1,0,0,0,0],
[0,0,0,0,0,0,0]]

trns = 2

Wh = Shapes(M, trns, "salmon")
allshapes.append(Wh)


M = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,1,0,0,0,0],
[0,0,1,1,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,0,1,0,0],
[0,0,0,0,0,0,0]]

trns = 2

Wih = Shapes(M, trns, "lawngreen")
allshapes.append(Wih)

def GiveNext():
	global allshapes
	NS = random.choice(allshapes)
	return(NS)

def GiveIndex(shp):
	global allshapes
	return allshapes.index(shp)

def GiveShape(ndx):
	global allshapes
	return allshapes[ndx]