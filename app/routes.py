from app import app, scrap
from flask import render_template, send_file ,flash, url_for
from flask import request
from app.forms import LoginForm
import requests, re, json , random , urllib
from bs4 import BeautifulSoup, SoupStrainer
_session = requests.session()

@app.route('/')
@app.route('/index')
def home():
	return render_template('index.html',title='LESSON')
	
@app.route('/image',methods=['POST','GET'])
def rest_image():
	this_query = request.args['query']
	this_rest = scrap.img(this_query)
	return json.dumps(this_rest, indent=4)
	
@app.route('/instagram',methods=['POST','GET'])
def rest_insta():
	this_user = request.args['username']
	this_rest = scrap.instaprofile(this_user)
	return json.dumps(this_rest, indent=4)

@app.route('/sifatnama',methods=['POST','GET'])
def rest_sifat():
	this_name = request.args['name']
	this_rest = scrap.sifatnama(this_name)
	return json.dumps(this_rest, indent=4)

@app.route('/cctv',methods=['POST','GET'])
def rest_cctv():
	this_code = request.args['code']
	this_rest = scrap.cctv(this_code)
	return json.dumps(this_rest, indent=4)

@app.route('/artinama',methods=['POST','GET'])
def rest_artinamax():
	this_nama = request.args['nama']
	this_rest = scrap.artinama(this_nama)
	return json.dumps(this_rest, indent=4)

@app.route('/bmkg',methods=['POST','GET'])
def rest_bmkgs():
	this_rest = scrap.bmkg()
	return json.dumps(this_rest, indent=4)

@app.route('/quotes',methods=['POST','GET'])
def rest_quotess():
	this_rest = scrap.quotes()
	return json.dumps(this_rest, indent=4)
