#!/usr/bin/env python3

import iris
import os
import matplotlib.pyplot as plt
import iris.quickplot as qplt
from iris.time import PartialDateTime
import iris.analysis
import numpy as np


def list_files(directory):
    """
    List all NetCDF files in a directory.

    :param directory: str
        Name of the directory
    :return: list

    """

    nc_files_list = []

    for item in os.listdir(directory):
        if item.endswith(".nc"):
            nc_files_list.append(item)

    return nc_files_list


def load_data_into_iris(data_directory, file_list):
    """
    Load NetCDF files into Iris cubes.

    :param data_directory: str
        Name of the directory containing the files
    :param file_list: list
        List of the files to load
    :return: cubes
        Iris cubes containing the data

    """

    filepaths = []
    for file in file_list:
        filepath = os.path.join(data_directory, file)
        filepaths.append(filepath)

    cubes = iris.load(filepaths)

    return cubes


def explore_netcdf_file(cube):
    """
    Explore the data.

    :param cube: cube
        Cube containing the data.
    :return: None

    """

    print("Cube name:", cube.standard_name)
    print("Cube units:", cube.units)
    print("Cube shape:", cube.shape)
    print("Cube dimensions:", cube.ndim)
    print("Cube details:", cube)


def check_coordinate_names_units(cube):
    """
    Check details of coordinates in cube.

    :param cube: cube
        Cube to describe.
    :return: None

    """

    cube_latitude = cube.coord("latitude")
    print(f"Latitude var name: {cube_latitude.standard_name}; Units: {cube_latitude.units} ")

    cube_longitude = cube.coord("longitude")
    print(f"Longitude var name: {cube_longitude.standard_name}; Units: {cube_longitude.units} ")

    cube_projection_y_coordinate = cube.coord("projection_y_coordinate")
    print(f"Y coord projection var name: {cube_projection_y_coordinate.standard_name}; Units: {cube_projection_y_coordinate.units} ")

    cube_projection_x_coordinate = cube.coord("projection_x_coordinate")
    print(f"X coord projection var name: {cube_projection_x_coordinate.standard_name}; Units: {cube_projection_x_coordinate.units} ")

    cube_time = cube.coord("time")
    print(f"Time var name: {cube_time.standard_name}; Units: {cube_time.units} ")


def subset_by_date_bounds(cube, min_month, max_month):
    """
    Subset a cube by date bounds.

    :param cube: cube
    :param min_month: int
        Month of lower date bound
    :param min_day: int
        Day of month of lower date bound
    :param max_month: int
        Month of upper date bound
    :param max_day: int
        Day of upper date bound
    :return: cube
        Data within the bounding dates

    """

    daterange = iris.Constraint(
        time=lambda cell: PartialDateTime(month=min_month) <= cell.point <= PartialDateTime(month=max_month))

    data_within_daterange = cube.extract(daterange)

    return data_within_daterange


def get_monthly_data_at_index(cube, proj_y_coord, proj_x_coord):
    """
    Get the data from the cube according to the indices specified for each dimension.

    :param cube: cube
    :return: cube
        Data within the index specified

    """

    data_at_index = cube[::, proj_y_coord, proj_x_coord]

    return data_at_index


def plot_1d_data(cube, year, lat, lon):
    """
    Plot 1D cube data.

    :param cube: cube
    :return: None

    """

    qplt.plot(cube)
    plt.grid(True, which='both', color='grey', alpha=0.5, linestyle='-', linewidth=0.5)

    plt.axis("tight")
    plt.xticks(which='both', rotation=45, minor=True)
    plt.xlabel("Month")
    plt.title(f"Average monthly air temperatures at location with lowest \n temperature across the UK, {year}.")
    plt.figtext(x=0.65, y=0.8, s=f"Lat: {round(lat, 2)} Lon: {round(lon, 2)}")

    fname = f"{year}_average_monthly_air_temperature.png"
    plt.savefig(fname, format='png')
    plt.close()


def get_season_year(cube):
    """
    Get the year.

    :param cube: cube
    :return: int
        Return year as an integer

    """

    season_year_att = cube.coord('season_year')
    year = int(min(season_year_att.points))

    print("Data from:", year)

    return year


def plot_cube_map(cube, month, year):
    """
    Plot map of data with coastlines and colour defining the dataset parameter.

    :param cube: cube
        Data to plot
    :return: None

    """

    plt.figure(figsize=(12, 5))
    plt.subplot(121)
    qplt.contourf(cube, 15)
    plt.gca().coastlines()
    plt.title(f"Average air temperature across the UK during month of minimum temperature. \n"
              f" {year} (month = {month})")

    fname = f"{year}_average_air_temperature.png"
    plt.savefig(fname, format='png')

    plt.close()


def get_index_min_annual_temperature(cube):

    min_temperature = cube.data.min()
    min_temperature_index = cube.data.argmin()
    index = np.unravel_index(min_temperature_index, cube.shape)

    print(f"Min temperature: {round(min_temperature, 2)}")

    return index


def get_location_of_point(cube_single_point):

    lat = cube_single_point.coord("latitude").points[0]
    lon = cube_single_point.coord("longitude").points[0]

    print(f"Latitude: {round(lat, 2)} and Longitude: {round(lon, 2)}")

    return lat, lon


def get_month_of_indexed_point(index):

    month = index[0] + 1 # add one to the index to get the number associated with the month of the year
    print(f"Month: {month}")

    return month


def main():

    met_data_dir = "ceda_data"

    nc_file_list = list_files(met_data_dir)
    cubes = load_data_into_iris(met_data_dir, nc_file_list)

    for cube in cubes[0:3]:
        explore_netcdf_file(cube)
        check_coordinate_names_units(cube)

        print("****** Minimum temperature data summary ******")

        # Get the year of the data.
        year = get_season_year(cube)

        # Find location of minimum temperature for each year and plot monthly temperatures at this location.
        index_min_temperature = get_index_min_annual_temperature(cube)
        monthly_data_at_index = get_monthly_data_at_index(cube, index_min_temperature[1], index_min_temperature[2])
        lat, lon = get_location_of_point(monthly_data_at_index)

        plot_1d_data(monthly_data_at_index, year, lat, lon)

        # Get the month of the minimum temperature and plot the temperature across the UK for this month.
        month = get_month_of_indexed_point(index_min_temperature)
        month_lowest_temperature = subset_by_date_bounds(cube, month, month)

        plot_cube_map(month_lowest_temperature, month, year)

        print("****** End temperature data summary ******")


if __name__ == "__main__":
    main()
