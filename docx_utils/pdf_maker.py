import subprocess
import os
import sys
import base64

def doc2pdf_linux(doc_path):
    pdf_extension = ".pdf"
    
    pdf_path = os.path.dirname(doc_path)
    print('pdf_path:', pdf_path)
    
    cmd = 'soffice --headless --convert-to pdf'.split() + [doc_path] + ['--outdir'] + [pdf_path]
    
    # cmd = 'soffice --headless --convert-to pdf'.split() + [doc_path] + ['--outdir'] + [pdf_path]
    
    
    p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    p.wait(timeout=30)
    stdout, stderr = p.communicate()
    # print(stdout)
    
    if stderr:
        raise subprocess.SubprocessError(stderr) 
    else:
        (shotname, extension) = os.path.splitext(doc_path) 
        return shotname + pdf_extension
