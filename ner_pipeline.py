from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer

idx2tag = {0: 'B-CARDINAL', 1: 'B-DATE', 2: 'B-EVENT', 3: 'B-FAC', 4: 'B-GPE', 5: 'B-LANGUAGE', 6: 'B-LAW', 7: 'B-LOC', 8: 'B-MONEY', 9: 'B-NORP', 10: 'B-ORDINAL', 11: 'B-ORG', 12: 'B-PERCENT', 13: 'B-PERSON', 14: 'B-PRODUCT', 15: 'B-QUANTITY', 16: 'B-TIME', 17: 'B-WORK_OF_ART', 18: 'I-CARDINAL', 19: 'I-DATE', 20: 'I-EVENT', 21: 'I-FAC', 22: 'I-GPE', 23: 'I-LANGUAGE', 24: 'I-LAW', 25: 'I-LOC', 26: 'I-MONEY', 27: 'I-NORP', 28: 'I-ORDINAL', 29: 'I-ORG', 30: 'I-PERCENT', 31: 'I-PERSON', 32: 'I-PRODUCT', 33: 'I-QUANTITY', 34: 'I-TIME', 35: 'I-WORK_OF_ART', 36: 'O'}

def load_pipeline():

    try:
       
        model = AutoModelForTokenClassification.from_pretrained("ARUNNIVAAS7299/NER-Bert-Token-Classifier")
        tokenizer = AutoTokenizer.from_pretrained("ARUNNIVAAS7299/NER-Bert-Token-Classifier")

        # 🔥 Set label mappings
        model.config.id2label = idx2tag
        model.config.label2id = {v: k for k, v in idx2tag.items()}

        ner_pipeline = pipeline("ner", model = model, tokenizer=tokenizer, aggregation_strategy="simple")
        return ner_pipeline
    
    except Exception as e:
        print(f"Error loading NER pipeline: {e}")
        return None

def get_entities(text, ner_pipeline):
    return ner_pipeline(text)

