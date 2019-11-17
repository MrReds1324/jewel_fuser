# jewel_fuser
Command line script written in python to run simulations for fusing 5 SSS jewels
- Requires Python 3.2 or higher 

Download or clone the repository to a directory of your choice

Navigate to the directory where the script is and run the script by calling ```python jewel_fusing.py <FILE NAME> <NUM OF SIMULATIONS>```

#Command line arguments
Optional arguments:
- -h shows the help
- -o output directory for the files, default will output the files to the same directory you call the script from
- -l the lucky type of jewel to use [A, S, SS]

Required arguments:
- file name
- number of simulations

#Example Run
```python jewel_fusing.py -o E:\ouput -l SS lucky_fuse 1000```