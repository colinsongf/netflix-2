#distutils: language = c++
from libcpp.unordered_map cimport unordered_map

int NUM_USERS = 458293

int NUM_MOVIES = 17770

cdef unordered_map[int, float] cache;


def cache_init():
    cdef int user, len_user, j, u, m

    for u in xrange(NUM_USERS):
        user = um_dta[u]
        len_user = len(user)

        # All values OBO
        for j in range(0, len_user, 2):
            # movie_id
            m = user[j] - 1

            cache[u * NUM_MOVIES + m] = 0.4
    
