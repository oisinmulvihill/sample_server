Sample Server
=============

This is the endpoint for the indoor_sampler will POST readings too. It only 
supports a single client POSTing data as I'm writing is to an append-only CSV 
file on receipt.

This is super "MVP". I simply persist the data to disk at the moment. There is 
only one arduino ethernet running so this isn't a problem.

The 

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
