from os import listdir
from os.path import isfile, join
import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from datetime import datetime
import logging

def on_created(event):
    print(f"hey, {event.src_path} has been created!")
    sort_files_in_a_folder(mypath)
    logging.basicConfig(filename='logs.log',
        filemode='a',
        format='%(asctime)s %(message)s',
        level=logging.DEBUG)
    logging.info(f"hey, {event.src_path} has been created!")

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    my_event_handler.on_created = on_created
    path = "C:\\Users\\Youri\\Documents\\test"
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

mypath="C:\\Users\\Youri\\Documents\\test"

def sort_files_in_a_folder(mypath):
    '''
    A function to sort the files in a download folder
    into their respective categories
    '''
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    file_type_variation_list=[]
    filetype_folder_dict={}
    for file in files:
        filetype=file.split('.')[-1]
        if filetype not in file_type_variation_list:
            file_type_variation_list.append(filetype)
            new_folder_name=mypath+'/'+ filetype + '_folder'
            filetype_folder_dict[str(filetype)]=str(new_folder_name)
            if os.path.isdir(new_folder_name)==True:  #folder exists
                continue
            else:
                os.mkdir(new_folder_name)
    for file in files:
        src_path = mypath+'/'+file
        filetype=file.split('.')[-1]
        try: 
            if  filetype in filetype_folder_dict.keys():
                dest_path=filetype_folder_dict[str(filetype)]
                shutil.move(src_path,dest_path)
        except os.error:
            return False

my_observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
    