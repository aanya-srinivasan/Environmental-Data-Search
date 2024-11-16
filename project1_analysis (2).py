#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:32:12 2024

@author: amandachiang

GROUP MEMBERS: Amanda Chiang, Mark Hrytchak, Aanya Srinivasan
"""

from part_one import read_air_qual
from part_one import read_uhf
from part_one import search

# returns a list of tuples (uhf_id, region, date, pm) based on a query that is either a uhf_id, date, zip code, borough, region, or year
def get_pm(query_type, query, geo_map, date_map, zip_map, borough_map):
    data = []
    if query_type.lower() == "zip" or query_type.lower() == "zip code":
        zip_code = query
        for i in range(len(zip_map[zip_code])):
            uhf_id = zip_map[zip_code][i]
            for j in range(len(geo_map[uhf_id])):
                region = geo_map[uhf_id][j][1]
                date = geo_map[uhf_id][j][2]
                pm = geo_map[uhf_id][j][3]
                entry = (uhf_id, region, date, pm)
                data.append(entry)
    elif query_type.lower() == "uhf id" or query_type.lower() == "id" or query_type.lower() == "uhf":
        uhf_id = query
        for j in range(len(geo_map[uhf_id])):
            region = geo_map[uhf_id][j][1]
            date = geo_map[uhf_id][j][2]
            pm = geo_map[uhf_id][j][3]
            entry = (uhf_id, region, date, pm)
            data.append(entry)
    elif query_type.lower() == "borough":
        borough = query
        for i in range(len(borough_map[borough])):
            uhf_id = borough_map[borough][i]
            for j in range(len(geo_map[uhf_id])):
                region = geo_map[uhf_id][j][1]
                date = geo_map[uhf_id][j][2]
                pm = geo_map[uhf_id][j][3]
                entry = (uhf_id, region, date, pm)
                data.append(entry)
    elif query_type.lower() == "date":
        date = query
        for i in range(len(date_map)):
            uhf_id = date_map[date][i][0]
            for j in range(len(geo_map[uhf_id])):
                region = geo_map[uhf_id][j][1]
                pm = geo_map[uhf_id][j][3]
                entry = (uhf_id, region, date, pm)
                data.append(entry)
    elif query_type.lower() == "year":
        # years are 2-digit inputs. 2019 is "19"
        if len(query) == 4:
            year = query[-2:]
        else:
            year = query
        for date in date_map:
            if date[-2:] == year:  
                for i in range(len(date_map[date])):
                    uhf_id = date_map[date][i][0]
                    for j in range(len(geo_map[uhf_id])):
                        region = geo_map[uhf_id][j][1]
                        pm = geo_map[uhf_id][j][3]
                        entry = (uhf_id, region, date, pm)
                        data.append(entry)
    return data
        
# returns a tuple (low, high) of the lowest and highest pollution ever recorded in a given zip code
def high_low_poll(zip_code, geo_map, date_map, zip_map, borough_map):
    li = get_pm("zip code", zip_code, geo_map, date_map, zip_map, borough_map)
    low = 100000000
    high = 0
    for i in range(len(li)):
        pm = float(li[i][3])
        if pm > high:
            high = pm
        if pm < low:
            low = pm
    return (low, high)
    
# returns the UHF id with the absolute maximum pollution in the given year
def worst_poll(year, geo_map, date_map, zip_map, borough_map):
    worst_id = ""
    worst_poll = 0
    data = get_pm("year", year, geo_map, date_map, zip_map, borough_map)
    
    for i in range(len(data)):
        if float(data[i][3]) > worst_poll:
            worst_id = data[i][0]
            worst_poll = float(data[i][3])
            
    return worst_id

def avg_poll(year, borough, geo_map, date_map, zip_map, borough_map):
    total = 0
    count = 0

    data = get_pm("year",year,geo_map,date_map,zip_map,borough_map)
    for i in range(len(data)):
        if data[i][0] in borough_map[borough]:
            total += float(data[i][3])
            count += 1
            
    return total / count
        
# Returns the borough with the highest pollution in a given year and its respective average
def highest_avg_poll(year, geo_map, date_map, zip_map, borough_map):
    # List highest will record the borough with the highest pollution and its average in the order [borough, avg]
    highest = ["",0]
    data = get_pm("year",year,geo_map,date_map,zip_map,borough_map)
    
    borough_poll = {}
    # Set up the different boroughs as unique keys
    for borough in borough_map:
        if borough not in borough_poll:
            borough_poll[borough] = 0
            
    for borough in borough_poll:
        borough_poll[borough] = avg_poll(year, borough, geo_map, date_map, zip_map, borough_map)
        if borough_poll[borough] > highest[1]:
            highest[0] = borough
            highest[1] = float(borough_poll[borough])
            
    return highest
     
           
# Returns the unique UHF neighborhoods in a given year within a borough that exceeded the pollution threshold
def uhf_above_threshold(thresh, year, borough, geo_map, date_map, zip_map, borough_map):
    # Extract data for the given year
    data = get_pm("year", year, geo_map, date_map, zip_map, borough_map)
    
    # Make borough map lookup faster
    # borough_zips is a set of all zip codes in the borough
    borough_zips = set(borough_map.get(borough, []))
    
    # Set to store unique UHF neighborhoods that exceeded the threshold
    unique_uhf = set()
    
    for i in range(len(data)):
        # Check if the zip code belongs to the specified borough
        if data[i][0] in borough_zips:
            # Check if the pollution level exceeds or meets the threshold
            pollution_level = float(data[i][3])
            if pollution_level >= thresh:
                # Add the UHF (assumed to be stored in data[i][0]) to the set
                unique_uhf.add(data[i][0])
    
    # Return the unique UHF neighborhoods
    return unique_uhf
    
    
def main():
    read_air_qual()
    read_uhf()
    
    geo_map, date_map = read_air_qual()
    zip_map, borough_map = read_uhf()
    
    dicts = [geo_map, date_map, zip_map, borough_map]
    
    z1 = "10027"
    h_l = high_low_poll(z1, geo_map, date_map, zip_map, borough_map)
    print(f"The lowest pollution ever recorded in zip code {z1} is: {h_l[0]} mcg/m^3")
    print(f"The highest pollution ever recorded in zip code {z1} is: {h_l[1]}")
    
    
    worst_id_19 = worst_poll("2019", geo_map, date_map, zip_map, borough_map)
    print(f"The UHF id with the worst/highest pollution in 2019 is: {worst_id_19}")

    avg_poll_man_08 = avg_poll("08", "Manhattan", geo_map, date_map, zip_map, borough_map)
    avg_poll_man_19 = avg_poll("19", "Manhattan", geo_map, date_map, zip_map, borough_map)
    print(f"The average air pollution in Manhattan in 2008 is: {avg_poll_man_08}")
    print(f"The average air pollution in Manhattan in 2019 is: {avg_poll_man_19}")
    
    print("RESEARCH QUESTION 1: Which UHF ids within Brooklyn exceeded 10 mcg/m^3 in 2019?")
    thresh_10_19_brook = uhf_above_threshold(10,"2019","Brooklyn",geo_map,date_map,zip_map,borough_map)
    print(thresh_10_19_brook)
    
    
    print("RESEARCH QUESTION 2: Which borough had the highest avg pollution in 2019?")
    high_avg_19 = highest_avg_poll("2019", geo_map, date_map, zip_map, borough_map)
    print(high_avg_19[0], "with", high_avg_19[1], "mcg/m^3 on average")
    

if __name__ == "__main__":
    main()