# encoding=utf8
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from api.serializers import SnippetSerializer
from api.models import Snippet
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import os
from api.sendmail import sendmail
from api.getALiYunAPI.getAliYunAPI import *
import uuid


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Regiser(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        username = request.data.get('userName')
        password = request.data.get('password')
        print(username, password)
        if not (username and password):
            sendmail("songyuanyuan.com：注册失败","ERROR Incorrect username or password \n 用户名：{0} 密码: {1} ".format(username, password))
            return Response({"reasoncode": -1, "reason": "ERROR Incorrect username or password"}, status=status.HTTP_200_OK)
        # 判断用户是否存在
        try:
            user = User.objects.get(username=username)
        except Exception  as err:
            user = None
        if user:
            sendmail("songyuanyuan.com：注册失败",
                     "The user has already existed \n 用户名：{0} 密码: {1} ".format(username, password))
            return Response({"reasoncode": 1, "reason": "The user has already existed"}, status=status.HTTP_200_OK)
        else:
            # 添加到数据库（还可以加一些字段的处理）
            user = User.objects.create_user(username=username, password=password)
            user.save()
            sendmail("songyuanyuan.com：注册成功",
                     "Regiser was successful \n 用户名：{0} 密码: {1} ".format(username, password))
            return Response({"reasoncode": 0, "reason": "Regiser was successful"}, status=status.HTTP_200_OK)


class Login(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        username = request.data.get('userName')
        password = request.data.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
        if user is not None:
            sendmail("songyuanyuan.com：登录成功",
                     "用户名：{0} 密码: {1} ".format(username, password))
            return Response({'uid': 1, 'permissions': ["auth", "auth/testPage", "auth/authPage", "auth/authPage/edit", "auth/authPage/visit"], 'role': "系统管理员", 'roleType': 1, 'userName': username}, status=status.HTTP_200_OK)
        sendmail("songyuanyuan.com：登录失败",
                 "用户名：{0} 密码: {1} ".format(username, password))
        return Response(status=status.HTTP_400_BAD_REQUEST)

class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetImgsList(APIView):
    def fifter(self, file_dir, files):
        files_r = []
        for i in files:
            (shotname, extension) = os.path.splitext(i)
            if extension.lower() in ['.jpg','.JPG','.png','.bmp','GIF','gif']:
                files_r.append(i)
        files_r = sorted(files_r, reverse=True, key=lambda x: os.path.getmtime(file_dir + x))
        return files_r

    def file_name(self, file_dir):
        imgs = []
        img5 = []
        i = 1
        for root, dirs, files in os.walk(file_dir):
            return self.fifter(file_dir,files)

    def getlist(self, files):
        imgs = []
        for i in range(len(files)):
            files[i] = "http://23.106.155.65:8001/%s" % files[i]
        count = len(files)
        l = int(count / 5)
        n = count % 5
        last = 0
        for i in range(5):
            if i < n:
                imgs.append(files[last:last + l + 1])
                last = last + l + 1
            else:
                imgs.append(files[last:last + l])
                last = last + l
        return imgs

    def get(self, request):
        imgs = self.getlist(self.file_name(os.path.join(BASE_DIR, "static/yuanyuan/images/")))
        print(imgs)
        return Response({"imgs": imgs}, status=status.HTTP_200_OK)


class GetWeather(APIView):
    def get(self, request):
        weaInfo = getWeather("")
        return Response(weaInfo, status=status.HTTP_200_OK)


class DelImage(APIView):
    def post(self, request):
        imgname = request.data.get('img-name')
        if imgname:
            print(imgname.split('/'))
            img = imgname.split('/')[-1]
            print(img)

            r_file = os.path.join(BASE_DIR, "static/yuanyuan/images/%s" % img)
            m_file = os.path.join(BASE_DIR, "static/yuanyuan/images/%s.removed" % img)
            if os.path.exists(r_file):
                os.rename(r_file, m_file)
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


def upload(request):
    if request.method == 'POST':
        obj = request.FILES.get('file')
        (shotname, extension) = os.path.splitext(obj.name)
        imgname = "{0}{1}".format( uuid.uuid1(),extension)
        f = open(os.path.join(BASE_DIR, "static/yuanyuan/images/%s" % imgname), 'wb')
        for line in obj.chunks():
            f.write(line)
        f.close()
        return HttpResponse('上传成功')


class Dash(APIView):
    def get(self, request):
        weaInfo = getWeather("")
        return Response(weaInfo, status=status.HTTP_200_OK)