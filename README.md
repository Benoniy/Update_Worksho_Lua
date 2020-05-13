# What is this?  
This is a python script that I created to update the workshop.lua file used by Garrysmod and other source games  
based on mod collections that can be made by any user on steam. It also removes unused .gma files from the server  
to ensure that there are no server/client conflicts and to save space. This script is by far the most useful that  
I have made for Gmod servers.

#### What does it work on?  
This was created for a linux based server, I dont think that it would work out of the box with a windows installation  
however it could be modified.  
  
#### Prerequisites:  
* Python 3  
* Urllib 3  

#### How to install:  

1) Install python 3
2) If using pip run the command "install -r requirements.txt"  
   If not using pip then you must install all of the prerequisite packages listed above.  
3) Place update_workshop.py in your servers install directory (it should also contain bin, garrysmod, platform,  
   sourceeengine, srcds_linux, srcds_run, steam_appid.txt, steamapps, steamcache, ThridPartyLegalNotices.txt)  

#### How to run:  
Its as easy as running update_workshop.py with the collection number as an argument "./update_workshop.py collection_no".  
this can be run from inside a server startup script and I personally have placed this command first in my start.sh.  

### Known Issues:  

There is a possibility that the script will throw an error when it is run, this is usually due to the differences  
in linux and windows text formatting (I develop on windows). You can solve this in the following ways:  
* Use dos2unix (apt-get install dos2unix, dos2unix winfile.txt unixfile.txt)