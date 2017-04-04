import sys
import subprocess
import getpass

# Set our roots 
#DataRoot = "\\\\buildserver\\data\\XB1\\"
#ExeRoot  = "\\\\buildserver\\executables\\XB1\\"
#ArchiveRoot = "\\\\buildserver\\archive\\XB1\\"
#_7zipRoot = "C:\\Program Files\\7-Zip\\"

#setting roots for local testing
DataRoot = "D:\\python\\CA-TEST\\buildserver\\data\\XB1\\"
ExeRoot  = "D:\\python\\CA-TEST\\buildserver\\executables\\XB1\\"
ArchiveRoot = "D:\\python\\CA-TEST\\buildserver\\archive\\XB1\\"
_7zipRoot = "C:\\Program Files\\7-Zip\\"

#Set the help message
zip_help = "Usage: \n ZipBuild.py $Branch $Changelist - archive Branch and Change \n ZipBuild.py help 		 - display this help and exit"


#Check our input isn't empty
                                        #fix this later
#if str(sys.argv[1]) or str(sys.argv[2]):
#       Branch = str(sys.argv[1])
#       ChangeList = str(sys.argv[2])
#else:
#       print("Error input")
#       sys.exit()

if str(sys.argv[1]) == "help":
	print(zip_help)
	sys.exit()


#put the captured arguments into variables
Branch = str(sys.argv[1])
ChangeList = str(sys.argv[2])

#password = getpass.getpass()
#print(password)

#print out what we'll do
print("I will archive branch " + Branch + " and changelist " + ChangeList)

print("Archiving: ")
data = (ExeRoot  + Branch + "\\" + ChangeList + "\\*")
print(data)

exe = (DataRoot + Branch + "\\" + ChangeList + "\\*")
print(exe)

print("to Archive location:")
archive = (ArchiveRoot + Branch + "\\" + ChangeList + "\\archive.7z")
print(archive)



#archive it
subprocess.call([_7zipRoot + '7z', 'a', '-mhe=on', '-v3g' , archive , data , exe, '-p' ])




