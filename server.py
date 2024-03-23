
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from openai import OpenAI

# API Key ImpakTz
client = OpenAI(
    api_key = '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'
)

def repondre_a_une_question(question,texte0):
    reponse = client.chat.completions.create(
      model="gpt-3.5-turbo", # ou un autre modèle
      messages=[
          {
              "role":"assistant",
              "content":texte0
          },
          {
              "role":"user",
              "content":"Reponds a cette question en 50 mots : "+question
          }
      ]
    )
    return reponse.choices[0].message.content

def resumer_texte(texte):
    reponse = client.chat.completions.create(
      model="gpt-3.5-turbo", # ou un autre modèle
      messages=[
          {
              "role":"user",
              "content":"Explique/detaille/resume ce contenu en 50 mots : " + texte
          }
      ]
    )
    return reponse.choices[0].message.content
"""
# Exemple d'utilisation
with open('pierre.txt', 'r', encoding='utf-8') as fichier:
    contenu = fichier.read()


print(contenu)
question = "Explique la blockchain ethereum"
resume = resumer_texte(contenu)


reponse = repondre_a_une_question(question)

print("Résumé:", resume)
print("\n Réponse à la question:", reponse)


while True:
    print()
    question = input("Pose une question : ")
    reponse = repondre_a_une_question(question)
    print("\n Réponse à la question:", reponse)
"""

app = Flask(__name__)

@app.route('/route1/')
def affichage_page1():
    contenu = request.args.get('texte', default="", type=str)
    #contenu="La belle au bois dormant"
    return resumer_texte(contenu)
    #return resumer_texte(contenu)

@app.route('/route2/')
def affichage_page2():
    contenu = request.args.get('texte', default="", type=str)
    contenu0 = request.args.get('texte0', default="", type=str)
    #contenu="La belle au bois dormant"
    return repondre_a_une_question(contenu,contenu0)