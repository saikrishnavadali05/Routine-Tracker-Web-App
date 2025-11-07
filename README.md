
# 📘 Daily Schedule Tracker (Flask Web App)

A simple and elegant **Flask-based web application** that helps you track your **daily activities, login/logout times, and remarks**, all stored neatly in a CSV file.

Originally built using **Tkinter**, this version converts the same functionality into a modern **Flask + Bootstrap** web app — accessible from any browser!

---

## 🌟 Features

✅ **Daily Schedule Display** — Predefined daily schedule with time slots and activities  
✅ **Login / Logout Tracking** — Record time stamps for each activity  
✅ **Remarks Section** — Add personal remarks or reflections for each task  
✅ **Persistent Data Storage** — Automatically stores all entries in `daily_schedule_tracking.csv`  
✅ **Bootstrap UI** — Clean, mobile-friendly web interface  
✅ **CSV-based History Table** — View all recorded logs, times, and remarks  

---

## 🏗️ Project Structure

```

daily-schedule-tracker/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Dependencies
├── templates/
│   └── index.html          # Web interface template
└── daily_schedule_tracking.csv  # Auto-created CSV file (data saved here)

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<your-username>/daily-schedule-tracker.git
cd daily-schedule-tracker
````

### 2️⃣ Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate      # For macOS/Linux
venv\Scripts\activate         # For Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask app

```bash
python app.py
```

### 5️⃣ Open in your browser

```
http://127.0.0.1:5000/
```

---

## 🧾 Usage

1. View your **daily schedule** on the main page.
2. Click **Login** when you start an activity.
3. Click **Logout** once you finish it.
4. Add **remarks** in the "Add Remark" box next to each logged entry.
5. All data is automatically saved in `daily_schedule_tracking.csv`.

---

## 📂 Data Format (CSV)

The app stores logs in `daily_schedule_tracking.csv` with the following columns:

| Date       | Day    | Scheduled Time    | Activity              | Login Time | Logout Time | Remarks       |
| ---------- | ------ | ----------------- | --------------------- | ---------- | ----------- | ------------- |
| 2025-11-07 | Friday | 5:30 AM - 6:00 AM | Omkaram & Suprabhatam | 05:35      | 06:00       | Felt peaceful |

---

## 🖼️ Screenshot (Sample UI)

```
+-----------------------------------------------------------+
| 📘 Daily Schedule Tracker (Flask Version)                 |
|-----------------------------------------------------------|
| Scheduled Time | Activity | [Login] [Logout]              |
|-----------------------------------------------------------|
| 5:30 AM - 6:00 AM | Omkaram & Suprabhatam | [Login] [Logout] |
| ...                                                     |
+-----------------------------------------------------------+
| Recorded Data (with Remarks)                             |
+-----------------------------------------------------------+
```

---

## 💡 Future Enhancements

* 🔍 Filter by date or day
* 📱 Responsive mobile view improvements
* 🧮 Auto statistics (e.g., punctuality score)
* ☁️ Cloud-based database (SQLite/PostgreSQL)

---

## 🧑‍💻 Author

**Sai Krishna Vadali**
📧 *[[your-email@example.com](mailto:your-email@example.com)]*
🌐 *Built with ❤️ using Flask and Pandas*

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use, modify, and share.

---

> *"Discipline is the bridge between goals and accomplishment." – Jim Rohn*

Would you like me to include a **screenshot preview section** (with placeholders for images you can add later)? It helps make your README look even more professional on GitHub.
```
