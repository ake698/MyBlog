# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models import Article,Tag,Classification,Comments
from django.template import RequestContext
import time


# Create your views here.

def blog_list(request):
	classi=Classification.objects.all()
        classdic={}
	for i in classi:
		classdic[i]=i.article_set.all().count()
	try:
		cat=request.GET.get('cat')
		allblog=classi.get(id=cat).article_set.all().order_by('-publish_time')
	except:
		allblog=Article.objects.all().order_by('-publish_time')
	blogpage=Paginator(allblog,2)	
	try:
		page=request.GET.get('page')
		blogs=blogpage.page(page)
	except:
		#page=1
		blogs=blogpage.page(1)
	return render(request,'index.html',{'blogs':blogs,'classdic':classdic,'count':len(allblog)})

def blog_art(request,cat):
	classi=Classification.objects.all()
        classdic={}
	tagdic={}
	p=0
	for i in classi:
		classdic[i]=i.article_set.all().count()
	try:
		artn=request.GET.get('artn')
	except:
		artn=1
	article = Article.objects.get(id=artn)
	comment=Comments.objects.filter(id=artn)
	tags = article.tags.all()
	result="1"
        for i in tags:
		tagdic[i.tag_name]=Tag.objects.get(tag_name=i.tag_name).article_set.all()
	try:
		for i in tagdic:
			p=p+1
			if p<=1:
				result=tagdic[i]
			else:
				result = list(set(result).intersection(set(tagdic[i])))
	except:
		pass
	result=list(set(result).difference(set(Article.objects.filter(id=artn))))
	return render(request,'blog.html',{'article':article,'tags':tags,'classdic':classdic,'result':result,'comment':comment})	


def blog_edit(request):
	return render(request,'edit.html')
	
'''
def upload_image(request):
    if request.method == 'POST':
        callback = request.GET.get('CKEditorFuncNum')
        try:
            path = "upload/" + time.strftime("%Y%m%d%H%M%S",time.localtime())  
            f = request.FILES["upload"]
            file_name = path + "_" + f.name
            des_origin_f = open(file_name, "wb+")
            for chunk in f:               
                des_origin_f.write(chunk)
            des_origin_f.close()
        except Exception, e:
            print e
        res = r"<script>window.parent.CKEDITOR.tools.callFunction("+callback+",‘/"+file_name+"‘, ‘‘);</script>"
        return HttpResponse(res)
    else:
        raise Http404()
'''

