from fastapi import FastAPI
from routes.user import router
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime, timedelta
from config.db import product_collection

app = FastAPI()

# Scheduler setup
scheduler = BackgroundScheduler()
scheduler.start()

last_count_time = datetime.now()

def count_records():
    global last_count_time
    current_time = datetime.now()
    new_records_count = product_collection.count_documents({
        "created_at": {"$gte": last_count_time, "$lt": current_time}
    })
    print(f"New records inserted from {last_count_time} to {current_time}: {new_records_count}")
    last_count_time = current_time

# Schedule the job every 5 minutes
scheduler.add_job(
    count_records,
    trigger=IntervalTrigger(minutes=5),
    id="count_records_job",
    name="Count records every 5 minutes",
    replace_existing=True
)

@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()

app.include_router(router, tags=["Product"], prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
