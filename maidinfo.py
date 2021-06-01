#
#####
#WMCinfo.py ~ Minimalist System/Hardware information tool
#Requires : platform , distro , colorama , psutil
#####
#
#Created by KagiSame/MaidLatteProject (c)2k21

#Init Depedencies
import distro
import platform
import psutil
from colorama import Fore , Style
from colorama import init
init()



#Define size units 
def get_size(bytes, suffix="B"):
     factor = 1024
     for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor




#System Section (Distro name , version etc.)
print(Fore.CYAN + "############ \nSystem Info \n############")
print(Fore.GREEN + "Distribution:" , Fore.WHITE + distro.name())
print(Fore.GREEN + "Version:" , Fore.WHITE + distro.version())
print(Fore.GREEN + "Codename:" , Fore.WHITE + distro.codename())
print(Fore.GREEN + "Kernel :" , Fore.WHITE + platform.release())
print(Fore.GREEN + "Hostname:" , Fore.WHITE + platform.node())

#Hardware Section (Very basic, will be expanded)
print(Fore.YELLOW + "############ \nHardware Information \n############")
print(Fore.MAGENTA + "CPU Type:" ,  Fore.WHITE + platform.machine())
print(Fore.MAGENTA + "CPU Cores:" , Fore.WHITE + str(psutil.cpu_count()))
print(Fore.MAGENTA + "CPU Frequency:" , Fore.WHITE + str(psutil.cpu_freq().max) , "Mhz")
print(Fore.MAGENTA + "CPU Usage %" , Fore.WHITE + f"{psutil.cpu_percent()}%")
print(Fore.MAGENTA + "RAM Memory:" , Fore.WHITE + get_size(psutil.virtual_memory().used) ,"/" , get_size(psutil.virtual_memory().total))

#Disk Section (Warning WORK IN PROGRESS)
print(Fore.CYAN + "############ \nDisk Information \n############")

#Init some partitions stuff
partitions = psutil.disk_partitions()
for partition in partitions:
	print(Fore.GREEN + "Device:" , Fore.WHITE + f"{partition.device}")
	print(Fore.GREEN + "Mountpoint:" , Fore.WHITE + f"{partition.mountpoint}")
	print(Fore.GREEN + "Filesystem:" , Fore.WHITE + f"{partition.fstype}")



#Disk Size information (work in progress please redo) 
#
#	try:
#		partition_usage = psutil.disk_usage(partition.mountpoint)
#	except PermissionError:
#		continue	
#print(Fore.GREEN + "Disk Usage:" ,  Fore.WHITE + f"{get_size(partition_usage.total)}")



#Simple Version information (Usually Consiting of State + Codename + Version)

print(Fore.RED + "\n~~maidinfo.py Alpha build 01062021 {Megistus}~~\n (c) 2k21 KagiSame/MaidLatteProject")

