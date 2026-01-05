# from argostranslate import translate


# def translate_text(text: str) -> str:
#     from_lang = translate.get_language_from_code("hi")
#     to_lang = translate.get_language_from_code("en")
#     translation_model = from_lang.get_translation(to_lang)

#     if translation_model is None:
#         raise RuntimeError("Hindi → English translation model is not installed!")
#     return translate.translate(text, from_code="hi", to_code="en")

from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-hi-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_text(text):
    translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
    return tokenizer.decode(translated[0], skip_special_tokens=True)


