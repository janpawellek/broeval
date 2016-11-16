
# Write results to this file
OUTFILE = 'runs/src8-tgt4/seq-bro-iter04000.result.csv'

# Source computers for the requests
SOURCE = ['10.0.0.11', '10.0.0.12', '10.0.0.13', '10.0.0.14', '10.0.0.31', '10.0.0.32', '10.0.0.33', '10.0.0.34']

# Should Bro be enabled on the source machines?
SOURCE_BRO = [True, True, True, True, True, True, True, True]

# Target machines for the requests (aka server)
TARGET = ['10.0.0.21', '10.0.0.22', '10.0.0.23', '10.0.0.24']

# Should Bro be enabled on the target machines?
TARGET_BRO = [True, True, True, True]

# Connection mode (par = parallel, seq = sequential)
MODE = 'seq'

# Number of evaluation repetitions to run
EPOCHS = 100

# Number of iterations to be run in each evaluation repetition
ITER = 4000

# Size of the file to be downloaded from target (in Bytes * 10^SIZE)
SIZE = 5

