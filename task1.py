import argparse
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Archive:
    _instance = None

    def __new__(cls, text="", number=0):
        logger.info("Creating new instance of Archive")
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        return cls._instance

    def __init__(self, text="", number=0):
        logger.info(f"Initializing Archive instance with text='{text}' and number={number}")
        self.text = text
        self.number = number
        self.timestamp = datetime.now()

        self.archive_text.append(self.text)
        self.archive_number.append(self.number)

    def __str__(self):
        logger.info("Converting Archive instance to string")
        current_data = f"Text is {self.text} and number is {self.number}. "
        archive_text = f"Also {self.archive_text}" if self.archive_text else ""
        archive_number = f" and {self.archive_number}" if self.archive_number else ""
        return current_data + archive_text + archive_number

    def __repr__(self):
        logger.info("Representing Archive instance")
        return f"Archive(text={self.text}, number={self.number})"

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--text', type=str, default="", help='Text for the archive')
    parser.add_argument('--number', type=int, default=0, help='Number for the archive')

    args = parser.parse_args()
    archive_instance = Archive(args.text, args.number)
    logger.info(f"Created archive instance: {archive_instance}")

if __name__ == "__main__":
    main()
