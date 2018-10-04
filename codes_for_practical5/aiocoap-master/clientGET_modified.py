#!/usr/bin/env python3
# coding=utf-8

# This file is part of the Python aiocoap library project.
#
# Copyright (c) 2012-2014 Maciej Wasilak <http://sixpinetrees.blogspot.com/>,
#               2013-2014 Christian Amsüss <c.amsuess@energyharvesting.at>
#
# aiocoap is free software, this file is published under the MIT license as
# described in the accompanying LICENSE file.

import logging
import asyncio
import time
import sys
import math

from aiocoap import *

logging.basicConfig(level=logging.INFO)


@asyncio.coroutine
def main():
    y=0
    x=1    
    reading_interval = 1 #The time interval between each GET request in second
    reading_num = 3 #How many RSSI samples you try to get?
    while x<reading_num:
        protocol = yield from Context.create_client_context()
        protocol1 = yield from Context.create_client_context()
        protocol2 = yield from Context.create_client_context()
        protocol3 = yield from Context.create_client_context()
        protocol4 = yield from Context.create_client_context()

        request = Message(code=GET)
        request1 = Message(code=GET)
        request2 = Message(code=GET)
        request3 = Message(code=GET)
        request4 = Message(code=GET)

        #Configure the IP address of the CoAP server here
        #Also, you may need to change the URL depending on the implementation of your CoAP server
        request.set_request_uri('coap://[aaaa::212:4b00:f10:6382]:5683/parent/RSSI')
        try:
            response = yield from protocol.request(request).response
        except Exception as e:
            print('Failed to fetch resource: ')
            print('Number 3: fail...')
            print(e)
        else:
            #print('Result: %s\n%r'%(response.code, response.payload))
            #Get the RSSI value from the payload
            print(response.payload.decode('ascii'))
            with open('record.txt', 'at') as f:
                f.write(response.payload.decode('ascii')+'\n')
            #y=y+int(response.payload.decode('ascii'))


        request1.set_request_uri('coap://[aaaa::212:4b00:f18:5b86]:5683/parent/RSSI')
        try:
            response1 = yield from protocol1.request(request1).response
        except Exception as e:
            print('Failed to fetch resource: ')
            print('Number 1: fail...')
            print(e)
        else:
             #print('Result: %s\n%r'%(response.code, response.payload))
             #Get the RSSI value from the payload
            print(response1.payload.decode('ascii'))
            with open('record.txt', 'at') as f:
                f.write(response1.payload.decode('ascii')+'\n')
        
        request3.set_request_uri('coap://[aaaa::212:4b00:f19:8501]:5683/parent/RSSI')
        try:
            response3 = yield from protocol3.request(request3).response
        except Exception as e:
            print('Failed to fetch resource: ')
            print('Number 5: fail...')
            print(e)
        else:
             #print('Result: %s\n%r'%(response.code, response.payload))
             #Get the RSSI value from the payload
            print(response3.payload.decode('ascii'))
            with open('record.txt', 'at') as f:
                f.write(response3.payload.decode('ascii')+'\n')
             #y=y+int(response.payload.decode('ascii'))



        request4.set_request_uri('coap://[aaaa::212:4b00:1666:3882]:5683/parent/RSSI')
        try:
            response4 = yield from protocol4.request(request4).response
        except Exception as e:
            print('Failed to fetch resource: ')
            print('Number 4: fail...')
            print(e)
        else:
             #print('Result: %s\n%r'%(response.code, response.payload))
             #Get the RSSI value from the payload
            print(response4.payload.decode('ascii'))
            with open('record.txt', 'at') as f:
                f.write(response4.payload.decode('ascii')+'\n')
             #y=y+int(response.payload.decode('ascii'))


        request2.set_request_uri('coap://[aaaa::212:4b00:a54:e080]:5683/parent/RSSI')
        try:
            response2 = yield from protocol2.request(request2).response
        except Exception as e:
            print('Failed to fetch resource: ')
            print('Number 2: fail...')
            print(e)
        else:
             #print('Result: %s\n%r'%(response.code, response.payload))
             #Get the RSSI value from the payload
            print(response2.payload.decode('ascii'))
            with open('record.txt', 'at') as f:
                f.write(response2.payload.decode('ascii')+'\n')
             #y=y+int(response.payload.decode('ascii'))
        print('Episode: ', x, 'Finished...')
        x=x+1

        #put into sleep
        time.sleep(reading_interval)



    #x=1
    print(x, reading_num)
    with open('record.txt', 'at') as f:
        f.write('-----End of Group-----\n')    
        
    #print(math.pow(10,(y/10+14.482)/-16.102), "cm")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
