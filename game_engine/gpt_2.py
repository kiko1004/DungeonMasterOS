from transformers import pipeline

def initialize():
    generator = pipeline('text-generation', model = 'gpt2')
    return generator