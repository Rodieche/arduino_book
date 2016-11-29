#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import sys, time, serial, os
#port = raw_input("Por favor seleccione el Puerto: ")
serialPort = '/dev/ttyACM0'
arduinoPort = serial.Serial(serialPort, 9600)
code1 = "LA ID DE LA TARJETA ES : 4294965045"
code2 = "LA ID DE LA TARJETA ES : 13918"
code3 = "LA ID DE LA TARJETA ES : 26369"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#							DATABASE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#	AUTOR
book_author = {code1 : "Stephen King", code2 : "Carlos Sisi", code3 : "Sebastian Hernaiz"}

#	TITULOS
book_title = {code1 : "Cementerio de Animales", code2 : "Los Caminantes", code3 : "El Arte de la Guerra en el Poker"}

#	SINOPSIS
book_sinopsis = {code1 : "Church estaba allí otra vez, como Louis Creed temía y deseaba. Porque su hijita Ellie le había encomendado que cuidara del gato, y Church había muerto atropellado. Louis lo había comprobado: el gato estaba muerto, incluso lo había enterrado más allá del cementerio de animales. Sin embargo, Church había regresado,y sus ojos eran más crueles y perversos que antes. Pero volvía a estar allí y Ellie no lo lamentaría. Louis Creed sí lo lamentaría. Porque más allá del cementerio de animales, más allá de la valla de troncos que nadie se atrevía a trasponer, más allá de los cuarenta y cinco escalones, el maligno poder del antiguo cementerio indio le reclamaba con macabra avidez... ﻿", code2 : "Nadie sabía cómo había empezado todo, exactamente. El mundo se había desestabilizado mucho antes de que ningún científico hubiese podido dar alguna explicación. Ningún programa de televisión aguantó el tiempo suficiente como para teorizar sobre el problema. Al principio podías verlo en la televisión. Hablaban sobre ello - muy poco al principio, pero luego cada vez más; en la televisión basura de la noche, en los programas nocturnos líderes de audiencia, hasta que ya no se hablaba de otra cosa y la noticia del año lo inundaba todo. ", code3 : "Cartas si, azar tambien... Pero el Poker es mucho mas que eso. Es un juego en el que personas apuestan contra otras personas sin conocer toda la informacion necesaria para saber si la apuesta es correcta o incorrecta. El Poker consiste en poder averiguar aquello que no se sabe y en evitar que nuestros rivales averigüen lo que no saben de nosotros. Partiendo de esta premisa, el jugador de poker puede cruzar el umbral tan deseado e ingresar al selecto grupo de los victoriosos, entendiendo que no sera la suerte sino nuestra estrategia para completar la informacion la que determinara si perdemos o ganamos. "}

#	PRECIOS
book_price = {code1 : 250, code2: 460, code3: 80}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#							CODE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while True:
	os.system('clear')
	print "Pase su libro por el lector"
	code = (arduinoPort.readline().strip())
	os.system('clear')
	print "#######################################################################"
	print ""
	print "SISTEMA DE BIBLIOTECA                             "
	print ""
	print "#######################################################################"
	print ""
	print "# %s"%(code)
	print "# Autor : %s "% (book_author[code])
	print "# Titulo : %s "% (book_title[code])
	print "# Sinopsis : %s"% (book_sinopsis[code])
	print "# Precio : $%i" % (book_price[code])
	print ""
	print "#######################################################################"
	print ""
	print "GRACIAS POR USAR NUESTRO SISTEMA DE BIBLIOTECAS"
	print "Sistema Generado por Castillo Marcos y Echenique Rodolfo ©"
	print ""
	print "#######################################################################"
	time.sleep(15)
