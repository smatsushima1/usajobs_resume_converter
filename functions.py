from datetime import datetime
import os, time


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
    for x, i in enumerate(os.scandir('convert_resumes')):
        fname = i.name
        if i.name.endswith('.txt'):
            print('Converting: ' + fname)
            convert_file(fname, x)
        else:
            print("'%s' file is not a .txt file; skipping..." % (fname))
    end_function(start_time)


# Check file
def convert_file(file_name, iteration):
    # Read file
    with open('convert_resumes/' + file_name, encoding = 'utf8') as mr:
        lines = mr.readlines()
        mr.close()
    # First find where resume starts
    for x, i in enumerate(lines):
        if '# RESUME' in i:
            resume_start = x
    # Start appending resume after the line it starts
    file_text = ''
    for x, i in enumerate(lines):
        if x > resume_start:
            # First iteration does away with '- ' since it won't need a ' '
            if x == resume_start + 1:
                file_text += i.rstrip()[2:]
                continue
            # Remove line breaks, start only after -
            file_text += i.rstrip()[1:]
    # Pull data from file name
    resume_info = file_name.replace('.txt', '').split('_')
    header_text = '%s\nLENGTH: %s' % (resume_info[1].upper(), len(file_text))
    print(header_text)
    # Append text to final converted resumes
    if iteration == 0:
        with open('converted_resumes/' + resume_info[2] + '_' + datetime.now().strftime('%Y%m%d') + '.txt', 'w', encoding = 'utf8') as wf:
            wf.writelines('%s\n%s\n\n' % (header_text, file_text))
    else:
        with open('converted_resumes/' + resume_info[2] + '_' + datetime.now().strftime('%Y%m%d') + '.txt', 'a', encoding = 'utf8') as wf:
            wf.writelines('%s\n%s\n\n' % (header_text, file_text))


convert_all()
