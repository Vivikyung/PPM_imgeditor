# PPM_imgeditor
Takes a PPM image and can apply a variety of effects to it.

2 files: effects and effects_tester.

effects:
	This file has every method for editing the files, including object_filter, shades_of_gray, negate_red, negate_green, negate_blue, and mirror. It also contains the master method, apply_effects, that manages the effects.

	object_filter takes in any number of objects and gets rid of unwanted pixels within the objects. 
	I imported and used the statistics library to find the mode pixel value between the files, and then saved that to a new ppm file.

	shades_of_gray takes the RGB values within a file and averages them, so that the entire image turns into shades of gray.

	negate_red takes the red value and negates it by taking subtracting it from 255, the full value of red. 

	negate_green takes the red value and negates it by taking subtracting it from 255, the full value of green. 

	negate_blue takes the red value and negates it by taking subtracting it from 255, the full value of blue. 

	mirror flips the image horizontally by taking the RGB pixel value trios from the right end of the line and putting them at the beginning of the line.

effects_tester:
	This file manipulates the effects file so that the user can specify which effects and which files they want. There is only a main function, which tells the user which effects there are and asks for input and output file names. It will then implement the effects in order and then return a final output file with all the effects applied.
