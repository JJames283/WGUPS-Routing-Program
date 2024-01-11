# Name: Joshua James
# Student ID: 011101737
# Course: Data Structures and Algorithms II
# Assessment: NHP2 Task 1: WGUPS Routing Program
# Created With: PyCharm 2023.1.3 (Community Edition), Python 3.9

# For this assessment, you will implement an algorithm to route delivery trucks that will allow you to meet all
# delivery constraints while traveling under a total of 140 miles.

import csv
import math
import datetime

# The following code below creates the new class "Package", which represents all the packages (for this project,
# 40 total) that will be delivered. Note: This is very similar to the creation of the Truck class below.
class Package:
    def __init__(self, packID, street, delivery_city, state, delivery_zip_code, delivery_deadline, package_weight_kilo,
                 special_notes):
        self.packID = packID
        self.street = street
        self.delivery_city = delivery_city
        self.state = state
        self.delivery_zip_code = delivery_zip_code
        self.delivery_deadline = delivery_deadline
        self.package_weight_kilo = package_weight_kilo
        self.special_notes = special_notes
        self.time_delivered = None
        self.delivery_status = False

    def __str__(self):
        return "%s, %s, %s, %s, %s ,%s, %s, %s" % (self.packID, self.street, self.delivery_city, self.state,
                                                   self.delivery_zip_code, self.delivery_deadline,
                                                   self.package_weight_kilo, self.special_notes)

# The following code below creates the new class Truck, which will be the vehicles (for this project, 3 trucks)
# that are delivering all 40 packages.
# Note: This is very similar to how the Package class was created above, just with different attributes and variables.
class Truck:
    def __init__(self, packages, address, mileage, time, truck_num):
        self.packages = packages
        self.address = address
        self.mileage = mileage
        self.time= time
        self.truck_num = truck_num

    def __str__(self):
        return "%s, %s, %s, %s" % (self.packages, self.address, self.mileage, self.time)


# The following code segment generates a HashTable class using chaining.
# Reference: ZyBooks Chapter 7, Figure 7.8.1: Structure of a HashTable class
# Reference: C950 - Webinar-1 - Let's Go Hashing
class ChainingHashTable:
    # First, the following code generates a new constructor which is defined with optional initial capacity parameter,
    # and then, assigns all buckets with an empty list.
    # The Time Complexity of this is O(n).
    def __init__(self, initial_capacity=10):
        # The following code initializes the hash table with all bucket list entries being empty.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # The following code inserts a new item into the recently created hash table.
    # This code portion will perform both the insert and update operations.
    # This code portion will also determine the bucket where each item will be placed.
    # The Time Complexity of this is O(n).
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucketlist = self.table[bucket]

        # The following code will update the key if the item happens to be already in the bucket.
        for kv in bucketlist:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # If the item is not in the bucket, this will append the item to the end of the bucket list.
        key_value = [key, item]
        bucketlist.append(key_value)
        return True

    # The following code searches for an item with a matching key in the hash table and returns the item if found,
    # or "None" if a matching key is not found.
    # The Time Complexity of this is O(1).
    def search(self, key):
        # The following code retrieves the bucket list where this specific key is.
        bucket = hash(key) % len(self.table)
        bucketlist = self.table[bucket]
        # print(bucketlist)

        # The following code searches for the key in the bucket list.
        for kv in bucketlist:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # The following code removes an item with a matching key from the hash table.
    # The Time Complexity of this is O(n).
    def remove(self, key):
        # The following code retrieves the bucket list location where this specific item will be removed from.
        bucket = hash(key) % len(self.table)
        bucketlist = self.table[bucket]

        # The following code removes the item from the bucket list if it is present in the list.
        for kv in bucketlist:
            # print (key_value)
            if kv[0] == key:
                bucketlist.remove([kv[0], kv[1]])


# The following section of code creates all 40 Package objects that are part of this project, along with their
# respective details, such as package ID (packID), address, city (delivery_city), state, zip (delivery_zip_code),
# delivery deadline (delivery_deadline), weight (package_weight_kilo), and special notes.
# Note: Another way to do this is would have been to create a separate Package table and import data via csv reader.
# The Time Complexity of this is O(1).
p1 = Package(1, "195 W Oakland Ave", "Salt Lake City", "UT", 84115, "10:30", 21, "")
p2 = Package(2, "2530 S 500 E", "Salt Lake City", "UT", 84106, "EOD", 44, "")
p3 = Package(3, "233 Canyon Rd", "Salt Lake City", "UT", 84103, "EOD", 2, "Can only be on truck 2")
p4 = Package(4, "380 W 2880 S", "Salt Lake City", "UT", 84115, "EOD", 4, "")
p5 = Package(5, "410 S State St", "Salt Lake City", "UT", 84111,"EOD", 5, "")
p6 = Package(6, "3060 Lester St", "West Valley City", "UT", 84119, "10:30 AM", 88, "Delayed on flight--will not arrive to depot until 9:05 a.m.")
p7 = Package(7, "1330 2100 S", "Salt Lake City", "UT", 84106, "EOD", 8, "")
p8 = Package(8, "300 State St", "Salt Lake City", "UT", 84103, "EOD", 9, "")
p9 = Package(9, "300 State St", "Salt Lake City", "UT", 84103, "EOD", 2, "Wrong address listed")
p10 = Package(10, "600 E 900 South", "Salt Lake City", "UT", 84105,"EOD", 1, "")
p11 = Package(11, "2600 Taylorsville Blvd", "Salt Lake City", "UT", 84118, "EOD", 1, "")
p12 = Package(12, "3575 W Valley Central Station bus Loop", "West Valley City", "UT", 84119, "EOD", 1, "")
p13 = Package(13, "2010 W 500 S", "Salt Lake City", "UT", 84104, "10:30 AM", 2, "")
p14 = Package(14, "4300 S 1300 E", "Millcreek", "UT", 84117, "10:30 AM", 88, "Must be delivered with 15, 19")
p15 = Package(15, "4580 S 2300 E", "Holladay", "UT", 84117, "9:00 AM", 4, "")
p16 = Package(16, "4580 S 2300 E", "Holladay", "UT", 84117, "10:30 AM", 88, "Must be delivered with 13, 19")
p17 = Package(17, "3148 S 1100 W", "Salt Lake City", "UT", 84119, "EOD", 2, "")
p18 = Package(18, "1488 4800 S", "Salt Lake City", "UT", 84123, "EOD", 6, "Can only be on truck 2")
p19 = Package(19, "177 W Price Ave", "Salt Lake City", "UT", 84115, "EOD", 37, "")
p20 = Package(20, "3595 Main St", "Salt Lake City", "UT", 84115, "10:30 AM", 37, "Must be delivered with 13, 15")
p21 = Package(21, "3595 Main St", "Salt Lake City", "UT", 84115, "EOD", 3, "")
p22 = Package(22, "6351 South 900 East", "Murray", "UT", 84121, "EOD", 2, "")
p23 = Package(23, "5100 South 2700 West", "Salt Lake City", "UT", 84118, "EOD", 5, "")
p24 = Package(24, "5025 State St", "Murray", "UT", 84107, "EOD", 7, "")
p25 = Package(25, "5383 S 900 East #104", "Salt Lake City", "UT", 84117, "10:30 AM", 7, "Delayed on flight--will not arrive to depot until 9:05 am")
p26 = Package(26, "5383 S 900 East #104", "Salt Lake City", "UT", 84117, "EOD", 25, "")
p27 = Package(27, "1060 Dalton Ave S", "Salt Lake City", "UT", 84104, "EOD", 5, "")
p28 = Package(28, "2835 Main St", "Salt Lake City", "UT", 84115, "EOD", 7, "Delayed on flight--will not arrive to depot until 9:05")
p29 = Package(29, "1330 2100 S", "Salt Lake City", "UT", 84106, "10:30 AM", 2, "")
p30 = Package(30, "300 State St", "Salt Lake City", "UT", 84103, "10:30 AM", 1, "")
p31 = Package(31, "3365 S 900 W", "Salt Lake City", "UT", 84119, "10:30 AM", 1, "")
p32 = Package(32, "3365 S 900 W", "Salt Lake City", "UT", 84119, "EOD", 1, "Delayed on flight--will not arrive to depot until 9:05 am")
p33 = Package(33, "2530 S 500 E", "Salt Lake City", "UT", 84106, "EOD", 1, "")
p34 = Package(34, "4580 S 2300 E", "Holladay", "UT", 84117, "10:30 AM", 2, "")
p35 = Package(35, "1060 Dalton Ave S", "Salt Lake City", "UT", 84104, "EOD", 88, "")
p36 = Package(36, "2300 Parkway Blvd", "West Valley City", "UT", 84119, "EOD", 88, "Can only be on truck 2")
p37 = Package(37, "410 S State St", "Salt Lake City", "UT", 84111, "10:30 AM", 2, "")
p38 = Package(38, "410 S State St", "Salt Lake City", "UT", 84111, "EOD", 9, "Can only be on truck 2")
p39 = Package(39, "2010 W 500 S", "Salt Lake City", "UT", 84104, "EOD", 9, "")
p40 = Package(40, "380 W 2880 S", "Salt Lake City", "UT", 84115, "10:30 AM", 45, "")

# The following code generates a new hash table.
# The Time Complexity of this is O(1).
packHashNew = ChainingHashTable()

# The next section uses the insert function to insert each of the 40 package objects created above,
# into the newly created "packHashNew" hash table that was just generated.
# The Time Complexity of this is O(1).

packHashNew.insert(1, p1)  # Package Delivery Address: 195 W Oakland Ave, Salt Lake City, UT, 84115
packHashNew.insert(2, p2)  # Package Delivery Address: 2530 S 500 E, Salt Lake City, UT, 84106
packHashNew.insert(3, p3)  # Package Delivery Address: 233 Canyon Rd, Salt Lake City, UT, 84103
packHashNew.insert(4, p4)  # Package Delivery Address: 380 W 2880 S, Salt Lake City, UT, 84115
packHashNew.insert(5, p5)  # Package Delivery Address: 410 S State St, Salt Lake City, UT, 84111
packHashNew.insert(6, p6)  # Package Delivery Address: 3060 Lester St, West Valley City, UT, 84119
packHashNew.insert(7, p7)  # Package Delivery Address: 1330 2100 S, Salt Lake City, UT, 84106
packHashNew.insert(8, p8)  # Package Delivery Address: 300 State St, Salt Lake City, UT, 84103
packHashNew.insert(9, p9)  # Package Delivery Address: 300 State St, Salt Lake City, UT, 84103
packHashNew.insert(10, p10)  # Package Delivery Address: 600 E 900 South, Salt Lake City, UT, 84105
packHashNew.insert(11, p11)  # Package Delivery Address: 2600 Taylorsville Blvd, Salt Lake City, UT, 84118
packHashNew.insert(12, p12)  # Package Delivery Address: 3575 W Valley Central Station bus Loop, West Valley City, UT, 84119
packHashNew.insert(13, p13)  # Package Delivery Address: 2010 W 500 S, Salt Lake City, UT, 84104
packHashNew.insert(14, p14)  # Package Delivery Address: 4300 S 1300 E, Millcreek, UT, 84117
packHashNew.insert(15, p15)  # Package Delivery Address: 4580 S 2300 E, Holladay, UT, 84117
packHashNew.insert(16, p16)  # Package Delivery Address: 4580 S 2300 E, Holladay, UT, 84117
packHashNew.insert(17, p17)  # Package Delivery Address: 3148 S 1100 W, Salt Lake City, UT, 84119
packHashNew.insert(18, p18)  # Package Delivery Address: 1488 4800 S, Salt Lake City, UT, 84123
packHashNew.insert(19, p19)  # Package Delivery Address: 177 W Price Ave, Salt Lake City, UT, 84115
packHashNew.insert(20, p20)  # Package Delivery Address: 3595 Main St, Salt Lake City, UT, 84115
packHashNew.insert(21, p21)  # Package Delivery Address: 3595 Main St, Salt Lake Cit, UT, 84115
packHashNew.insert(22, p22)  # Package Delivery Address: 6351 South 900 East, Murray, UT, 84121
packHashNew.insert(23, p23)  # Package Delivery Address: 5100 South 2700 West, Salt Lake City, UT, 84118
packHashNew.insert(24, p24)  # Package Delivery Address: 5025 State St, Murray, UT, 84107
packHashNew.insert(25, p25)  # Package Delivery Address: 5383 South 900 East #104, Salt Lake City, UT, 84117
packHashNew.insert(26, p26)  # Package Delivery Address: 5383 South 900 East #104, Salt Lake City, UT, 84117
packHashNew.insert(27, p27)  # Package Delivery Address: 1060 Dalton Ave S, Salt Lake City, UT, 84104
packHashNew.insert(28, p28)  # Package Delivery Address: 2835 Main St, Salt Lake City, UT, 84115
packHashNew.insert(29, p29)  # Package Delivery Address: 1330 2100 S, Salt Lake City, UT, 84106
packHashNew.insert(30, p30)  # Package Delivery Address: 300 State St, Salt Lake City, UT, 84103
packHashNew.insert(31, p31)  # Package Delivery Address: 3365 S 900 W, Salt Lake City, UT, 84119
packHashNew.insert(32, p32)  # Package Delivery Address: 3365 S 900 W, Salt Lake City, UT, 84119
packHashNew.insert(33, p33)  # Package Delivery Address: 2530 S 500 E, Salt Lake City, UT, 84106
packHashNew.insert(34, p34)  # Package Delivery Address: 4580 S 2300 E, Holladay, UT, 84117
packHashNew.insert(35, p35)  # Package Delivery Address: 1060 Dalton Ave S, Salt Lake City, UT, 84104
packHashNew.insert(36, p36)  # Package Delivery Address: 2300 Parkway Blvd, West Valley City, UT, 84119
packHashNew.insert(37, p37)  # Package Delivery Address: 410 S State St, Salt Lake City, UT, 84111
packHashNew.insert(38, p38)  # Package Delivery Address: 410 S State St, Salt Lake City, UT, 84111
packHashNew.insert(39, p39)  # Package Delivery Address: 2010 W 500 S, Salt Lake City, UT, 84104
packHashNew.insert(40, p40)  # Package Delivery Address: 380 W 2880 S, Salt Lake City, UT, 84115


# Below is an algorithm that uses the Nearest Neighbor algorithm in order to find the shortest distance
# to deliver all 40 packages. Please note, this algorithm uses each individual truck as a parameter. All packages on
# each of the three trucks is looped, and during the second loop, a comparison is made between the truck and the onboard
# package's delivery address, which then the shortest distance is selected.
# The Time Complexity of this is O(n^2).
def packNearestNeighbor(truck):
    print("\nTruck", truck.truck_num, "Departure Time from hub:", truck.time)

    # The first loop goes through all the packages that are on the delivery truck currently.
    for i in truck.packages:
        optimalPack = None
        optimalDist = 1000000

        # The following code loops all package's package ID that are on the truck currently.
        for package_id in truck.packages:

            # By using a hash table look up, we are then able to obtain the package's information.
            package = packHashNew.search(package_id)

            # The following array will hold the distance separating each of the truck's addresses and their package's
            # eventual delivery destination address.
            distance = dist_2D_array[address_dict[truck.address]][address_dict[package.street]]

            # This uses the Nearest Neighbor algorithm to determine whether the next package
            # has a shorter distance than the previous package checked. If the next pacakge is of a shorter
            # distance than the previous package checked, then it is saved as the "optimalPack".
            if distance < optimalDist and package.time_delivered is None:
                optimalPack = package
                optimalDist = distance

        # This makes sure that the subsequent package that will be delivered is the one with the shortest
        # distance (the "optimalPack").
        package = optimalPack
        if package != None:

            # The below code ensures that the time of the delivery of the package, as well as the distance
            # traveled by the delivery vehicle (truck), is recorded.
            distance = dist_2D_array[address_dict[truck.address]][address_dict[package.street]]
            truck.mileage += distance
            truck.time += datetime.timedelta(minutes=(distance / (18 * (1 / 60))))

            truck.address = package.street
            package.time_delivered = truck.time
            package.delivery_status = True
            package.truck_num = truck.truck_num
            print("Package:", package.packID, "     Truck Number:", truck.truck_num,
                  "\n  Distance traveled from last address:", distance, "\n  Delivery Time:",
                  package.time_delivered, "  Delivery Deadline:", package.delivery_deadline, "\n  Delivery Address: ",
                  package.street, package.delivery_city, package.state, package.delivery_zip_code,
                  "\n  Package Weight (kilo):", package.package_weight_kilo,
                  "\n  Special Notes:", package.special_notes)

    distance = dist_2D_array[address_dict[truck.address]][address_dict["4001 South 700 East"]]
    truck.mileage += distance
    truck.time += datetime.timedelta(minutes=(distance / (18 * (1 / 60))))
    print("Truck", truck.truck_num, "Time arrived at Hub:", truck.time, "        Distance to return to Hub:", distance)


# The following generates a dictionary, and in an array, each address is added to the dictionary and associated with
# a location (index).
# The Time Complexity of this is O(1).
address_dict = {"4001 South 700 East": 0, "1060 Dalton Ave S": 1, "1330 2100 S": 2, "1488 4800 S": 3,
                "177 W Price Ave": 4, "195 W Oakland Ave": 5, "2010 W 500 S": 6, "2300 Parkway Blvd": 7,
                "233 Canyon Rd": 8, "2530 S 500 E": 9, "2600 Taylorsville Blvd": 10, "2835 Main St": 11,
                "300 State St": 12, "3060 Lester St": 13, "3148 S 1100 W": 14, "3365 S 900 W": 15,
                "3575 W Valley Central Station bus Loop": 16, "3595 Main St": 17, "380 W 2880 S": 18,
                "410 S State St": 19, "4300 S 1300 E": 20, "4580 S 2300 E": 21, "5025 State St": 22,
                "5100 South 2700 West": 23, "5383 S 900 East #104": 24, "600 E 900 South": 25,
                "6351 South 900 East": 26}

# Western Governors University Address: 4001 South 700 East, index 0
# International Peace Gardens Address: 1060 Dalton Ave S, index 1
# Sugar House Park Address: 1330 2100 S, index 2
# Taylorsville-Bennion Heritage Address: 1488 4800 S, index 3
# Salt Lake City Division of Health Services Address: 177 W Price Ave, index 4
# South Salt Lake Public Works Address: 195 W Oakland Ave, index 5
# Salt Lake City Streets and Sanitation Address: 2010 W 500 S, index 6
# Deker Lake Address: 2300 Parkway Blvd, index 7
# Salt Lake City Ottinger Hall Address: 233 Canyon Rd, index 8
# Columbus Library Address: 2530 S 500 E, index 9
# Taylorsville City Hall Address: 2600 Taylorsville Blvd, index 10
# South Salt Lake Police Address: 2835 Main St, index 11
# Council Hall Address: 300 State St, index 12
# Redwood Park Address: 3060 Lester St, index 13
# Salt Lake County Mental Health Address: 3148 S 1100 W, index 14
# Salt Lake County/United Police Dept Address: 3365 S 900 W, index 15
# West Valley Prosecutor Address: 3575 W Valley Central Station bus Loop, index 16
# Housing Auth. of Salt Lake County Address: 3595 Main St, index 17
# Utah DMV Administrative Office Address: 380 W 2880 S, index 18
# Third District Juvenile Court Address: 410 S State St, index 19
# Cottonwood Regional Softball Complex Address: 4300 S 1300 E, index 20
# Holiday City Office Address: 4580 S 2300 E, index 21
# Murray City Museum Address: 5025 State St, index 22
# Valley Regional Softball Complex Address: 5100 South 2700 West, index 23
# City Center of Rock Springs Address: 5383 S 900 East #104, index 24
# Rice Terrace Pavilion Park Address: 600 E 900 South, index 25
# Wheeler Historic Farm Address: 6351 South 900 East, index 26


# The next section of code generates a new list that holds the distances between the 27 addresses.
# The Time Complexity of this is O(1).
# Note: Another way to have done this would have been to create a separate Distance table (similar to Presents).

# Western Governors University, Address: 4001 South 700 East
distance_WesternGovernorsUniversity = [0, 7.2, 3.8, 11, 2.2, 3.5, 10.9, 8.6, 7.6, 2.8, 6.4, 3.2, 7.6, 5.2, 4.4, 3.7,
                                          7.6, 2, 3.6, 6.5, 1.9, 3.4, 2.4, 6.4, 2.4, 5, 3.6]
# International Peace Gardens, Address: 1060 Dalton Ave S
distance_InternationalPeaceGardens = [7.2, 0, 7.1, 6.4, 6, 4.8, 1.6, 2.8, 4.8, 6.3, 7.3, 5.3, 4.8, 3, 4.6, 4.5, 7.4,
                                         6, 5, 4.8, 9.5, 10.9, 8.3, 6.9, 10, 4.4, 13]
# Sugar House Park, Address: 1330 2100 S
distance_SugarHousePark = [3.8, 7.1, 0, 9.2, 4.4, 2.8, 8.6, 6.3, 5.3, 1.6, 10.4, 3, 5.3, 6.5, 5.6, 5.8, 5.7, 4.1,
                              3.6, 4.3, 3.3, 5, 6.1, 9.7, 6.1, 2.8, 7.4]
# Taylorsville-Bennion Heritage, Address: 1488 4800 S
distance_TaylorsvilleBennionHeritage = [11, 6.4, 9.2, 0, 5.6, 6.9, 8.6, 4, 11.1, 7.3, 1, 6.4, 11.1, 3.9, 4.3, 4.4,
                                           7.2, 5.3, 6, 10.6, 5.9, 7.4, 4.7, 0.6, 6.4, 10.1, 10.1]
# Salt Lake City Division of Health Services, Address: 177 W Price Ave
distance_SaltLakeCityHealthServices = [2.2, 6, 4.4, 5.6, 0, 1.9, 7.9, 5.1, 7.5, 2.6, 6.5, 1.5, 7.5, 3.2, 2.4, 2.7,
                                          1.4, 0.5, 1.7, 6.5, 3.2, 5.2, 2.5, 6, 4.2, 5.4, 5.5]
# South Salt Lake Public Works, Address: 195 W Oakland Ave
distance_SaltLakeCityPublicWorks = [3.5, 4.8, 2.8, 6.9, 1.9, 0, 6.3, 4.3, 4.5, 1.5, 8.7, 0.8, 4.5, 3.9, 3, 3.8, 5.7,
                                       1.9, 1.1, 3.5, 4.9, 6.9, 4.2, 9, 5.9, 3.5, 7.2]
# Salt Lake City Streets and Sanitation, Address: 2010 W 500 S
distance_SLCStreetsSanitation = [10.9, 1.6, 8.6, 8.6, 7.9, 6.3, 0, 4, 4.2, 8, 8.6, 6.9, 4.2, 4.2, 8, 5.8, 7.2, 7.7,
                                    6.6, 3.2, 11.2, 12.7, 10, 8.2, 11.7, 5.1, 14.2]
# Deker Lake, Address: 2300 Parkway Blvd
distance_DekerLake = [8.6, 2.8, 6.3, 4, 5.1, 4.3, 4, 0, 7.7, 9.3, 4.6, 4.8, 7.7, 1.6, 3.3, 3.4, 3.1, 5.1, 4.6, 6.7,
                         8.1, 10.4, 7.8, 4.2, 9.5, 6.2, 10.7]
# Salt Lake City Ottinger Hall, Address: 233 Canyon Rd
distance_SLCOttingerHall = [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0, 4.8, 11.9, 4.7, 0.6, 7.6, 7.8, 6.6, 7.2, 5.9,
                               5.4, 1, 8.5, 10.3, 7.8, 11.5, 9.5, 2.8, 14.1]
# Columbus Library, Address: 2530 S 500 E
distance_ColumbusLibrary = [2.8, 6.3, 1.6, 7.3, 2.6, 1.5, 8, 9.3, 4.8, 0, 9.4, 1.1, 5.1, 4.6, 3.7, 4, 6.7, 2.3, 1.8,
                               4.1, 3.8, 5.8, 4.3, 7.8, 4.8, 3.2, 6]
# Taylorsville City Hall, Address: 2600 Taylorsville Blvd
distance_TaylorsvilleCityHall = [6.4, 7.3, 10.4, 1, 6.5, 8.7, 8.6, 4.6, 11.9, 9.4, 0, 7.3, 12, 4.9, 5.2, 5.4, 8.1,
                                    6.2, 6.9, 11.5, 6.9, 8.3, 4.1, 0.4, 4.9, 11, 6.8]
# South Salt Lake Police, Address: 2835 Main St
distance_SSLPolice = [3.2, 5.3, 3, 6.4, 1.5, 0.8, 6.9, 4.8, 4.7, 1.1, 7.3, 0, 4.7, 3.5, 2.6, 2.9, 6.3, 1.2, 1, 3.7,
                         4.1, 6.2, 3.4, 6.9, 5.2, 3.7, 6.4]
# Council Hall, Address: 300 State St
distance_CouncilHall = [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.6, 5.1, 12, 4.7, 0, 7.3, 7.8, 6.6, 7.2, 5.9, 5.4,
                           1, 8.5, 10.3, 7.8, 11.5, 9.5, 2.8, 14.1]
# Redwood Park, Address: 3060 Lester St
distance_RedwoodPark = [5.2, 3, 6.5, 3.9, 3.2, 3.9, 4.2, 1.6, 7.6, 4.6, 4.9, 3.5, 7.3, 0, 1.3, 1.5, 4, 3.2, 3, 6.9,
                           6.2, 8.2, 5.5, 4.4, 7.2, 6.4, 10.5]
# Salt Lake County Mental Health, Address: 3148 S 1100 W
distance_SLCMentalHealth = [4.4, 4.6, 5.6, 4.3, 2.4, 3, 8, 3.3, 7.8, 3.7, 5.2, 2.6, 7.8, 1.3, 0, 0.6, 6.4, 2.4, 2.2,
                               6.8, 5.3, 7.4, 4.6, 4.8, 6.3, 6.5, 8.8]
# Salt Lake County/United Police Dept., Address: 3365 S 900 W
distance_SLCUnitedPoliceDept = [3.7, 4.5, 5.8, 4.4, 2.7, 3.8, 5.8, 3.4, 6.6, 4, 5.4, 2.9, 6.6, 1.5, 0.6, 0, 5.6, 1.6,
                                   1.7, 6.4, 4.9, 6.9, 4.2, 5.6, 5.9, 5.7, 8.4]
# West Valley Prosecutor, Address: 3575 W Valley Central Station bus Loop
distance_WVProsecutor = [7.6, 7.4, 5.7, 7.2, 1.4, 5.7, 7.2, 3.1, 7.2, 6.7, 8.1, 6.3, 7.2, 4, 6.4, 5.6, 0, 7.1, 6.1,
                            7.2, 10.6, 12, 9.4, 7.5, 11.1, 6.2, 13.6]
# Housing Auth. of Salt Lake County, Address: 3595 Main St
distance_HousingAuthSLCounty = [2, 6, 4.1, 5.3, 0.5, 1.9, 7.7, 5.1, 5.9, 2.3, 6.2, 1.2, 5.9, 3.2, 2.4, 1.6, 7.1, 0,
                                   1.6, 4.9, 3, 5, 2.3, 5.5, 4, 5.1, 5.2]
# Utah DMV Administrative, Office Address: 380 W 2880 S
distance_UtahDMVAdmin = [3.6, 5, 3.6, 6, 1.7, 1.1, 6.6, 4.6, 5.4, 1.8, 6.9, 1, 5.4, 3, 2.2, 1.7, 6.1, 1.6, 0, 4.4,
                            4.6, 6.6, 3.9, 6.5, 5.6, 4.3, 6.9]
# Third District Juvenile Court, Address: 410 S State St
distance_TDJuvenileCourt = [6.5, 4.8, 4.3, 10.6, 6.5, 3.5, 3.2, 6.7, 1, 4.1, 11.5, 3.7, 1, 6.9, 6.8, 6.4, 7.2, 4.9,
                               4.4, 0, 7.5, 9.3, 6.8, 11.4, 8.5, 1.8, 13.1]
# Cottonwood Regional Softball Complex, Address: 4300 S 1300 E
distance_CRSoftballComplex = [1.9, 9.5, 3.3, 5.9, 3.2, 4.9, 11.2, 8.1, 8.5, 3.8, 6.9, 4.1, 8.5, 6.2, 5.3, 4.9, 10.6,
                                 3, 4.6, 7.5, 0, 2, 2.9, 6.4, 2.8, 6, 4.1]
# Holiday City Office, Address: 4580 S 2300 E
distance_HolidayCityOffice = [3.4, 10.9, 5, 7.4, 5.2, 6.9, 12.7, 10.4, 10.3, 5.8, 8.3, 6.2, 10.3, 8.2, 7.4, 6.9, 12,
                                 5, 6.6, 9.3, 2, 0, 4.4, 7.9, 3.4, 7.9, 4.7]
# Murray City Museum, Address: 5025 State St
distance_MurrayCityMuseum = [2.4, 8.3, 6.1, 4.7, 2.5, 4.2, 10, 7.8, 7.8, 4.3, 4.1, 3.4, 7.8, 5.5, 4.6, 4.2, 9.4, 2.3,
                                3.9, 6.8, 2.9, 4.4, 0, 4.5, 1.7, 6.8, 3.1]
# Valley Regional Softball Complex, Address: 5100 South 2700 West
distance_VRSoftballComplex = [6.4, 6.9, 9.7, 0.6, 6, 9, 8.2, 4.2, 11.5, 7.8, 0.4, 6.9, 11.5, 4.4, 4.8, 5.6, 7.5, 5.5,
                                 6.5, 11.4, 6.4, 7.9, 4.5, 0, 5.4, 10.6, 7.8]
# City Center of Rock Springs, Address: 5383 S 900 East #104
distance_CCRockSprings = [2.4, 10, 6.1, 6.4, 4.2, 5.9, 11.7, 9.5, 9.5, 4.8, 4.9, 5.2, 9.5, 7.2, 6.3, 5.9, 11.1, 4,
                             5.6, 8.5, 2.8, 3.4, 1.7, 5.4, 0, 7, 1.3]
# Rice Terrace Pavilion Park, Address: 600 E 900 South
distance_RTPavilionPark = [5, 4.4, 2.8, 10.1, 5.4, 3.5, 5.1, 6.2, 2.8, 3.2, 11, 3.7, 2.8, 6.4, 6.5, 5.7, 6.2, 5.1,
                              4.3, 1.8, 6, 7.9, 6.8, 10.6, 7, 0, 8.3]
# Wheeler Historic Farm, Address: 6351 South 900 East
distance_WheelerHistoricFarm = [3.6, 13, 7.4, 10.1, 5.5, 7.2, 14.2, 10.7, 14.1, 6, 6.8, 6.4, 14.1, 10.5, 8.8, 8.4,
                                   13.6, 5.2, 6.9, 13.1, 4.1, 4.7, 3.1, 7.8, 1.3, 8.3, 0]

# The following turns the Distance table that was just created above, into an array of the distances between each
# of the 27 addresses.
# The Time Complexity of this is O(1).
dist_2D_array = [distance_WesternGovernorsUniversity, distance_InternationalPeaceGardens, distance_SugarHousePark,
                 distance_TaylorsvilleBennionHeritage, distance_SaltLakeCityHealthServices,
                 distance_SaltLakeCityPublicWorks, distance_SLCStreetsSanitation, distance_DekerLake,
                 distance_SLCOttingerHall, distance_ColumbusLibrary, distance_TaylorsvilleCityHall, distance_SSLPolice,
                 distance_CouncilHall, distance_RedwoodPark,distance_SLCMentalHealth,
                 distance_SLCUnitedPoliceDept, distance_WVProsecutor, distance_HousingAuthSLCounty,
                 distance_UtahDMVAdmin, distance_TDJuvenileCourt, distance_CRSoftballComplex,
                 distance_HolidayCityOffice, distance_MurrayCityMuseum, distance_VRSoftballComplex,
                 distance_CCRockSprings, distance_RTPavilionPark, distance_WheelerHistoricFarm]


# Delivery Truck Assumptions:
# 1. Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.
# 2. The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.
# 3. There are no collisions.
# 4. Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that
# truck is in service.
# 5. Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages
# if needed.
# 6. The delivery and loading times are instantaneous, i.e., no time passes while at a delivery or when moving packages
# to a truck at the hub (that time is factored into the calculation of the average speed of the trucks)
# 7. There is up to one special note associated with a package.
# 8. The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m.
# WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the
# correct address (410 S State St., Salt Lake City, UT 84111) until 10:20 a.m.
# 9. The distances provided in the WGUPS Distance Table are equal regardless of the direction traveled.
# 10. The day ends when all 40 packages have been delivered.

# Based on the above truck assumptions, each package's delivery deadline, and special notes (if the package has any),
# I decided to split the packages into 3 separate groups (40 total packages). These are the groups the packages
# will be loaded into for each of the 3 delivery vehicles (truck).

# The following code adds 14 total packages to first delivery vehicle (truck1).
# Truck 1's Packages: 1, 13, 14, 15, 16, 19, 20, 27, 29, 30, 31, 34, 37, 40
# Truck 1 has package 15, which must be delivered first (by 9:00 a.m.). All other packages on Truck 1 have a 10:30 a.m.
# delivery deadline.
truck1_packID = [p1.packID, p13.packID, p14.packID, p15.packID, p16.packID, p19.packID, p20.packID, p27.packID,
                 p29.packID, p30.packID, p31.packID, p34.packID, p37.packID, p40.packID]

# The following code generates the "truck1" object.
t1 = datetime.timedelta(hours=8, minutes=0)
truck1 = Truck(truck1_packID, "4001 South 700 East", 0, t1, 1)

# The following code adds 11 total packages to the second delivery vehicle (truck2).
# Truck 2's Packages: 3, 6, 18, 25, 28, 32, 33, 35, 36, 38, 39
# Truck 2 has packages 25, 28, 32, 6, which are delayed and will arrive to the delivery depot at 9:05 a.m. Package 6
# and Package 25 must be delivered by 10:30 a.m. Package 9 has the wrong address and won't be updated until 10:20 a.m.
# All other packages on Truck 2 can be delivered by end of day (EOD).
truck2_packID = [p3.packID, p6.packID,  p18.packID, p25.packID, p28.packID, p32.packID, p33.packID, p35.packID,
                 p36.packID, p38.packID, p39.packID]

# The following code generates the "truck2" object.
t2 = datetime.timedelta(hours=9, minutes=5)
truck2 = Truck(truck2_packID, "4001 South 700 East", 0, t2, 2)

# The following code adds all the remaining packages (15 total) to the third delivery vehicle (truck3).
# Truck 3's Packages: 2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 26
# Truck 3's packages all do not have any special notes and can all be delivered by end of day (EOD).
truck3_packID = [p2.packID, p4.packID, p5.packID, p7.packID, p8.packID, p9.packID, p10.packID, p11.packID,
                 p12.packID, p17.packID, p19.packID, p21.packID, p22.packID, p23.packID, p24.packID, p26.packID]

# As with "truck1" and "truck2", the following code generates the "truck3" object.
# One of the conditions of the project states that while there are 3 trucks, there are only two drivers available.
# Once the driver of Truck 1 has finished all of their deliveries (by 10:30 a.m.), they will then return to the
# delivery hub become the driver and start deliveries for Truck 3. All packages on Truck 3 don't have be delivered
# any earlier than end of day (EOD).
t3 = datetime.timedelta(hours=12, minutes=0)
truck3 = Truck(truck3_packID, "4001 South 700 East", 0, t3, 3)

print("Truck 1's onboard packages to be delivered at start of shift: ", truck1_packID)
print("Truck 2's onboard packages to be delivered at start of shift: ", truck2_packID)
print("Truck 3's onboard packages to be delivered at start of shift: ", truck3_packID)

# The following performs the Nearest Neighbor function defined earlier, for all packages in each of the 3 trucks.
packNearestNeighbor(truck1)
packNearestNeighbor(truck2)
packNearestNeighbor(truck3)


# The following code generates a new list that contains each of the 40 Package IDs.
# The Time Complexity of this is  O(1).
everyPackID = [p1.packID, p2.packID, p3.packID, p4.packID, p5.packID, p6.packID, p7.packID, p8.packID, p9.packID,
               p10.packID, p11.packID, p12.packID, p13.packID, p14.packID, p15.packID, p16.packID, p17.packID,
               p18.packID, p19.packID, p20.packID, p21.packID, p22.packID, p23.packID, p24.packID, p25.packID,
               p26.packID, p27.packID, p28.packID, p29.packID, p30.packID, p31.packID, p32.packID, p33.packID,
               p34.packID, p35.packID, p36.packID, p37.packID, p38.packID, p39.packID, p40.packID]


# This section loops through all Package IDs on each of the 3 delivery trucks and prints the total mileage for each
# delivery truck, as well as the total mileage for all 3 delivery trucks combined.
# The Time Complexity of this is O(n).
for i in everyPackID:
    package = packHashNew.search(i)
    print("Package ID:", package.packID, "Time Delivered:", package.time_delivered)

print("Truck 1's individual total miles: ", truck1.mileage)
print("Truck 2's individual total miles: ", truck2.mileage)
print("Truck 3's individual total miles: ", truck3.mileage)
totalMileage = (truck1.mileage + truck2.mileage + truck3.mileage)
print("Total Miles for all 3 Trucks combined: ", totalMileage)

# Per the project's instructions "to show the status of all packages at a time between 8:35 a.m. and 9:25 a.m.",
# the following code is set to check the delivery status of all the packages at 8:45 a.m.
# The Time Complexity of this is O(1).
testing_time = datetime.timedelta(hours=8, minutes=45)
testDelivery_Status = ""

print("\nThis is the status of all the packages at", testing_time)

# Per the project's instructions mentioned above, the following code will loop through all packages on each truck to
# determine their delivery status ("at the hub", "en route", or "delivered") at 8:45 a.m.
# The Time Complexity is O(n).
for i in everyPackID:
    package = packHashNew.search(i)

    Delivery_Status = ""

    if package.truck_num == 1:
        if testing_time <= t1:
            Delivery_Status = "At The Hub"
        elif t1 < testing_time < package.time_delivered:
            Delivery_Status = "En Route"
        elif testing_time >= package.time_delivered:
            Delivery_Status = "Delivered at %s" % package.time_delivered
    if package.truck_num == 2:
        if testing_time <= t2:
            Delivery_Status = "At The Hub"
        elif t2 < testing_time < package.time_delivered:
            Delivery_Status = "En Route"
        elif testing_time >= package.time_delivered:
            Delivery_Status = "Delivered at %s" % package.time_delivered
    if package.truck_num == 3:
        if testing_time <= t3:
            Delivery_Status = "At The Hub"
        elif t3 < testing_time < package.time_delivered:
            Delivery_Status = "En Route"
        elif testing_time >= package.time_delivered:
            Delivery_Status = "Delivered at %s" % package.time_delivered
    print("Package ID:", package.packID, "Delivery Status:", Delivery_Status)


# Per the project's instructions "to show the status of all packages at a time between 9:35 a.m. and 10:25 a.m.",
# the following code is set to check the delivery status of all the packages at 9:55 a.m.
# The Time Complexity of this is O(1)
testing_time = datetime.timedelta(hours=9, minutes=55)
print("\nThis is the status of all the packages at", testing_time)

# Per the project's instructions mentioned above, the following code will loop through all packages on each
# truck, to determine their delivery status ("at the hub", "en route", or "delivered") at 9:55 a.m.
# The Time Complexity of this is O(n).
for i in everyPackID:
    package = packHashNew.search(i)

    Delivery_Status = ""

    if package.truck_num == 1:
        if testing_time <= t1:
            Delivery_Status = "At The Hub"
        elif t1 < testing_time < package.time_delivered:
            Delivery_Status = "En Route"
        elif testing_time >= package.time_delivered:
            Delivery_Status = "Delivered at %s" % package.time_delivered
    if package.truck_num == 2:
        if testing_time <= t2:
            Delivery_Status = "At The Hub"
        elif t2 < testing_time < package.time_delivered:
            Delivery_Status = "En Route"
        elif testing_time >= package.time_delivered:
            Delivery_Status = "Delivered at %s" % package.time_delivered
    if package.truck_num == 3:
        if testing_time <= t3:
            Delivery_Status = "At The Hub"
        elif t3 < testing_time < package.time_delivered:
            Delivery_Status = "En Route"
        elif testing_time >= package.time_delivered:
            Delivery_Status = "Delivered at %s" % package.time_delivered
    print("Package ID:", package.packID, "Delivery Status:", Delivery_Status)

# Per the project's instructions "to show the status of all packages at a time between 12:03 p.m. and 1:12 p.m.",
# the following code is set to check the delivery status of all the packages at 12:45 p.m.
# The Time Complexity of this is O(1).
testing_time = datetime.timedelta(hours=12, minutes=45)
print("\nThis is the status of all the packages at", testing_time)

# Per the project's instructions mentioned above, the following code will loop through all packages on each
# truck, to determine their delivery status ("at the hub", "en route", or "delivered") at 12:45 p.m.
# The Time Complexity of this is O(n).
for i in everyPackID:
    package = packHashNew.search(i)

    Delivery_Status = ""

    if package.truck_num == 1:
        if testing_time <= t1:
            Delivery_Status = "At The Hub"
        elif t1 < testing_time < package.time_delivered:
            Delivery_Status = "En Route"
        elif testing_time >= package.time_delivered:
            Delivery_Status = "Delivered at %s" % package.time_delivered
    if package.truck_num == 2:
        if testing_time <= t2:
            Delivery_Status = "At The Hub"
        elif t2 < testing_time < package.time_delivered:
            Delivery_Status = "En Route"
        elif testing_time >= package.time_delivered:
            Delivery_Status = "Delivered at %s" % package.time_delivered
    if package.truck_num == 3:
        if testing_time <= t3:
            Delivery_Status = "At The Hub"
        elif t3 < testing_time < package.time_delivered:
            Delivery_Status = "En Route"
        elif testing_time >= package.time_delivered:
            Delivery_Status = "Delivered at %s" % package.time_delivered
    print("Package:", package.packID, "Delivery Status:", Delivery_Status)

# This next section of code creates the User Interface (UI), in which a user is presented with a menu where they
# have the ability to either check the status of a specific, individual package at a specific time, check the mileage
# for each delivery vehicles, as well as the combined total for all three delivery vehicles to ensure it stays under
# the project's limit of 140 combined total miles. Finally, the UI also has an "exit" option as well.
# The Time Complexity of this is O(1).
while(1):
    user_ContinueSelection = ''
    user_MenuSelection = int(input('\n Please enter "1" to Check Package Status'
                                   '\n Please enter "2" to Check Delivery Truck Mileage'
                                   '\n Please enter "3" to Exit Program\n'))

    # If the user selects that they want to check the status of a specific package, they will first be asked to enter
    # a Package ID (1-40).
    if user_MenuSelection == 1:
        while user_ContinueSelection != 'no':
            userPackageId = int(input('\nPlease enter a specific Package ID (1-40):\n'))

            # The user will then be asked to enter a time (Hours:Minutes).
            user_time = input('\nPlease enter a time (HH:MM) during the travel of the route:\n')
            (h, m) = user_time.split(":")
            userinput_Time = datetime.timedelta(hours=int(h), minutes=int(m))

            userPackage = packHashNew.search(userPackageId)
            userDelivery_Status = ""

            # Based on the time entered by the user, the following then determines the delivery status of the specified
            # package and subsequently displays whether it is "at the hub", "en route" or "delivered".
            if userPackage.truck_num == 1:
                if userinput_Time <= t1:
                    userDelivery_Status = "At The Hub"
                elif t1 < userinput_Time < userPackage.time_delivered:
                    userDelivery_Status = "En Route"
                elif userinput_Time >= userPackage.time_delivered:
                    userDelivery_Status = "Delivered at %s" % userPackage.time_delivered
            if userPackage.truck_num == 2:
                if userinput_Time <= t2:
                    userDelivery_Status = "At The Hub"
                elif t2 < userinput_Time < userPackage.time_delivered:
                    userDelivery_Status = "En Route"
                elif userinput_Time >= userPackage.time_delivered:
                    userDelivery_Status = "Delivered at %s" % userPackage.time_delivered
            if userPackage.truck_num == 3:
                if userinput_Time <= t3:
                    userDelivery_Status = "At The Hub"
                elif t3 < userinput_Time < userPackage.time_delivered:
                    userDelivery_Status = "En Route"
                elif userinput_Time >= userPackage.time_delivered:
                    userDelivery_Status = "Delivered at %s" % userPackage.time_delivered


            print("\n\nUser Time:", userinput_Time, "\nPackage ID:", userPackage.packID, "       Delivery Status:", userDelivery_Status, "\nDeadline:", userPackage.delivery_deadline, "\nDelivery Address: ", userPackage.street, userPackage.delivery_city, userPackage.state, userPackage.delivery_zip_code, "\nPackage Weight (kilo):", userPackage.package_weight_kilo, "\nSpecial Notes:", userPackage.special_notes,  "\nTruck Number:", userPackage.truck_num)

            # The user is prompted whether they would like to check the status for a different package. If they enter
            # "yes", they are returned back to beginning of "check package status". If they enter "no" they are
            # returned to the main menu.
            user_ContinueSelection = (input('Do you want to check the status for a different package (yes/no)?\n'))

    # If the user selects option 2 to display the mileage, then each of the three delivery truck's individual total
    # mileage will display, as well as their combined, overall mileage.
    # Note: Goal of project is to stay under 140 total miles. The project's current total miles is 126.7.
    if user_MenuSelection == 2:
        print("Delivery Truck 1's individual total miles: ", truck1.mileage)
        print("Delivery Truck 2's individual total miles: ", truck2.mileage)
        print("Delivery Truck 3's individual total miles: ", truck3.mileage)
        totalMileage = (truck1.mileage + truck2.mileage + truck3.mileage)
        print("Total Miles for all 3 trucks combined: ", totalMileage)

    # If the user selects option 3, they will "exit" the program.
    if user_MenuSelection == 3:
        break