# USAJobs Resume Builder

## 1.0 - PURPOSE
This converts all bullet points in a text file into one solid paragraph to be inserted in whatever USAJobs resume that will be submitted. This will allow for easier organization of creating the resume by first allowing the user to organize information by bullet points, but then will convert it to the default format used by USAJobs. In addition, this will count the amount of characters utilized in each resume in order to meet the character limit (5,000 as of 20230220).

## 2.0 - ASSUMPTIONS
1. A text editor is utilized for writing the resume, not word
2. No formatting is used (e.g., indentation, spacing, margins, etc.)
3. All bullets utilized are "- " (e.g., "- I work and do things")
4. Resumes to be converted are saved as text files with the naming format "[job series]_[agency worked for]_[agency applying for]" (e.g., "1102_nasa_army")

## 3.0 - PROCESS
1. User pulls whatever resume language desired from the `resumes` folder, saves it in the `convert_resumes` folder, and renames it to the required format explained in point 4 in section 2.0.
2. Job requirements and responsibilities are pasted in the text file to be converted in the first included section for `# JOB REQUIREMENTS` at the top.
3. Resume is updated according to whatever keywords are utilized in the posting in the second section `# RESUME`.
4. User runs the `functions.py` file which will convert all files in the `convert_resumes` folder to the required format in the `converted_resumes` folder.

