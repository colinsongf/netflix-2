import numpy as np

# Number of users in all.dta
NUM_USERS = 458293

# Number of movies
NUM_MOVIES = 17770

# Open files using a large buffer
alldata = open("mu/all.dta", "r", buffering=(2<<26))
index = open("mu/all.idx", "r", buffering=(2<<26))

# Raw data. A list of numpy arrays containing (movie, rating) pairs
# raw = [None for i in range(NUM_USERS + 1)]

# For mu:
raw = [None for i in range(NUM_MOVIES + 1)]


while True:
    data = alldata.readline()
    idx = index.readline()

    if data == "":
        break

    # convert data into a list of ints => [user, movie, date, rating]
    data = data.split()

#     data = [int(data[0]), np.int16(data[1]), np.int16(data[2]), np.int16(data[3])]

    # For mu
    data = [int(data[0]), np.int16(data[1]), np.int16(data[2]), np.int16(data[3])]

#     if data[0] % 10000 == 0:
#         print data[0]

    # For mu
    if data[1] % 10000 == 0:
        print data[1]


    idx = int(idx)

    # If it corresponds to the training set
#     if idx in [1, 2, 3]:

    # If it's training
    if idx in [1, 2, 3]:

#         # If we already have this user, add (movie, rating) tuple to array
#         if raw[data[0]] != None:
#             raw[data[0]] = np.append(raw[data[0]], (data[1], data[3]))
# 
#         # Else create array
#         else:
#             raw[data[0]] = np.array((data[1], data[3]), dtype=np.int16)


        # For mu

        # If we already have this movie, add (user, rating) tuple to array
        if raw[data[1]] != None:
            raw[data[1]] = np.append(raw[data[1]], (data[0], data[3]))

        # Else create array
        else:
            raw[data[1]] = np.array((data[0], data[3]), dtype=np.int32)
        



