##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2021
## Author: Nadia Swit nadia.swit@duke.edu (for ENV859)
##---------------------------------------------------------------------

# Import modules
import sys, os, arcpy

# Set input variables (Hard-wired)
#read file
inputFile = 'V:/ARGOSTracking/Data/ARGOSData/1997dg.txt' #absolute path; strings that are valid paths because point to file
outputFC = "V:/ARGOSTracking/Scratch/ARGOStrack.shp"
#forward slashes or two backwards slashes can work for file path (if only backwards, has diff function)
#creating points where input and output files are going to live

#%% Construct a while loop to iterate through all lines in the datafile

#Open the ARGOS data file for reading 
inputFileObj = open(inputFile, 'r') #open in read only mode

#Get the first line of data, so we can use a while loop
lineString = inputFileObj.readline() #read first line as string, stores as string

#Start the while loop; want to read large files (doesn't store in memory)
#becomes true (because valid string, text in there) - when done running, sets to null object, making the while loop stop iterating
#when it reaches the end, becomes no data value, which trips the while loop
while lineString: 
    #set code to run only if the line contains the string "Date: "
    if ("Date :" in lineString):
        
        #parse the line into a list
        lineData = lineString.split()
        
        #extract attributes from the datum header line
        tagID = lineData [0]
        obsDate = lineData[3]
        obsTime = lineData[4]
        obsLocation = lineData[7]
        
        #extract location info from the next line
        #need to do this because lat/long info in next line (not first line that we already split)
        line2String = inputFileObj.readline()
        
        #parse the line into a list
        line2Data = line2String.split()
        
        #extract the date we need to variables
        obsLat = line2Data[2]
        obsLon = line2Data[5]
        
        #print results to see how we're doing
        print (tagID, obsDate, obsTime, obsLocation, "Lat:"+obsLat,"Long:"+obsLon)
        
    #move to the next line so the while loop progresses
    #moves to this section to execute code if the line doesn't have "Date :"; will skip all the above ^ (no else if statement)
    lineString = inputFileObj.readline()
    
#close the file object
inputFileObj.close()
    