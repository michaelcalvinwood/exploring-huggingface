from transformers import pipeline

# classifier = pipeline("zero-shot-classification")
# result = classifier(
#     "This is a course about the Transformers library",
#     candidate_labels=["education", "politics", "business"],
# )

# classifier.save_pretrained('../models/')

saved_classifier = pipeline("zero-shot-classification", model='../models/')

result = saved_classifier(
    "The US Speaker of the House is a Republican.",
    candidate_labels=["education", "politics", "business"]
)

print(result)