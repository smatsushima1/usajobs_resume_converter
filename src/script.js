
// Update the total character count
function updateTotal() {
    var cchar = document.getElementById('counter');
    var ftext = document.getElementById('final_text');
    // Convert to a four-digit character and take the last four digits regardless
    cchar.innerHTML = ("000" + String(ftext.value.length)).slice(-4);
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
    // Split at linebreaks to get an array of values
    var rtext_lines = rtext.value.split("\n");
    var ftext_val = "";
    // [i] will give the iteration of the value
    for (let i = 0; i < rtext_lines.length; ++i) {
        var rtext_val = rtext_lines[i].trimRight();
        // Convert empty lines to XXXXXXXXXX, to be replaced later; otherwise will cause null error
        if (rtext_val == "") {
            rtext_val = "XXXXXXXXXX";
        }
        // Add a period if there already isn't one
        if (rtext_val.slice(-1) != ".") {
            rtext_val = rtext_val.concat(".");
        }
        // Find first instance of a character and only start from there
        var rtext_index = rtext_val.indexOf(rtext_val.match(/[a-zA-Z]/).pop());
        // Add a space for the sentence only after the first bullet point
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
    const file = new Blob([content], {type: 'text/plain'});
    // Add file content in the object URL
    link.href = URL.createObjectURL(file);
    // Add date to file name
    var nd = new Date();
    var year = String(nd.getFullYear());
    // Convert to a two digit character and take last two characters regardless
    var month = ("0" + String(nd.getMonth() + 1)).slice(-2);
    var day = ("0" + String(nd.getDate())).slice(-2);
    // All must be strings in order to concatenate, otherwise dates will be added as a number
    link.download = "USAJobs Resume " + year + month + day + ".txt";
    // Add click event to <a> tag to save file.
    link.click();
    URL.revokeObjectURL(link.href);
    console.log("exportText ran successfully on: " + Date());
}


// Pull USAJobs web address
function pullAddress() {
    document.getElementById("jt").value = "";
    document.getElementById("dt").value = "";
    document.getElementById("ot").value = "";
    document.getElementById("ad").value = "";
    var fetch_ex = fetch(document.getElementById("posting").value);
    console.log(fetch_ex);
    return String(document.getElementById("posting").value);
    console.log("pullAddress ran successfully on: " + Date());
}
