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


// Handle modal image loading for CSV table
// document.addEventListener('DOMContentLoaded', function () {
//   const imageModal = document.getElementById('imageModal');

//   if (imageModal) {
//     $('#imageModal').on('show.bs.modal', function (event) {
//       const button = $(event.relatedTarget); // Button that triggered the modal
//       const imageSrc = button.data('image'); // Get image path
//       const modal = $(this);
//       modal.find('#sensorImage').attr('src', imageSrc);
//     });
//   }
// });
// Wait for document to load
document.addEventListener("DOMContentLoaded", function () {

  $('#imageModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Button that triggered the modal
    var imageSrc = button.data('image'); // Extract info from data-* attribute
    var sensorId = button.data('sensorid'); // Extract sensor ID
    
    var modal = $(this);
    var img = modal.find('#sensorImage');
    
    img.attr('src', '').hide(); 
    modal.find('#noImageText').remove();

    var testImg = new Image();
    testImg.onload = function() {
      img.attr('src', imageSrc).show();
    };
    testImg.onerror = function() {
      img.hide();
      modal.find('.modal-body').append('<p id="noImageText">No image available.</p>'
      );
    };
    testImg.src = imageSrc;
    modal.find('#imageId').text('Sensor ID: ' + sensorId);
  });
  
    $('#imageModal').on('hidden.bs.modal', function () {
    var modal = $(this);
    modal.find('#sensorImage').attr('src', imageSrc);
    modal.find('#noImageText').remove();
  });
});

// sort table by column
document.addEventListener("DOMContentLoaded", function () {
  const table = document.querySelector("#data-table");
  if (!table) return;

  const headers = table.querySelectorAll("th");

  headers.forEach((header, index) => {
    header.style.cursor = "pointer";
    header.title = "Click to sort"; // tooltip
    header.addEventListener("click", () => {
      const isCurrentlyAsc = header.classList.contains("th-sort-asc");
      sortTableByColumn(table, index, !isCurrentlyAsc);
    });
  });

  // Automatically sort SensorID (first column) descending
  sortTableByColumn(table, 0, false);
});

function sortTableByColumn(table, columnIndex, asc = true) {
  const dirModifier = asc ? 1 : -1;
  const tBody = table.tBodies[0];
  const rows = Array.from(tBody.querySelectorAll("tr"));

  const sortedRows = rows.sort((a, b) => {
    const aText = a.querySelector(`td:nth-child(${columnIndex + 1})`).textContent.trim();
    const bText = b.querySelector(`td:nth-child(${columnIndex + 1})`).textContent.trim();

    const aNum = parseFloat(aText.replace(/,/g, ""));
    const bNum = parseFloat(bText.replace(/,/g, ""));
    if (!isNaN(aNum) && !isNaN(bNum)) {
      return (aNum - bNum) * dirModifier;
    }
    return aText.localeCompare(bText) * dirModifier;
  });

  // Rebuild the table body
  tBody.innerHTML = "";
  tBody.append(...sortedRows);

  // Remove sort classes from all headers
  table.querySelectorAll("th").forEach(th => th.classList.remove("th-sort-asc", "th-sort-desc"));
  // Add class to the sorted column
  table.querySelector(`th:nth-child(${columnIndex + 1})`).classList.toggle("th-sort-asc", asc);
  table.querySelector(`th:nth-child(${columnIndex + 1})`).classList.toggle("th-sort-desc", !asc);
}

// --- Styling for hover & sort indicators ---
const style = document.createElement("style");
style.textContent = `
  th {
    user-select: none;
    transition: background-color 0.2s ease, color 0.2s ease;
  }
  th:hover {
    background-color: #f1f3f4;
    color: #007bff;
  }
  th.th-sort-asc::after {
    content: " ▲";
    font-size: 0.8em;
    color: #007bff;
  }
  th.th-sort-desc::after {
    content: " ▼";
    font-size: 0.8em;
    color: #007bff;
  }
`;
document.head.appendChild(style);

