import pygame
import random
from pygame import *

def principal():
	pantalla = pygame.display.set_mode([480, 500])
	fps = pygame.time.Clock()
	colorFondo = [255,255,255]
	salir = False

	#####Bordes#########
	bordeIz = pygame.Rect(0, 0, 10, 500)
	bordeDer = pygame.Rect(470, 0, 10, 500)
	bordeAr = pygame.Rect(0, 0, 500, 10)
	bordeAb = pygame.Rect(0, 490, 500, 10)

	####Serpiente#######				

	colorSerpiente = [59, 187, 36]
		#serpiente = pygame.Rect(380, 430, 5, 5)
	velocidadX = 0
	velocidadY = 0
	listaSerp = []
	lider_x = 380
	lider_y = 430
	largoSerp = 1

	####Comidas######
	colorComida = [243, 7, 0]

	xcomida = random.randrange(11, 469)
	ycomida = random.randrange(11, 489)
	#comida = pygame.Rect(xcomida, ycomida, 5,5)
	manzana = pygame.sprite.Sprite()
	manzanaImagen = pygame.image.load("manzana.PNG")
	manzana.image = manzanaImagen
	manzana.rect = manzanaImagen.get_rect()
	manzana.rect.left = xcomida
	manzana.rect.top = ycomida
	comidaYaComida = []

	####Variables auxiliares#####
	ha_chocado = False
	fuente = pygame.font.Font("letrasjuego.ttf", 35)
	texto = fuente.render("Has perdido :(",2,[255,255,255])
	pregunta = fuente.render("¿Quieres jugar de nuevo?",2,[255,255,255])
	XD = fuente.render("XD", 2, [255,255,255])
	fuenteOpcion = pygame.font.Font("letrasjuego.ttf", 25)
	colorLetraJugar = [232, 232, 232]
	colorLetraSalir = [232, 232, 232]
	jugarDeNuevo = fuenteOpcion.render("JUGAR",2,colorLetraJugar)
	quieroSalir = fuenteOpcion.render("MENU",2,colorLetraSalir)

	colorJugar = [39, 144, 13]
	colorSalir = [144, 13, 13]
	botonJugar = pygame.Rect(180, 280, 150, 60)
	botonSalir = pygame.Rect(180, 380, 150, 60)
	rectMouse = pygame.Rect(20, 20, 1,1)
	sobreMouseJugar = [51, 203, 13]
	sobreMouseSalir = [210, 26, 26]
	sobreMouse = False

####Sonidos#########
	comer = pygame.mixer.Sound("comer.wav")
	sonidoBoton = pygame.mixer.Sound("botones.wav")

	####Bucle principal#######
	while salir != True:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				salir = True
			if evento.type == pygame.MOUSEBUTTONDOWN:
				if rectMouse.colliderect(botonJugar):
					sonidoBoton.play()
					principal()
				elif rectMouse.colliderect(botonSalir):
					sonidoBoton.play()
					menu()
			if ha_chocado == False:
				if evento.type == pygame.KEYDOWN:
					if evento.key == pygame.K_UP:
						velocidadY = - 4
						velocidadX = 0

					elif evento.key == pygame.K_DOWN:
						velocidadY = 4
						velocidadX = 0

					elif evento.key == pygame.K_LEFT:
						velocidadX = - 4
						velocidadY = 0

					elif evento.key == pygame.K_RIGHT:
						velocidadX = 4
						velocidadY = 0

	######En pantalla#########
		fps.tick(60)
		pantalla.fill(colorFondo)
		pantalla.blit(manzana.image, manzana.rect)
		lider_x += velocidadX
		lider_y += velocidadY
		cabeza = []
		cabeza.append(lider_x)
		cabeza.append(lider_y)
		listaSerp.append(cabeza)

		if len(listaSerp) > largoSerp:
			del listaSerp[0]

		for cadaSegmento in listaSerp[:-1]:
			if cadaSegmento == cabeza:
				ha_chocado = True

	########Al mover la serpiente#########
		def movimientos(listaSerp):
			global serpiente
			global punta
			for XeY in listaSerp:
				serpiente = pygame.Rect([XeY[0],XeY[1],5,5])
				pygame.draw.rect(pantalla, colorSerpiente, serpiente)#Vibora

		movimientos(listaSerp)

		if serpiente.colliderect(bordeIz) or serpiente.colliderect(bordeDer) or serpiente.colliderect(bordeAb) or serpiente.colliderect(bordeAr):
			ha_chocado = True

		if ha_chocado == True:

			pantalla.fill([99, 120, 255])
			pygame.draw.rect(pantalla, [255,255,255], rectMouse)			
			pygame.draw.rect(pantalla, colorJugar, botonJugar)
			pygame.draw.rect(pantalla, colorSalir, botonSalir)
			pantalla.blit(texto, [140,50])
			pantalla.blit(pregunta, [35, 150])
			pantalla.blit(XD, [228, 200])
			pantalla.blit(jugarDeNuevo, [224, 297])
			pantalla.blit(quieroSalir, [226, 397])
			(rectMouse.left, rectMouse.top) = pygame.mouse.get_pos()
			if rectMouse.colliderect(botonJugar):
				sobreMouse = True
				if sobreMouse == True:
					colorJugar = sobreMouseJugar
					colorLetraJugar = [255,255,255]
			elif rectMouse.colliderect(botonSalir):
				sobreMouse = True
				if sobreMouse == True:
					colorSalir = sobreMouseSalir
					colorLetraSalir = [255,255,255]
			else:
				sobreMouse = False

			if sobreMouse == False:
				colorJugar = [39, 144, 13]
				colorSalir = [144, 13, 13]

	########Las paredes#########
		pygame.draw.rect(pantalla, [0,0,0], bordeAb)
		pygame.draw.rect(pantalla, [0,0,0], bordeAr)
		pygame.draw.rect(pantalla, [0,0,0], bordeIz)
		pygame.draw.rect(pantalla, [0,0,0], bordeDer)
			
	########Al comer############
		if serpiente.colliderect(manzana.rect):
			comer.play()
			comidaYaComida.append(1)
			manzana.rect.left = random.randrange(11,469)
			manzana.rect.top = random.randrange(11,479)
			largoSerp += 1

		pygame.display.update()

def menu():
	pygame.init()
	icono = pygame.image.load("icono.ico")
	pygame.display.set_icon(icono)
	pantalla = pygame.display.set_mode([480, 500])
	pygame.display.set_caption("Serpiente")
	salirse = False
	reloj = pygame.time.Clock()

####Botones#####
	iniciarJuego = pygame.Rect(180, 280, 150, 60)
	quitarJuego = pygame.Rect(180, 380, 150, 60)
	colorIniciar = [39, 144, 13]
	colorQuitar = [144, 13, 13]
	fuenteMenu = pygame.font.Font("letrasjuego.ttf", 25)
	textoIniciar = fuenteMenu.render("JUGAR",2,[255,255,255])
	textoQuitar = fuenteMenu.render("SALIR",2,[255,255,255])
	fuenteMensaje = pygame.font.Font("letrasjuego.ttf", 17)
	sonidoBoton = pygame.mixer.Sound("botones.wav")
####Etiquetas#####
	presentacion = fuenteMensaje.render("Hola XD es mi segundo juego que hago usando python :D",2,[255,255,255])
	miTwitter = fuenteMenu.render("Mi Twitter: @_PabloAvelar",2,[255,255,255])
####Mi logo XD######
	logo = pygame.image.load("logo.JPG")
####Auxiliares menú#######
	superficie = pygame.Rect(20, 20, 1,1)
	cambiarColorIniciar = [51, 203, 13]
	cambiarColorQuitar = [210, 26, 26]
	sobreMouse = False

	while salirse != True:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				salirse = True
			if evento.type == pygame.MOUSEBUTTONDOWN:
				if superficie.colliderect(quitarJuego):
					sonidoBoton.play()
					salirse = True
				elif superficie.colliderect(iniciarJuego):
					sonidoBoton.play()
					principal()
				
	
	####Poner en pantalla######
		reloj.tick(60)
		pantalla.fill([0, 0, 0])
		pygame.draw.rect(pantalla, colorIniciar, iniciarJuego)
		pygame.draw.rect(pantalla, colorQuitar, quitarJuego)
		pygame.draw.rect(pantalla, [0,0,0], superficie)
		pantalla.blit(textoIniciar,[224, 297])
		pantalla.blit(textoQuitar, [226, 397])
		pantalla.blit(presentacion, [40, 10])
		pantalla.blit(miTwitter, [100, 50])
		pantalla.blit(logo, [130, 100])
		(superficie.left, superficie.top) = pygame.mouse.get_pos()

		if superficie.colliderect(iniciarJuego):
			sobreMouse = True
			if sobreMouse == True:
				colorIniciar = cambiarColorIniciar
		elif superficie.colliderect(quitarJuego):
			sobreMouse = True
			if sobreMouse == True:
				colorQuitar = cambiarColorQuitar
		else:
			sobreMouse = False

		if sobreMouse == False:
			colorIniciar = [39, 144, 13]
			colorQuitar = [144, 13, 13]

		pygame.display.update()
	pygame.quit()

if __name__ == "__main__":
	menu()