# Geospatial Relationship functions

You have now learned about how PostGIS supports a full set of standard spatial and distance relationship functions.

More technical details about spatial relationships and the Dimensionally-Extended 9 Intersection Model (DE-9IM) are available [here](https://en.wikipedia.org/wiki/DE-9IM).

The relationship functions and their definitions are summarized below:

## Spatial Relationship functions

* ST_Contains(geometry A, geometry B): Returns true if and only if no points of B lie in the exterior of A, and at least one point of the interior of B lies in the interior of A. The converse of ST_Within.

* ST_CoveredBy(geometry A, geometry B): Returns true if and only if no points of A lie in the exterior of B. In other words, A lies completely inside B. The converse of ST_Covers.

* ST_Covers(geometry A, geometry B): Returns true if and only if no points of B lie in the exterior of A. In other words, B lies completely inside A. The converse of ST_CoveredBy.

* ST_Crosses(geometry A, geometry B): Returns true if the supplied geometries have some, but not all, interior points in common.

* ST_Disjoint(geometry A , geometry B): Returns true if the geometries do not spatially intersect - i.e. if they do not share any points in common. The inverse of ST_Intersects.

* ST_Equals(geometry A, geometry B): Returns true if the geometries have the exact same shape. Directionality is not considered.

* ST_Intersects(geometry A, geometry B): Returns true if the geometries “spatially intersect” - i.e. if they have at least one spatial point in common. The inverse of ST_Disjoint.

* ST_Overlaps(geometry A, geometry B): Returns true if the geometries share space, are of the same dimension, but are not completely contained by each other.

* ST_Touches(geometry A, geometry B): Returns true if the geometries have at least one point in common, but their interiors do not intersect.

* ST_Within(geometry A , geometry B): Returns true if the geometry A is completely inside geometry B. The converse of ST_Contains.

## Relate functions

* ST_Relate(geometry A, geometry B): Returns the DE-9IM code indicating the full topological relationhips between A and B.

* ST_Relate(geometry A, geometry B, text mask): Tests whether the geometries A and B have a DE-9IM code which matches the given mask.

## Distance Relationship functions

* ST_Distance(geometry A, geometry B): Returns the 2-dimensional cartesian minimum distance between two geometries, in the units of the spatial reference system.

* ST_DWithin(geometry A, geometry B, radius): Returns true if two geometries are within the specified distance (radius) of one another.

## Operators

Useful for doing distance ordering and nearest neighbor limits using KNN gist functionality:

* <-> (A, B)  the distance between the floating point bounding box
**center point(centroid)** is returned

* <#> (A, B) **bounding box** distance calculations.

* ST_Distance, deffectively return 2-dimensional
cartesian minimum distance based on spatial ref.

* ***The <-> operator is finding the closest polygon by the kNN distance and ordering results accordingly***, but your actual distance metric is being determined by **ST_Distance**, which will definitely return the distance to the nearest point on exterior of the polygon, not the centroid.


