function goto_logout(){
    window.location.href="../templates/logout.html";
}

function goto_employee_login_creation(){
    window.location.href="../templates/employee_login_creation.html"
}
function get_details() {
    const ename = document.getElementById("ename").value;
    const fromDate = new Date(document.getElementById("from_date").value);
    const toDate = new Date(document.getElementById("to_date").value);

    if (!ename || isNaN(fromDate) || isNaN(toDate) || fromDate > toDate) {
        alert("Please enter a valid name and date range.");
        return;
    }

    const outputDiv = document.getElementById("output");
    outputDiv.innerHTML = "";  

    const table = document.createElement("table");
    table.border = "1";

    const headerRow = document.createElement("tr");
    const nameCell = document.createElement("th");
    nameCell.innerText = "Activity \\ Date";
    headerRow.appendChild(nameCell);

    const dateList = [];
    for (let d = new Date(fromDate); d <= toDate; d.setDate(d.getDate() + 1)) {
        const dateCell = document.createElement("th");
        const dateStr = d.toISOString().split('T')[0];
        dateCell.innerText = dateStr;
        headerRow.appendChild(dateCell);
        dateList.push(dateStr);
    }


    const totalHeader = document.createElement("th");
    totalHeader.innerText = "Total";
    headerRow.appendChild(totalHeader);

    table.appendChild(headerRow);

    const activities = ["Coding", "Meeting"];

    for (let activity of activities) {
        const row = document.createElement("tr");
        const activityCell = document.createElement("td");
        activityCell.innerText = activity;
        row.appendChild(activityCell);

        let totalHours = 0;

        for (let i = 0; i < dateList.length; i++) {
            const dataCell = document.createElement("td");
            dataCell.innerText = (i+1); 
            totalHours += (i+1);
            row.appendChild(dataCell);
        }

        const totalCell = document.createElement("td");
        totalCell.innerText = totalHours;
        row.appendChild(totalCell);

        table.appendChild(row);
    }

outputDiv.appendChild(table);
}
function updateWorkDetails() {
    const addDateInput = document.getElementById("add_date").value;
    const workHoursInput = document.getElementById("work_hours").value;

    if (!addDateInput || !workHoursInput || isNaN(workHoursInput) || workHoursInput <= 0) {
        alert("Please enter a valid date and number of work hours.");
        return;
    }

    const ename = document.getElementById("ename").value || "Unknown Employee";

    // For now, just append a row to the output table if exists
    const outputDiv = document.getElementById("output");
    let table = outputDiv.querySelector("table");

    if (!table) {
        alert("No timesheet table found. Please get timesheet first.");
        return;
    }

    // Check if a row for this date already exists
    const dateStr = new Date(addDateInput).toISOString().split('T')[0];
    let dateIndex = Array.from(table.rows[0].cells).findIndex(cell => cell.innerText === dateStr);

    if (dateIndex === -1) {
        alert("Date not in current timesheet range. Please use 'GET TIMESHEET' first.");
        return;
    }

    // Add work hours to existing activities (here we just add to first activity as example)
    const activityRow = table.rows[1]; // Assuming first activity is row 1
    activityRow.cells[dateIndex].innerText = workHoursInput;

    // Update total for the activity
    let total = 0;
    for (let i = 1; i < activityRow.cells.length - 1; i++) {
        total += parseInt(activityRow.cells[i].innerText) || 0;
    }
    activityRow.cells[activityRow.cells.length - 1].innerText = total;

    alert(`Updated ${ename}'s work hours for ${dateStr}.`);
}
