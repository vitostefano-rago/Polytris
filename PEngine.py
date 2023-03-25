import pygame
import PModules.PShapes
import PModules.PDisplay
import PModules.PSave
import random

pygame.init()

WT = 750
AW = 25
AH = 30
BS = 30

pf = [[0 for _ in range(AW + 3)] for _ in range(AH + 5)]


def TouchDetect(shp, xp, yp, rp, idir):
	global pf
	
	#Intended direction: 0-down 1-left 2-right 3-rotate
	
	if idir == 0:
		yo, xo, ro = 1, 0, 0
	elif idir == 1:
		yo, xo, ro = 0, -1, 0
	elif idir == 2:
		yo, xo, ro = 0, 1, 0
	elif idir == 3:
		yo, xo, ro = 0, 0, 1
	else:
		yo, xo, ro = 0, 0, 0
	
	co = shp.CurrRotation(rp + ro)
	
	for cntr in range(7):
		for cntc in range(7):
			if co[cntr][cntc] != 0 and pf[yp + cntr + yo][xp + cntc + xo] != 0:
				return 1
	
	return 0

def AddToWall(shp, xp, yp, rp):
	global pf
	
	co = shp.CurrRotation(rp)
	try:
		for cntr in range(7):
			for cntc in range(7):
				if co[cntr][cntc] != 0:
					pf[yp + cntr][xp + cntc] = shp.color
		return 1
	
	except:
		return 0

def FullLineManage():
	global pf
	global AW
	
	cl = len(pf) - 1
	clrd = 0
	
	while cl >= 0:
		if 0 not in pf[cl][0 : AW]:
			clrd += 1
			for cll in range(cl, -1, -1):
				if cll > 0:
					pf[cll] = pf[cll - 1][:]
				if cll == 0:
					pf[0] = [0 for _ in range(AW + 3)]
		
		else:
			cl -= 1
	
	if clrd == 0:
		return 0
	
	else:
		return 3 ** (clrd - 1)

def ArcadeMode(bn):
	global pf
	global AH
	
	if bn % 10 == 2:
		for cl in range (AH):
			if cl == 0 and pf[0].count(0) < len(pf[0]):
				return 0
			pf[cl] = pf[cl + 1][:]
			if cl == AH - 1:
				for cnt in range(len(pf[cl])):
					if random.randint(0,1000) % 10 <= 7:
						pf[cl][cnt] = "darkgrey"
	
	return 1

def main():
	global WT
	global AW
	global BS
	global pf
	
	comingshape = PModules.PShapes.GiveNext()
	currshape = PModules.PShapes.GiveNext()
	rot = 0
	currx = AW // 2 - 3
	curry = -3
	ld = 0
	ff = 1
	psd = 0
	offs = 18
	cscore = 0
	gmor = 0
	cloop = 0
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			
			if event.type == pygame.KEYDOWN:
				#PAUSE
				if event.key == pygame.K_p:
					if psd == 0:
						psd = 1
					elif gmor != 1:
						psd = 0
						gmor = 0
				
				#SAVE
				if event.key == pygame.K_s:
					if psd == 1:
						PModules.PSave.ExportData(pf, cscore, cloop, PModules.PShapes.GiveIndex(currshape), PModules.PShapes.GiveIndex(comingshape), currx, curry, rot)
						gmor = 2
				
				#LOAD
				if event.key == pygame.K_l:
					if psd == 1:
						if PModules.PSave.ImportData()[0] == False:
							#corrupted data
							gmor = 3
						else:
							#No issue with data integrity
							impd = PModules.PSave.ImportData()
							pf = impd[1]
							cscore, cloop = impd[2], impd[3]
							currshape, comingshape = PModules.PShapes.GiveShape(impd[4]), PModules.PShapes.GiveShape(impd[5])
							currx, curry, rot = impd[6], impd[7], impd[8]
				
				#ESCAPE
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
				
				if psd == 0 and gmor == 0:
					#Act on other keys only if game is not currently paused
					if event.key == pygame.K_UP:
						#If there is enough space to rotate, rotate
						if currx - currshape.CurrFree(rot + 1)[3] >= -3 and currx + currshape.CurrFree(rot + 1)[1] <= AW - 4 and curry + currshape.CurrFree(rot + 1)[2] <= AH - 5 and TouchDetect(currshape, currx, curry, rot, 3) == 0:
							rot += 1
					elif event.key == pygame.K_LEFT:
						#If there is enough space to go left, go left
						if currx - currshape.CurrFree(rot)[3] > -3 and TouchDetect(currshape, currx, curry, rot, 1) == 0:
							currx -= 1
					elif event.key == pygame.K_RIGHT:
						#If there is enough space to go right, go right
						if currx + currshape.CurrFree(rot)[1] < AW - 4 and TouchDetect(currshape, currx, curry, rot, 2) == 0:
							currx += 1
					elif event.key == pygame.K_DOWN:
						curry += 1
						ff = 0.2
				
				
				PModules.PDisplay.DwArea(cscore, gmor)
				if gmor == 0:
					PModules.PDisplay.DwFill(pf)
					PModules.PDisplay.DisplayShape(currshape, currx * BS + offs, curry * BS + offs, rot)
					PModules.PDisplay.DisplayNext(comingshape)
					PModules.PDisplay.DwGrid()
				
				
		if pygame.time.get_ticks() >= ld + WT*ff and psd == 0:
			ld = pygame.time.get_ticks()
			
			if TouchDetect(currshape, currx, curry, rot, 0) == 0 and curry + currshape.CurrFree(rot)[2] <= AH - 5:
				#Move down
				curry += 1
			else:
				if AddToWall(currshape, currx, curry, rot) == 0 or ArcadeMode(cloop) == 0:
					#Case of game over, new shape would need to be added too high
					gmor = 1
				else:
					#Call new shape and fix the position of the old one
					rot = 0
					currshape = comingshape
					comingshape = PModules.PShapes.GiveNext()
					curry = -3
					currx = AW // 2 - 3
					ff = 1
					cscore += FullLineManage()
					cloop += 1
					if TouchDetect(currshape, currx, curry, rot, 4) == 1:
						#Case new shape is already touching an old one when called
						gmor = 1
			
			PModules.PDisplay.DwArea(cscore, gmor)
			if gmor == 0:
				PModules.PDisplay.DwFill(pf)
				PModules.PDisplay.DisplayShape(currshape, currx * BS + offs, curry * BS + offs, rot)
				PModules.PDisplay.DisplayNext(comingshape)
				PModules.PDisplay.DwGrid()

main()
