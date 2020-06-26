Sample Server
=============

.. contents::

This is the endpoint for the indoor_sampler will POST readings too. It only 
supports a single client POSTing data as I'm writing is to an append-only CSV 
file on receipt.

This is super "MVP". I simply persist the data to disk at the moment. There is 
only one arduino ethernet running so this isn't a problem.

This is part of the `House Weather Project <https://github.com/users/oisinmulvihill/projects/3>`_.

Development
-----------

To set up the code for development you can::

    mkvirtualenv --clear -p python3 sample_server
    pip install -r requirements.txt
    pip install -r test-requirements.txt
    
To run the server enable the environment and then::

    # activate the env
    workon sample_server

    # from the sample_server checkout dir:
    python sample_server/main.py


REST API
--------

POST /log/sample/indoor
~~~~~~~~~~~~~~~~~~~~~~~

The `Indoor Sampler <https://github.com/oisinmulvihill/indoor_sampler>`_. uses 
this endpoint when logging samples.

For simplicity sake the Ardunio Ethernet code POSTs the body as Content-Type
application/x-www-form-urlencoded. For example this looks like::

    type=bme680&t=02473&h=040913&p=101461&g=01358087

The endpoint returns 200 "Received OK, Thanks." in response. 

The endpoint also looks for the customer header X-MAC. This is the MAC address 
of the board logging samples.


