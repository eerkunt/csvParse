# csvParse

This scripts parses a CSV file based on configuration file directives.
```
usage: csvParse [-h] [--verbose] [--version] [--config FILENAME]
                [--output FILENAME] --input FILENAME [--delimeter [DELIMETER]]
                [--strip [CHAR/STRING]]

This scripts reads csvParse.conf file in the current directory and parses the
CSV file based on configurative directives.

optional arguments:
  -h, --help            show this help message and exit
  --verbose, -v         Verbose mode
  --version             Show version
  --config FILENAME, -c FILENAME
                        Use this configuration file instead of ./csvParse.conf
  --output FILENAME, -o FILENAME
                        Filtered results will be written on this output in CSV
                        format.
  --input FILENAME, -i FILENAME
                        Input file that will be parsed ( must be in CSV format
                        )
  --delimeter [DELIMETER], -d [DELIMETER]
                        Use given delimeter in CSV format. Default is ","
  --strip [CHAR/STRING], -s [CHAR/STRING]
                        Strips given character or string from output
```
Based on configuration file, script filters out selected headers into an output file.

# Configuration File

A sample configuration file is shown as below ;
```
# csvParse.conf
# This file is used for configurative directives for csvParse script.
#
# You should just add HEADER/COLUMN names that exists in related CSV file line by line
#
# Example:
# IMPU
# CORE IP
# CORE PORT
# CORE TRP
# IMPLICIT IMPUS
# PBXTYPE
#
# Script will read this config file and ONLY filters out these HEADER/COLUMs
#
IMPU
REMOTE IP
REMOTE PORT
LOCAL IP
NETWORK ID
USER AGENT
BSID
```



