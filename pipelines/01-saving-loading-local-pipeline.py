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

# Another Way to Load Saved Pipeline Models

# from transformers import pipeline, AutoModel, AutoTokenizer

# model = AutoModel.from_pretrained('/path/to/your/model')
# tokenizer = AutoTokenizer.from_pretrained('/path/to/your/tokenizer')

# pipe = pipeline(task='summarization',  # replace with whatever task you have
#                 model=model,
#                 tokenizer=tokenizer)