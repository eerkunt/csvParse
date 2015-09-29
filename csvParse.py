#!/usr/bin/python
#
# csvPare     -  This scripts reads csvParse.conf file in the current directory
#                and parses the CSV file based on configurative directives.
#
# Author            Emre Erkunt
#                   emre.erkunt <at> gmail.com
#
#
# History :
# ---------------------------------------------------------------------------------------------
# Version               Editor          Date            Description
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# 0.0.1_AR              EErkunt         20150929        Initial ALPHA Release
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

import os.path
import re
import argparse
import sys

sys.stdout.flush()

__progName__ = "csvParse"
__author__ = "Emre Erkunt"
__copyright__ = "Copyright 2015, Emre Erkunt"
__credits__ = []
__license__ = "GPL"
__version__ = "0.0.1_AR"
__maintainer__ = "Emre Erkunt"
__email__ = "emre.erkunt at gmail.com"
__status__ = "Development"

# Defaults
defOutputFile = "./output.csv"
defConfigFile = "./csvParse.conf"
defDelimeter = ','

# Background colors
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
# Argument Handling
class argHandling(object):
    pass
    
args = argHandling();
parser = argparse.ArgumentParser(prog=__progName__, description="This scripts reads csvParse.conf file in the current directory and parses the CSV file based on configurative directives.")
parser.add_argument("--verbose", "-v", dest='verbose', action="count", help="Verbose mode")
parser.add_argument("--version", action="version", version='%(prog)s '+__version__, help="Show version")
parser.add_argument("--config", "-c", dest='configFile', metavar='FILENAME', type=file, default=defConfigFile, help="Use this configuration file instead of "+defConfigFile)
parser.add_argument("--output", "-o", dest='outputFile', metavar='FILENAME', type=argparse.FileType('w'), default=defOutputFile, help="Filtered results will be written on this output in CSV format.")
parser.add_argument("--input", "-i", dest="inputFile", required=True, metavar="FILENAME", type=file, default=False, help="Input file that will be parsed ( must be in CSV format )")
parser.add_argument("--delimeter", "-d", dest='delimeter', metavar='DELIMETER', nargs='?', default=defDelimeter, help="Use given delimeter in CSV format. Default is \""+defDelimeter+"\"")
parser.parse_args(namespace=args)

def verboseMsg( level, msg ):
    if args.verbose >= level:
        if level == 1:
            # Normal verbose
            print msg
        elif level == 2:
            print colors.OKBLUE+"[DEBUG ]: "+colors.ENDC+msg
        elif level == 3:
            print colors.HEADER+"[PROTOCOL ]: "+colors.ENDC+msg
    return
    
if args.verbose == 1:
    print "Verbose mode ON"
elif args.verbose == 2:
    print "DEBUG mode ON"
    
# Array/Variable casts
filterOut = []
filterOutIndexes = []
suffix = ""

print __progName__,colors.HEADER+"v"+__version__+colors.ENDC
verboseMsg(1, "Reading configuration file "+colors.BOLD+str(args.configFile.name)+colors.ENDC)
regex = re.compile(r'^(?!#)(.*)')
for line in args.configFile:
    match = regex.search(line)
    if ( match is not None ):
        filterOut.append(match.group(0))
        verboseMsg(1, colors.WARNING+"* Filtering "+str(match.group(0))+"!"+colors.ENDC)

if len(filterOut) > 1:
    suffix = "s"

verboseMsg(1, colors.OKGREEN+str(len(filterOut))+colors.ENDC+" filter"+suffix+" will be applied")
verboseMsg(1, "Delimeter will be "+args.delimeter)

verboseMsg(1, "Parsing "+args.inputFile.name+"..")
lineCount = 0


for line in args.inputFile:
    columns = line.split(args.delimeter)
    # Check for header
    if lineCount == 0:
        for index, columnName in enumerate(columns):
            if ( columnName in filterOut ):
                filterOutIndexes.append(index)
                verboseMsg(2, "Found "+columnName+" on "+str(index)+". index")
        args.outputFile.write(args.delimeter.join(filterOut)+"'\n")
        
    else:
        found = []
        for index, columnValue in enumerate(columns):
            if ( index in filterOutIndexes ):
                found.append(columnValue)
                verboseMsg(2, "Filtered "+columnValue+" on "+str(index)+". index")
        args.outputFile.write(args.delimeter.join(found)+"'\n")     
    
    lineCount += 1
print "Parsing process of "+args.inputFile.name+" into "+args.outputFile.name+" finished."




    
        




            
            
    
            
