import wget  # type: ignore


def fetch_ical_file(url):
    """
    Fetch .ical file from url
    """
    wget.download(url)


if __name__ == "__main__":
    fetch_ical_file('url')
