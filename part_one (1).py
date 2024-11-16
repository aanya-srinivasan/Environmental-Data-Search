#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 13:37:42 2024

@author: amandachiang

GROUP MEMBERS: Amanda Chiang, Mark Hrytchak, Aanya Srinivasan
"""
    
# reads air quality csv file, returns a tuple (geo_map, date_map)
# geo_map is a dictionary mapping each UHF id to a list of measurement tuples (UHF id, region, date, pm) with that UHF id
# date_map is a dictionary mapping each date to a list of measurement tuples (UHF id, region, date, pm) from that date
def read_air_qual():
    
    geo_map = {}
    date_map = {}
    
    with open("air_quality.csv", "r") as air_quality:
    
        for line in air_quality:
            # Clean the line
            line = line.strip()
            line = line.strip("\ufeff")
            data = tuple(line.split(","))
            
            if data[0] not in geo_map:
                geo_map[data[0]] = []
            geo_map[data[0]].append(data)
            if data[2] not in date_map:
                date_map[data[2]] = []
            date_map[data[2]].append(data)

    print(geo_map["101"])
    return geo_map, date_map
    
# reads UHF csv files and returns a tuple (zip_map, borough_map)
# zip_map is a dictionary that maps each zip code to a list of corresponding UHF ids
# borough_map is a dictionary that maps each borough to a list of corresponding UHF ids
def read_uhf():
    
    zip_map = {}
    borough_map = {}
    
    with open("uhf.csv", "r") as uhf:
    
        for line in uhf:
            line = line.strip()
            data = list(line.split(","))
            zips = data[3:]
            for i in range(len(zips)):
                if zips[i] not in zip_map:
                    zip_map[zips[i]] = []
                zip_map[zips[i]].append(data[2])
            if data[0] not in borough_map:
                borough_map[data[0]] = []
            # prevent duplicate geo IDs
            if data[2] not in borough_map[data[0]]:
                borough_map[data[0]].append(data[2])
    return zip_map, borough_map


def search(geo_map, date_map, zip_map, borough_map):
    query_type = input("Would you like to search by 'zip code', 'UHF id', 'borough', or 'date'?\n")
    
    if query_type.lower() == "zip" or query_type.lower() == "zip code":
        zip_code = input("Enter zip code: ")
        for i in range(len(zip_map[zip_code])):
            uhf_id = zip_map[zip_code][i]
            for j in range(len(geo_map[uhf_id])):
                region = geo_map[uhf_id][j][1]
                date = geo_map[uhf_id][j][2]
                pm = geo_map[uhf_id][j][3]
                print(date, " UHF ", uhf_id, " ", region, " ", pm, " mcg/m^3")
    elif query_type.lower() == "uhf id" or query_type == "id":
        uhf_id = input("Enter UHF id: ")
        for j in range(len(geo_map[uhf_id])):
            region = geo_map[uhf_id][j][1]
            date = geo_map[uhf_id][j][2]
            pm = geo_map[uhf_id][j][3]
            print(date, " UHF ", uhf_id, " ", region, " ", pm, " mcg/m^3")
    elif query_type.lower() == "borough":
        print("Borough options: 'Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'StatenIsland'")
        borough = input("Enter borough (case sensitive): ")
        for i in range(len(borough_map[borough])):
            uhf_id = borough_map[borough][i]
            for j in range(len(geo_map[uhf_id])):
                region = geo_map[uhf_id][j][1]
                date = geo_map[uhf_id][j][2]
                pm = geo_map[uhf_id][j][3]
                print(date, " UHF ", uhf_id, " ", region, " ", pm, " mcg/m^3")
    elif query_type.lower() == "date":
        date = input("Enter date: ")
        for i in range(len(date_map[date])):
            uhf_id = date_map[date][i][0]
            for j in range(len(geo_map[uhf_id])):
                region = geo_map[uhf_id][j][1]
                pm = geo_map[uhf_id][j][3]
                print(date, " UHF ", uhf_id, " ", region, " ", pm, " mcg/m^3")
    else:
        inp = input("Invalid input. Please re-enter what you would like to search by: ")
        search(geo_map, date_map, zip_map, borough_map)
    
    
def main():
        
    geo_map, date_map = read_air_qual()
    zip_map, borough_map = read_uhf()
    
    hi = 2
    search(geo_map, date_map, zip_map, borough_map)

    
if __name__ == "__main__":
    main()

    
        
    
    


    