
# Write results to this file
OUTFILE = 'runs/1000KB/src2-tgt1/par-nobro-iter02500.result.csv'

# Source computers for the requests
SOURCE = ['10.0.0.1', '10.0.0.3']

# Should Bro be enabled on the source machines?
SOURCE_BRO = [False, False]

# Target machines for the requests (aka server)
TARGET = ['10.0.0.2']

# Should Bro be enabled on the target machines?
TARGET_BRO = [False]

# Connection mode (par = parallel, seq = sequential)
MODE = 'par'

# Number of evaluation repetitions to run
EPOCHS = 100

# Number of iterations to be run in each evaluation repetition
ITER = 2500

# Size of the file to be downloaded from target (in Bytes * 10^SIZE)
SIZE = 6

