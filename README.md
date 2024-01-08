# haduk-met-data-at-site-locations
Extracting HadUK meteorology data at a set of locations. 

This repository downloads data from the Had-UK GRID and extracts variables from a set of specified locations.

## Data

Meteorology data: HadUK-Grid Gridded Climate Observations on a 1km grid over the UK, v1.2.0.ceda (1836-2022), available from CEDA under the Open Government License: https://dx.doi.org/10.5285/46f8c1377f8849eeb8570b8ac9b26d86

Site locations: CSV file of named location with latitude and longitude of site.

## Using this repository

1. Create a virtual environment `python3 -m venv venv` 
2. Activate the virtual environment `. venv/bin/activate`
3. Install the packages from `requirements.txt`: `pip3 install -r requirements.txt`
4. Create a user account on the (CEDA website)[https://services.ceda.ac.uk/cedasite/myceda].
5. Configure your FTP account. Login, then go to (MyCEDA)[https://services.ceda.ac.uk/cedasite/myceda]  then click on Configure FTP Account. Click on the link to Create Password. For further help with this step, consult https://help.ceda.ac.uk/article/280-ftp.
6. Run the script `download_haduk_data.py`

## Examples
 