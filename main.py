import openai
import sys
import os

###----------[ LOGIN APIKEY OPEN AI ]---------- ###
os.system("clear")
#fl=open("apikey.txt","r")
apikey="import openai
import sys
import os

###----------[ LOGIN APIKEY OPEN AI ]---------- ###
os.system("clear")


##===[Masukan apikey di sini]===##
apikey="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"
if(apikey==""):
  print("PLEASE ENTER YOUR API KEY")
  print("OPEN https://platform.openai.com/account/api-keys")
  print("TO GET YOUR API KEY")
else:
  openai.api_key = apikey
  print("----------------------")
  print("WELCOME TO OPENAI CHATBOT")
  print("MADE BY: FAUZI XD")
  print("FB : FAUZI")
  print("TEAM :Termux indonesia ")
  print("CTRL + C TO EXIT")
  print("script ini login menggunakan Apikey")
  print("-----------------------")
  while True:
    pertanyaan=input("[Masukan pertanyaan] ")
    if(not(pertanyaan=="")):
      print("LOADING...")
      respon=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
              {"role": "system", "content": pertanyaan}
          ]
      )
      print ("[Jawaban:⬇️] {}\n".format(respon['choices'][0]['message']['content']))
    else:
      print("[+] PLEASE ASK SOMETHIND DUDE")
if(apikey==""):
  print("PLEASE ENTER YOUR API KEY")
  print("OPEN https://platform.openai.com/account/api-keys")
  print("TO GET YOUR API KEY")
else:
  openai.api_key = apikey
  print("----------------------")
  print("WELCOME TO OPENAI CHATBOT")
  print("MADE BY: FAUZI XD")
  print("FB : FAUZI")
  print("TEAM :Termux indonesia ")
  print("CTRL + z TO STOP")
  print("-----------------------")
  while True:
    pertanyaan=input("[Masukan pertanyaan] ")
    if(not(pertanyaan=="")):
      print("LOADING...")
      respon=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
              {"role": "system", "content": pertanyaan}
          ]
      )
      print ("[Jawaban:⬇️] {}\n".format(respon['choices'][0]['message']['content']))
    else:
      print("[+] PLEASE ASK SOMETHIND DUDE")
