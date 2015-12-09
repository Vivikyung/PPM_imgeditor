# -*- coding: utf-8 -*-
"""
effects module for assignment 4
Created on Sat Nov  7 15:31:36 2015

@author: Vivian Shen vhs2106
"""

def apply_effects(in_filename, out_filename, effects, filter_filenames):
    '''primary function that is called by the effects_tester. 
    in_filename the name the primary input file 
    out_filename refers is the name of the output file
    effects is a list of booleans where each position indicates whether we want
    that effect activated
	effects[0] object_filter
 	effects[1] shades_of_gray
	effects[2] indicates negate_red
	effects[3] indicates negate_green
	effects[4] indicates negate_blue
	effects[5] indicates mirror

    filter_filenames stores the names of additional files for the object_filter
    I made the list of needed files for object_filter in my effects_tester,
    so filter_filenames is already a list of files instead of individual files.
    	''' 
    #runs one case at a time. continuously called by effects_tester
    if effects[0]:
        object_filter(filter_filenames, out_filename)
    elif effects[1]:
        shades_of_gray(in_filename, out_filename)
    elif effects[2]:
        negate_red(in_filename, out_filename)
    elif effects[3]:
        negate_green(in_filename, out_filename)
    elif effects[4]:
        negate_blue(in_filename, out_filename)
    elif effects[5]:
        mirror(in_filename, out_filename)
     
import statistics
def object_filter(in_file_list, out_file):
    '''Filters out pixel values that appear in only a minority
    of the images in the parameter in_file_list'''
    img = []
    for i in range(0,len(in_file_list)):    
        file = open(in_file_list[i], 'r')
        temp = []
        for line in file:
            temp.append(line.split()) 
        img.append(temp) #stores the multiple files' contents in a list
    out = open(out_file, 'w')
    full_pic = []
    for j in range(3, len(img[0])):
        for k in range(0, len(img[0][j])):
            values = []
            for i in range(0, len(img)):
                values.append(img[i][j][k])
            #finds the mode of the multiple files' pixel values
            full_pic.append(str(statistics.mode(values)) + ' ') 
    count = 0
    new_line = len(img[0][4])
    out.write(img[0][0][0] + '\n' + img[0][1][0] + ' ' + img[0][1][1] \
            + '\n' + img[0][2][0] + '\n') #prints out the header
    for i in full_pic:
        count += 1
        out.write(i) #prints out the body pixel values
        if count == new_line:
            out.write('\n')
            count = 0
    out.close()

def shades_of_gray(in_file, out_file):
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

def negate_red(in_file, out_file):
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
    
def negate_green(in_file, out_file):
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

def negate_blue(in_file, out_file):
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
    
def mirror(in_file, out_file):
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
