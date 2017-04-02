import sys
import subprocess
import getpass

# Set our roots 
#DataRoot = "\\\\buildserver\\data\\XB1\\"
#ExeRoot  = "\\\\buildserver\\executables\\XB1\\"
#ArchiveRoot = "\\\\buildserver\\archive\\XB1\\"

#setting roots for local testing
DataRoot = "D:\\python\\CA-TEST\\buildserver\\data\\XB1\\"
ExeRoot  = "D:\\python\\CA-TEST\\buildserver\\executables\\XB1\\"
ArchiveRoot = "D:\\python\\CA-TEST\\buildserver\\archive\\XB1\\"
_7zipRoot = "C:\\Program Files\\7-Zip\\"

#Check our input isn't empty
                                        #fix this later
#if str(sys.argv[1]) or str(sys.argv[2]):
#       Branch = str(sys.argv[1])
#       ChangeList = str(sys.argv[2])
#else:
#       print("Error input")
#       sys.exit()

#put the captured arguments into variables
Branch = str(sys.argv[1])
ChangeList = str(sys.argv[2])

#password = getpass.getpass()
#print(password)

#print out what we'll do
print("I will archive branch " + Branch + " and changelist " + ChangeList)

print("Archiving: ")
#print(ExeRoot  + Branch + "\\" + ChangeList)
data = (ExeRoot  + Branch + "\\" + ChangeList + "\\*")
print(data)

#print(DataRoot + Branch + "\\" + ChangeList)
exe = (DataRoot + Branch + "\\" + ChangeList + "\\*")
print(exe)


#print("to Archive location:")
archive = (ArchiveRoot + Branch + "\\" + ChangeList + "\\archive.7z")
print(archive)


#archive it
print(_7zipRoot + '7z', 'a', '-mhe=on' , archive , data , exe, '-p' )
subprocess.call([_7zipRoot + '7z', 'a', '-mhe=on' , archive , data , exe, '-p' ])




