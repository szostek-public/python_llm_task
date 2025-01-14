## 1. Instructions to run script

From the same directory as this README file: 
- Follow [4] to set up virtual environment. (Python version used: Python 3.9.6 )
- Note this is for example only as there are no non native python packages. 

Run script using either python: 

- `python3 exact_requirements.py`

or bash (I am on a mac)
- make executable: `chmod +x ./exact_requirements.py`
- run:  `./exact_requirements.py`


## 2. Assumptions and design decisions

- The contents of `regulations.txt` is a "copy paste" from:
     page3 of https://docs.londonstockexchange.com/sites/default/files/documents/rules-of-the-london-stock-exchange-effective-5-february-2024.pdf at 11.27am 14/01/25. 

- Python 3.9.6 

- Assumption: `regulations.txt` is small enough to be held in python memory. IE do not need to read in line by line. 

## 3. Explanation of how LLM integration is simulated

This has been simulated by returning the first five tokens in each section.


## 4. Dependencies and installation instructions

This is for illustration only. I have not used any packages that need installing. 

Create virtualenv
`python3 venv .venv`

Activate virtualenv
`source .vene/bin/activate`

Install pip packages
`pip3 install requirements.txt`


## More time
 - add better paragraph splitter. 
 - EG https://medium.com/@npolovinkin/how-to-chunk-text-into-paragraphs-using-python-8ae66be38ea6
