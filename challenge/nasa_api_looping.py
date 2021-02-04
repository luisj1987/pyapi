#!/usr/bin/python3

import requests


def main():
    roverresp = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=gT8fYoCsl1LkiFELTUe1kBKSPpMgxAVoVGwSmG6F").json()

    #Challeng #1: Hard
    #for photos in roverresp["photos"]:
    #    print (photos["img_src"])
    
    #Challeng #2: Harder
    #for photos in roverresp["photos"]:
    #    print (photos["rover"]["name"])
    #    print (photos["earth_date"])
    #    print (photos["img_src"])
    #    print ()     

    #Challenge #3: Hardest
    camera = input("Which camera would you like to see? ")
    all_cams= ["FHAZ","RHAZ","MAST","CHEMCAM","NAVCAM"]
    for roverdict in roverresp["photos"]:
        if roverdict["camera"]["name"] == camera:
            print(roverdict["rover"]["name"])
            print(roverdict["earth_date"])
            print(roverdict["img_src"])
            print() 



if __name__ == "__main__":
    main()
