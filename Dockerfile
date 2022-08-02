FROM zhangxiaozhou/centos8zh_python39_libreoffice
 
ENV LANG="zh_CN.UTF-8"
ENV LANGUAGE="zh_CN.UTF-8"

#设置path soffice
ENV LIBREOFFICE /opt/libreoffice7.2/program
ENV PATH $LIBREOFFICE:$PATH

#拷贝项目到容器
COPY ./ /wwwroot/document_utils

#暴露端口
EXPOSE 7000

#用户工作目录
WORKDIR /wwwroot/document_utils

ENTRYPOINT uwsgi --ini uwsgi.ini


 

