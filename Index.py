import os
import shutil
from datetime import datetime
import mimetypes
import re
from platformdirs import user_pictures_dir, user_videos_dir, user_documents_dir

monitor_dir=input('Enter the full-path of your monitor directory: ')
parts = re.split(r"[:/\\,|]", monitor_dir)

dir_map = {
    "image": user_pictures_dir(),
    "video": user_videos_dir(),
    "application": user_documents_dir(),
    "text": os.path.join(user_documents_dir(), "TextFiles"),
    "others": os.path.join(user_documents_dir(), "Others")
}

def data_log(file_,destination):
    now=datetime.now()
    day_month_year=now.strftime('%d-%m-%Y')
    hours_minutes_second=now.strftime('%H:%M:%S')
    with open(f'data_{parts[-1]}.txt','a') as f:
        f.write(f'file:{file_} was transferred to destination: {destination} at {hours_minutes_second} on {day_month_year}\n')

def move_file(file,src_dir):
    os.chdir(monitor_dir)
    mimetype,_=mimetypes.guess_type(file)
    category='others'
    if mimetype:
        for key in dir_map:
            if key in mimetype:
                category=key
    dest_dir=dir_map[category]
    src_path=os.path.join(src_dir,file)
    dest_path=os.path.join(dest_dir,file)
    for i in os.listdir(dest_dir):
        if i == file:               
            name,ext=os.path.splitext(file)
            name_number=1
            new_name=f'{name}_({name_number}){ext}'
            while new_name in os.listdir(dest_dir):
                 name_number+=1
                 new_name=f'{name}_({name_number}){ext}'
            shutil.move(src_path,os.path.join(dest_dir,new_name))
            data_log(new_name, dest_dir)
    else:
            shutil.move(src_path,dest_path)
            data_log(file, dest_dir)

def file_transfer(monitor_dir):
    for file in os.listdir(monitor_dir):
        try:
            if file==f'data_{parts[-1]}.txt':
                continue
            if os.path.isfile(os.path.join(monitor_dir,file)):
                move_file(file, monitor_dir)
        except FileNotFoundError:
            continue

file_transfer(monitor_dir)
