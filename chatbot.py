import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage

load_dotenv()

llm=ChatGroq(
    api_key=os.environ.get("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",
)
def chatbot_mode(state:MessagesState):
    response= llm.invoke(state['messages'])
    return{"messages":[response]}

builder=StateGraph(MessagesState)
builder.add_node("chatbot",chatbot_mode)
builder.add_edge(START,"chatbot")
builder.add_edge("chatbot",END)

memory=MemorySaver()
graph=builder.compile(checkpointer=memory)

print("Chatbot is ready to use : type 'end' to end the conversion \n ")
config={"configurable":{"thread_id":"session-1"}}
while True:
    user_input= input("You: ")
    if user_input.lower()=="end":
        print("goodbye")
        break
    result=graph.invoke({"messages":[HumanMessage(content=user_input)]},
                        config=config
                        )
    print(f"Bot : {result['messages'][-1].content}\n")