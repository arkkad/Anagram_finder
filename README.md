Anagram finder http service

This is simple http service developed on Django framework

Usage example:
    
    curl localhost:8000/load -d '["foobar", "aabb", "baba", "boofar", "живу", "вижу", "AbbA", "BaBa"]' - for adding list of words
    
    curl localhost:8000/get?word=BaBa - to searching anagrams
    
    curl localhost:8000/clear - to clear anagram list
    
Two options to start this service:
    
    1 Options 
    
    Step 1:

    Installing virtualenv $ python3 -m pip install --user virtualenv

    Creating a virtual environment $ python3 -m venv env

    Activating a virtual environment $ source env/bin/activate

    Using requirements files $ pip install -r requirements.txt

    Step 2:

    To run the application, use the command (port can be changed)

    $ python3 manage.py runserver 0:8000
    
    
    
    2 Option (using docker)
    
    Step 1 - install and configure Docker
    
    Step 2 
    
    From a docker-compose.yaml file folder run command - $ docker-compose up
    
    
Unit tests are located in test.py file

    For starting test rum command - $ python3 manage.py test
    