#!/usr/bin/python3

def main():

    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

    x=(challenge[2][1])
    y=(trial[2]['eyes'])
    z=(nightmare[0]['d'])

    print (challenge[2][1])
    print (trial[2]['eyes'])
    print (nightmare[0]['d'])

    print ("My "+x+"!"+" The "+y+" do "+z+"!")

if __name__ == "__main__":
    main()

