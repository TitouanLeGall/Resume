import openai

# Remplace par ta clé API personnelle
openai.api_key = "sk-..."

def summarize(text):
    prompt = f"Résume ce texte en quelques phrases simples :\n{text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # ou "gpt-4" si tu y as accès
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.5,
    )
    
    return response['choices'][0]['message']['content']

# Exemple d'utilisation
if __name__ == "__main__":
    texte_long = """
    L'intelligence artificielle est un domaine en pleine croissance qui touche à la fois la santé, l'éducation, l'industrie et bien d'autres secteurs. 
    Les modèles de langage, comme ChatGPT, sont capables de générer des textes cohérents, de répondre à des questions complexes et d'assister les humains dans de nombreuses tâches.
    """
    print("Résumé généré :\n", summarize(texte_long))
