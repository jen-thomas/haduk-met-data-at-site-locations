# Explore HadUK meteorology data

## Introduction

Temperature data from across the UK are required to understand the conditions at specific locations when aphids undertake their first flight in spring. The temperature during the preceding months is also of huge importance as it can influence the date of the first flight (Bell et al., 2015). This repository makes use of gridded air temperature data from across the UK from the Met Office. 

This repository is primarily a means of testing how to work with this particular type of data (gridded temperature data in NetCDF files) using Iris, a Python module for dealing with these data. In particular, it focuses on the minimum temperatures across the UK in the years of interest. Data are worked with on an annual basis, because each season will be considered separately. 

This proof of concept analysis could be extrapolated to understand the temperatures throughout the year at locations in which aphids are found and to summarise the data preceding their first flights, for example.

## Data

### Monthly air temperature data

HadUK-Grid Gridded Climate Observations on a 1km grid over the UK, v1.2.0.ceda (1836-2022), available from CEDA under the Open Government License: https://dx.doi.org/10.5285/46f8c1377f8849eeb8570b8ac9b26d86

See steps 5-7 below for how to access and download the data.

## Using this repository

This code and instructions have been tested on Debian Bookworm with Python 3.11.

This repository uses [Iris](https://scitools-iris.readthedocs.io/en/latest/index.html)  which is not tested for use on Mac or Windows (see [installation instructions](https://scitools-iris.readthedocs.io/en/latest/installing.html#installing-iris)).

1. Clone this repository `git clone https://github.com/jen-thomas/haduk-met-data-at-site-locations.git`
2. In the cloned directory, create a virtual environment `python3 -m venv venv`
3. Activate the virtual environment. If using bash, do `. venv/bin/activate`
4. Install the packages from `requirements.txt`: `pip3 install -r requirements.txt`
5. Create a user account on the [CEDA website](https://services.ceda.ac.uk/cedasite/myceda). 
6. Configure your FTP account. Login, then go to [MyCEDA](https://services.ceda.ac.uk/cedasite/myceda) then click on Configure FTP Account. Click on the link to Create Password. For the [help pages about FTP](https://help.ceda.ac.uk/article/280-ftp) for further help with this step. 
7. Run the script `download_haduk_data.py` to download three NetCDF files containing the meteorology data. 
8. Run the script `get_haduk_data_at_sites.py` to explore and plot the data.

## Outputs

### `download_haduk_data.py`

A data directory will be created and the NetCDF files saved within this directory. 

### `get_haduk_data_at_sites.py`

Data exploration will be printed to the console. This shows the structure of the original NetCDF files and describes the parameters which are contained within the file, as well as additional file metadata. 

Following the data exploration for the year, a short summary of the year, minimum temperature and month of when this was, is also printed to the console.

The following plots will be created and saved as `PNG` files in the repository directory: 
* `YEAR_average_air_temperature.png` shows the average temperature of the month in which the minimum temperature of that year, was found. This plot covers the UK. 
* `YEAR_average_monthly_air_temperature.png` shows the average monthly temperatures at the location in which the minimum temperature of that year, was found. 

## Methods

### Data file exploration

NetCDF are binary files containing all parameters and metadata describing such parameters within the file. These are read into Python using the Iris module, which uses a data structure called a cube to represent the data.

Initial exploration of the data files allows us to understand the data structure. The shape and number of dimensions describe the structure of the gridded data. Printing a summary of the data once it has been read into an Iris cube shows this information, as well as all of the parameters that are included in the data file. 

The parameters of interest are explored further by looking at their names and units to ensure they are used correctly for the remainder of the analysis.

### Minimum temperatures

The location of the minimum average monthly temperature in the UK for each year, is found by first getting the index of the point within the dataset that has the minimum temperature. The latitude and longitude of this location are then extracted from the dataset. Annual temperature data at this location are extracted by subsetting the dataset, obtaining the monthly temperatures at each loction. These data are then plotted in the files, `YEAR_average_monthly_air_temperature.png`. 

The dataset is then subsetted to get the temperatures from the same month as the minimum temperature, but this time from across the UK. This is done by keeping the month constant and extracting the temperature at each of the gridded locations. Temperatures across the UK for the month in which the minimum temperature was found, are plotted on a map in the files, `YEAR_average_air_temperature.png`.

## Results

### Data file exploration

All data files are in the same format. Each one consists of an average monthly gridded temperature at the 1-km scale from across the UK. Each geographical location, represented by `latitude` (degrees) and `longitude` (degrees) and also projected into an x-y grid (metres), has a temperature value associated with it for each month of the year. Data are represented in a separate cube for each year. 

The month and year of the data points are represented by the parameters, `month_number` and `season_year`, respectively.

### Minimum temperatures

From the three years of interest, the coldest average monthly temperatures (-5.08 deg C) were found in March 2018 at the location with latitude: 57.07 and longitude: -3.66. Minimum temperatures in the other two years did not fall as low, reaching only -3.65 deg C in January 2019 and -3.56 deg C in February 2020, although they were found to be in very similar locations (2019: latitude: 57.07 and longitude: -3.49; latitude: 57.07 and longitude: -3.66). 

An example of the output plots for 2018 are shown below: 


## Summary and conclusions

NetCDF files are a useful way to store gridded data, such as the temperature data from across the UK, which is used in this repository. Iris, a Python module, can be used to read, subset and summarise the data. 

The HadUK 1-km gridded monthly temperatures across the UK could be used to better understand the dates of the first aphid flights in spring, by looking at the monthly averages in the months preceding these flights. Additionally, the dataset can be interrogated to find temperatures at specific locations that are of interest, or to find locations where the temperatures reach a particular limit of interest. 

This repository provides a proof of concept of how to download, read, explore and perform some analysis on these data. 

## References

Bell, J.R., Alderson, L., Izera, D., Kruger, T., Parker, S., Pickup, J., Shortall, C.R., Taylor, M.S., Verrier, P. and Harrington, R. (2015) ‘Long‐term phenological trends, species accumulation rates, aphid traits and climate: five decades of change in migrating aphids’, Journal of Animal Ecology. Edited by K. Wilson, 84(1), pp. 21–34. Available at: [https://doi.org/10.1111/1365-2656.12282](https://doi.org/10.1111/1365-2656.12282).

Met Office, Hollis, D., McCarthy, M., Kendon, M., Legg, T. (2023) 'HadUK-Grid Gridded Climate Observations on a 1km grid over the UK, v1.2.0.ceda (1836-2022)', NERC EDS Centre for Environmental Data Analysis, 30 August 2023. Available at: [https://dx.doi.org/10.5285/46f8c1377f8849eeb8570b8ac9b26d86](https://dx.doi.org/10.5285/46f8c1377f8849eeb8570b8ac9b26d86).

 
