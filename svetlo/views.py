# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse
import RPi.GPIO as GPIO
P0 = 12 # LED pin
P1 = 13 # LED pin
P2 = 11 # LED pin
#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(P0, GPIO.OUT)
GPIO.setup(P1, GPIO.OUT)
GPIO.setup(P2, GPIO.OUT)

def Klikni():
	GPIO.output(P0, not GPIO.LOW)
	pass
	
def zmena(request,gpio):
	i = int(gpio)
	GPIO.output(i, not GPIO.input(i))
	return HttpResponseRedirect('/')
	
def index(request):
	templates = 'index.html'
	promenne = {
	'PageName': "Kontrola",
	'Stav12': GPIO.input(12),
	'Stav13': GPIO.input(13),
	'Stav11': GPIO.input(11),
	}
	return render(request,templates, promenne)
	
def test(request):
	templates = 'new/index.html'
	promenne = {
	'PageName': "Dodak",
	}
	return render(request,templates, promenne)
