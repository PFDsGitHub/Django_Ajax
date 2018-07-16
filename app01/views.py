from django.shortcuts import render, HttpResponse
import json
import os
import uuid


def index(request):

    return render(request, 'index.html')


def ajax1(request):
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    # print(request.body)
    ret = {'status':True, 'message':'abc'}

    return HttpResponse(json.dumps(ret))


def upload(request):

    return render(request, 'upload.html')


def upload_img(request):
    nid = str(uuid.uuid4())
    ret = {'status': True, 'data':None, 'message':None}
    obj = request.FILES.get('k3')
    file_path = os.path.join('static', nid+obj.name)

    f = open(file_path, 'wb')
    for line in obj.chunks():
        f.write(line)
    f.close()
    ret['data'] = file_path

    return HttpResponse(json.dumps(ret))


def jsonp(request):
    return render(request, 'jsonp.html')


def ajax3(request):
    return HttpResponse('本域名服务器发送的请求')