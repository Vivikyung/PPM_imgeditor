# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:31:36 2015

@author: Vivian Shen vhs2106
"""

def application(in_filename, out_filename, effects):
    '''primary function that is called by the effects_tester. 
    in_filename the name the primary input file 
    out_filename refers is the name of the output file
    effects is a list of booleans where each position indicates whether we want
    that effect activated
 	effects[0] shades_of_gray
	effects[1] indicates negate_red
	effects[2] indicates negate_green
	effects[3] indicates negate_blue
	effects[4] indicates mirror
    	''' 
    #runs one case at a time. continuously called by effects_tester
    if effects[0]:
        shades_of_gray(in_filename, out_filename)
    elif effects[1]:
        negate_red(in_filename, out_filename)
    elif effects[2]:
        negate_green(in_filename, out_filename)
    elif effects[3]:
        negate_blue(in_filename, out_filename)
    elif effects[4]:
        mirror(in_filename, out_filename)

def black_and_white(in_file, out_file):
    '''Converts the color image in_file to black and white'''
    img = open(in_file, 'r')
    c = []
    for line in img:
        c.append(line.split())
    img.close()
    out = open(out_file, 'w')
    for j in range(3, len(c)):
        i = 0
        while (i < len(c[j]) - 2):
            #averages the values of the RGB pixel sequence
            temp = str((float(c[j][i]) + float(c[j][i+1]) + float(c[j][i+2]))/3)
            c[j][i] = temp #sets all 3 RGB values to the average
            c[j][i+1] = temp
            c[j][i+2] = temp
            i += 3
    for i in range(0, len(c)):
        for j in range(0, len(c[i])):
            out.write(c[i][j] + " ")
        out.write('\n')
    out.close() 

def red_swap(in_file, out_file):
    '''Negates the red in an image'''
    img = open(in_file, 'r')
    c = []
    for line in img:
        c.append(line.split())
    img.close()
    out = open(out_file, 'w')
    for j in range(3, len(c)):
        i = 0
        while (i < len(c[j])):
            temp = str(255 - float(c[j][i]))
            c[j][i] = temp
            i += 3
    for i in range(0, len(c)):
        for j in range(0, len(c[i])):
            out.write(c[i][j] + " ")
        out.write('\n')
    out.close()
    
def green_swap(in_file, out_file):
    '''Negates the green in an image'''
    img = open(in_file, 'r')
    c = []
    for line in img:
        c.append(line.split())
    img.close()
    out = open(out_file, 'w')
    for j in range(3, len(c)):
        i = 1
        while (i < len(c[j])):
            temp = str(255 - float(c[j][i]))
            c[j][i] = temp
            i += 3
    for i in range(0, len(c)):
        for j in range(0, len(c[i])):
            out.write(c[i][j] + " ")
        out.write('\n')
    out.close()

def blue_swap(in_file, out_file):
    '''Negates the blue in an image'''
    img = open(in_file, 'r')
    c = []
    for line in img:
        c.append(line.split())
    img.close()
    out = open(out_file, 'w')
    for j in range(3, len(c)):
        i = 2
        while (i < len(c[j])):
            temp = str(255 - float(c[j][i]))
            c[j][i] = temp
            i += 3
    for i in range(0, len(c)):
        for j in range(0, len(c[i])):
            out.write(c[i][j] + " ")
        out.write('\n')
    out.close()  
    
def mirror_image(in_file, out_file):
    '''Creates a mirror image by flipping an image horizontally'''
    img = open(in_file, 'r')
    c = []
    for line in img:
        c.append(line.split())
    img.close()
    out = open(out_file, 'w')
    new_pic = [c[0], c[1], c[2]]
    for i in range(3, len(c)):
        a = len(c[i]) - 1
        temp = []
        while a >= 2:
            temp.append(c[i][a-2])
            temp.append(c[i][a-1])
            temp.append(c[i][a])
            a -=3
        new_pic.append(temp)
    for i in range(0, len(new_pic)):
        for j in range(0, len(new_pic[i])):
            out.write(new_pic[i][j] + " ")
        out.write('\n')
    out.close()
