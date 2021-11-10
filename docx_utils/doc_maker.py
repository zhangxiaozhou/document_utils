import time
import uuid
import os

from docxtpl import DocxTemplate

def save_template_file(file_data):
    
    FILE_BASE_PATH = 'doc_tmp' 
    FILE_EXTENSION = '.docx'
    
    now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    
    file_dir = os.getcwd() + os.sep + FILE_BASE_PATH + os.sep + str(now) 
    exists = os.path.exists(file_dir)
    if not exists:
        os.makedirs(file_dir)
        
    file_id = uuid.uuid4() 
    
    file_path = file_dir + os.sep + str(file_id) + FILE_EXTENSION
        
    print('file_path:', file_path)
    
    file = open(file_path, 'wb')
    file.write(file_data)
    file.close
     
    return file_path


def render_doc(file_path, data):
    
    doc = DocxTemplate(file_path)
    doc.render(data)
    doc.save(file_path)
    
    return file_path 
 
    