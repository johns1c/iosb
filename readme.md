# Reads and displays IOS Backups 

The idea is that it should allow you to explore iOS backups produced by iTunes
recovering files of interest

# This version ( September 2021 )

* lists backups 
* displays status and device information
* reads version 3.3 iTunes backup manifest
* list domains and files
* will clip the full path to the backup file to the paste bin

Does Not
* properly exit
* deal with old style manifests and old style file locations
* do anything other than clip del with encrypted files 
* allow browsing to backups in other loacations such as backup
* handle default locations on other platforms
* handle encrypted backups even where password is known
* have a menu that 

# Requirements

This code is written in Python 3.  It requires packages for sqlite3 and handling binary and xml plists and will later require a crypto package



