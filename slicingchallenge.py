#!/usr/bin/python3

def main():

    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]    
    print ("Challenge")
    print ("---------------------------------")
    print ("challenge[2][1]")
    print ("challenge[2][0]")
    print ("challenge[3]")
    print (f"My {challenge[2][1]}, the {challenge[2][0]} do {challenge[3]}!")
    
    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
    print ("")
    print ("Trial")
    print ("---------------------------------")
    print ("trial[2]['goggles']")
    print ("trial[2]['eyes']")
    print ("trial[3]")
    print (f"My {trial[2]['goggles']}, the {trial[2]['eyes']} do {trial[3]}")

    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]
    print ("")
    print ("Nightmare")
    print ("---------------------------------")
    print ("nightmare[0]['user']['name']['first']")
    print ("nightmare[0]['kumquat']")
    print ("nightmare[0]['d']")
    print(f"Nightmare = My {nightmare[0]['user']['name']['first']}, the {nightmare[0]['kumquat']} do {nightmare[0]['d']}!")

if __name__ == "__main__":
    main()

