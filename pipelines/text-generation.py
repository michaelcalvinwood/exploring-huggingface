# Text Generation Models: https://huggingface.co/models?pipeline_tag=text-generation&sort=trending

from transformers import pipeline

generator = pipeline("text-generation")
result = generator("In this course, we will teach you how to", max_new_tokens=100)
print(result)

result = generator(
    "In this course, we will teach you how to",
    max_new_tokens=100,
    num_return_sequences=2,
)
print("\n\n", result)