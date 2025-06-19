# SAFE-ROOM | מערכת ניהול ממ״דים

מערכת מלאה לניהול ממ"דים, משתמשים, מיקומים וזיהוי בזמן אמת.

---

## 📦 מבנה הפרויקט

safe-room/
├── backend/
│ └── app/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── create_tables.py
│ ├── crud/
│ ├── routers/
│ ├── schemas/
│ └── requirements.txt
├── frontend/
│ ├── index.html
│ ├── js/
│ ├── css/
│ └── img/


---

## 🛠 איך להפעיל את השרת (אחרי שתעתיק לשרת שלך)

1. **התקן PostgreSQL**
2. **צור בסיס נתונים ומשתמש**:
```sql
CREATE DATABASE safe_room_db;
CREATE USER safe_user WITH PASSWORD 'safe_pass';
GRANT ALL PRIVILEGES ON DATABASE safe_room_db TO safe_user;

התקן תלויות:

pip install -r requirements.txt

צור את הטבלאות במסד:

python3 app/create_tables.py

הרץ את השרת:

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

גש לכתובת:

http://<ip-address>:8000


ממשק משתמש
הקבצים בצד frontend/ הם הממשק, וניתן להפעילם ישירות מהדפדפן או לשרת אותם דרך FastAPI בהמשך.

yaml
Copy code

---

📌 עכשיו כל הקוד והקבצים מוכנים.
אם תרצה אפשר גם להכין את ה־`__init__.py` הריקים בכל תיקיה — רק בשביל תקינות Python מלאה.

רוצה שאשלים גם אותם ואז נתחיל את הצד של ה־frontend והחיבור ל־API?