import pygame
import PModules.PShapes

pygame.init()


#colors (possibly) used
coldict = {"maroon" : (128,0,0),
"darkred" : (139,0,0),
"brown" : (165,42,42),
"firebrick" : (178,34,34),
"crimson" : (220,20,60),
"red" : (255,0,0),
"tomato" : (255,99,71),
"coral" : (255,127,80),
"indianred" : (205,92,92),
"lightcoral" : (240,128,128),
"darksalmon" : (233,150,122),
"salmon" : (250,128,114),
"lightsalmon" : (255,160,122),
"orangered" : (255,69,0),
"darkorange" : (255,140,0),
"orange" : (255,165,0),
"gold" : (255,215,0),
"darkgoldenrod" : (184,134,11),
"goldenrod" : (218,165,32),
"palegoldenrod" : (238,232,170),
"darkkhaki" : (189,183,107),
"khaki" : (240,230,140),
"olive" : (128,128,0),
"yellow" : (255,255,0),
"yellowgreen" : (154,205,50),
"darkolivegreen" : (85,107,47),
"olivedrab" : (107,142,35),
"lawngreen" : (124,252,0),
"chartreuse" : (127,255,0),
"greenyellow" : (173,255,47),
"darkgreen" : (0,100,0),
"green" : (0,128,0),
"forestgreen" : (34,139,34),
"lime" : (0,255,0),
"limegreen" : (50,205,50),
"lightgreen" : (144,238,144),
"palegreen" : (152,251,152),
"darkseagreen" : (143,188,143),
"mediumspringgreen" : (0,250,154),
"springgreen" : (0,255,127),
"seagreen" : (46,139,87),
"mediumaquamarine" : (102,205,170),
"mediumseagreen" : (60,179,113),
"lightseagreen" : (32,178,170),
"darkslategray" : (47,79,79),
"teal" : (0,128,128),
"darkcyan" : (0,139,139),
"aqua" : (0,255,255),
"cyan" : (0,255,255),
"lightcyan" : (224,255,255),
"darkturquoise" : (0,206,209),
"turquoise" : (64,224,208),
"mediumturquoise" : (72,209,204),
"paleturquoise" : (175,238,238),
"aquamarine" : (127,255,212),
"powderblue" : (176,224,230),
"cadetblue" : (95,158,160),
"steelblue" : (70,130,180),
"cornflowerblue" : (100,149,237),
"deepskyblue" : (0,191,255),
"dodgerblue" : (30,144,255),
"lightblue" : (173,216,230),
"skyblue" : (135,206,235),
"lightskyblue" : (135,206,250),
"midnightblue" : (25,25,112),
"navy" : (0,0,128),
"darkblue" : (0,0,139),
"mediumblue" : (0,0,205),
"blue" : (0,0,255),
"royalblue" : (65,105,225),
"blueviolet" : (138,43,226),
"indigo" : (75,0,130),
"darkslateblue" : (72,61,139),
"slateblue" : (106,90,205),
"mediumslateblue" : (123,104,238),
"mediumpurple" : (147,112,219),
"darkmagenta" : (139,0,139),
"darkviolet" : (148,0,211),
"darkorchid" : (153,50,204),
"mediumorchid" : (186,85,211),
"purple" : (128,0,128),
"thistle" : (216,191,216),
"plum" : (221,160,221),
"violet" : (238,130,238),
"magenta" : (255,0,255),
"orchid" : (218,112,214),
"mediumvioletred" : (199,21,133),
"palevioletred" : (219,112,147),
"deeppink" : (255,20,147),
"hotpink" : (255,105,180),
"lightpink" : (255,182,193),
"pink" : (255,192,203),
"antiquewhite" : (250,235,215),
"beige" : (245,245,220),
"bisque" : (255,228,196),
"blanchedalmond" : (255,235,205),
"wheat" : (245,222,179),
"cornsilk" : (255,248,220),
"lemonchiffon" : (255,250,205),
"lightgoldenrodyellow" : (250,250,210),
"lightyellow" : (255,255,224),
"saddlebrown" : (139,69,19),
"sienna" : (160,82,45),
"chocolate" : (210,105,30),
"peru" : (205,133,63),
"sandybrown" : (244,164,96),
"burlywood" : (222,184,135),
"tan" : (210,180,140),
"rosybrown" : (188,143,143),
"moccasin" : (255,228,181),
"navajowhite" : (255,222,173),
"peachpuff" : (255,218,185),
"mistyrose" : (255,228,225),
"lavenderblush" : (255,240,245),
"linen" : (250,240,230),
"oldlace" : (253,245,230),
"papayawhip" : (255,239,213),
"seashell" : (255,245,238),
"mintcream" : (245,255,250),
"slategray" : (112,128,144),
"lightslategray" : (119,136,153),
"lightsteelblue" : (176,196,222),
"lavender" : (230,230,250),
"floralwhite" : (255,250,240),
"aliceblue" : (240,248,255),
"ghostwhite" : (248,248,255),
"honeydew" : (240,255,240),
"ivory" : (255,255,240),
"azure" : (240,255,255),
"snow" : (255,250,250),
"black" : (0,0,0),
"dimgrey" : (105,105,105),
"grey" : (128,128,128),
"darkgrey" : (169,169,169),
"silver" : (192,192,192),
"lightgrey" : (211,211,211),
"gainsboro" : (220,220,220),
"whitesmoke" : (245,245,245),
"white" : (255,255,255)}

LB = 1
TL = 3
BS = 30
AW = 25
AH = 30
SB = 300
WT = 750


#window, to be changed later
window = pygame.display.set_mode((1,1))

def DwArea(dsc, fnsh):
	global LB
	global TL
	global BS
	global AW
	global AH
	global SB
	global coldict
	global window
	
	wdth = AW*BS + TL + TL + SB
	hght = AH*BS + TL + TL
	window = pygame.display.set_mode((wdth, hght))
	window.fill(coldict["white"])
	pygame.display.set_caption("Polytris game")
	
	
	#Write texts
	tfont = pygame.font.SysFont("Arial", 30)
	bfont = pygame.font.SysFont("Arial", 60)
	efont = pygame.font.SysFont("Arial", 90)
	tkeys = tfont.render("Game control keys:", False, coldict["black"])
	tesc = tfont.render("ESC to exit", False, coldict["black"])
	tp = tfont.render("P to pause", False, coldict["black"])
	ts = tfont.render("S to save", False, coldict["black"])
	tlo = tfont.render("L to load", False, coldict["black"])
	tau = tfont.render("UP to flip", False, coldict["black"])
	tad = tfont.render("DOWN to move down", False, coldict["black"])
	tal = tfont.render("LEFT to move left", False, coldict["black"])
	tar = tfont.render("RIGHT to more right", False, coldict["black"])
	scr = bfont.render("SCORE", False, coldict["black"])
	nx = bfont.render("NEXT", False, coldict["black"])
	dscst = bfont.render(str(dsc), False, coldict["black"])
	gm = efont.render("GAME", False, coldict["red"])
	ov = efont.render("OVER", False, coldict["red"])
	svd = efont.render("SAVED", False, coldict["red"])
	sfl = efont.render("SUCCESSFULLY", False, coldict["red"])
	ldd = efont.render("LOADED DATA", False, coldict["red"])
	crpt = efont.render("CORRUPTED", False, coldict["red"])
	
	window.blit(tkeys, (AW*BS + TL + TL + (SB - tkeys.get_width())//2,40))
	window.blit(tesc, (AW*BS + TL + TL + (SB - tesc.get_width())//2,80))
	window.blit(tp, (AW*BS + TL + TL + (SB - tp.get_width())//2,120))
	window.blit(ts, (AW*BS + TL + TL + (SB - ts.get_width())//2,160))
	window.blit(tlo, (AW*BS + TL + TL + (SB - tlo.get_width())//2,200))
	window.blit(tau, (AW*BS + TL + TL + (SB - tau.get_width())//2,240))
	window.blit(tad, (AW*BS + TL + TL + (SB - tad.get_width())//2,280))
	window.blit(tal, (AW*BS + TL + TL + (SB - tal.get_width())//2,320))
	window.blit(tar, (AW*BS + TL + TL + (SB - tar.get_width())//2,360))
	
	window.blit(scr, (AW*BS + TL + TL + (SB - scr.get_width())//2,450))
	window.blit(dscst, (AW*BS + TL + TL + (SB - dscst.get_width())//2,520))
	window.blit(nx, (AW*BS + TL + TL + (SB - nx.get_width())//2,600))
	
	if fnsh == 1:
		#Send game over message
		window.blit(gm, ((AW*BS - gm.get_width())//2,250))
		window.blit(ov, ((AW*BS - ov.get_width())//2,450))
		
		pygame.display.update()
	
	elif fnsh == 2:
		#Send game over message
		window.blit(svd, ((AW*BS - svd.get_width())//2,250))
		window.blit(sfl, ((AW*BS - sfl.get_width())//2,450))
		
		pygame.display.update()
	
	elif fnsh == 3:
		#Send game over message
		window.blit(ldd, ((AW*BS - ldd.get_width())//2,250))
		window.blit(crpt, ((AW*BS - crpt.get_width())//2,450))
		
		pygame.display.update()


def DwGrid():
	global LB
	global TL
	global BS
	global AW
	global AH
	global SB
	global coldict
	global window
	
	#Draw inside grid of main window
	for cnt in range (AH):
		pygame.draw.line(window,coldict["grey"],[0,TL + cnt * BS], [TL + BS*AW, TL + cnt * BS], LB)
	for cnt in range (AW):
		pygame.draw.line(window,coldict["grey"],[TL + cnt * BS, 0],[TL + cnt*BS, TL + BS * AH], LB)
	
	#Draw rectangle delimiting main window
	pygame.draw.rect(window, coldict["black"], [0,0,AW*BS+2*TL, AH*BS + 2*TL], TL)
	
	
	#Draw inside grid of next window
	for cnt in range(6):
		pygame.draw.line(window,coldict["grey"],[818,703 + cnt * BS], [998, 703 + cnt * BS], LB)
	for cnt in range(6):
		pygame.draw.line(window,coldict["grey"],[818 + cnt * BS,703], [818 + cnt * BS, 883], LB)
	
	#Draw rectangle delimiting next window
	pygame.draw.rect(window, coldict["black"], [815,700,6*BS + 2*TL, 6*BS + 2*TL], TL)
	
	pygame.display.update()

def DisplayShape(shp, xp, yp, cr):
	global BS
	global window
	global coldict
	
	for cntr in range(7):
		for cntc in range(7):
			if shp.CurrRotation(cr)[cntc][cntr] == 1:
				pygame.draw.rect(window, coldict[shp.color],[xp + cntr * BS - BS*0.5, yp + cntc * BS -BS * 0.5, BS, BS],0)
				pygame.draw.rect(window, coldict["white"],[xp + cntr * BS - BS*0.5 + 3, yp + cntc * BS -BS * 0.5 + 3, BS - 6, BS - 6],2)
	#print(shp.blocklayout)
	#print(shp.CurrRotation(0))
	#pygame.display.update()

def DwFill(fl):
	global BS
	global window
	global coldict
	global AW
	global AH
	global TL
	
	pygame.draw.rect(window,coldict["white"], [TL, TL, BS*AW, BS*AH], 0)
	for cntr in range(AW):
		for cntc in range(AH):
			if fl[cntc][cntr] != 0:
				pygame.draw.rect(window, coldict[fl[cntc][cntr]], [cntr * BS + TL, cntc * BS + TL, BS, BS],0)
				pygame.draw.rect(window, coldict["white"],[cntr * BS + 3 + TL, cntc * BS + 3 + TL, BS - 6, BS - 6],2)

def DisplayNext(nxt):
	DisplayShape(nxt, 804, 719, 0)

