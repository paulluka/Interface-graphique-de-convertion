#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  convertion.py
#  Paul Lukasiewicz et Ilyess Boussif

#import des modules
from tkinter import * # interface graphique


#------------------------------------------------------------------------------------
def main():

	def convertion_binaire_en_decimal() :
		"""
			Convertis le binaire en décimale avec gestion d'erreur(taille de l'octet ...)
			
			reponse_binaire local type str
			reponse_binaire local type str
			saisie_octet le str rentré dans le widget
			
			retourne reponse_decimale
		
		"""
		
		reponse_binaire = saisie_octet.get()#On recupere la valeure saisie dans le widget

		reponse_decimale = 0 	#init la variable qui acceuil la convertion
		
		#verifier que on a bien 1 octet
		while len(reponse_binaire)!=8 :  
			reponse_binaire = input("Merci d'écrire ce nombre sur 8 bits : ") 
		
		#on converti et on stock dans reponse_decimale
		for k in range(8):
			reponse_decimale= reponse_decimale +int(reponse_binaire[7-k])*2**k

		#affichage console pour debbugage
		#print("Le nombre binaire " , reponse_binaire , "vaut ", reponse_decimale , " en base 10.")
		
		#on retourne la valeure de reponse_decimale
		return reponse_decimale
		
	def convertir_en_hexadecimale():	
		"""
		retourne la valeure hexadecimale de reponse_decimale
		"""

		return hex(convertion_binaire_en_decimal())


	#On regarde quelle base a été selectionée

	#base 10 et 16 choisis
	if reponse_base_dix.get() == 1:
		print(convertion_binaire_en_decimal())
		if reponse_base_seize.get() == 1:
			print(convertir_en_hexadecimale())
	#base 16 choisie
	if reponse_base_dix.get() == 0:
		if reponse_base_seize.get() == 1:
			print(convertir_en_hexadecimale())

	#Si rien n'est sélctionnée
	if reponse_base_dix.get() == 0 and reponse_base_seize.get() == 0:
		reponse_base_dix.set(1)
		reponse_base_seize.set(1)

		#------------------------------------------------------------
		# Création de l'interface de reponse
		#------------------------------------------------------------
		


#------------------------------------------------------------------------------------------------
#Création de l'interface graphique
#---------------------------------

# Premiere fenetre interface_insertion
interface_insertion = Tk()
interface_insertion.geometry("300x100")
interface_insertion.title("Convertion d'un nombre binaire")


#  text de Saisie de l'octet
text_saisir_octet = Label(interface_insertion, text="Saisir l'octet a convertir : ")
text_saisir_octet.grid(row=0, column=0)

#text de choix convertion
text_choix_base = Label(interface_insertion, text="Convertir en : ")
text_choix_base.grid(row=1, column=0)

#Boutton de validataion 
boutton_valider = Button(interface_insertion, text="valider", command=main)
boutton_valider.grid(row=3, column=0)

#saisir l'octet
saisie_octet = Entry(interface_insertion)
saisie_octet.grid(row=0, column=1)

#saisir la base 
reponse_base_dix = IntVar()
reponse_base_dix.set(1)
saisie_choix_base_dix = Checkbutton(interface_insertion, text="décimale", variable=reponse_base_dix)
saisie_choix_base_dix.grid(row=1, column=1)

reponse_base_seize = IntVar()
reponse_base_seize.set(0)
saisie_choix_base_seize = Checkbutton(interface_insertion, text="hexadecimale", variable=reponse_base_seize, onvalue=1, offvalue=0)
saisie_choix_base_seize.grid(row=2, column=1)

#boutton quitter
boutton_quitter = Button(text="Quitter", command=interface_insertion.destroy)
boutton_quitter.grid(row=3, column=1)


interface_insertion.mainloop()







