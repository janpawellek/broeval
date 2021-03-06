
# Write results to this file
OUTFILE = 'runs/src8-tgt4/seq-nobro-iter00200.result.csv'

# Source computers for the requests
SOURCE = ['10.0.0.11', '10.0.0.12', '10.0.0.13', '10.0.0.14', '10.0.0.31', '10.0.0.32', '10.0.0.33', '10.0.0.34']

# Should Bro be enabled on the source machines?
SOURCE_BRO = [False, False, False, False, False, False, False, False]

# Target machines for the requests (aka server)
TARGET = ['10.0.0.21', '10.0.0.22', '10.0.0.23', '10.0.0.24']

# Should Bro be enabled on the target machines?
TARGET_BRO = [False, False, False, False]

# Connection mode (par = parallel, seq = sequential)
MODE = 'seq'

# Number of evaluation repetitions to run
EPOCHS = 100

# Number of iterations to be run in each evaluation repetition
ITER = 200

# Size of the file to be downloaded from target (in Bytes * 10^SIZE)
SIZE = 5

