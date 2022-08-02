from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

import json 

import base64

from docx_utils.doc_maker import save_template_file, render_doc

from docx_utils.pdf_maker import doc2pdf_linux, file2base64

import logging

# Create your views here.

def home(request):
    
    return render(request, 'home.html')


def makeDoc(request):
    
    logger = logging.getLogger('django')
    
    if request.method == 'POST':
        
        logger.info('开始处理请求') 
        
        request_body = request.body 
        
        request_dict = json.loads(request_body) 
        logger.info('请求参数 %s', str(request_dict))
        
        file_base64 = request_dict.get('file_base64')
        file_data = base64.b64decode(file_base64)
        template_path = save_template_file(file_data)
         
        contract_docx_path = render_doc(template_path, request_dict)
        
      
        pdf_base64 = file2base64(contract_docx_path)
        
        result = {
            'docx_base64': str(pdf_base64, encoding='utf-8'),
            'msg': 'ok'
        }
        
        logger.info('结束处理请求，并返回客户端')
        
        return JsonResponse(result) 
    else:
        result = {
            'docx_base64': '',
            'msg': '接口仅支持post方法,请先访问项目根路径查看文档'
        } 
        
        logger.info('get请求返回错误信息给客户端')
        
        return JsonResponse(result)
         

def contract(request):
    
    logger = logging.getLogger('django')
    
    if request.method == 'POST':
        
        logger.info('开始处理请求') 
        
        request_body = request.body 
        
        request_dict = json.loads(request_body) 
        logger.info('请求参数 %s', str(request_dict))
        
        file_base64 = request_dict.get('file_base64')
        file_data = base64.b64decode(file_base64)
        template_path = save_template_file(file_data)
         
        contract_docx_path = render_doc(template_path, request_dict)
        
        pdf_path = doc2pdf_linux(contract_docx_path)
        
        pdf_base64 = file2base64(pdf_path)
        
        result = {
            'pdf_base64': str(pdf_base64, encoding='utf-8'),
            'msg': 'ok'
        }
        
        logger.info('结束处理请求，并返回客户端')
        
        return JsonResponse(result) 
    else:
        result = {
            'pdf_base64': '',
            'msg': '接口仅支持post方法,请先访问项目根路径查看文档'
        } 
        
        logger.info('get请求返回错误信息给客户端')
        
        return JsonResponse(result)
         

