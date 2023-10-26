from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("I've been waiting for a HuggingFace course my whole life.")
print(result)

sentences = [
    "I've been waiting for a HuggingFace course my whole life.",
    "I hate that movie."
]

result = classifier(sentences);
print(result)