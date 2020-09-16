# io_utilities.py

def read_vanilla(filepath):
    with open(filepath, 'r') as fp:
        data = fp.read()
        fp.close()

dataLines = data.split('\n')
dataFinal = [f.split(',') for f in dataLines]

return dataFinal
