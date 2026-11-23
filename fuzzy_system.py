"""
# Universe Definition
A universe is the full range of values a variable can take, stored as a NumPy array.

## Three universes will be created for our study:
	1. Traffic density (input): how congested the intersection is. Measured in cars/min
	2. Waiting time (input): how long cars have been waiting. Measured in seconds
	3. Green Light duration (output): how long the green light should stay on. Measured in seconds

In Ghana major arterial intersections in cities like Accra handle roughly 40,000 to 70,000+ vehicles per 
day (averaging 25 to 75+ vehicles per minute during peak periods). 
[citation](http://www.mlgrd.gov.gh/images/Ghana_Urban_Forum/er.pdf)

For our study, we will assume that:
	- The maximum traffic density is 80 cars/minute,
	- The maximum waiting time is 120 seconds,
	- The minimum green light duration is between 10 and 60 seconds inclusive.

# Membership Functions
Membership functions are used to define fuzzy sets. They map the input values to a degree of membership.

(More info here...)
"""