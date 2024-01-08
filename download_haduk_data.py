#!/usr/bin/env python3

import ftplib
import os


def create_data_dir(dir_name):
    """
    Create the data directory where the CEDA files will be downloaded.

    :param dir_name : str
        Name of the data directory
    :return : None

    """

    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)


def get_ceda_ftp_username():
    """
    Get the username for the CEDA FTP site.

    :return : str
        Username for the FTP site
    """

    username = os.environ.get("CEDA_FTP_USERNAME")

    if username is None:
        username = input("Enter CEDA FTP username: ")

    return username


def get_ceda_ftp_password():
    """
    Get the password for the CEDA FTP site.

    :return : str
        password for the FTP site
    """

    password = os.environ.get("CEDA_FTP_PASSWORD")

    if password is None:
        password = input("Enter CEDA FTP password: ")

    return password


def login_to_ceda_ftp(username, password):
    """
    Log in to the CEDA FTP site.

    :param username : str
    :param password : str

    :return :
        FTP object
    """

    try:
        ftp_object = ftplib.FTP("ftp.ceda.ac.uk", username, password)
    except ftplib.error_perm:
        print("Login to FTP site failed.")
        raise SystemExit(1)

    return ftp_object


def construct_data_file_name(year):
    """
    Create the file name to download from the FTP site. For these particular data, the file name includes the year so
    this needs to be changed for each file.

    :param year: int
        Year of data collection

    :return: str
        File name
    """

    file = "tas_hadukgrid_uk_1km_mon_%d01-%d12.nc" % (year, year)

    return file


def get_ceda_ftp_data(ftp_object, years):
    """
    Download data files from CEDA FTP. Save files in the data directory.

    :param ftp_object : ftpLib.FTP
    :param years : list(int)
        List of the years of interest

    :return : None
    """
    # Change to the directory on the FTP site
    ftp_object.cwd("/badc/ukmo-hadobs/data/insitu/MOHC/HadOBS/HadUK-Grid/v1.2.0.ceda/1km/tas/mon/v20230328")

    # Get the data for each year
    for year in years:
        file = construct_data_file_name(year)
        try:
            print(f"Trying to get file: {file}")
            ftp_object.retrbinary("RETR %s" % file, open(file, "wb").write)
        except ftplib.all_errors as errors:
            print(f"Not able to download file: {file}. Error: {errors}")

    # Close the FTP connection
    ftp_object.close()


if __name__ == "__main__":

    ceda_data_dir = "ceda_data"
    create_data_dir(ceda_data_dir)
    os.chdir(ceda_data_dir)

    username = get_ceda_ftp_username()
    password = get_ceda_ftp_password()
    ftp_object = login_to_ceda_ftp(username, password)

    years = [2018, 2019, 2020]
    get_ceda_ftp_data(ftp_object, years)
    