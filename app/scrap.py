import requests, re, json , random , urllib
from re import match
from bs4 import BeautifulSoup, SoupStrainer
_session = requests.session()

def getStr(string,start,end, index = 1):
    str = string.split(start)
    str = str[index].split(end)
    return str[0]

def img(query):
    imagedata = []
    link = 'https://www.google.co.in/search?q={}&source=lnms&tbm=isch'.format(query)
    soup = requests.get(link)
    soup = BeautifulSoup(soup.content,"lxml")
    for clu in soup.findAll('img'):
        if 'textinput' not in clu['src']:
            imagedata.append(clu['src'])
    result = {
        'status':'200',
        'creator':'Asa Xyz',
        'result':imagedata
        }
    return(result)

def bmkg():
    dsa ="https://www.bmkg.go.id/"
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'id,en-US;q=0.7,en;qe=0.3',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers',
    }
    re = requests.get(dsa, headers=headers).text
    waktu = getStr(re, '<li><span class="waktu">', '</li>')
    magnitude = getStr(re, '<li><span class="ic magnitude"></span>', '</li>')
    kedalaman = getStr(re, '<li><span class="ic kedalaman"></span>', '</li>')
    kordinat = getStr(re, '<li><span class="ic koordinat"></span>', '</li>')
    lokasi = getStr(re, '<li><span class="ic lokasi"></span>', '</li>')
    img = getStr(re, '<img class="img-responsive" src="', '"')
    himbau = ["Hati-hati terhadap gempabumi yang akan terjadi selanjutnya","Buat warga sekitar di mohon untuk tetap waspada","Waspada gempabumi susulan yang mungkin saja terjadi","Warga sekitar di mohon untuk tidak panik dan tetap memantau kondisi yang akan mungkin terjadi"]
    himbauan = random.choice(himbau)
    diras = ["Gempabumi dirasakan","Gempabumi Tidak dirasakan"]
    dirasakan = random.choice(diras)
    result = {
        "status":"200",
        "creator":"Asa Xyz",
        "result": {
            "lokasi": lokasi,
            "waktu": waktu,
            "magnitude": magnitude,
            "kordinat": kordinat,
            "kedalaman": kedalaman,
            "subjek": dirasakan,
            "img": img,
            "himbauan": himbauan
        }
    }
    return(result)

def artinama(nama):
    dsa ="http://primbon.com/arti_nama.php?nama1={}&proses=+Submit%21+".format(nama)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'id,en-US;q=0.7,en;q=0.3',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers',
    }
    response = requests.get(dsa, headers=headers).text
    anu = getStr(response, '<b>ARTI NAMA</b><br><br>', '<TABLE>')
    st=str(anu).replace("<b><i>",": ").replace("</i></b>","").replace("<br><br>","").replace(".<br><br>","").replace("memiliki arti:","\nArti :")
    ret = "%s"%(st)
    result = {
        "status":"200",
        "creator":"Asa Xyz",
        "result": {
            "arti_nama": ret
        }
    }
    return(result)

def cctv(code):
    headerss = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    uye = "http://lewatmana.com/cam/{}/bundaran-hi/".format(str(code))
    r = requests.get(uye, headers=headerss)
    soup = BeautifulSoup(r.text, 'html5lib')
    soup2 = BeautifulSoup(r.content, 'lxml', parse_only=SoupStrainer('div', {'class':'panel-body'}))
    title = soup2.find('h1').get_text()
    location = soup2.find_all('p')[0].find_all('a')[1].get_text()
    video = soup.find('source')['src']
    desc = soup2.find_all('p')[1].get_text()
    result = {
        "status":"200",
        "creator":"Asa Xyz",
        "result": {
            "title": title,
            "description": desc,
            "link_video": video,
            "location": location
        }
    }
    return(result)

def sifatnama(name):
    romnts = ["0%","1%","2%","3%","4%","5%","6%","9%","10%","11%","12%","13%","14%","15%","16%","17%","18%","19%","20%","21%","22%","23%","24%","25%","26%","27%","28%","29%","30%","31%","32%","33%","34%","35%","36%","37%","38%","39%","40%","41%","42%","43%","44%","45%","46%","47%","48%","49%","50%","51","52","53","54%","55%","56%","57%","58%","59%","60%","61%","62%","63%","64%","65%","66%","67%","68%","69%","70%","71%","72%","73%","74%","75%","76%","77%","78%","79%","80%","81%","82%","83%","84%","85%","86%","87%","88%","89%","90%","91%","92%","93%","94%","95%","96%","97%","98%","99%","100%"]
    romantis = random.choice(romnts)
    ngagn = ["0%","1%","2%","3%","4%","5%","6%","9%","10%","11%","12%","13%","14%","15%","16%","17%","18%","19%","20%","21%","22%","23%","24%","25%","26%","27%","28%","29%","30%","31%","32%","33%","34%","35%","36%","37%","38%","39%","40%","41%","42%","43%","44%","45%","46%","47%","48%","49%","50%","51","52","53","54%","55%","56%","57%","58%","59%","60%","61%","62%","63%","64%","65%","66%","67%","68%","69%","70%","71%","72%","73%","74%","75%","76%","77%","78%","79%","80%","81%","82%","83%","84%","85%","86%","87%","88%","89%","90%","91%","92%","93%","94%","95%","96%","97%","98%","99%","100%"]
    ngangenin = random.choice(ngagn)
    msm = ["0%","1%","2%","3%","4%","5%","6%","9%","10%","11%","12%","13%","14%","15%","16%","17%","18%","19%","20%","21%","22%","23%","24%","25%","26%","27%","28%","29%","30%","31%","32%","33%","34%","35%","36%","37%","38%","39%","40%","41%","42%","43%","44%","45%","46%","47%","48%","49%","50%","51","52","53","54%","55%","56%","57%","58%","59%","60%","61%","62%","63%","64%","65%","66%","67%","68%","69%","70%","71%","72%","73%","74%","75%","76%","77%","78%","79%","80%","81%","82%","83%","84%","85%","86%","87%","88%","89%","90%","91%","92%","93%","94%","95%","96%","97%","98%","99%","100%"]
    msum = random.choice(msm)
    mris = ["0%","1%","2%","3%","4%","5%","6%","9%","10%","11%","12%","13%","14%","15%","16%","17%","18%","19%","20%","21%","22%","23%","24%","25%","26%","27%","28%","29%","30%","31%","32%","33%","34%","35%","36%","37%","38%","39%","40%","41%","42%","43%","44%","45%","46%","47%","48%","49%","50%","51","52","53","54%","55%","56%","57%","58%","59%","60%","61%","62%","63%","64%","65%","66%","67%","68%","69%","70%","71%","72%","73%","74%","75%","76%","77%","78%","79%","80%","81%","82%","83%","84%","85%","86%","87%","88%","89%","90%","91%","92%","93%","94%","95%","96%","97%","98%","99%","100%"]
    miris = random.choice(mris)
    tlus = ["0%","1%","2%","3%","4%","5%","6%","9%","10%","11%","12%","13%","14%","15%","16%","17%","18%","19%","20%","21%","22%","23%","24%","25%","26%","27%","28%","29%","30%","31%","32%","33%","34%","35%","36%","37%","38%","39%","40%","41%","42%","43%","44%","45%","46%","47%","48%","49%","50%","51","52","53","54%","55%","56%","57%","58%","59%","60%","61%","62%","63%","64%","65%","66%","67%","68%","69%","70%","71%","72%","73%","74%","75%","76%","77%","78%","79%","80%","81%","82%","83%","84%","85%","86%","87%","88%","89%","90%","91%","92%","93%","94%","95%","96%","97%","98%","99%","100%"]
    tulus = random.choice(tlus)
    lyal = ["0%","1%","2%","3%","4%","5%","6%","9%","10%","11%","12%","13%","14%","15%","16%","17%","18%","19%","20%","21%","22%","23%","24%","25%","26%","27%","28%","29%","30%","31%","32%","33%","34%","35%","36%","37%","38%","39%","40%","41%","42%","43%","44%","45%","46%","47%","48%","49%","50%","51","52","53","54%","55%","56%","57%","58%","59%","60%","61%","62%","63%","64%","65%","66%","67%","68%","69%","70%","71%","72%","73%","74%","75%","76%","77%","78%","79%","80%","81%","82%","83%","84%","85%","86%","87%","88%","89%","90%","91%","92%","93%","94%","95%","96%","97%","98%","99%","100%"]
    loyal = random.choice(lyal)
    sold = ["0%","1%","2%","3%","4%","5%","6%","9%","10%","11%","12%","13%","14%","15%","16%","17%","18%","19%","20%","21%","22%","23%","24%","25%","26%","27%","28%","29%","30%","31%","32%","33%","34%","35%","36%","37%","38%","39%","40%","41%","42%","43%","44%","45%","46%","47%","48%","49%","50%","51","52","53","54%","55%","56%","57%","58%","59%","60%","61%","62%","63%","64%","65%","66%","67%","68%","69%","70%","71%","72%","73%","74%","75%","76%","77%","78%","79%","80%","81%","82%","83%","84%","85%","86%","87%","88%","89%","90%","91%","92%","93%","94%","95%","96%","97%","98%","99%","100%"]
    solid = random.choice(sold)
    stia = ["0%","1%","2%","3%","4%","5%","6%","9%","10%","11%","12%","13%","14%","15%","16%","17%","18%","19%","20%","21%","22%","23%","24%","25%","26%","27%","28%","29%","30%","31%","32%","33%","34%","35%","36%","37%","38%","39%","40%","41%","42%","43%","44%","45%","46%","47%","48%","49%","50%","51","52","53","54%","55%","56%","57%","58%","59%","60%","61%","62%","63%","64%","65%","66%","67%","68%","69%","70%","71%","72%","73%","74%","75%","76%","77%","78%","79%","80%","81%","82%","83%","84%","85%","86%","87%","88%","89%","90%","91%","92%","93%","94%","95%","96%","97%","98%","99%","100%"]
    setia = random.choice(stia)
    result = {
        "status":"200",
        "creator":"Asa Xyz",
        "result": {
            "romantis": romantis,
            "ngangenin": ngangenin,
            "mesum": msum,
            "miris": miris,
            "tulus": tulus,
            "loyal": loyal,
            "solid": solid,
            "setia": setia
        }
    }
    return(result)

def quotes():
    r = requests.get("http://apitrojans.herokuapp.com/quotes")
    data=r.text
    data=json.loads(data)
    quotes = data["result"]["quotes"]
    result = {
        "status":"200",
        "creator":"Asa Xyz",
        "result": quotes
    }
    return(result)

def instaprofile(user):
    r = requests.get("http://apitrojans.herokuapp.com/instagram/user?username={}".format(str(user)))
    data=r.text
    data=json.loads(data)
    username = data["result"]["username"]
    name = data["result"]["fullname"]
    picture = data["result"]["profile_img"]
    biography = data["result"]["bio"]
    followers = data["result"]["followers"]
    following = data["result"]["following"]
    private = data["result"]["private"]
    media = data["result"]["media"]
    biography_link = data["result"]["external_url"]
    result = {
        "status":"200",
        "creator":"Asa Xyz",
        "result": {
            "username": username,
            "fullname": name,
            "profile_img": picture,
            "bio": biography,
            "bio_link":biography_link,
            "followers": followers,
            "following": following,
            "media": media,
            "private": private
        }
    }
    return(result)
