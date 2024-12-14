# from langchain_text_splitters import RecursiveCharacterTextSplitter

# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=100,
#     chunk_overlap=100,
# )

# createDocuments = text_splitter.create_documents
# from utils.constants import VECTOR_DB_KEY
from utils.constants import VECTOR_DB_KEY
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from time import sleep


class PineConeService:
    """Pinecone service class to abstract pinecone methods

    Attributes:
    pinecone_instance: the pinecone interaction variable
    my_index: index key for the current session
    my_namespace: namespace for the current session
    index: index to handle handle crud

    Methods:
    __createPineconeIndex() -> None
    checkIndexStatus(str) -> boolean
    getPineconeInstance() -> PineconeGRPC
    embedText(list[str]) -> list
    upsert(list[str]) -> None
    search(str, int = 3) -> dict
    wipeData(str) -> None
    """

    def __init__(self):
        self.pinecone_instance = Pinecone(api_key=VECTOR_DB_KEY)
        self.my_index = "human-info-v1"
        self.my_namespace = "current-space"
        self.__createPineconeIndex()
        self.index = self.pinecone_instance.Index(self.my_index)

    def __createPineconeIndex(self):
        if not self.pinecone_instance.has_index(self.my_index):
            self.pinecone_instance.create_index(
                name=self.my_index,
                dimension=1024,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )

        while not self.checkIndexStatus("ready"):
            sleep(1)

    def checkIndexStatus(self, status: str):

        return self.pinecone_instance.describe_index(self.my_index).status[status]

    def getPineconeInstance(self):
        return self.pinecone_instance

    def embedText(self, items: list[dict]):
        embeddings = self.pinecone_instance.inference.embed(
            model="multilingual-e5-large",
            inputs=[i["text"] for i in items],
            parameters={"input_type": "passage", "truncate": "END"},
        )

        return embeddings

    def upsert(self, items: list[dict]):
        embeddings = self.embedText(items)
        records = []

        for item, embedding in zip(items, embeddings):
            records.append(
                {
                    "id": item["id"],
                    "values": embedding["values"],
                    "metadata": {"text": item["text"]},
                }
            )

        self.index.upsert(vectors=records, namespace=self.__class__.my_namespace)
        sleep(10)

    def search(self, query: str, count: int = 3):
        query_embedding = self.pinecone_instance.inference.embed(
            model="multilingual-e5-large",
            inputs=[query],
            parameters={
                "input_type": "query",
            },
        )[0]

        return self.index.query(
            namespace=self.__class__.my_namespace,
            vector=query_embedding.values,
            top_k=count,
            include_values=False,
            include_metadata=True,
        )

    def wipeData(self, index_name):
        self.pinecone_instance.delete_index(index_name)
