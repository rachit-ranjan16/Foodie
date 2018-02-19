# foodie
Command Line App to use Food2Fork's Search API through REST to fetch top recipe for the given ingredients and report missing ones

## Prerequisites 
- Python 3.5+ with **pip installed** 
    - Preferably in a virtualenv (pyvenv, virtualenv, anaconda)
- Internet Connection with Proxy Settings at OS level
    - For installing dependencies and running the app 
    
## Ops  
- Install dependencies 
    - `python setup.py develop`
- Run Application 
    - Windows
        - `python foodie\ingreds.py`
    - Linux/Mac
        -  `python foodie/ingreds.py`

## Design 
![Could not display. Check design/SequenceDiag.png](/design/SequenceDiag.png?raw=true "Component Diagram")
