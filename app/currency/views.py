from currency.utils import generate_password as gp, read_txt

from django.http import HttpResponse
# from django.shortcuts import render

#########Rdjwdghwefhwv w l ur





def generate_pass(request):
    password = gp()
    return HttpResponse(password)


def requirements(request):
    reader = read_txt('/home/bav/python/currency/requirements.txt')
    return HttpResponse(reader)
