from transformers import pipeline

generator = pipeline("text-generation")
result = generator("In this course, we will teach you how to", max_new_tokens=500)
print(result)