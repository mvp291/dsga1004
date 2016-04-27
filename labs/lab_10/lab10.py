
# coding: utf-8

# In[3]:

import spatial as sp
from rtree import index


# ## Part 2 - Using custom code for spatial queries
# 1) Read the taxi data using python.
# 
# 2) Using the provided functions, identify all trips whose drop-off points are in JFK. Report the result size and query execution time.
# This is accomplished by iterating through all trips, and for each trip checking whether the drop-off location is within the query polygon of not. 
# 
# 3) Identify all trips whose drop-off points are in LaGuardia, using the same technique as above. Report the result size and query execution time.

# In[4]:

def read_polygons(filename):
    polygons = {}
    poly = open(filename, 'r')
    
    while True:
        try:
            line = poly.readline()
            name = line.split()[0]
            num_points = int(poly.readline())
            points = []
            for i in xrange(num_points):
                lon, lat = poly.readline().split(',')
                lon, lat = float(lon), float(lat)
                poly_point = sp.Point(lat, lon)
                points.append(poly_point)
            polygons[name] = sp.Polygon(points)
            poly.readline()
        except IndexError:
            break
    return polygons


# In[46]:

def dropoff_in_polygon(filename, polygons, do='JFK', idx_intersect=None):
    # Dropoff latitude and Longitude indexes
    d_lat_ix = 2
    d_long_ix = 3
    
    in_poly = []

    j = 0
    trips = open(filename, 'r')
    for i, t in enumerate(trips):
        if idx_intersect and j == len(idx_intersect):
            break
        elif idx_intersect and i != idx_intersect[j]:
            continue
        elif idx_intersect:
            j += 1
        splitted = t.replace('\n', '').replace('\r', '').split(',')
        try:
            d_lat = float(splitted[d_lat_ix])
            d_long = float(splitted[d_long_ix])
        except ValueError: # header
            continue
        trip_do = sp.Point(d_lat, d_long)
        if polygons[do].contains(trip_do):
            in_poly.append(i)
    return in_poly


# In[30]:

# Initialize polygons
poly_filename = 'neighborhoods.txt'
poly = read_polygons(poly_filename)


# In[31]:

# Check if trips dropoff is within polygon
def check_dropoff(data_filename, poly, do='JFK', idx_intersect=None):
    in_poly = dropoff_in_polygon(data_filename, poly, do, idx_intersect)
    return in_poly


# In[67]:

res = check_dropoff('sample-taxi-data.csv', poly)
print 'Sample data: size', len(res)
get_ipython().magic(u"timeit check_dropoff('sample-taxi-data.csv', poly)")
res = check_dropoff('taxigreen06_15.csv', poly)
print 'Taxigreen06_15: size', len(res)
get_ipython().magic(u"timeit res = check_dropoff('taxigreen06_15.csv', poly)")


# In[68]:

res = check_dropoff('sample-taxi-data.csv', poly, 'LGA')
print 'Sample data: size', len(res)
get_ipython().magic(u"timeit check_dropoff('sample-taxi-data.csv', poly, 'LGA')")
res = check_dropoff('taxigreen06_15.csv', poly, 'LGA')
print 'Taxigreen06_15: size', len(res)
get_ipython().magic(u"timeit res = check_dropoff('taxigreen06_15.csv', poly, 'LGA')")


# 4) Create a R-tree index on drop-off locations using the Rtree module.
# 
# 5) Execute the above two queries using the Rtree. As mentioned in the lab, the Rtree only supports rectangular queries. So a polygonal query can be executed as follows:
# 
# a) Obtain the bound of a given polygon
# 
# b) Query on Rtree using this bound   
# 
# c) For each resulting point, check if that point is within the polygon or not (using a loop, similar to (2) above).

# In[8]:

def build_idx(filename):
    # Dropoff latitude and Longitude indexes
    d_lat_ix = 2
    d_long_ix = 3
    
    idx = index.Index()

    trips = open(filename, 'r')
    for i, t in enumerate(trips):
        splitted = t.replace('\n', '').replace('\r', '').split(',')
        try:
            d_lat = float(splitted[d_lat_ix])
            d_long = float(splitted[d_long_ix])
        except ValueError: # header
            continue
        trip_do = sp.Point(d_lat, d_long)
        idx.insert(i, (trip_do.x,trip_do.y,trip_do.x,trip_do.y))
    return idx


# In[9]:

sample_idx = build_idx('sample-taxi-data.csv')
data_idx = build_idx('taxigreen06_15.csv')


# In[49]:

do_place = 'JFK'
idx_intersect = list(sample_idx.intersection(poly[do_place].bounds()))
data_intersect = list(data_idx.intersection(poly[do_place].bounds()))
idx_intersect.sort()
data_intersect.sort()
res = check_dropoff('sample-taxi-data.csv', poly,  do_place, idx_intersect)
print 'Sample data: size', len(res)
get_ipython().magic(u"timeit check_dropoff('sample-taxi-data.csv', poly, do_place, idx_intersect)")
res = check_dropoff('taxigreen06_15.csv', poly, do_place, data_intersect)
print 'Taxigreen06_15: size', len(res)
get_ipython().magic(u"timeit res = check_dropoff('taxigreen06_15.csv', poly, do_place, data_intersect)")


# In[52]:

do_place = 'LGA'
idx_intersect = list(sample_idx.intersection(poly[do_place].bounds()))
data_intersect = list(data_idx.intersection(poly[do_place].bounds()))
idx_intersect.sort()
data_intersect.sort()
res = check_dropoff('sample-taxi-data.csv', poly, do_place, idx_intersect)
print 'Sample data: size', len(res)
get_ipython().magic(u"timeit check_dropoff('sample-taxi-data.csv', poly, do_place, idx_intersect)")
res = check_dropoff('taxigreen06_15.csv', poly, do_place, data_intersect)
print 'Taxigreen06_15: size', len(res)
get_ipython().magic(u"timeit res = check_dropoff('taxigreen06_15.csv', poly, do_place, data_intersect)")


# 6. Report the result sizes and running times. Briefly discuss why the running times are different between (2,3) and (5).
# #### Result sizes and running times for 2 on sample data and green taxi one month data
#     Sample data: size 151
#     
#     10 loops, best of 3: 165 ms per loop
#     
#     Taxigreen06_15: size 13979
#     
#     1 loops, best of 3: 27.7 s per loop
# #### Result sizes and running times for 3 on sample data and green taxi one month data
#     Sample data: size 265
#     
#     10 loops, best of 3: 167 ms per loop
#     
#     Taxigreen06_15: size 21437
#     
#     1 loops, best of 3: 27.1 s per loop
# #### Result sizes and running times for 3 on sample data and green taxi one month data
# #### JFK
#     Sample data: size 151
#     
#     100 loops, best of 3: 6.29 ms per loop
#     
#     Taxigreen06_15: size 13979
#     
#     1 loops, best of 3: 819 ms per loop
# #### LGA
#     Sample data: size 265
#     
#     100 loops, best of 3: 9.09 ms per loop
#     
#     Taxigreen06_15: size 21437
#     
#     1 loops, best of 3: 1.08 s per loop
# 
# The reason why it is much faster in the second case is that we're only testing the points that intersect with the polygon bound in the point index. This decreases the number of Polygon tests considerably.

# In[ ]:



