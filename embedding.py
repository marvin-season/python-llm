import chromadb
import ollama

embedding_model = 'mxbai-embed-large'
documents = [
    "在一个寒冷的冬天，赶集完回家的农夫在路边发现了一条冻僵了的蛇。他很可怜蛇，就把它放在怀里。当他身上的热气把蛇温暖以后，蛇很快苏醒了，露出了残忍的本性，给了农夫致命的伤害——咬了农夫一口。农夫临死之前说：“我竟然救了一条可怜的毒蛇，就应该受到这种报应啊！",
]

dbclient = chromadb.Client()
collection = dbclient.create_collection(name="docs")

ollama = ollama.Client(host="http://localhost:11434")

# store each document in a vector embedding database
for i, d in enumerate(documents):
    response = ollama.embeddings(
        model=embedding_model,
        prompt='Llamas are members of the camelid family',
    )
    embedding = response["embedding"]
    collection.add(ids=[str(i)], embeddings=[embedding], documents=[d])

# an example prompt
prompt = "农夫死前在想什么？"

# generate an embedding for the prompt and retrieve the most relevant doc
response = ollama.embeddings(
    prompt=prompt,
    model="mxbai-embed-large"
)
results = collection.query(
    query_embeddings=[response["embedding"]],
    n_results=1
)
data = results['documents'][0][0]

# generate a response combining the prompt and data we retrieved in step 2
output = ollama.generate(
    model="llama3.1",
    prompt=f"使用数据: {data}. 回复问题: {prompt}"
)

print(output['response'])
print(data)
