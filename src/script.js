
// Update the total character count
function updateTotal() {
    var cchar = document.getElementById('counter');
    var ftext = document.getElementById('finaltext');
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
    var rtext = document.getElementById('resumetext');
    var ftext = document.getElementById('finaltext');
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
            var ftext_val = ftext_val.concat(rtext_val.substring(rtext_index));
        } else {
            ftext_val = ftext_val.concat(" ", rtext_val.substring(rtext_index));
        }
    }
    // Replace all XXXXXXXXXX, whether as the first sentence or otherwise
    ftext_val = ftext_val.replaceAll(" XXXXXXXXXX.", "").replaceAll("XXXXXXXXXX. ", "");
    ftext.value = ftext_val;
    // Rerun to get total character count
    updateTotal();
    console.log("Function ran successfully on: " + Date())
}
