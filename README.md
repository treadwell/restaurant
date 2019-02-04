# Project: Restaurant Web Application

This application allows users to capture various information
about restaurants and their menu items.

## Design

The project uses python in a flask framework to access two
sqlite tables:

* Restaurants
* MenuItems

### Pages

### Routes

### Tables

### Python scripts

The python script consists of a single module containing a function that establishes a connection to the database, executes a query string and returns a result. The module uses a simple for-loop to execute each query and format the results to the console.

## Getting Started

### Prerequisites

1. [Python 3](https://www.python.org/download/releases/python-372/) - The code uses ver 3.7.2
2. [Vagrant](https://www.vagrantup.com/) - A tool for building and managing virtual machine environments in a single workflow
3. [VirtualBox](https://www.virtualbox.org/) - An open source virtualization product for x86 hardware.
4. [Git](https://git-scm.com/) - An open source version control system

* Virtual machine setup downloaded and installed per class instructions
* News database setup per class instructions
* newslogs.py

### Installing

 1. Download the latest version of Python from the link in Prerequisites.
 2. Download and install Vagrant and VirtualBox.
 3. Download this Udacity [folder](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) with preconfigured vagrant settings and unzip it in a desired location.
 4. Clone this repository.
 5. Download [this](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) database.
 6. Navigate to the Udacity folder created in step 3. Inside that cd into the vagrant folder.
 7. Open a terminal and launch the virtual machine with`vagrant up`
 8. Once Vagrant installs necessary files use `vagrant ssh` to access the virtual machine.
 9. The command line will now start with vagrant. Here cd into the /vagrant folder.
 10. Unpack the  database folder contents downloaded in step 5 here.
 11. Load the database with `psql -d news -f newsdata.sql`

## Instructions

* Use command `python newslogs.py` to execute queries on the
  database

## Authors

* Ken Brooks, Treadwell Media Group
