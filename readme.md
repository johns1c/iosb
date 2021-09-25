# Reads and displays IOS Backups 

The idea is that it should allow you to explore iOS backups produced by iTunes
recovering files of interest

# This version ( September 2021 )

* lists backups 
* displays status and device information
* reads version 3.3 and 2.4 iTunes backup manifest
* list domains and files
* allows filtering (query) on domain and relativePath
* will clip the full path to the backup file to the paste bin

Does Not
* properly exit
* deal with old style manifests with mdbx files
* do anything other than clip del with encrypted files 
* allow browsing to backups in other loacations such as backup
* handle default locations on other platforms
* handle encrypted backups even where password is known
* have a final menu
 OK
# Usage

## Menu

** File Open ** displays a list of backup directories.  Selecting one will display backup information and clicking **OK** will populate the domain list on the main panel.

Clicking on a domain will display the associated file and directory entries

Right clicking on a file entry gives a list of file options at present only allows allows you to clip the backup file location to the clipboard.

** Query Enter ** and ** Query Execute **  Allow you to filter domains and file names using SQL wild carded patterns ( % and _ ).  This should work for SQLITE and file based manifests.

You can

* Show all domains and entries
    
* Show domains with selected names (by leaving the file critera empty) and then all entries
    
* Show selected domains having matching files (by completing the domain and file critera ) and then the matching entries

* Obtain the last criteria.


for example domain % and file %.plist will first show all domains which have backed up plist files and then display the plists for the selected domain.

# Requirements

This code is written in Python 3.  It requires packages for sqlite3 and handling binary and xml plists and will later require a crypto package



