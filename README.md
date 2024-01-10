# Explore HadUK meteorology data

This repository downloads data from the Had-UK GRID and explores the data. In particular, it finds the location within the UK with the minimum temperature each year and explores the temperatures across the year at this location. The aim of this is understand ways of working with these temperature data in order to work with data from specific locations or within specific date ranges and temperature profiles.  

## Data

Monthly air temperature data: HadUK-Grid Gridded Climate Observations on a 1km grid over the UK, v1.2.0.ceda (1836-2022), available from CEDA under the Open Government License: https://dx.doi.org/10.5285/46f8c1377f8849eeb8570b8ac9b26d86

See the section below for how to create a user account and access the data.

## Using this repository

Note: this repository uses (Iris)[https://scitools-iris.readthedocs.io/en/latest/index.html]  which is not tested for use on Mac or Windows (see https://scitools-iris.readthedocs.io/en/latest/installing.html#installing-iris)

1. Clone this repository.
2. In the cloned directory, create a virtual environment `python3 -m venv venv`
3. Activate the virtual environment `. venv/bin/activate`
4. Install the packages from `requirements.txt`: `pip3 install -r requirements.txt`
5. Create a user account on the (CEDA website)[https://services.ceda.ac.uk/cedasite/myceda]. 
6. Configure your FTP account. Login, then go to (MyCEDA)[https://services.ceda.ac.uk/cedasite/myceda]  then click on Configure FTP Account. Click on the link to Create Password. For further help with this step, consult https://help.ceda.ac.uk/article/280-ftp. 
7. Run the script `download_haduk_data.py` to download three NetCDF files containing the meteorology data. 
8. Run the script `get_haduk_data_at_sites.py` to explore and plot the data.

## Outputs

Data exploration will be printed to the console. This shows the structure of the original NetCDF files and describes the parameters which are contained within the file, as well as additional file metadata. 

Following the data exploration for the year, a short summary of the year, minimum temperature and month of when this was, is also printed to the console.

The following plots will be created and saved as `png` files in the repository directory: 
* `YEAR_average_air_temperature.png` plots the average temperature of the month in which the minimum temperature of that year, was found. This plot covers the UK. 
* `YEAR_average_monthly_air_temperature.png` shows the average monthly temperatures at the location in which the minimum temperature of that year, was found. 
 