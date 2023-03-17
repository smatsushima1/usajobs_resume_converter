from datetime import datetime
from bs4 import BeautifulSoup as bsp
import os, time, spacy, requests


# Start timer for functinos
def start_function(func_name):
    start_time = time.time()
    print('\n' + ('#' * 80))
    print('Function: %s\nStarting...' % (func_name))
    return start_time


# End timer for functions
def end_function(start_time):
    end_time = time.time() - start_time
    if end_time > 60:
        res = end_time / 60
        res_spl = str(res).split('.')
        mins = res_spl[0]
        secs = round(float('.' + res_spl[1]) * 60, 3)
        print('''Function finished in %s' %s"''' % (mins, secs))
    else:
        print('Function finished in %s"' % round(time.time() - start_time, 3))


# Run
def convert_all():
    start_time = start_function('convert_all')    
    # First move all files in 'converted_resumes' to 'resumes'
    ld = os.listdir('resumes_converted')
    if len(ld) > 0:
        while True:
            answer = input('Move files in the "resumes_converted" folder before proceeding? (y/n): ')
            if answer.lower().strip() not in ('y', 'n'):
                print("You must type either 'y' or 'n'.")
            else:
                break
        if answer.lower().strip() == 'y':
            for i in ld:
                os.rename('resumes_converted/' + i, 'resumes/' + i)
                print('Moved: ' + i)
    print('\nProceeding to file conversions...\n')
    for x, i in enumerate(os.scandir('resumes_working')):
        fname = i.name
        if i.name.endswith('.txt'):
            print('Converting: ' + fname)
            convert_file(fname, x)
        else:
            print("'%s' file is not a .txt file; skipping...\n" % (fname))
    end_function(start_time)


# Check file
def convert_file(file_name, iteration):
    # Read file
    with open('resumes_working/' + file_name, encoding = 'utf8') as mr:
        lines = mr.readlines()
        mr.close()
    # Start appending resume after the line it starts
    file_text = ''
    for x, i in enumerate(lines):
        # Continue if empty line
        if i == '\n':
            continue
        # Start at first character, remove line break, add period and space
        file_text += i[int(i.find(next(filter(str.isalpha, i)))):].rstrip() + '. '
        # Remove extra period
        file_text = file_text.replace('..', '.')
    # Pull data from file name
    resume_info = file_name.replace('.txt', '').split('_')
    header_text = '%s\nLENGTH: %s' % (resume_info[1].upper(), len(file_text.rstrip()))
    print(header_text + '\n')
    # Append text to final converted resumes
    if iteration == 0:
        with open('resumes_converted/' + resume_info[2] + '_' + datetime.now().strftime('%Y%m%d') + '.txt', 'w', encoding = 'utf8') as wf:
            wf.writelines('%s\n%s\n\n' % (header_text, file_text.rstrip()))
    else:
        with open('resumes_converted/' + resume_info[2] + '_' + datetime.now().strftime('%Y%m%d') + '.txt', 'a', encoding = 'utf8') as wf:
            wf.writelines('%s\n%s\n\n' % (header_text, file_text.rstrip()))


# Find keywords
def keyword_search():
    spcy = spacy.load("en_core_web_sm")

    # taking input
    text = "Writing"
      
    # returns a document of object
    doc = spcy(text)
      
    # checking if it is a noun or not
    if(doc[0].tag_ == 'NNP'):
        print(text, " is a noun.")
    else:
        print(text, " is not a noun.")


keyword_search()






