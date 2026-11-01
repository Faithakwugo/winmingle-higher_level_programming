#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxi = None
    maxi_key = None
    for key, value in a_dictionary.items():
        if maxi is None or value > maxi:
            maxi = value
            maxi_key = key
    return(maxi_key)
