from geographiclib.geodesic import Geodesic
import math
geod = Geodesic.WGS84  # define the WGS84 ellipsoid

l = geod.InverseLine(40.1, 116.6, 37.6, -122.4)
ds = 1000e3; 
n = int(math.ceil(l.s13 / ds))
print("n:", n)

for i in range(n + 1):

 if i == 0:
    print("distance latitude longitude azimuth")
 s = min(ds * i, l.s13)
 g = l.Position(s, Geodesic.STANDARD | Geodesic.LONG_UNROLL)

 print("{:.0f} {:.5f} {:.5f} {:.5f}".format(
        g['s12'], g['lat2'], g['lon2'], g['azi2']))