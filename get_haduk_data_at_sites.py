#!/usr/bin/env python3

import iris
import os


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
    print(f"Latitude var name: {cube_latitude.standard_name}; Units: {cube_latitude.units} ", )

    cube_longitude = cube.coord("longitude")
    print(f"Longitude var name: {cube_longitude.standard_name}; Units: {cube_longitude.units} ", )

    cube_time = cube.coord("time")
    print(f"Time var name: {cube_time.standard_name}; Units: {cube_time.units} ", )


if __name__ == "__main__":

    met_data_dir = "ceda_data"

    nc_file_list = list_files(met_data_dir)
    cubes = load_data_into_iris(met_data_dir, nc_file_list)

    for cube in cubes[0:3]:
        explore_netcdf_file(cube)
        check_coordinate_names_units(cube)