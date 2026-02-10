import requests

# Türkçe'den İngilizce'ye çeviri fonksiyonu

def translate_turkish_to_english(text):
    url = 'https://api.translation-service.com/translate'
    payload = {'text': text, 'source': 'tr', 'target': 'en'}
    response = requests.post(url, json=payload)
    return response.json()['translatedText']

# Anime prompt oluşturma fonksiyonu

def generate_anime_prompt():
    prompts = [
        "Futuristic city with robots",
        "Magic school with wizards",
        "Post-apocalyptic world with survivors"
    ]
    return random.choice(prompts)  # Rastgele bir prompt seçiyoruz

# Stable Diffusion API ile resim üretme

def generate_image_with_replicate(prompt):
    url = 'https://api.replicate.com/v1/models/stability-ai/stable-diffusion/generate'
    headers = {'Authorization': f'Token YOUR_REPLICATE_API_TOKEN'}
    data = {'input': {'prompt': prompt}}
    response = requests.post(url, json=data, headers=headers)
    return response.json()['image_url']

# Örnek kullanım
if __name__ == '__main__':
    turkish_text = "Merhaba Dünya"
    english_text = translate_turkish_to_english(turkish_text)
    print(f'Translated: {english_text}')
    prompt = generate_anime_prompt()
    image_url = generate_image_with_replicate(prompt)
    print(f'Generated image URL: {image_url}')