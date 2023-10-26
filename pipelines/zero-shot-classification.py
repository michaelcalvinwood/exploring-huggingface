# Available Models: https://huggingface.co/models?pipeline_tag=zero-shot-classification&sort=trending

from transformers import pipeline

classifier = pipeline("zero-shot-classification")
result = classifier(
    "This is a course about the Transformers library",
    candidate_labels=["education", "politics", "business"],
)

print(result)