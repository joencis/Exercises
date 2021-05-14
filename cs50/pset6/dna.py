import csv
import sys
import re


def main():

    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py FILENAME FILENAME")

    STRs = []
    with open(f"{sys.argv[1]}", "r") as data: # opening the persons file and storing it as a list of dicts
        for line in csv.DictReader(data):
            STRs.append(line)

    with open(f"{sys.argv[2]}", "r") as data: # opening the sequence file and storing is a list of only one string
        for line in csv.reader(data):
            sequence = line

    STRs_counter = matcher(STRs, sequence[0])    # call the matcher functions which returns a dict with the keys (STRS) and values (number of consecutive repteats) counted in the sequence

    List_of_keys = STRs[0].keys()                # gives back a list list of the keys of the dict
    List_of_keys = list(List_of_keys)
    number_of_items = len(list(STRs[0].keys())) #counts the total number of items for the iteration
    match_found = 0

    for person in STRs:                                 #iterates over each person for a match
        match_counter = 0
        for item in range(1, number_of_items):          #iterates over each key of each person dict for a match
            item_string = List_of_keys[item]
            if int(person[item_string]) == STRs_counter[item_string]:
                match_counter += 1
            if match_counter == number_of_items - 1:        #checks if all the required keys matched except the name key
                match = person["name"]
                print(f"{match}")
                match_found += 1
                break
    if match_found == 0:
        print("No match")


def matcher(STRs, sentences):           #this function calculates the longest consecutive count of each key of the STRs in the sentences and returns it as a dict.
    STRs_total = {}
    List_of_items = STRs[0].keys()
    List_of_items = list(List_of_items)
    number_of_items = len(List_of_items)
    for item in range(1, number_of_items):
        max_length = 0
        string = List_of_items[item]
        p = rf'({string})+'             #string with the syntax for the RE engine. the + means check for 1 or more of consecutive repeats of the capture group
        res = re.finditer(p, sentences) #findither returns and iterator yelding all the match objects found in the sentence
        for match in res:
            match_length = len(match.group())
            if match_length > max_length:
                max_length = match_length
        item_counter = max_length / len(List_of_items[item]) #divides the length of the total sequence by the length of the repeating string to calculate the number of repeats
        STRs_total[string] = int(item_counter)
    return STRs_total                   #returns a dict with all the keys and the counts found for each in the sequence. like the person STRs loaded before, but only missing the name key


main()