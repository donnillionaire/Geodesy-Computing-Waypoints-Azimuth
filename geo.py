from geographiclib.geodesic import Geodesic

A = (44.27364400, -121.17116400) #Point A (lat, lon)
B = (44.27357900, -121.17006800) #Point B (lat, lon)
s = 10 #Distance (m)

#Define the ellipsoid
geod = Geodesic.WGS84

#Solve the Inverse problem
inv = geod.Inverse(A[0],A[1],B[0],B[1])

azi1 = inv['azi1']
print('Initial Azimuth from A to B = ' + str(azi1))

#Solve the Direction problem
dir = geod.Direct(A[0],A[1],azi1,s)
C = (dir['lat2'],dir['lon2'])
print('C = ' + str(C))