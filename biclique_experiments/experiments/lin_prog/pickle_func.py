import pickle

def save_object(obj, filename):
    with open(filename, 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

def open_pkl_file(filename):
    with open(filename, 'rb') as inp:
        obj = pickle.load(inp)
        return obj
