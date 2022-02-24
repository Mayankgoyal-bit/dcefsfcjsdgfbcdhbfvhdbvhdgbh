import logging
import json
from aiogram import *
import asyncio
import time
from aiogram.types import chat_permissions, inline_keyboard
import requests
from bs4 import BeautifulSoup
import random
import pymongo
from pymongo import MongoClient
import urllib.parse
from datetime import datetime, timedelta
import string

Admin = '@Naman1357'
BotName = 'Chegg unblur by MG'
mainGroupId = -1001715866580
adminGroupId = -1001179487467
logsGroupId = -1001664380876
adminId = 1703027575


botLink = "https://t.me/cheggcheapunblurbot"

# API_TOKEN = '1834750087:AAFfudHVQ5vb-ZyiJr0errhBmUWanleTpo8'
API_TOKEN = '5103490677:AAH0iBcFwIRK603JVSZp31M9UTWBUYzeB1A'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
client = Dispatcher(bot)


@client.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    print(message.chat.id)
    await message.reply(f"\n\n Hi!\n\n This is {BotName} \n\n want to buy premium contact {Admin} \n\n 4) /mydata to check your validity")



# @client.message_handler(commands=['price'])
# async def udata(message: types.Message):
#     price_message = "**PRICES AND PACKAGES LIST**\n\n=>285₹ or 4$ for 30days : Unlimited solutions.\n\n=>200₹ 0r 3$ for 15days : unlimited solutions\n\n=>100₹ or 2$ for 10days : unlimited solutions"
#     await message.reply(price_message)


# @client.message_handler(commands=['pay'])
# async def udata(message: types.Message):
#     price_message = "**HOW TO PAY?**\n\n**FOR INDIAN MEMBERS**\n\n1)Check Prices by using this command /price\n\n2)select your package and pay the money to this UPI Id : jaffa4321@apl\n\n3)After your payment completed send screen short to Owner {Admin}\n\nYour package will added as soon as owner sees the screenshort\n\nThat's it Thankyou."
#     await message.reply(price_message)


# @client.message_handler(commands=['tutorial'])
# async def udata(message: types.Message):
#     price_message = "**TUTORIAL**\n\nAfter Your payment completed check this video\n\n "
#     await message.reply(price_message)
all_genid = []






lock_permissions = {
    'can_send_messages': False,
    'can_send_media_messages': None,
    'can_send_polls': None,
    'can_send_other_messages': None,
    'can_add_web_page_previews': None,
    'can_change_info': None,
    'can_invite_users': None,
    'can_pin_messages': None
}
unlock_permissions = {
    'can_send_messages': True,
    'can_send_media_messages': None,
    'can_send_polls': None,
    'can_send_other_messages': None,
    'can_add_web_page_previews': None,
    'can_change_info': None,
    'can_invite_users': None,
    'can_pin_messages': None
}

s = requests.Session()

cookie_list = [{
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'cookie': 'optimizelyEndUserId=oeu1645456970243r0.5709479619316735; C=0; O=0; _pxvid=2fac09c8-932a-11ec-a43f-5a497a567757; usprivacy=1YNY; _omappvp=qwOiyMdEZJ1EiYtcXUntCUn5LKDwli15nVSDZ9csKrUwKtb0v54LUPjc4uUebr2aAf2SX8oXCoSXeZMwjZPXgy2YxG5J0dcm; __gads=ID=8d98b293e74de9d9:T=1645457018:S=ALNI_MZGlNMYsX_GlvZ-46AYU0wKcfNfBw; _ga=GA1.2.813661929.1645537045; _gid=GA1.2.1661930020.1645537045; _gcl_au=1.1.1389109368.1645537045; _cs_c=0; _fbp=fb.1.1645537046909.1733216053; _ym_d=1645537047; _ym_uid=1641914173296202124; DFID=web|P7zFqSxsOirICr7MJTAj; _vid_t=R6W3JBsNcOCN77ck6VKmQMAEI85zUG4hs0IjEIXwWBI6yGB7HOBwnFt15huWqi4dPtmeECROMkmFpA==; _rdt_uuid=1645537601809.c5db993b-574d-46f6-b541-f555f9896d7b; _scid=4b6c06ba-6c26-4dd6-a26a-4c7514f74b1c; _sctr=1|1645468200000; al_cell=2022-2-18-wt-main-1-control; sbm_country=IN; _pbjs_userid_consent_data=3524755945110770; _pubcid=910a09f8-559e-4670-9c5d-01368b11c4dd; _lr_env_src_ats=false; pbjs-unifiedid=%7B%22TDID%22%3A%22e3072ade-92b7-46e8-bb8d-cd699ac531b3%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-01-22T14%3A02%3A16%22%7D; AMZN-Token=v2FweHxzRFZJamRtc3NtQlB0WC9vampQS3BGVzUxSS8vOWpEVnFyTzNVaVN3REdMUXlzeW5LUmhsYkZUMldwOVV3b0crbFlyZjR5Yml1WCtrc3FrQ3RtQlloSm9wMnhjcUhaVFZhY3psQnFQbDNrNUl2Mmt4M3dMOGR6NUZCT0E9Ymt2AWJpdnggNzcrOVowenZ2NzBvNzcrOTc3Kzk3Nys5NzcrOVBRTVj/; V=9f2ac16cc40bef0d5295a4f56c018d9762163059624dd4.24537432; opt-user-profile=9f2ac16cc40bef0d5295a4f56c018d9762163059624dd4.24537432%252C21052020077%253A21048420088; CVID=59c885d0-4782-4561-b457-720b3ec902f5; user_geo_location=%7B%22country_iso_code%22%3A%22IN%22%2C%22country_name%22%3A%22India%22%2C%22region%22%3A%22RJ%22%2C%22region_full%22%3A%22Rajasthan%22%2C%22city_name%22%3A%22Jaipur%22%2C%22postal_code%22%3A%22302012%22%2C%22locale%22%3A%7B%22localeCode%22%3A%5B%22en-IN%22%2C%22hi-IN%22%2C%22gu-IN%22%2C%22kn-IN%22%2C%22kok-IN%22%2C%22mr-IN%22%2C%22sa-IN%22%2C%22ta-IN%22%2C%22te-IN%22%2C%22pa-IN%22%5D%7D%7D; CSID=1645621340510; local_fallback_mcid=73116808738836291513246531079322659782; s_ecid=MCMID|73116808738836291513246531079322659782; pxcts=dbf7da23-94a8-11ec-9f7f-41455473564a; exp=A803B%7CC026A; expkey=4A33044EB83FFE21EFDF1B1132A0DC3A; PHPSESSID=ka245ldq26kgl5kbnah5d9n5hg; CSessionID=36ad1535-f2d5-4175-b378-8f03cc427060; sbm_a_b_test=1-control; forterToken=6093569fde01495fb305f6a08e0cfdaa_1645621522396__UDF43-mnf_13ck; schoolapi=null; IR_gbd=chegg.com; _clck=1sfkio9|1|ez8|0; chgmfatoken=%5B%20%22account_sharing_mfa%22%20%3D%3E%201%2C%20%22user_uuid%22%20%3D%3E%20d52f538d-8c85-4d46-8642-aac3e004def9%2C%20%22created_date%22%20%3D%3E%202022-02-23T13%3A06%3A15.154Z%20%5D; id_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImJ1YnV1YXNpdWRhczY1NjVAb3V0bG9vay5jb20iLCJpc3MiOiJodWIuY2hlZ2cuY29tIiwic3ViIjoiZDUyZjUzOGQtOGM4NS00ZDQ2LTg2NDItYWFjM2UwMDRkZWY5IiwiYXVkIjoiQ0hHRyIsImlhdCI6MTY0NTYyMTYxNywiZXhwIjoxNjYxMTczNjE3LCJyZXBhY2tlcl9pZCI6ImFwdyJ9.6pKo7Tu2fgoekH-SDaKZBOommj0ox6bD5GaQsc_N1UYSdb9xpfeDV0dWIHO6TeJuEvDWSl2M1kwqxsgtb2LEuSz3pKZpMawVpEbxnfE9Yp0goUUCcz0gS_Tgbz9uAdrPtfCxf8Nc-4TgCRmKWBgX1DVweIxICCKmwIZyIOuYSVMhm-0C3IbkCsPyIEk4l0TpWiue6PU19j4qyHEMO4tHv_5nNygURNKvddZibX4TlOABeIS36T_MNko0RVH1uOdbErFwwwmXFgqhl_H3cugOSA_vMiJtP_WIVetjyLVJuD2di9VB7n59bmrAUT5GHJGHt5vvULCdol0AXnCCDPLzPw; SU=kqFAPsBisswSD4fnmI3wQ9T0DHmcV_fBE_AWcESY2v0xb7J36zx2arJdBHn7UZnVsHmiI3SH5eXep5ZGiBF3Kv_ubQbk0xC2Lb52oFjITDOQKCOaOBU8Vwv8B6AI9BjJ; U=4ffbc77edab1554a95a6fb97f744b5c5; chegganalytics=[{"eventName":"Sign In Success","eventValue":"Chegg","eventID":"event51","type":"auth","timeStamp":"2022-02-23T13:06:55.946Z"}]; _sdsat_authState=Hard%20Logged%20In; _sdsat_cheggUserUUID=d52f538d-8c85-4d46-8642-aac3e004def9; _pxff_tm=1; _pxff_rf=1; ab.storage.deviceId.b283d3f6-78a7-451c-8b93-d98cdb32f9f1=%7B%22g%22%3A%226f1477ed-63df-e55e-1b18-662f31968892%22%2C%22c%22%3A1641902010716%2C%22l%22%3A1645621625634%7D; ab.storage.userId.b283d3f6-78a7-451c-8b93-d98cdb32f9f1=%7B%22g%22%3A%22d52f538d-8c85-4d46-8642-aac3e004def9%22%2C%22c%22%3A1645621625621%2C%22l%22%3A1645621625637%7D; OptanonConsent=consentId=cdeafacd-1beb-4358-9ed7-3723605f7850&datestamp=Wed+Feb+23+2022+18%3A37%3A06+GMT%2B0530+(India+Standard+Time)&version=6.18.0&interactionCount=1&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=snc%3A1%2Cfnc%3A1%2Cprf%3A1%2CSPD_BG%3A1%2Ctrg%3A1&AwaitingReconsent=false; _px3=1a3832670e570af0715cdcadca6318145c5f32f3482df9c85ac471c052022ad7:KLpk81RZPEPrWy3g6AfhjfiOpK7+XkgvlsItW4Yk8g/d1gUQ8KZoYi9M+UH3QXFOSbottF/eAvsvtEBQV50HAQ==:1000:hyJUHIW7LFdqi7xlyVw1RRb/s0EyP8MT4kIjoXi4DMAg8nSqw8LdURqXIfcs4KypAnzj9YwJAhu44PpHMGe+RYmNDlrAvWGqXPhaZC7pS4p3dHGpni2T7m8pA/ZLJQ25lc2VLEJpM1yFKbPyzHte+TLj3MJ5kZA3TBvtt2hTfo/YrvKSb75JBYuPgeAd7+6au4QszxoLJmzd+vCxDXmhyA==; _px=KLpk81RZPEPrWy3g6AfhjfiOpK7+XkgvlsItW4Yk8g/d1gUQ8KZoYi9M+UH3QXFOSbottF/eAvsvtEBQV50HAQ==:1000:e4GmfrImFbXB2HCet/p4Je//mmr6nGoUQcyjZ0DcJ/pcWXdDo3HPRWofvDvuS4P7pEDZzHaqtoMJ4lk/BhnKUHevCYRMxH+XYuc9Z/XlS847iwJA74XGC7dBl/vSh5e5pmtxruJENXoIXTKIK1ELNA6fZkcXtZnpcmI4WYR2Aom9ei5NsVNiwprsp170WHpzxy7pytD5gUK2RbONEqXj5mo2bBcTlStf0BJWGKRoGTiD3f5wrobWILl+UHDy/NIzE6CsrKoraqCVHNTItvoT4g==; mcid=72141475282029839330538722462069057767; _tq_id.TV-8145726354-1.ad8a=a6cf34eff1a185ef.1645537047.0.1645621630..; IR_14422=1645621629589%7C0%7C1645621629589%7C%7C; _uetsid=91ef8b7093e411ec98b361ee54049bc2; _uetvid=1a79c48072d511ecaaebdb0eee95c6b7; ab.storage.sessionId.b283d3f6-78a7-451c-8b93-d98cdb32f9f1=%7B%22g%22%3A%2287cdf6df-b9f3-463e-a85e-9b2c047dee2b%22%2C%22e%22%3A1645623431504%2C%22c%22%3A1645621625630%2C%22l%22%3A1645621631504%7D; _gat=1; _cs_cvars=%7B%221%22%3A%5B%22Page%20Name%22%2C%22home%20page%22%5D%7D; _cs_id=f9ae0797-0783-a53b-89a6-fd7f25480b76.1645537052.2.1645621633.1645621633.1.1679701052346; _cs_s=1.0.0.1645623433995; _ym_isad=2; _clsk=1sxjkl8|1645621635994|2|0|k.clarity.ms/collect',
    'origin': 'https://www.chegg.com',
    'accept': 'application/json',
    'content-type': 'application/json',
    "cache-control": "max-age=0",
    "deviceFingerPrintId": "web|A0oUFYO50M5NYadliOz5"
}]


@client.message_handler(commands=['statues', 's'])
async def account_statues(message: types.Message):
    for i, item in enumerate(cookie_list):
        req = requests.get("https://www.chegg.com/homework-help/questions-and-answers/simulate-following-circuit-qucs-save-simulation-file-results-pdf-file-submit-e-learning-sh-q50117215?trackid=ef79e9639575&strackid=2b896ff805f6", headers=item)
        soup = BeautifulSoup(req.content, 'html.parser')
        qution = soup.find(
            "div", {"class": "ugc-base question-body-text"}, 'html.parser')
        answer = soup.find(
            "div", {"class": "answer-given-body ugc-base"}, 'html.parser')
        if answer == None:
            await message.reply(f"{i} account Notworking")
        else:
            await message.reply(f"{i} account is working")


def remove_tags(html):

    # parse html content
    soup = BeautifulSoup(html, "html.parser")

    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
    soup.find("h2", {"class": "guidance-header"}).decompose()
    soup.find("section", {"id": "general-guidance"}).decompose()
    soup.find("div", {"id": "select-view"}).decompose()
    # return data by retrieving the tag content
    return soup


@client.message_handler()
async def chegg(message: types.Message, amount=1):
        if "https://www.chegg.com" in message.text:
            print("getting")
            user = str(message.from_user.id)
             return
                c_headers = random.choice(cookie_list)
                try:
                    if 'https://www.chegg.com' in message.text:
                        await bot.set_chat_permissions(mainGroupId, permissions=lock_permissions)
                        # await bot.send_message(-1001468490071,f"@{message.from_user.username or message.from_user.first_name} ask me the solution now please wait until the below timer complets..")
                        try:
                            if "questions-and-answers" in message.text:
                                req = requests.get(
                                    message.text, headers=c_headers)
                                soup = BeautifulSoup(
                                    req.content, 'html.parser')
                                qution = soup.find(
                                    "div", {"class": "ugc-base question-body-text"}, 'html.parser')
                                answer = soup.find(
                                    "div", {"class": "answer-given-body ugc-base"}, 'html.parser')
                                answer_by = soup.find_all(
                                    "span", {"class": "answerer-name"}, 'html.parser')
                                for tag in soup.select(".answer-given-body.ugc-base img"):
                                    if 'd2vlcm61l7u1fs.cloudfront.net' in tag['src']:
                                        tag["src"] = "https:" + tag["src"]
                                aid = str(req.content).split(
                                    'answerId="')[1].split('" >')[0]
                                like_dislike = requests.post(
                                    'https://www.chegg.com/study/_ajax/contentfeedback/getreview?entityType=ANSWER&entityId=+{}'.format(aid), headers=c_headers)
                                like_soup = like_dislike.json()
                                l1 = (like_soup['review_count'])
                                l2 = (l1['result'])
                                if "0" in l2:
                                    like = (l2['0'])
                                    like_number = (like['count'])
                                else:
                                    like_number = 0
                                if "1" in l2:
                                    dislike = (l2['1'])
                                    dislike_number = (dislike['count'])
                                else:
                                    dislike_number = 0
                                main_html = '''
                                                            <!DOCTYPE html>
                                                            <html lang="en">
                                                            <head>
                                                                <meta charset="UTF-8" />
                                                                <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                                                                    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                                                                    <!-- CSS only -->
                                                                    <link
                                                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"
                                                                    rel="stylesheet"
                                                                    integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
                                                                    crossorigin="anonymous"
                                                                    />
                                                                    <title>Powered by Homework Hub server</title>
                                                                </head>
                                                                <style>
                                                                    .body {
                                                                    width: 100px;
                                                                    }
                                                                    .alert {
                                                                    text-align: center;
                                                                    }
                                                                    .qution_header{
                                                                    text-align: center;
                                                                    color: rgb(
                                                                        37, 70, 175);

                                                                    }
                                                                    img {

                                                                max-width: 100%;

                                                                }
                                                                .question{
                                                                    padding: 30px;
                                                                }
                                                                .answer{
                                                                    padding: 30px;
                                                                }
                                                                </style>
                                                                <body>
                                                                    <div class="alert alert-success" role="alert">
                                                                    Powered by Homework Hub server | | join for chegg answers : https://discord.gg/HfYBKVWM9y
                                                                    </div>
                                                                </body>
                                                                <body>
                                                                    <div class="alert alert-danger" role="alert">
                                                                    THIS ANSWER LINK WILL EXPIRE IN 10 MIN
                                                                    </div>
                                                                </body>
                                                                </html>
                                                                '''
                                like_dislike_html = '''
                                                                <section >
                                                                    <div class="container my-3 bg-light">
                                                                    <div class="col-md-12 text-center">
                                                                    <button type="button" class="btn btn-primary">
                                                                        likes <span class="badge bg-secondary">{}</span>
                                                                    </button>
                                                                    <button type="button" class="btn btn-primary">
                                                                        dislikes <span class="badge bg-danger">{}</span>
                                                                    </button>
                                                                    </div>
                                                                </div>
                                                                </section>
                                                                '''
                                answer_given = '''
                                                                <section>
                                                                    <div class="card text-center">
                                                                        <div class="card-header">
                                                                        ANSWER GIVEN BY
                                                                        </div>
                                                                        <div class="card-body">
                                                                        <h5 class="card-title">{}</h5>
                                                                        </div>
                                                                        <div class="card-footer text-muted">
                                                                        Powered by Homework Hub server
                                                                        </div>
                                                                    </div>
                                                                </section>
                                                                '''
                                qution_html = '''
                                                                <section>
                                                                <div class="container my-5">
                                                                    <div
                                                                    class="row p-4 pb-0 pe-lg-0 pt-lg-5 align-items-center rounded-3 border shadow-lg"
                                                                    >
                                                                    <h1 class="qution_header">QUESTION</h1>
                                                                    <div class="question">
                                                                        {}
                                                                    </div>
                                                                    </div>
                                                                    </div>
                                                                </div>
                                                                </section>
                                                                '''
                                answer_html = '''
                                                                <section>
                                                                <div class="container my-5">
                                                                    <div
                                                                    class="row p-4 pb-0 pe-lg-0 pt-lg-5 align-items-center rounded-3 border shadow-lg"
                                                                    >
                                                                    <h1 class="qution_header">ANSWER</h1>
                                                                    <div class="answer">
                                                                        {}
                                                                    </div>
                                                                    </div>
                                                                    </div>
                                                                </div>
                                                                </section>
                                                                '''
                                file = open('Answer.html', 'w',
                                            encoding='utf-8')
                                file.write(str(main_html))
                                file.write(
                                    str(answer_given).format(answer_by))
                                file.write(str(like_dislike_html).format(
                                    like_number, dislike_number))
                                file.write(str(qution_html).format(qution))
                                file.write(str(answer_html).format(answer))
                                file.close()
                                # try:
                                #     url = "https://siasky.net/skynet/skyfile"
                                #     link_files = [
                                #         ('file', ("Answer.html", open(
                                #             './Answer.html', 'rb'), 'text/html'))
                                #     ]
                                #     headers7 = {
                                #         'referrer': 'https://siasky.net/'
                                #     }
                                #     response = requests.request(
                                #         "POST", url, headers=headers7, files=link_files)
                                #     limb = "https://siasky.net/" + \
                                #         response.json()["skylink"]
                                #     keyboard = inline_keyboard.InlineKeyboardMarkup(
                                #         row_width=3)
                                #     button = inline_keyboard.InlineKeyboardButton(
                                #         'Answer', url=limb)
                                #     keyboard.add(button)
                                #     await message.reply(f"✅🟢✅🟢✅🟢✅🟢✅🟢✅🟢\n\n @{message.from_user.username or message.from_user.first_name} please click the below link and download \n\n ✅🟢✅🟢✅🟢✅🟢✅🟢✅🟢", reply_markup=keyboard)
                                # except Exception as e:
                                #     print(e)
                                #     doc = open('Answer.html', 'rb')
                                #     # try:
                                #     #   await bot.send_document(message.from_user.id, doc)
                                #     # except:
                                #     #   await bot.send_document(message.chat.id, doc)
                                #     # await message.reply('dont send another question immediately check @freejaffawarrior ')
                                #     await bot.send_document(message.chat.id, doc, caption=f"✅🟢✅🟢✅🟢✅🟢✅🟢✅🟢\n\n @{message.from_user.username or message.from_user.first_name} the above file is your answer please download \n\n ✅🟢✅🟢✅🟢✅🟢✅🟢✅🟢")
                                doc = open('Answer.html', 'rb')
                                # try:
                                #   await bot.send_document(message.from_user.id, doc)
                                # except:
                                #   await bot.send_document(message.chat.id, doc)
                                # await message.reply('dont send another question immediately check @freejaffawarrior ')
                                await bot.send_document(message.chat.id, doc, caption=f"✅🟢✅🟢✅🟢✅🟢✅🟢✅🟢\n\n @{message.from_user.username or message.from_user.first_name} the above file is your answer please download \n\nyour subscription expires on {Expdate}  \n\n✅🟢✅🟢✅🟢✅🟢✅🟢✅🟢")

                            wait_time = random.randint(60, 120)
                            #wait_time = 60
                            sent = await bot.send_message(message.chat.id, f'Ok.! i will take rest for \n ⏱ {wait_time} sec Uh..😴 ')
                            await asyncio.sleep(wait_time)
                            await bot.edit_message_text('Now i am ready.', message.chat.id, sent.message_id)
                            await bot.set_chat_permissions(mainGroupId, permissions=unlock_permissions)
                        except Exception as e:
                            print(e)
                            await bot.set_chat_permissions(mainGroupId, permissions=unlock_permissions)
                            # await message.reply('your qustion dont have answer or maybe you send a wrong qustion')
                            # await bot.send_message(-1001468490071,f"@{message.from_user.username or message.from_user.first_name}'s question dont have answer or send wrong question , Now another person can ask me solution")
                            await message.reply('🛑❌🛑❌🛑❌🛑❌🛑❌\n\nYour qustion dont have answer or maybe you send a wrong link\n\n🛑❌🛑❌🛑❌🛑❌🛑❌')

                    else:
                        pass
                except Exception as e:
                    print(e)
                    pass
        else:
            allow_ids = [-528128941, adminId, 1462786490]
            if message.from_user.id in allow_ids:
                return
            else:
                m = '''🛑❌🛑❌🛑❌🛑❌🛑❌\n\nplease send only chegg links here\n\n🛑❌🛑❌🛑❌🛑❌🛑❌'''
                send = await message.reply(m)
                await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                await bot.delete_message(chat_id=message.chat.id, message_id=send.message_id)
    else:
        m = '''🛑❌🛑❌🛑❌🛑❌🛑❌\n\nplease use premium  group for chegg answers.\n\nBut here you can check your validity using /mydata\n\nAnd you can redeem your token also here by /redeem <token>\n\n🛑❌🛑❌🛑❌🛑❌🛑❌'''
        await message.reply(m)


if __name__ == '__main__':
    executor.start_polling(client, skip_updates=True)
