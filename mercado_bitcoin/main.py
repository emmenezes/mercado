import datetime
from time import sleep
from schedule import repeat, every, run_pending


from ingestors import DaysummaryIngestor
from writer import S3Writer


if __name__ == '__main__':
    day_summary_ingestor = DaysummaryIngestor(
        writer=S3Writer, 
        coins=["BTC", "ETH", "LTC"], 
        default_start_date=datetime.date(2021,11,10)
    )

    @repeat(every(1).seconds)
    def job():
        day_summary_ingestor.ingest()

    while(True):
        run_pending()
        sleep(0.5)
