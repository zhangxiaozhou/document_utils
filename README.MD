docx模板生成目标docx, 目标docx转换pdf

1、项目开发采用python3.9  django3.2  
    采用python docxtpl从合同模板和数据生成合同。
    采用libreoffice转换docx到pdf。
    服务接收参数和返回参数均采用json格式。其中文件采用base64编码后作为json字段传输。

2、由于部署繁琐，需要安装python3.9  pip3  libreoffice ，还需要系统安装中文语言包，所以环境采用docker方式安装部署和发布。 

3、docker镜像以 centos8为基础。 安装了中文语言包。中文字体。python3.9。 pip3。 libreoffice。 

4、项目运行。
    先在项目根目录执行   “ docker build -t docutils . ”
    
    注意后面那个 "." 

    再运行 docker run -itd -p 7000:7000 docutils  

    其中docutils部分可根据喜好更换
    
    至此7000端口服务已经可以正常访问。
