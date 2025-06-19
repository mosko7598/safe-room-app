const API_BASE = "http://localhost:8000";  // שנה לפי השרת שלך

async function registerUser() {
  const name = document.getElementById("name").value.trim();
  const phone = document.getElementById("phone").value.trim();

  if (!name || !phone) {
    alert("יש למלא שם ומספר טלפון");
    return;
  }

  const userData = {
    name: name,
    phone: phone
  };

  try {
    const response = await fetch(`${API_BASE}/users/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(userData)
    });

    if (!response.ok) {
      const err = await response.json();
      alert("שגיאה: " + err.detail);
      return;
    }

    const user = await response.json();
    localStorage.setItem("currentUser", JSON.stringify(user));

    if (user.is_admin) {
      window.location.href = "admin.html";
    } else {
      window.location.href = "map.html";
    }

  } catch (err) {
    console.error("Error registering user:", err);
    alert("תקלה בחיבור לשרת");
  }
}
