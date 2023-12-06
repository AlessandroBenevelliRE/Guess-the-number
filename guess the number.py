import random 
def guess3(min, max): 

  a = min
  b = max
  nr_generato = random.randint(a, b)

  nr_scelto = 0  

  while nr_scelto != nr_generato: 
   
    nr_scelto = int(input(f'Scegli un numero tra {a} e {b}: '))

    
    if (nr_scelto != nr_generato):
      if ((nr_scelto != nr_generato) & (abs(nr_scelto - nr_generato)/(b-a) < 0.03)): 
        print('Fuoco!')
      elif (abs(nr_scelto - nr_generato)/(b-a) <= 0.05): 
        print('Fuochino!')
      elif (abs(nr_scelto - nr_generato)/(b-a) <= 0.1): 
        print('Acqua!')
      else: 
        print('Oceano!')
  else: 
    print('Congratulazioni, hai indovinato il numero!')
   
guess3(1, 100)# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

