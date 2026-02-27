from google import genai
import os


def get_car_ai_bio(model_year, brand, year):
    client = genai.Client(
        api_key=os.getenv('GOOGLE_API_KEY')
    )

    prompt = '''
        Gerar uma bio para um carro do modelo {}, da marca {} e do ano {}.
        Com no máximo 250 caracteres.
        Adicionar especificações técnicas, para venda do carro.
        Deixar somente a bio, sem nenhuma outra informação.
    '''
    prompt = prompt.format(model_year, brand, year)

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )

    return response.text
