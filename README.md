# zipBuild

Using ZipBuild.py in a few simple steps

1. Using the command prompt navigate to ZipBuild.py 's location.
2. Run "ZipBuild.py $Branch $Changelist" Without quotes and substituting the variables for actual values.
3. ZipBuild.py will Archive that Branch and Changelist in the archive directory with the same names.
4. ZipBuild.py will prompt you for a password to protect the archive.


Configuring ZipBuild.py 

1. Place Zipbuild.py in a sensible location on your local machine (some where you'll remember)
2. Open ZipBuild.py in your favourite editor (notepad, Vim, nano)
3. Change the config directories to match your machine and setup:

DataRoot = "\\\\buildserver\\data\\XB1\\"
ExeRoot  = "\\\\buildserver\\executables\\XB1\\"
ArchiveRoot = "\\\\buildserver\\archive\\XB1\\"
_7zipRoot = "C:\\Program Files\\7-Zip\\"

