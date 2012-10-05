# import numpy as np
#
# def find_nearest(a, a_find):
#     "Element in nd array a closest to the scalar value a_find"
#     idx = np.abs(a - a_find).argmin()
#     return idx
from get_variables import get_variables

from PIL import Image
import urllib, cStringIO, pickle
from math import *

def make_image(*args, **kwargs):
    # img = get_variables.image(url, resize=False, localfile=True)
    img = get_variables.image(*args, **kwargs)
    profile_pic = img.img

    (width, height) = profile_pic.size

    square_size = 300
    # w_count = int(ceil(width / float(square_size)))
    # h_count = int(ceil(height / float(square_size)))
    w_count = width / square_size # NOTE: this relies on integer division
    h_count = height / square_size # NOTE: this relies on integer division

    p_image = []

    xy_list = [(x, y) for x in xrange(w_count) for y in xrange(h_count)]
    for (x,y) in xy_list:
        img_part = get_variables.image(
                     profile_pic.crop(( x    * square_size,  y    * square_size,
                                       (x+1) * square_size, (y+1) * square_size))
                   , type='image')

        p_image.append(img_part.brightness)


    def find_nearest(search_val, array, disabled=[]):
        c_min = float('inf')
        c_idx = -1
        for idx, val in enumerate(array):
            if idx not in disabled and abs(search_val - val) < c_min:
                c_min = abs(search_val - val)
                c_idx = idx
        return c_idx

    database = pickle.load(open("get_variables/images_info.pickle", "rb"))
    p_database = [x[1] for x in database]

    disabled = set()
    p_result = []

    for p in p_image:
        idx = find_nearest(p, p_database, disabled)
        p_result.append(idx)
        # disabled.add(id) # Don't repeat images


    profile_pic.show()

    img_thumbs = {}

    for i, db_idx in enumerate(p_result):
        p_result[i] = p_database[db_idx]

        d_id = database[db_idx][0]
        if d_id not in img_thumbs:
            url = get_variables.parse_id(database[db_idx][0])
            print url
            img_thumbs[d_id] = get_variables.image(database[db_idx][0],
                    square_size, type='id', cache=True).img

        x, y = xy_list[i]
        profile_pic.paste(img_thumbs[d_id], (x * square_size, y * square_size))

    profile_pic.show()

    return profile_pic

