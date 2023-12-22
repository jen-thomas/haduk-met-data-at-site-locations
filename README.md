# haduk-met-data-at-site-locations
Extracting HadUK meteorology data at a set of locations. 

This repository downloads data from the Had-UK GRID and extracts variables from a set of specified locations. 


## Data

Had-UK 1km-GRID data (available from CEDA under the Open Government License v XX).

Site locations: CSV file of named location with latitude and longitude of site.

## Using this repository

1. Create a virtual environment `python3 -m venv venv` 
2. Activate the virtual environment `. venv/bin/activate`
3. Install the packages from `requirements.txt`: `pip3 install -r requirements.txt`
4. Create a directory called `ceda_data` where the data will be downloaded

## Examples
 