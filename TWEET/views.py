from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
import string
import os
import numpy as np

from TWEET.models import Mix2,Ref
#from TWEET.forms import DocumentForm
#from TWEET.forms import ContactForm

import pandas as PN
from pandasql import sqldf
from sqlalchemy import create_engine
from django.conf import settings
# Create your views here.
import datetime
import time
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.db.models import Q
from django.utils import timezone

# Create your views here.

	
def index(request):
	sort = request.GET.get('sort','')	
	

	yesterday = datetime.now() - timedelta(days=30)
	
	liste_tweet = Mix2.objects.filter(col__gte=yesterday).filter(col__gte=yesterday).order_by('-retweet_count').filter(media_url__contains="http").exclude(t_id__gte=5999)[0:40]
	title="Tous les tweets de vos politiques francais sur PoliTweets"
	#liste_tweet = Mix2.objects.filter(text__contains="").filter(col__year='2016',col__month='12',col__day='7').order_by('-retweet_count')[0:10]

		#.filter(col=datetime(2016, 12, 7))
		
	template = loader.get_template('LTE/index_.html')
	AA=1
	context = RequestContext(request, {
        'liste_tweet': liste_tweet,
		'title':title,
		'AA':AA,
		

		
	})
	return HttpResponse(template.render(context))
	

def top(request,sort,periode):
	club = request.GET.get('club','')
	country_league = request.GET.get('country_league','')
	search = request.GET.get('search','')
	if periode=="":
		periode='J7'	
	if sort=="tw":	
		typsort='-retweet_count'
	elif sort=="fav":
		typsort='-favorite_count'
	elif sort=="rec":
		typsort='-col'
	else:
		typsort='-col'

	yesterday = timezone.now() - timedelta(days=7)
	if periode=='J7':
		how_many_days = 7
	if periode=='J30':
		how_many_days = 30
	if periode=='J365':
		how_many_days = 365

	if club:
		texte="Top tweets: "+club+" / "+country_league
		texte2="?club="+club
	elif country_league:
		texte="Top tweets: "+country_league		
		texte2="?country_league="+country_league
	else:
		texte="Top tweets: All players"		
		texte2=""
	
	if club:
		liste_tweet = Mix2.objects.order_by(typsort).filter(club=club).exclude(t_id__gte=5999).exclude(retweet_count__isnull=True).filter(col__gte=timezone.now()-timedelta(days=how_many_days))[0:40]
		league=Ref.objects.filter(club=club).distinct('league_field').values_list('league_field')
		liste_clubs=Ref.objects.filter(league_field=country_league).filter(entraineur=3).order_by('-followers_count')
		ref_=Ref.objects.filter(nom=club).filter(entraineur=3).order_by('-followers_count')
	elif country_league:
		liste_tweet = Mix2.objects.order_by(typsort).filter(country_league=country_league).exclude(t_id__gte=5999).exclude(retweet_count__isnull=True).filter(col__gte=timezone.now()-timedelta(days=how_many_days))[0:40]
		liste_clubs=Ref.objects.filter(country_league=country_league).filter(entraineur=3).order_by('-followers_count')
		ref_=Ref.objects.filter(league_field=country_league).filter(entraineur=2).order_by('-followers_count')
	elif search:
		liste_tweet = Mix2.objects.order_by(typsort).filter(nom__contains=search).exclude(t_id__gte=5999).exclude(retweet_count__isnull=True).filter(col__gte=timezone.now()-timedelta(days=how_many_days))[0:40]
		liste_clubs=Ref.objects.filter(entraineur=3).order_by('-followers_count')
		ref_=""
	else:		
		liste_tweet = Mix2.objects.order_by(typsort).exclude(t_id__gte=5999).exclude(retweet_count__isnull=True).filter(col__gte=timezone.now()-timedelta(days=how_many_days))[0:40]
		liste_clubs=Ref.objects.filter(entraineur=3).order_by('-followers_count')
		ref_=""
	#liste_tweet = Mix2.objects.filter(text__contains="").filter(col__year='2016',col__month='12',col__day='7').order_by('-retweet_count')[0:10]
	liste_league=Ref.objects.filter(entraineur=2).order_by('-followers_count')
	
	
	count=1
		#.filter(col=datetime(2016, 12, 7))
	for obj in liste_tweet:
		obj.numero=count
		count=count+1		
	template = loader.get_template('LTE/index_pmg.html')
	liste_mandat=Ref.objects.order_by('club').distinct('club')
	z=2
	liste_parti=Ref.objects.order_by('country_league').distinct('country_league')
	
	title="Les meilleurs tweets de vos politiques francais sur PoliTweets - "+club+" / "+country_league
	
	AA=3
	context = RequestContext(request, {
        'liste_tweet': liste_tweet,
		'sort':sort,
		'liste_mandat':liste_mandat,
		'liste_parti':liste_parti,
		'parti':club,
		'mandat':country_league,
		'periode':periode,
		'how_many_days':how_many_days,
		'search':search,
		'z':z,
		'title':title,
		'liste_league':liste_league,
		'liste_clubs':liste_clubs,
		'ref_':ref_,
		'texte':texte,
		'texte2':texte2,
		'AA':AA,
	})
	return HttpResponse(template.render(context))
	
	


def parti(request):
	club = request.GET.get('club','')
	country_league = request.GET.get('country_league','')
	search = request.GET.get('search','')
	periode='J365'	
	typsort='-col'

	yesterday = timezone.now() - timedelta(days=7)
	if periode=='J7':
		how_many_days = 7
	if periode=='J30':
		how_many_days = 30
	if periode=='J365':
		how_many_days = 365
	
	if club:
		texte="Timeline: "+club+" / "+country_league
	else:
		texte="Timeline: "+country_league
	
	if club:
		liste_tweet = Mix2.objects.order_by(typsort).filter(club=club).exclude(t_id__gte=5999).exclude(retweet_count__isnull=True).filter(col__gte=timezone.now()-timedelta(days=how_many_days))[0:40]
		league=Ref.objects.filter(club=club).distinct('league_field').values_list('league_field')
		liste_clubs=Ref.objects.filter(country_league=country_league).filter(entraineur=3).order_by('-followers_count')
		ref_=Ref.objects.filter(nom=club).filter(entraineur=3).order_by('-followers_count')
	elif country_league:
		liste_tweet = Mix2.objects.order_by(typsort).filter(country_league=country_league).exclude(t_id__gte=5999).exclude(retweet_count__isnull=True).filter(col__gte=timezone.now()-timedelta(days=how_many_days))[0:40]
		liste_clubs=Ref.objects.filter(country_league=country_league).filter(entraineur=3).order_by('-followers_count')
		ref_=Ref.objects.filter(league_field=country_league).filter(entraineur=2).order_by('-followers_count')
	elif search:
		liste_tweet = Mix2.objects.order_by(typsort).filter(nom__contains=search).exclude(t_id__gte=5999).exclude(retweet_count__isnull=True).filter(col__gte=timezone.now()-timedelta(days=how_many_days))[0:40]
		liste_clubs=Ref.objects.filter(entraineur=3).order_by('-followers_count')
		ref_=""
	else:		
		liste_tweet = Mix2.objects.order_by(typsort).exclude(t_id__gte=5999).exclude(retweet_count__isnull=True).filter(col__gte=timezone.now()-timedelta(days=how_many_days))[0:40]
		liste_clubs=Ref.objects.filter(entraineur=3).order_by('-followers_count')
		ref_=""
	liste_league=Ref.objects.filter(entraineur=2).order_by('-followers_count')
	#liste_tweet = Mix2.objects.filter(text__contains="").filter(col__year='2016',col__month='12',col__day='7').order_by('-retweet_count')[0:10]
	count=1
	
		#.filter(col=datetime(2016, 12, 7))
	for obj in liste_tweet:
		obj.numero=count
		count=count+1		
	template = loader.get_template('LTE/index_pmg.html')
	liste_mandat=Ref.objects.order_by('club').distinct('club')
	z=2
	liste_parti=Ref.objects.order_by('country_league').distinct('country_league')
	AA=4
	title="Les meilleurs tweets de vos politiques francais sur PoliTweets - "+club+" / "+country_league
	context = RequestContext(request, {
        'liste_tweet': liste_tweet,
		
		'liste_mandat':liste_mandat,
		'liste_parti':liste_parti,
		'parti':club,
		'mandat':country_league,
		'periode':periode,
		'search':search,
		'z':z,
		'title':title,
		'liste_league':liste_league,
		'liste_clubs':liste_clubs,
		'ref_':ref_,
		'texte':texte,
		'AA':AA,
		
	})
	return HttpResponse(template.render(context))
	
	

def ann(request,sort):
	alpha = request.GET.get('alpha','')
	club = request.GET.get('club','')
	country_league = request.GET.get('country_league','')
	search = request.GET.get('search','')
	
	
	
	if sort=="":
		sort="fav"
	
	if sort=="tw":
		typsort='-statuses_count'
	else:
		typsort='-followers_count'
		
	if alpha:
		BT=Ref.objects.filter(nom__istartswith=alpha).order_by(typsort).exclude(t_id__gte=5999)[0:]
		liste_clubs=Ref.objects.filter(entraineur=3).order_by('-followers_count')
	elif club:
		BT=Ref.objects.filter(club=club).order_by(typsort).exclude(t_id__gte=5999)[0:]
		league=Ref.objects.filter(club=club).distinct('league_field').values_list('league_field')
		liste_clubs=Ref.objects.filter(league_field=league).filter(entraineur=3).order_by('-followers_count')
		ref_=Ref.objects.filter(nom=club).filter(entraineur=3).order_by('-followers_count')
	elif country_league:
		BT=Ref.objects.filter(country_league=country_league).order_by(typsort).exclude(t_id__gte=5999)[0:]
		liste_clubs=Ref.objects.filter(country_league=country_league).filter(entraineur=3).order_by('-followers_count')
		ref_=Ref.objects.filter(country_league=country_league).filter(entraineur=2).order_by('-followers_count')
	elif search:
		BT=Ref.objects.filter(nom__icontains=search).order_by(typsort).exclude(t_id__gte=5999)[0:]
		liste_clubs=Ref.objects.filter(entraineur=3).order_by('-followers_count')
		ref_=""
	elif sort=="tw":
		BT=Ref.objects.order_by(typsort).exclude(t_id__gte=5999)[0:]
		ref_=""
	else:	
		BT=Ref.objects.order_by(typsort).exclude(t_id__gte=5999)[0:]
		liste_clubs=Ref.objects.filter(entraineur=3).order_by('-followers_count')
		ref_=""
	liste_mandat=Ref.objects.order_by('club').distinct('club')

	
	liste_league=Ref.objects.filter(entraineur=2).order_by('-followers_count')
	
	AA=2
	
	liste_alpha=list(string.ascii_lowercase)
	template = loader.get_template('LTE/Index_ANN.html')
	count=1
	for obj in BT:
		obj.numero=count
		count=count+1	
	#BT['numero']=BT.index+1
	if sort=="":
		sort="fav"
	z=1
	title="Les profils et comptes de vos politiques francais sur PoliTweets - "+club+" "+country_league
	context = RequestContext(request, {
        'BaseTweetos': BT,
		'liste_clubs':liste_clubs,
		
		
		'liste_league':liste_league,
		'liste_clubs':liste_clubs,
		'liste_alpha': "",
		'liste_mandat': liste_mandat,
		'alpha':alpha,
		'club':club,
		'country_league':country_league,
		'search':search,
		'sort':sort,
		'z':z,
		'title':title,
		'ref_':ref_,
		'AA':AA,
	})
	return HttpResponse(template.render(context))

	
	
	
def depute(request,depute):
	sort=request.GET.get('sort', '')
	if sort=="":
		sort="tw"
	if request.GET.get('sort', '')=="fav":
		liste_tweet = Mix2.objects.filter(id_twit=depute).order_by('-favorite_count').exclude(retweet_count__isnull=True).exclude(t_id__gte=5999)[0:10]
	else:
		liste_tweet = Mix2.objects.filter(id_twit=depute).order_by('-retweet_count').exclude(retweet_count__isnull=True).exclude(t_id__gte=5999)[0:10]
	BT=Ref.objects.filter(screen_name=depute)
	liste_tweet2 = Mix2.objects.filter(id_twit=depute).order_by('-col').exclude(retweet_count__isnull=True).exclude(t_id__gte=5999)[0:10]
	parti=Mix2.objects.filter(id_twit=depute).distinct('club').values_list('club')
	league=Mix2.objects.filter(id_twit=depute).distinct('league_field').values_list('league_field')
	liste_clubs=Ref.objects.filter(league_field=league).filter(entraineur=3).order_by('-followers_count')
	liste_league=Ref.objects.filter(entraineur=2).order_by('-followers_count')
	liste_collegue=Ref.objects.filter(club=parti).order_by('-followers_count')
	liste_parti=Ref.objects.order_by('country_league').distinct('country_league')

	
	template = loader.get_template('LTE/Index_AS.html')
	z=1
	def xstr(s):
		if s is None:
			return ''
		return str(s.encode('utf8'))
	count=1	
	for obj in liste_tweet:
		obj.numero=count
		count=count+1	
		
	count=1
	for obj in liste_tweet2:
		obj.numero=count
		count=count+1	
		
	A=2	
	for B in BT:
		title="Compte Twitter et les meilleurs tweets de "+xstr(B.name)+":"+xstr(B.club)+" "+xstr(B.country_league)
	context = RequestContext(request, {
        'BaseTweetos': BT,
		'liste_tweet':liste_tweet,
		'liste_tweet2':liste_tweet2,
		'liste_collegue':liste_collegue,
		'liste_parti':liste_parti,
		'liste_league':liste_league,
		'liste_clubs':liste_clubs,
		'sort':sort,
		'z':z,
		'title':title,
		'AA':AA,

	})
	return HttpResponse(template.render(context))

	