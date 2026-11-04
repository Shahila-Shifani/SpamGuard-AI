from pathlib import Path
from urllib.request import urlretrieve
import zipfile

DATA_DIR = Path("data")
ZIP_PATH = DATA_DIR / "sms_spam_collection.zip"
DATA_URL = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"

def download_dataset():
    DATA_DIR.mkdir(exist_ok=True)
    print("Downloading the UCI SMS Spam Collection...")
    urlretrieve(DATA_URL, ZIP_PATH)
    with zipfile.ZipFile(ZIP_PATH, "r") as archive:
        archive.extractall(DATA_DIR)
    ZIP_PATH.unlink(missing_ok=True)
    print("Dataset extracted to data/SMSSpamCollection")

if __name__ == "__main__":
    download_dataset()
