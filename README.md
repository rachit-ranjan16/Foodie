# foodie
Command Line App to use Food2Fork's Search API through REST calls to fetch top recipe for the given ingredients and report missing ones

## Prerequisites 
- Git installed and configured 
- Python 3.5+ with **pip installed** (Refer [Anaconda](https://conda.io/docs/user-guide/install/index.html') for quick setup)
    - Preferably in a virtualenv (pyvenv, virtualenv, conda)
- Internet Connection with Proxy Settings at OS level
    - For installing dependencies and running the app 
    
## Ops  
- Clone Git Repo 
    - `git clone https://github.com/rachit-ranjan16/foodie.git`
- Navigate to `~foodie/`
- Install dependencies 
    - `python setup.py develop`
- Run Application 
    - Linux/Mac
        -  `python foodie/ingreds.py`
    - Windows
        - `python foodie\ingreds.py`


## Design 
#### Sequence Diagram
![Could not display. Check design/SequenceDiag.png](/design/SequenceDiag.png?raw=true "Component Diagram")
