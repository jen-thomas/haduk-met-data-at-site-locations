#!/usr/bin/env python3

import iris
import os
import matplotlib.pyplot as plt
import iris.plot as iplt
import iris.quickplot as qplt
from iris.time import PartialDateTime


def list_files(directory):

    nc_files_list = []

    for item in os.listdir(directory):
        if item.endswith(".nc"):
            nc_files_list.append(item)

    return nc_files_list


def load_data_into_iris(data_directory, file_list):

    filepaths = []
    for file in file_list:
        filepath = os.path.join(data_directory, file)
        filepaths.append(filepath)

    cubes = iris.load(filepaths)

    return cubes


def explore_netcdf_file(cube):
    print("Cube name:", cube.standard_name)
    print("Cube units:", cube.units)
    print("Cube shape:", cube.shape)
    print("Cube dimensions:", cube.ndim)
    print("Cube details:", cube)


def check_coordinate_names_units(cube):
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


def subset_by_date_bounds(cube, min_month, min_day, max_month, max_day):
    daterange = iris.Constraint(
        time=lambda cell: PartialDateTime(month=min_month, day=min_day) <= cell.point < PartialDateTime(month=max_month, day=max_day))

    data_within_daterange = cube.extract(daterange)

    return data_within_daterange


def get_data_at_index(cube):
    data_at_index = cube[::, 600, 600]

    return data_at_index


def plot_1d_data(cube):
    qplt.plot(cube)
    plt.grid(True)

    plt.axis("tight")

    iplt.show()


def latitude_within_degree(cell):
    return 52.4 < cell < 52.5


def subset_by_coordinates(cube, min_lat, max_lat):
    location_lat = iris.Constraint(name="air_temperature", projection_y_coordinate=latitude_within_degree)

    cube.extract(location_lat)
    print(cube)

    for sub_cube in cube.slices(['projection_y_coordinate', 'projection_x_coordinate']):
        print(sub_cube)

        data_at_location_lat = sub_cube.extract(location_lat)
        print("************************")
        print(data_at_location_lat)

    return data_at_location_lat


def plot_cube_map(cube):
    plt.figure(figsize=(12, 5))
    plt.subplot(121)
    qplt.contourf(cube, 15)
    plt.gca().coastlines()
    iplt.show()


def main():

    met_data_dir = "ceda_data"

    nc_file_list = list_files(met_data_dir)
    cubes = load_data_into_iris(met_data_dir, nc_file_list)

    for cube in cubes[0:3]:
        explore_netcdf_file(cube)
        check_coordinate_names_units(cube)

        # Plot average April monthly temperatures across the UK
        april_monthly_temps = subset_by_date_bounds(cube, 4, 10, 4, 25)
        plot_cube_map(april_monthly_temps)

        # Plot annual temperature data at specific location
        data_at_index = get_data_at_index(cube)
        plot_1d_data(data_at_index)

        #subset_by_coordinates(cube , 100000, 101000)


if __name__ == "__main__":
    main()