from transformers import pipeline

# Gunakan pipeline text-generation untuk versi transformers terbaru
question_answerer = pipeline('text-generation', model='gpt2')

# Contoh penggunaan
result = question_answerer("What is Artificial Intelligence?", max_length=50)
print(result)