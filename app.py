import pinecone
from pinecone import ServerlessSpec

import pinecone



from pinecone import Pinecone, ServerlessSpec

# 使用环境变量中的API密钥创建Pinecone实例
pc = Pinecone(
  api_key=""
#   environment="northamerica-northeast1-gcp"
)
cloud = 'PINECONE_CLOUD'
spec = ServerlessSpec(cloud='aws', region='us-west-2')

index_name = "indexmybbb"
if index_name not in pc.list_indexes().names():
    pc.create_index(
            index_name,
            dimension=1536,  # dimensionality of text-embedding-ada-002
            metric='cosine',
            spec=spec
    )

# connect to index
index = pc.Index(index_name)
# view index stats
print(index.describe_index_stats())