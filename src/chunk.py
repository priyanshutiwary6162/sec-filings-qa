def chunk_text(text, size, overlap):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + size])
        start = start + size - overlap
    return chunks
filing = (
    "Apple Inc. designs, manufactures and markets smartphones, personal "
    "computers, tablets, wearables and accessories. The Company's fiscal "
    "year ends on the last Saturday of September. Net sales were driven "
    "by iPhone and Services. Risk factors include supply chain disruption, "
    "competition, and regulatory changes."
) 

print("Total characters:", len(filing))

chunks = chunk_text(filing, 60, 15)
for i in range(len(chunks)):
    print(f"Chunk {i} ({len(chunks[i])} chars): {chunks[i]}")
    