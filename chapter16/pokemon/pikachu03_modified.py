#!/usr/bin/python3

## for accepting arguments from the cmd line
import argparse

## for making HTTP requests
## python3 -m pip install requests
import requests

## for working with data in lots of formats
## python3 -m pip install pandas
import pandas

POKEMON = "http://pokeapi.co/api/v2/pokemon/"

def main():

    # Make HTTP GET request using requests
    # and decode JSON attachment as pythonic data structure
    # Also, append the URL ITEMURL with a parameter to return 1000
    # items in one response
    items = requests.get(f"{POKEMON}?limit=898")
    items = items.json()

    # create a list to store items with the word searched on
    matchedwords = []

    # Loop through data, and print pokemon names
    # item.get("results") will return the list
    # mapped to the key "results"
    for item in items.get("results"):
        # check to see if the current item's VALUE mapped to item["name"]
        # contains the search word
        #if args.searchword in item.get("name"):
            # if TRUE, add that item to the end of list matchedwords
        matchedwords.append(item.get("name"))

    finishedlist = matchedwords.copy()
    ## map our matchedword list to a dict with a title
    matchedwords = {}
    matchedwords["Pokemon List"] = finishedlist
    cnt = len(finishedlist)+1

    ## list all words containing matched word
    print(f"There are a total of {cnt} pokemon in the Pokemon API!")
    #print(f"List of Pokemon items containing '{args.searchword}': ")
    #print(matchedwords)

    ## export to excel with pandas
    # make a dataframe from our data
    itemsdf = pandas.DataFrame(matchedwords)
    # export to MS Excel XLSX format
    # run the following to export to XLSX
    # python -m pip install openpyxl
    # index=False prevents the index from our dataframe from
    # being written into the data
    itemsdf.to_csv("pokemonlist.csv", index=False)
    itemsdf.to_json("pokemonlist.json")
    itemsdf.to_excel("pokemonlist.xlsx", index=False)

    print("Gotta catch 'em all!")

if __name__ == "__main__":
    main()

