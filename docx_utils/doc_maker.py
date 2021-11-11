import time
import uuid
import os

import logging

from docxtpl import DocxTemplate

logger = logging.getLogger('django')

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
        
    logger.info('保存请求中word模板，路径: %s', file_path)
    
    file = open(file_path, 'wb')
    file.write(file_data)
    file.close
     
    return file_path


def render_doc(file_path, data):
    
    logger.info('开始使用模板 %s 生成docx', file_path)
    
    doc = DocxTemplate(file_path)
    doc.render(data)
    doc.save(file_path)
    
    logger.info('模板 %s 填充完毕', file_path)
    
    return file_path 
 
    