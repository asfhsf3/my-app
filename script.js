const users = JSON.parse(localStorage.getItem("users") || "[]");

document.getElementById("loginForm").addEventListener("submit", e => {
  e.preventDefault();
  const u = document.getElementById("username").value;
  const p = document.getElementById("password").value;
  const found = users.find(x => x.u === u && x.p === p);
  if (found) location.href = "openmusic.html";
  else alert("خطأ في البيانات!");
});

document.getElementById("registerBtn").addEventListener("click", () => {
  const u = prompt("اختر اسم مستخدم:");
  const p = prompt("اختر كلمة مرور:");
  if (!u||!p) return;
  if (users.some(x=>x.u===u)) {
    alert("اسم مستخدم موجود!");
    return;
  }
  users.push({u,p});
  localStorage.setItem("users", JSON.stringify(users));
  alert("تم إنشاء الحساب 🎉");
});
