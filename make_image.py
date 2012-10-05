# import numpy as np
#
# def find_nearest(a, a_find):
#     "Element in nd array a closest to the scalar value a_find"
#     idx = np.abs(a - a_find).argmin()
#     return idx

p_database = [4, 3, 2, 5]

def find_nearest(search_val, array, disabled=[]):
    c_min = float('inf')
    c_idx = -1
    for idx, val in enumerate(array):
        if idx not in disabled and abs(search_val - val) < c_min:
            c_min = abs(search_val - val)
            c_idx = idx
            print c_min
    print "Result", c_idx, array[c_idx]
    return c_idx


disabled = set()
p_image = [1, 2, 3, 4]
p_temp = list(p_database) # clone list (http://stackoverflow.com/questions/2612802/how-to-clone-a-list-in-python)
p_result = []

for p in p_image:
    print "Ny"
    idx = find_nearest(p, p_temp, disabled)
    p_result.append(idx)
    disabled.add(idx)



for i, db_idx in enumerate(p_result):
    p_result[i] = p_database[db_idx]

print p_image
print p_database
print p_result


