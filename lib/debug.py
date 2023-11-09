#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
    rmnp = NationalPark("Rocky Mountain National Park")
    me = Visitor("ellen")
    jos = Visitor("josie")
    proposal = Trip(me, rmnp, "05/31/2021", "06/01/2021")

    ipdb.set_trace()
