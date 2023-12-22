#!/usr/bin/env python3

import ftplib
import os


def create_data_dir(dir_name):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)


def get_ceda_ftp_username():

    username = os.environ.get("CEDA_FTP_USERNAME")

    if username is None:
        username = input("Enter CEDA FTP username: ")

    return username


def get_ceda_ftp_password():
    password = os.environ.get("CEDA_FTP_PASSWORD")

    if password is None:
        password = input("Enter CEDA FTP password: ")

    return password


def login_to_ceda_ftp(username, password):

    ftp_object = ftplib.FTP("ftp.ceda.ac.uk", username, password)

    return ftp_object


def construct_data_file_name(year):

    file = "tas_hadukgrid_uk_1km_mon_%d01-%d12.nc" % (year, year)

    return file


def get_ceda_ftp_data(ftp_object, years):

    # Change to the directory on the FTP site
    ftp_object.cwd("/badc/ukmo-hadobs/data/insitu/MOHC/HadOBS/HadUK-Grid/v1.2.0.ceda/1km/tas/mon/v20230328")

    # Get the data for each year
    for year in years:
        file = construct_data_file_name(year)
        ftp_object.retrbinary("RETR %s" % file, open(file, "wb").write)

    # Close the FTP connection
    ftp_object.close()


def get_files_to_download():
    return


if __name__ == "__main__":

    ceda_data_dir = "ceda_data"
    create_data_dir(ceda_data_dir)
    os.chdir(ceda_data_dir)

    username = get_ceda_ftp_username()
    password = get_ceda_ftp_password()
    ftp_object = login_to_ceda_ftp(username, password)

    years = [2018, 2019, 2020]
    get_ceda_ftp_data(ftp_object, years)

