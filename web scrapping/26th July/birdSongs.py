import requests 
import csv, os

response = requests.get("https://xeno-canto.org/api/2/recordings?query=cnt:uganda")

if response.status_code == 200:
    data = response.json()
    recordings = data['recordings']

    directory = os.getcwd()
    filePath = os.path.join(directory, 'birdSongs.csv')
    
    with open(filePath, 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['Gen', 'Species', 'English Name', 'Recordist', 'Country', 'Location', 'Type', 'Length', 'Date Uploaded', 'Remarks'])

        for recording in recordings:
            details = [recording['gen'], recording['sp'], recording['en'], recording['rec'], recording['cnt'], recording['loc'], recording['type'], recording['length'], recording['uploaded'], recording['rmk']]
            try:
                writer.writerow(details)
            except UnicodeEncodeError:
                pass
    csvFile.close()
    print("Operation Complete!")
else:
    print("Failed to establish connection")