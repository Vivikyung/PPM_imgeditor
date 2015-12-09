# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 00:15:35 2015

@author: Vshen
"""

import effects
import os
def multiple_effects():
    '''Greets the user and lets them choose multiple effects that it applies
    all at once. The program applies the filters in the order that they are
    listed.'''
    print('''Welcome to Portable Pixmap (PPM) Image Editor!
        Choose the effect you would like to try:
        1) object_filter
        2) shades_of_gray
        3) negate_red
        4) negate_green
        5) negate_blue
        6) mirror''')
    file_list = []
    effectnum = input('Enter the numbers of the effects you want, '\
                      'separated by spaces: ')
    effectnum = effectnum.split()
    elist = [0,0,0,0,0,0]
    for i in effectnum:
        elist[int(i) - 1] = 1
    in_file = input('Enter a main input file name: ') #input file name
    out_file = input('Enter name of output file: ') #output file name
    temp_name = out_file
    a = False
    while elist.count(1) != 0: #as long as there are still effects left to apply
        num = elist.index(1)
        if num == 0:
            file_list = input('Enter your three input files, '\
                              'separated by spaces: ').split()
        if os.path.isfile(out_file):
            in_file = temp_name #turns the input file into the previous output file
            out_file = 'temp.ppm' #creates a temporary output file
            a = True
        effects.apply_effects(in_file, out_file, elist, file_list)
        if a == True:
            os.remove(temp_name) #deletes the original output file
            os.rename('temp.ppm', temp_name) #renames the temporary file to output
        elist[num] = 0


multiple_effects()
