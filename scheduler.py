# scheduler.py

import time
from main import run_pipeline

POLL_INTERVAL_MINUTES = 60

def start_scheduler():
    print(f"Scheduler started. Polling emails every {POLL_INTERVAL_MINUTES} minutes.")

    while True:
        try:
            run_pipeline()
        except Exception as e:
            print(f"Error during pipeline execution: {e}")

        time.sleep(POLL_INTERVAL_MINUTES * 60)
