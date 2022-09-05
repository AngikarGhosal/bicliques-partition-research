import pickle

def save_object(obj, filename):
    with open(filename, 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

def open_pkl_file(filename):
    with open(filename, 'rb') as inp:
        obj = pickle.load(inp)
        return obj

def print_to_dual(f,ans,y,prob,program):

    # Print result.
    f.write("\nThe optimal value is ")
    f.write(str(ans))
    f.write("\nA solution y is ")
    f.write(str(y.value))
    f.write("\n")
    for i in range(len(y.value)):
        if (y.value)[i]>0.01 or (y.value)[i]<-0.01:
            f.write(str(i))
            f.write(", ")
            f.write(str((y.value)[i]))
            f.write("\n")
    f.write("DUAL\n")
    if prob.constraints[0].dual_value is not None:
        f.write(str(prob.constraints[0].dual_value))
    else:
        f.write("DUAL DOES NOT EXIST\n")
    f.write("DUAL OVER\n")
    return
