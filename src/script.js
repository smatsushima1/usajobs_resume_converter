
// Update the total character count
function updateTotal() {
    var cchar = document.getElementById('counter');
    var ftext = document.getElementById('final_text');
    cchar.innerHTML = ftext.value.length;
    // If max limit is reached, turn color to red
    if (ftext.value.length < 5000) {
        cchar.style.color = "black";
    } else {
        cchar.style.color = "red";
    }
}


// Convert text to one paragraph
function convertText() {
    var rtext = document.getElementById("resume_text");
    var ftext = document.getElementById("final_text");
    var rtext_lines = rtext.value.split("\n");
    var ftext_val = "";
    // [i] will give the iteration of the value
    for (let i = 0; i < rtext_lines.length; ++i) {
        var rtext_val = rtext_lines[i].trimRight();
        // Convert empty lines to XXXXXXXXXX, to be replaced later
        if (rtext_val == "") {
            rtext_val = "XXXXXXXXXX";
        }
        // Add a period if there already isn't one
        if (rtext_val.slice(-1) != ".") {
            rtext_val = rtext_val.concat(".");
        }
        // Find first instance of a character and only start from there
        var rtext_index = rtext_val.indexOf(rtext_val.match(/[a-zA-Z]/).pop());
        // Add a space only after the first bullet point
        if (i == 0) {
            ftext_val = ftext_val.concat(rtext_val.substring(rtext_index));
        } else {
            ftext_val = ftext_val.concat(" ", rtext_val.substring(rtext_index));
        }
    }
    // Replace all XXXXXXXXXX, whether as the first sentence or otherwise
    ftext_val = ftext_val.replaceAll(" XXXXXXXXXX.", "").replaceAll("XXXXXXXXXX. ", "");
    ftext.value = ftext_val;
    // Rerun to get total character count
    updateTotal();
    console.log("convertText ran successfully on: " + Date());
}


// Copies text to the clipboard
function copyText() {
    var ctext = document.getElementById("final_text").value;
    navigator.clipboard.writeText(ctext);
    alert("Text is copied.");
    console.log("copyText ran successfully on: " + Date());
}


// Exports text to .txt file
function exportText() {
    // Create element with <a> tag
    const link = document.createElement("a");
    const content = document.getElementById("final_text").value;
    // Create a blog object with the file content which you want to add to the file
    const file = new Blob([content], { type: 'text/plain' });
    // Add file content in the object URL
    link.href = URL.createObjectURL(file);
    // Add file name
    var nd = new Date();
    var year = String(nd.getFullYear());
    var month = String(nd.getMonth() + 1);
    var day = String(nd.getDate());
    var ndv = year + addZero(month) + addZero(day);
    link.download = "USAJobs Resume " + ndv + ".txt";
    // Add click event to <a> tag to save file.
    link.click();
    URL.revokeObjectURL(link.href);
    console.log("exportText ran successfully on: " + Date());
}


// Add zeroes to month and day if they are one digit long
function addZero(number_value) {
    if (number_value.length < 2) {
        return "0" + number_value;
    } else {
        return number_value;
    }
}

