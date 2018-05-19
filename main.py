import lxml.etree as etree
from urllib.request import urlopen
import csv, os.path

# The URL to the MLB Gameday API site, can be formatted to specify what day the URL links to
url = ('http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1:02d}/day_{2:02d}/')

# Gets the desired date by user input. date_split splits up the date so the url can use the data (see open_url variable)
# filename replaces '/' with '_' to make the save the files. (used in for loop at bottom to name the saved files)
date = input("Enter date (Format as 'yyyy/mm/dd'):")
date_split = date.split("/")
filename = date.replace("/","_")

# formats the url
open_url = urlopen(url.format(int(date_split[0]),int(date_split[1]),int(date_split[2])) + 'grid.xml')

# parse_xml parses the formatted url to enable navigation while root will get the parsed xml's root elements
parse_xml = etree.parse(open_url)
root = parse_xml.getroot()

# iterates through the root elements and gets all of the attributes of the elements labeled 'game'
for game in root:
    to_csv = [game.attrib]
    if os.path.isfile(filename): # checks to see if the file exists in the current directory, if it does it will append the attributes to the file
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(to_csv)
    else:
        with open(filename, 'w', newline='') as csvfile: # if the file does not exist yet, it will create a new file in the working directory
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(to_csv)


print("CSV file successfully created in working directory")


