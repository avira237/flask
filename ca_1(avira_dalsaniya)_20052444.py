# -*- coding: utf-8 -*-
"""CA_1(Avira_Dalsaniya)_20052444.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D9ZAJeSzW_r87unf9pNLvJZaXpt-jbIN
"""

import requests
import json
import pandas as pd

url='https://www.jobs.ie/membersarea/api/recommendedjobs?count=20'

headers = {
  'Accept': '*/*' ,
   'Accept-Language': 'en-US,en;q=0.9',
   'Connection': 'keep-alive',
   'Cookie': 'VISITOR_ID=c2cfb9d447e4540ad36c7f169e2a3cf8; sc_vid=bb2628fb13cbc06ddc6c2be8c6dc5226; s_fid=456dc47bc47b932a-6b6970d270ce40d7; anonymousUserId=ff18d5e1-adcf-368b-4164-31037f2e3593; _fbp=fb.1.1726738173485.354831022723737359; _gcl_au=1.1.456229745.1726738174; _hjSessionUser_256105=eyJpZCI6IjYzOTQ4YTUxLTU0MmItNTQzZi1hZjJlLTdjOWQ2OTIzMTU1NCIsImNyZWF0ZWQiOjE3MjY3MzgxNzM2NDIsImV4aXN0aW5nIjp0cnVlfQ==; STEPSTONEV5LANG=en; JBM_COOKIE=; isMobile=0; SessionCookie=d8d853f8-9ff1-4762-914e-49e5ff59468b; SearchSession=SessionGuid=04f91145-586a-4be7-abae-f83fb8895da4&LogSource=JBE; listing_page__qualtrics=empty; SsaSessionCookie=6d97b5de-08d2-427b-bffd-71094660bed8; EntryUrl=/jobs/radisson-blu-royal-hotel?cmp=1; SearchResults="103360464,103545010,103544437,103542630,103542627,103542533,103542165,103542151,103542146,103542109,103541775,103541774,103386056,103386060,103535549,103384684,103384641,103386089"; _abck=06879274B45338847EBAA18816BD617D~0~YAAQJWJkX3bQcWiSAQAAFiXdngy/VWhlcWTQrOUnQd5asOTVDUdKaAlIdLxb/5ea0Ktp4MjSp5skCCsACBGbSwUpZpia7CJd5aLpT0Gt2nz946Ts3ciXeMtw2mq54quGmhBZKcG9aNzZSGYQvwvK2LXpLpOagz0l/SI+MjKUXTFDd0aoiUb/C2b+6m0WuIpRMq7td8wJwwFm22ngP6vgS3xMOZGcFYjXTbrWvNj3vJHxaPQQRfC3ZSIINjdmmsYmNpqFb7aV1fW1MNAX2I3FN5mpmS22b9aiLUb1/Zob4bA3cdEBTkor753hlcV5fdp185f+LslJczQ/+SpWNr+IVHSJnrlbLe3pqAk3XSqgRbV4AXJY/etLZ7vHdhmcgUokxyOb2axZS2dRi5MpAAEAiqeVXTTiQRKWLdOS1Tqj3jvsdI7Ig67exiljFmMYsLA+uLyEQfDB~-1~-1~-1; SoftLoginDiagnostics=MqYEI%2f100AQFWuMeGD%2bXFQKy63ys26xFi3OuPOw5szckTDHQRk9h1Abw003mq0jttNTFzConbwaJRjyiDA2XghR2ypjVuzyUOyyQvvnUgDnJERY1L%2b00qVGGBw4jB2sVprYlUhhsboczft7YquXp4ad1FxHpies5tRJg4UWcdXHHsQbctwCHmgqZPVBtrM2BOwL6lD2aBF%2f4MNGoLeTqFEXe4dTsZUM4CojMj%2flXSS%2fnpujd0ZDqMIk6lKRujlNg36Q%2bus5yX2K3D71WRgNeF9taiNKjkdV78CVB0vri2dSkw%2fu9DcxNaAe4eVuAtidj%2fKeQoYjF50KOkHfXEyiGG8BafcPK%2bdxTulOCGtkvRH1bMK0269WJtYKNGdV2mq4FRlhRMBCvzBwlwIoQG%2bB3paWgroDksta62iy903gEg6UfdfhYG65YUkUsOXadVliaLmmjs%2bREDqRzXxc5x7JvwA%3d%3d; TealiumCampaignPersist=R_EM_JaJob_JIE_ST_18102024_jobTitle; _clck=3dizcu%7C2%7Cfq4%7C0%7C1723; .AspNetCore.Antiforgery.wvKeFR1tGVk=CfDJ8BgOs-WGknxPrClPZMpaMM22Y1dhjiQzhuCm_pwIroIxq3LTed-hNVv7e_U3UlgFkylO7PzQgomU0aZC70_ZeKgaHE5aOPo4QzYJEPzWwEybuXN3vK4RLxgCPuMQdeEZZluokV5idGbwKYy4i1FWB1c; XSRF-RLAC-TOKEN=CfDJ8BgOs-WGknxPrClPZMpaMM3xDn0CV3pCz8LoMe007eGyFBEYdO1_9Ydx2DrohUsmaGssn4jtq-poH3rYSyywDlEwkiWXY72BW8AejfKBOPaR2g2AqBK7eG-paghnWfKVhsMk0SUoBIoFY64VOUlQNJs; JSAUTH=CfDJ8B0jTrFxNrBOst9pXI9dL_Wgi4xO8yDf7NUqSeVqEzQOgFVUSBZlVIKStRzADzC_TfoP0er9oT7HFeQg8EXiODJYdYwaJ1GflY4ej6E6_WUJSgMqXHM5fixCCspQUrb5UA9jIyCgfxBeAoDtkhIhJVMtOUQ4GEOde4nMttePaK6C8z4SWmF0BbVU_3VicjKiC5Rd8wpMmQuzIIyliboBI2UdxkYw60tu2u8UyXRjkTzGZnhjntFXKETnVhRKtPoBBbmbI84k97PSTW_4QWHOLDOqB2E9LfyQ1eoPrHCK3wul7prMfxOkEs-8l_ZNY2wXwxx6zeQEHStTkWWl9l1x7n7wXwSFnc2bHVzQHHDxK12anf13CA6rFDp_o5lkN8Kw7qJ92TcFt81_P9qBybakJY018M3fwxuVgI3-WN3UH1OcwGLO_xV0dNc0-5OTgD4v-oy7RhSFt71bDuAN05ONWjQ; SoftLoginCookie=QiUfUP1z5wWSqXvZkdLjGGY%2Bz4jSJHaN4%2BMzt2DX%2F1I4iRa9ebtqsHsBorUJbiXbzub6dpqvjTMpb2SK3HYJQuPpW1istH4NtgXDL%2BjX9XiSpHZroZGws0avoi2eNxJqRHPK%2B1vCI7G45msD9kHH37jPRTPvWUChWtgiTmLx%2BFgIhz1oXGjvKx4Igoz6jMqWcuDrHM4RjnlyZqZyWS%2FlrMi%2FH02jk%2B%2FGwst7DydtPgA%3D; GetAccountDetailsCacheClear=CLEAR; SoftLoginCA=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJTdGVwU3RvbmUgQ2FuZGlkYXRlIEF1dGgiLCJhdWQiOiIzMDIiLCJwdXJwIjoiU29mdExvZ2luIiwiY2lkIjoiZmI4NjYyZjctYWM1My00ZmUzLWEwNTktODRlMTY0ZTM1ZmI2IiwibGVnYWN5SWQiOiJkODlmMzlkOC0zYWQzLTRhMjUtYTlmYi1lMTc5NDhmNzE0ZmMiLCJuYmYiOjE3MjkyNDIxOTYsImV4cCI6MTczNzAxODE5NiwiaWF0IjoxNzI5MjQyMTk2fQ.ZRSmeSaaJFsqRqMjhByi-5O2ZgB6X71SMQ8ild6jg1P1AFaC6q8s7MWFebpq0Xvobd8AP2_vEHDkyFmc61pBAze2HWciw16RIlSvERxAd5rWNxSAFQQxNg6cshtVJeQMqZGjZUyesXtczevT1O_GiXk6mMHsJ5kUq5_MkzQh5Q3Zhrt-kUK6GmRFFrXvJPahV5NN0eZSJPMTXEv2MbaSeeI9cRFNUROwBfWI9whR4-zo5AchpQUK5bw4TxL7BvAnWVHo_-mo4HLpp3OnjSj__-B2Rkjs8zYSr4xaRaO_WHYd6DEUG3MRaUA63ILEolsb_p3dnvxz2hDd0dmF6xPlFRi-vnlMLrAheoADeZoVs-wj81Cxqb54s_pYBYG3yJafxIAZG_Fj759tMr3IDgkii8BXmfgcyqcrXRQUnCIbgBKL1EBSkni4Oz6tR_FGe4HzE25H_8nIOQ9r1iNhnqSdJ8Oss66mhdW4AI8EcKE-7c1LjV4Av77teNd9jvAOWTSanY1_lHEpIE4GM5d-Qb01kXvIZ8YLpJq3PLxvIRSk8aCpIH2BRfRpeScdjoy26fKjiFL0469ua_di4JsAFqssCytPihg64LoVhfD6GEIdjfWk5yKGTapZy7lmBXrIePsNUNIabcal5bidwI1tPeG31Dk1INNCJCJI7sThqO5_5nQ; AuthCARefresh=6a18d100-ee70-4e10-a7bb-a5a2d80e55d7; AnonymousUser=MemberId=d89f39d8-3ad3-4a25-a9fb-e17948f714fc&IsAnonymous=False; s_ppvl=404%2520Error%2520Page%2C96%2C96%2C744%2C804%2C744%2C1536%2C864%2C1.25%2CP; s_ppv=404%2520Error%2520Page%2C90%2C90%2C744%2C804%2C744%2C1536%2C864%2C1.25%2CP; bm_sz=CAB69FB5B4DF5A0ED60C09797EB04B30~YAAQJWJkX/sJcmiSAQAAwD/knhmjrrtppxEm/xnKLWd3PcS3sE/UsLrr6cu4VfXyPuoSeCYGY7Wh54Bupj/NU05aRLxSnLKXVDfRS/9GZEhJa/hCDAs0SaS/JGsUDcAEcAVYamAWXWaI3dL2W61HDFCg1KpRolKTJFIz5GDxsaruVfgt8kFBFwuD5L40pSYbIjGCGQ0DGiRRUN2ODRXQ15O6J0BQ5GdMYkFlK+2knhieFtEXf48b1PFz1G3lvDrE/4QvyOvIZJfsCj5IdBXXryKtIchRPvG8bItvYi+26HKbiON3GMtnYddeeHfbbHvrhQhTwDRwJw2p0ezJAs8UUts+Ncx1U/OrlvC2Osup41WbMzQLFir1TknSqLMkR54nFjOcnGCM7ypI9u650vqV0u4q9Oz9hsgA3G8XyFf151HnDhwiS7/FfHxb04dVutwd0xWs1QqM/IYpDswaQ2GnFjUVegeLVaa/9N2defy2RdkjiSA2d8CgLTCkaIfxv618/RorJg==~3225904~3293493; AuthCA=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJTdGVwU3RvbmUgQ2FuZGlkYXRlIEF1dGgiLCJhdWQiOiIzMDIiLCJwdXJwIjoiQXV0aCIsImNpZCI6ImZiODY2MmY3LWFjNTMtNGZlMy1hMDU5LTg0ZTE2NGUzNWZiNiIsImxlZ2FjeUlkIjoiZDg5ZjM5ZDgtM2FkMy00YTI1LWE5ZmItZTE3OTQ4ZjcxNGZjIiwianRpIjoiZTM5MDQwYTYtMjNkMi00MDJlLWEzZDAtZWNhYjI5N2U4ZGExIiwibmJmIjoxNzI5MjUyOTU2LCJleHAiOjE3MjkyNTM4NTYsImlhdCI6MTcyOTI1Mjk1Nn0.j05VYdC_FfWJVINBX5E4qYr2qLrX8dIo_-0YNSXc-CXMSYID-DDbXMUYz89GRRQxN3whdQqKYhdRDcxPXy9E0c04LSKT7cJ3jTKgluBLoZLGrJJJ5MwNyhE1UJxhWGaYHLdqW479Sof1wYUnfhwAkhWvwsXFpHUAUSLOhmbrUDbu6mvCwQvGRzWrOsjQNgjHSa0Q9Ca9n4POMo7bcwvPi49Zz1vHyj9tnyWLJp2ST3t7tr3H9zzGH_Wz0tTw13JkTtyXJcwOnLU2bIVgpv5A1TS1As-Yh70YfURbTLxasrzBkXiewNBSS_yVZXUKa27pTkjPqRmtFxJLWlAlmGemtEN97o5_MI9t6kiEJil4Wcehm_gN72PJaI98D3kcB71mJmXEaHY4TMqzt4G93uz15LOnRQx_xzdb2gM8AASXhDI0chuJuk-WbASsjJZaREk_ZGlKw34Ja2EDMeY8XA8EifeaV-fJWuE5UkWqr-cbTJf9zhi1prmwY4nA3vVxjho1A-bhqUTaNA6UgGQcz5k7m9hf_bDZxU4P1cRoRGd5nZ7YJsxGro6jjwXTMP8pLAWxSwawaivvLbHGbjRBIj5PkpYxeYWkFO18tbqEWBvP8a0LBo86eMdGiC-eydOq4NukmUoXbV6O8pKh340jSvI3Y7AHlaovwhhhJJJU0r49rpA; ak_bmsc=C5C5DBB2243AD31732E662AD3333765A~000000000000000000000000000000~YAAQJWJkXxM3eWiSAQAAeCOCnxmbPymAJS6WFqsxjWoQdOMl8XKA34kuRGLUD3fH17XC2Rj52YPFzPX8BUwhw82I25Wr4ZBERoFtk4zLB30Li40z0msT1wsCBr+z4KzNZrfMvv31XJXAqRsWyqlsptE59R2QqVoZXX3bc67oS7kMHZsTRZT3HztDyDGLoZT9lHgEH/ugUCvP2xAplPSe7/fzBNMCrNbpI0aD/wVLiYcPu1tiCq948EJxxhlbxR74/LNsSZIbnnPI6f1IDvUb1rVsKZdsOPcmYUABwMN+DppD44IqRVPWz6/IrbikciUn9p516WpHBMtiiRzQ3aj/zCxwDJCEaTSbfBPSmGKcBt6AnnQ1O0sJ34f/uZvcO9z9WpygkxhNCa/1ApUwWcqSQ8gtUX9qHdAKkPjLw1Kyn968B5wSC5MIItC0xhufFpo=; CONSENTMGR=c1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:0%7Cc6:1%7Cc7:1%7Cc8:0%7Cc9:1%7Cc10:0%7Cc11:0%7Cc12:1%7Cc13:1%7Cc14:0%7Cc15:0%7Cts:1729252960604%7Cconsent:true; utag_main=v_id:0192099d81b7001ec792de1c4bd90506f001406700978$_sn:12$_se:2$_ss:0$_st:1729254760605$dc_visit:12$ses_id:1729252960266%3Bexp-session$_pn:1%3Bexp-session$PersistedClusterId:JE-OTHER-9999%3Bexp-session$PersistedFreshUserValue:0.1%3Bexp-session$prev_p:%3Bexp-session$dc_event:1%3Bexp-session$dc_region:eu-central-1%3Bexp-session; _uetsid=d469fc208b9b11ef9cf9c746f7764d5d; _uetvid=ae11ee60766911efa23c472f1829adaf; cto_bundle=9EVAOV9lQ3JkTm5oN3dpNjRKekVGdUpjY1cxT2VvNGl5OGRSViUyQiUyQmozbU12NFN1czZTVmU1dWIlMkJxS3pFY2hQSDRYQSUyRnRHNGhOcml3OU8xd0Z1WVBFVTdUYVpvZFJrWklXVlZDUDJCYTExeHpjZDkyMklnU1F2ZGRtcEhTWEhoV1hqMVJJZ0pxNzVXamFJQVdTdXlwUEN1dmhCUSUzRCUzRA; _hjSession_256105=eyJpZCI6Ijg4YzdiZmFiLTE2ZTUtNGM1ZS1hYTczLWYwNDQwYTM1NWQ5MCIsImMiOjE3MjkyNTI5NjEyMzEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _clsk=1itttm9%7C1729252961498%7C2%7C1%7Cq.clarity.ms%2Fcollect; _dd_s=rum=0&expire=1729253859513' ,
   'Sec-Fetch-Dest': 'empty',
   'Sec-Fetch-Mode': 'cors',
   'Sec-Fetch-Site': 'same-origin',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36' ,
   'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"' ,
   'sec-ch-ua-mobile': '?0' ,
   'sec-ch-ua-platform': '"Windows"'
};

r=requests.get(url,headers = headers)
r

r.content

j=json.loads(r.content)

j.keys()

df = pd.json_normalize(j['recommendedJobs'])
df

df.columns

df.rename(columns={
    'title': 'Job Title',
    'companyName': 'Company Name',
    'companyLogo':'Company Logo',
    'location': 'Location',
    'datePosted': 'Date Posted',
    'dateExpire': 'Expiry Date',
}, inplace=True)

df['Date Posted'] = pd.to_datetime(df['Date Posted']).dt.strftime('%Y-%m-%d %H:%M:%S')
df['Expiry Date'] = pd.to_datetime(df['Expiry Date']).dt.strftime('%Y-%m-%d %H:%M:%S')

df['Job Status'] = df['Expiry Date'].apply(lambda x: 'Open' if pd.to_datetime(x) > pd.Timestamp.now() else 'Closed')

def process_salary(salary):
    import re
    match = re.search(r"€([\d.,]+)", salary)  # Extract numeric value
    salary_amount = float(match.group(1).replace(",", "")) if match else 0
    salary_type = None
    if "per hour" in salary:
        salary_type = "Hourly"
    elif "per week" in salary:
        salary_type = "Weekly"
    elif "per month" in salary:
        salary_type = "Monthly"
    elif "per anum" in salary:
        salary_type = "Yearly"
    else:
        salary_type = "Not Disclosed"
    return salary_amount, salary_type

# Apply this function to your DataFrame
df["Salary Amount"], df["Pay Type"] = zip(*df["salary"].apply(process_salary))

df = df[['Job Title', 'Company Name', 'Company Logo','Location', 'Salary Amount','Pay Type', 'Date Posted', 'Expiry Date','Job Status']]
df

import sqlite3

connection = sqlite3.connect('jobData.db',check_same_thread=False)

cursor = connection.cursor()

df.to_sql('jobsData', connection, if_exists='append', index=False)

cursor.execute("SELECT * FROM jobsData")
rows = cursor.fetchall()



from flask import Flask, request, jsonify,render_template
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/get_jobs', methods=['GET'])
def getJobsData(): # Name of the method
  cursor.execute("SELECT * FROM jobsData")
  rows = cursor.fetchall()
  rows
  Results=[]
  for row in rows: #Format the Output Results and add to return string
    Result={}
    Result['Job_Title']=row[0]
    Result['Company_Name']=row[1]
    Result['Company_Logo']=row[2]
    Result['Location']=row[3]
    Result['Salary Amount']=row[4]
    Result['Pay Type']=row[5]
    Result['Date_Posted']=row[6]
    Result['Expiry_Date']=row[7]
    Result['Job Status']=row[8]
    Results.append(Result)
  response={'Results':Results, 'count':len(Results)}
  ret=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret #Return the data in a string format

@app.route("/job_add", methods=['GET', 'POST']) #Add Student
def job_add():
  if request.method == 'POST':
    Job_Title = request.form['Job_Title']
    Company_Name = request.form['Company_Name']
    Company_Logo = request.form['Company_Logo']
    Location = request.form['Location']
    Salary_Amount = request.form['Salary_Amount']
    Pay_Type= request.form['Pay_Type']
    Date_Posted=  request.form['Date_Posted']
    Expiry_Date=  request.form['Expiry_Date']

    # Determine job status
    today = datetime.now().date()
    date_posted = datetime.strptime(Date_Posted, '%Y-%m-%d').date()
    expiry_date = datetime.strptime(Expiry_Date, '%Y-%m-%d').date() if Expiry_Date else None
    if expiry_date and expiry_date < today:
      Job_Status = 'Closed'
    elif date_posted <= today:
      Job_Status = 'Open'
    else:
      Job_Status = 'Closed'  # Handle cases where posted date is in the future

    print(Job_Title, Company_Name, Company_Logo, Location, Salary_Amount, Pay_Type, Date_Posted, Expiry_Date, Job_Status)
    cur = mysql.cursor() #create a connection to the SQL instance
    s='''INSERT INTO jobsData(Job_Title,Company_Name,Company_Logo,Location,Salary_Amount,Pay_Type,Date_Posted,Expiry_Date,Job_Status) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}');'''.format(Job_Title,Company_Name,Company_Logo,Location,Salary_Amount,Pay_Type,Date_Posted,Expiry_Date,Job_Status)
    app.logger.info(s)
    cur.execute(s)
    mysql.commit()
  else:
    return render_template('job_add.html')

  return '{"Result":"Success"}'

  
@app.route('/')
def home():
    return "Test Flask is running!"

@app.route("/job.html") #Default - Show Data
def index(): # Name of the method
    return render_template('job.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080