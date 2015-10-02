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
