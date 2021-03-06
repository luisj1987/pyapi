#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    ## first I want to grab my credentials
    with open("/home/student/pyapi/chapter12/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")        

    ## update the date below, if you like
    inputdate = input("Please enter a start date (YYYY-MM-DD):  " )
    startdate = "&start_date="+inputdate

    ## the value below is not being used in this
    ## version of the script
    enddate = input("Optional, enter an end date (YYYY-MM-DD):  " )

    if enddate == "":
        neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)
        
    else:
        enddate = "&end_date="+enddate
        neowrequest = requests.get(NEOURL + nasacreds + startdate + enddate)
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    #neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print('Number of asteriods: ' + str(neodata["element_count"]))
    
    asteroid_sizes= {}
    asteroid_names= []
    danger_count= 0
    #print(f"Total Asteroids in Range: {neodata['element_count']}")
    for date in neodata["near_earth_objects"].keys():
        for aster in neodata["near_earth_objects"][date]:
            asteroid_sizes[aster["name"]]= aster["estimated_diameter"]["meters"]["estimated_diameter_max"]
            asteroid_names.append(aster["name"])
            if aster["is_potentially_hazardous_asteroid"]:
                danger_count += 1

    print(f"Largest Asteroid (meters): {max(asteroid_sizes)}")
    print(f"Number of potentially hazardous asteroids: {danger_count}")
    #input("Press ENTER to see a list of all asteroids.")
    #print(asteroid_names) 

if __name__ == "__main__":
    main()

