import schedule
import time
import subprocess

def run_pipeline():
    print("🚀 Running Reddit data pipeline...")
    subprocess.run(["python", "reddit_data_pipeline.py"])
    print("✅ Data pipeline execution completed!")

# Schedule: Runs every hour
schedule.every(1).hour.do(run_pipeline)

print("⏳ Scheduler started. Waiting for next execution...")

while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for a minute before checking again
