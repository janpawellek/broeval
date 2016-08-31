
# Write results to this file
OUTFILE = 'runs/test2.result.csv'

# Source computer for the requests
SOURCE = ['10.0.0.3']

# Should Bro be enabled on the source machine?
SOURCE_BRO = [True]

# Target machine for the requests (aka server)
TARGET = ['10.0.0.2']

# Should Bro be enabled on the target machine?
TARGET_BRO = [True]

# Connection mode (par = parallel, seq = sequential)
MODE = 'par'

# Number of evaluation repetitions to run
EPOCHS = 5

# Number of iterations to be run in each evaluation repetition
ITER = 1000

# Size of the file to be downloaded from target (in Bytes * 10^SIZE)
SIZE = 5

