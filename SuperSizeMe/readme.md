# SuperSizeMe

# author: Jakub Szafran
# email: jszafran.pv@gmail.com
# github: github.com/jszafran

Simple python script for expanding csv files to required size.
Example usecase: say suppose you're developing some csv parser
and using input of small size. You'd like to test your program's
behaviour when feeding input of much larger size. 

SuperSizeMe will read your csv input (which could be 1KBs) and
by copying and appending input's rows to output path, will increase 
output file to size you request.

Time benchmark: expanding 1KB csv file to 2GBs took ~60 seconds.

Example usage of script:
#########
import supersizeme

ssm = supersizeme.SuperSizeMe().
	          read_csv('/path/to/input/file.csv').
                  expand_to(500).
                  save_at('/path/to/output/file.csv')

Above snippet would read csv from provided path, estimate how much data
should be created in order to reach 500MBs (expand_to() param) and start
saving output file at path provided.

Quick documentation:
#########

read_csv()

arg1: path (str)
returns: self
Path to input csv file which will be used for populating output file.

arg2: header (boolean, default=True)
returns: self  
Set to True if your input file has header. next() method
is invoked on csv file iterator to capture first line of input as a header.
If set to False, header will not be appended to output file.
It also sets values of internal variables:
                                          self._input_file_path
					  self._input_file_size
#########

expand_to()

arg1: size (int)
returns: self
Size of the input file you're expecting to have.

Please note that calling this function will not trigger any write action
on your filesystem - it is just validating input + setting value of
internal variable self._output_size.
#########

save_at()

arg1: path (str)
returns: self

Saving supersized output to path provided. 
Function estimates iterations required for reaching output size set with 
expand_to() function. Then, if required, appends header and start iterating
and appending input data to output file.
#########
