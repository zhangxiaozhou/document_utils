from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

import json 

import base64

import time


from docx_utils.doc_maker import save_template_file, render_doc

from docx_utils.pdf_maker import doc2pdf_linux

# Create your views here.

def home(request):
    
    
    return render(request, 'home.html')


def contract(request):
    if request.method == 'POST':
        
        print('开始生成pdf: ' + time.strftime("%Y%m%d%H%M%S", time.localtime()))
        
        request_body = request.body 
        
        request_dict = json.loads(request_body) 
        
        file_base64 = request_dict.get('file_base64')
        
        file_data = base64.b64decode(file_base64)
        
        template_path = save_template_file(file_data)
         
        contract_docx = render_doc(template_path, request_dict)
        
        pdf_path = doc2pdf_linux(contract_docx)
        
        with open(pdf_path, 'rb') as f:
            
            file_content = f.read()
            pdf_base64 = base64.b64encode(file_content)
            
            json_str = json.dumps({'pdf_base64': str(pdf_base64, encoding='utf-8')})
            
            response = HttpResponse(json_str);
            response['Content-type'] = 'application/json'
            
            
            print('结束生成pdf: ' + time.strftime("%Y%m%d%H%M%S", time.localtime()))

            return response
         

