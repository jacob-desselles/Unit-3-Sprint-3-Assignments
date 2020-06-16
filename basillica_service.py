import basilica
with basilica.Connection('e48df2f4-43b8-4ba5-4557-487450c29edb') as c:
    embeddings = c.embed_sentences(["Hello world!", "How are you?"])
    print(list(embeddings)) # [[0.8556405305862427, ...], ...]