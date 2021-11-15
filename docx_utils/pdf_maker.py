import subprocess
import os 
import base64 
import logging


def doc2pdf_linux(doc_path):
    
    logger = logging.getLogger('django')

    pdf_extension = ".pdf"
    
    pdf_path = os.path.dirname(doc_path)
    logger.info('开始转换word到pdf, 文件目录: %s', pdf_path) 
    
    cmd = 'soffice --headless --convert-to pdf'.split() + [doc_path] + ['--outdir'] + [pdf_path] 
     
    p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    p.wait(timeout=30)
    stdout, stderr = p.communicate() 
    
    if stderr:
        logger.error("soffice出错, %s", stderr)
        raise subprocess.SubprocessError(stderr) 
    else:
        (shotname, extension) = os.path.splitext(doc_path) 
        
        logger.info('结束转换pdf ,目录: %s, 文件名: %s', pdf_path, shotname + pdf_extension)
        
        return shotname + pdf_extension


def file2base64(file_path):
    
    logger = logging.getLogger('django')
    
    logger.info("%s 转换 base64开始");
    
    with open(file_path, 'rb') as f:
            
        file_content = f.read()
        pdf_base64 = base64.b64encode(file_content)
        
        logger.info("%s 转换 base64结束");
        
        return pdf_base64