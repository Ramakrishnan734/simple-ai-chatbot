from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import graph
from langchain_core.messages import HumanMessage
app=FastAPI()
class ChatRequest(BaseModel):
    message:str
    thread_id:str

@app.post("/chat")
async def chat(request :ChatRequest):
    config={"configurable":{"thread_id":request.thread_id}}
    result=await graph.ainvoke({'messages':[HumanMessage(content=request.message)]},config=config)
    return {"response":result['messages'][-1].content}






