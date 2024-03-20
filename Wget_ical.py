import wget


def FetchIcalFile(url):
    """
    Fetch .ical file from url
    """
    wget.download(url)


if __name__ == "__main__":
    FetchIcalFile('http://192.168.88.206:7878/feed/v3/calendar/Radarr.ics?unmonitored=true&asAllDay=true&apikey=fbb06d91e5cb4905ab37539a68c900c6')

# http://192.168.88.206:7878/feed/v3/calendar/Radarr.ics?unmonitored=true&asAllDay=true&apikey=fbb06d91e5cb4905ab37539a68c900c6
# http://192.168.88.206:30000/feed/v3/calendar/sonarr.ics?pastDays=7&futureDays=31&unmonitored=true&premieresOnly=false&asAllDay=true&apikey=5089fe943413408e895d4584330d7cf9