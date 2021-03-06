#!/usr/bin/python3

# JSON is part of the Python Standard Library
import json

def main():
    ## open the file
    with open("challenge.json", "r") as challenge:
        challengestring = challenge.read()

    challengedecoded = json.loads(challengestring )
    
    #print(f"Full name: {challengedecoded[3]['name']}")
    #print(f"Eye color: {challengedecoded[3]['eyeColor']}")
    #print(f"Favorite Fruit: {challengedecoded[3]['favoriteFruit']}")

    for info in challengedecoded:
        print(f"Name: {info['name']}")
        print(f"Email: {info['email']}")
        print(f"Phone: {info['phone']}")
        print(f"Address: {info['address']}")
        print ("")

if __name__ == "__main__":
    main()
