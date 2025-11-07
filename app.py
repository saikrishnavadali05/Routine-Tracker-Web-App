from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

FILE_NAME = "daily_schedule_tracking.csv"

# ------------------ Schedule Data ------------------
SCHEDULE = [
    ("5:00 AM", "Wake up -> Music / Devotional Songs Begin"),
    ("5:30 AM - 6:00 AM", "Omkaram & Suprabhatam"),
    ("6:10 AM - 6:30 AM", "Fitness Session"),
    ("7:10 AM - 7:30 AM", "Breakfast Counter Open"),
    ("9:00 AM", "College Begins (with Prayer)"),
    ("3:45 PM", "College Ends"),
    ("4:00 PM", "Return to Hostel"),
    ("4:00 PM - 4:30 PM", "Relaxation & Evening Snacks"),
    ("5:00 PM", "Start to Kulwant Hall"),
    ("5:15 PM", "Bhajans at Sai Kulwant Hall"),
    ("7:10 PM - 7:30 PM", "Dinner Counter Open"),
    ("8:00 PM - 9:45 PM", "Study Hours"),
    ("10:20 PM - 10:30 PM", "Night Prayer & Swami's Discourse Clip"),
]

# ------------------ Helper Functions ------------------
def initialize_csv():
    """Create CSV file if not present."""
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=[
            "Date", "Day", "Scheduled Time", "Activity", "Login Time", "Logout Time", "Remarks"
        ])
        df.to_csv(FILE_NAME, index=False)

def read_data():
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)
    else:
        initialize_csv()
        return pd.read_csv(FILE_NAME)

def write_data(df):
    df.to_csv(FILE_NAME, index=False)

# ------------------ Routes ------------------
@app.route("/")
def index():
    df = read_data()
    data = df.to_dict(orient="records")
    return render_template("index.html", schedule=SCHEDULE, data=data)

@app.route("/record", methods=["POST"])
def record_action():
    activity = request.form["activity"]
    sched_time = request.form["sched_time"]
    action_type = request.form["action"]

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    day = now.strftime("%A")
    current_time = now.strftime("%H:%M")

    df = read_data()
    mask = (df["Date"] == date) & (df["Activity"] == activity)

    if action_type == "Login":
        if mask.any():
            flash(f"Login already recorded for '{activity}'.", "info")
        else:
            new_row = pd.DataFrame([[date, day, sched_time, activity, current_time, "", ""]],
                                   columns=df.columns)
            df = pd.concat([df, new_row], ignore_index=True)
            write_data(df)
            flash(f"✅ Login recorded for '{activity}' at {current_time}", "success")

    elif action_type == "Logout":
        if mask.any():
            idx = df.index[mask][0]
            if pd.isna(df.at[idx, "Logout Time"]) or df.at[idx, "Logout Time"] == "":
                df.at[idx, "Logout Time"] = current_time
                write_data(df)
                flash(f"✅ Logout recorded for '{activity}' at {current_time}", "success")
            else:
                flash(f"Logout already recorded for '{activity}'.", "info")
        else:
            flash(f"No login found for '{activity}' today.", "warning")

    return redirect(url_for("index"))

@app.route("/remark", methods=["POST"])
def add_remark():
    date = request.form["date"]
    activity = request.form["activity"]
    remark = request.form["remark"].strip()

    if not remark:
        flash("Remark cannot be empty.", "warning")
        return redirect(url_for("index"))

    df = read_data()
    mask = (df["Date"] == date) & (df["Activity"] == activity)

    if mask.any():
        idx = df.index[mask][0]
        df.at[idx, "Remarks"] = remark
        write_data(df)
        flash(f"📝 Remark added for '{activity}'.", "success")
    else:
        flash("No record found for this activity.", "warning")

    return redirect(url_for("index"))

# ------------------ Run ------------------
if __name__ == "__main__":
    initialize_csv()
    app.run(debug=True)
