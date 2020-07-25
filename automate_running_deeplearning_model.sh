#!/bin/bash

# this script save my life when I was doing automated agricultural analysis course
# we have field image of 18 weeks. 
# in the 2d model, we tried to predict crop production from individual weeks
# For each week, I have to manually take one week image from Field_1 and Nassar
# place them in a data folder then preprocess, train, test the model.
# put the results according to week name. 
# imagine how painful the tasks is for 18 weeks.
# I write this script to automate the pain.
# as I am running the model from terminal so the manual effort is very high. 
# with the script, I went to sleep and bam. I am done with 18 week results. 


for counter in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18
do
	echo $counter
	
	cp -r  Fields_main/Field_1/$counter/ Fields/Field_1
        cp -r Fields_main/Nassar/$counter/  Fields/Nassar	
	
	mkdir results
    mkdir data
    python data_gen.py
    python training.py
    python results.py

	mv results result$counter
	mv  result$counter all_results
	
	
	rm -r data

        rm -r Fields/Field_1/$counter/
        rm -r Fields/Nassar/$counter/
done


