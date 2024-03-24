from openai import OpenAI

# API Key ImpakTz
client = OpenAI(
    api_key = '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'
) #'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' # key2 

def repondre_a_une_question(question):
    reponse = client.chat.completions.create(
      model="gpt-3.5-turbo", # ou un autre modèle
      messages=[
          {
              "role":"user",
              "content":question
          }
      ]
      #temperature=0.7,
      #max_tokens=150
      #top_p=1.0,
      #frequency_penalty=0.0,
      #presence_penalty=0.0,
      #stop=["\n"]
    )
    return reponse.choices[0].message.content

def resumer_texte(texte):
    reponse = client.chat.completions.create(
      model="gpt-3.5-turbo", # ou un autre modèle
      messages=[
          {
              "role":"user",
              "content":"Explique/detaille/resume ce contenu en 100 mots : " + texte
          }
      ]
      #prompt=f"Résumez ce texte: {texte}",
      #temperature=0.7,
      #max_tokens=150,
      #top_p=1.0,
      #frequency_penalty=0.0,
      #presence_penalty=0.0,
      #stop=["\n"]
    )
    return reponse.choices[0].message.content

# Exemple d'utilisation
with open('pierre.txt', 'r', encoding='utf-8') as fichier:
    contenu = fichier.read()

print(contenu)
question = "Explique la blockchain ethereum"
resume = resumer_texte(contenu)
"""

reponse = repondre_a_une_question(question)

print("Résumé:", resume)
print("\n Réponse à la question:", reponse)
"""

while True:
    print()
    question = input("Pose une question : ")
    reponse = repondre_a_une_question(question)
    print("\n Réponse à la question:", reponse)
