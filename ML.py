# Use a pipeline as a high-level helper
from transformers import pipeline

def load_model():
    pipe = pipeline("translation", model="utrobinmv/t5_translate_en_ru_zh_base_200", device=-1)
    def model(lang:str, text:str):
        txt_for_translation = f"translate to {lang}: {text}"
        translated_text = pipe(txt_for_translation)[0]['translation_text']
        return translated_text
    return model

