# Résumeur de texte avec OpenAI GPT

Un petit projet Python qui utilise l’API OpenAI pour générer automatiquement des résumés à partir de textes longs.

## Prérequis
- Python 3.x
- Une clé API OpenAI : [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)


### 💡 Variante (sans clé OpenAI)
Tu peux faire exactement la même chose avec l'API Hugging Face gratuite en modifiant l’appel `requests.post` vers un endpoint comme `https://api-inference.huggingface.co/models/facebook/bart-large-cnn` avec ton token HF.


