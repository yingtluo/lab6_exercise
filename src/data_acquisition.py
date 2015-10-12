import hashlib

"""
This module contains functions for downloading and verifying data from
the internet.
"""
import os
import urllib2
import json
import nibabel as nib

def download_data(url):
    """
    Download and save data from a url.

    Parameters
    ----------
    url : string
        The full url pointing to the data to be downloaded

    Returns
    -------
    data : str
         Return the data that results from reading the downloaded info, e.g.
         f.read() where f is the handle to the data buffer.

    Hint
    ----
    Consider the urllib2 or wget python modules
    """
    return urllib2.urlopen(url).read()

def save_data(data, output_filename):
    """
    Save data to file.

    If the file already exists, the function will not save the data and return
    1

    Parameters
    ----------
    data : str
        String containing the data you wish to write out to a file

    output_filename : str
        Path (full or relative) to the file you will save the data into.

    Returns
    -------
    out : int
        Return 0 if the data was saved successfully. Return 1 if the file
        already exists.

    Hint
    ----
    Check out the os module for determining whether a file exists already.
    """

    # Getting absolute path of file
    abs_filename = os.path.abspath(output_filename)
    if is_file(abs_filename):
        return 1
    else:
        f = open(abs_filename, 'w')
        f.write(data)
        return 0

def is_file(filename):
    """
    Helper function that returns whether the file already exists.

    Parameters
    ----------
    filename : str
        Absolute path to the file

    Returns
    -------  
    out : bool
        Return true if file already exists, false otherwise
    """
    
    return os.path.isfile(filename)


def verify_data(data, known_checksum):
    """
    This function verifies the data by comparing it to the known sha1 hash for
    the given data.

    Parameters
    ----------
    data : str
         The data to be verified

    known_checksum : str
         The sha1 hash with which to compare the result of hashing data

    Returns
    -------
    out : bool
        Return True if the hashes match, False otherwise

    Hint
    ----
    Check out the hashlib module
    """

    return hashlib.sha1(data).hexdigest() == known_checksum

def load_parsed_data(fname):
    """
    Load fmri data in .nii and parse into a numpy array

    Parameters
    ----------
    fname : str
        Path to an .nii file containing fmri data

    Returns
    -------
    img_ary : numpy.core.memmap.memmap
        Parsed data will be stored in a numpy container

    Hint
    ----
    Use nibabel
    """
    return NotImplemented

def main(data.json):
    """
    This function will be run if data_acquisition.py is called as a script. It
    is intended to be used with the %run method in ipython to initialize a
    session for data analysis

    This function should load a filename, url, and verified checksum from a
    json archive. It will then check if a file with the given name already
    exists in ../data. If not, download the data from the given url, save it
    to ../data/<filename>. Then verify the data. If the data verification
    passes, the data should be parsed into a useful numpy format.

    Parameters
    ----------
    data.json : str
        Path to a json file containing at least 'name', 'url', and 'sha1'
        fields

    Returns
    -------
    data : numpy.core.memmap.memmap
        The fMRI data in a numpy memmap representation, ready for analysis

    Hint
    ----
    Use the functions you've implemented above
    """
    json_file = open(data.json)
    json_data = json.load(infile)
    json_file.close()
    file_name = json_data['name']
    if not is_file(file_name):
        save_data(download_data(json_data['url']), file_name)
    data = open('../data/' + file_name).read()
    if verify_data(data, json_data['sha1']):
        return nib.load('../data/' + file_name).get_data()

### Add lines here that guarantees main() is run with example_data.json when
### called as a script
if __name__ == '__main__':
    main()
