document.addEventListener("DOMContentLoaded", function() {
  console.log("CSV Table page loaded successfully.");

  // Example: highlight a row on click
  const rows = document.querySelectorAll("table tbody tr");
  rows.forEach(row => {
    row.addEventListener("click", () => {
      rows.forEach(r => r.classList.remove("table-active"));
      row.classList.add("table-active");
    });
  });
});

console.log("CSV Table loaded successfully!");
