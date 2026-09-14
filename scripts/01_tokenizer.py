from transformers import AutoTokenizer

model_name = "Qwen/Qwen2.5-0.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)

text = "I want to learn how AI models work."

tokens = tokenizer.tokenize(text)
token_ids = tokenizer.encode(text)

print("Original text:")
print(text)

print("\nTokens:")
print(tokens)

print("\nToken IDs:")
print(token_ids)

print("\nNumber of tokens:")
print(len(token_ids))

print("\nDecoded back to text:")
print(tokenizer.decode(token_ids))