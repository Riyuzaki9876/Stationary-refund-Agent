from models import model
from tools import calculate_right_refund, get_today_date
from tools import issue_refund_ticket, get_user_purchase_history
from dotenv import load_dotenv
from langchain.agents import create_agent
from prompts import agent_system_prompt
from objects import Answer
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage
from uuid import uuid4
import json

load_dotenv()

agent = create_agent(
    model=model,
    system_prompt=agent_system_prompt,
    tools=[calculate_right_refund, get_user_purchase_history, issue_refund_ticket, get_today_date],
    response_format=Answer,
    checkpointer=InMemorySaver()
)


def run_conversation():
    config = {"configurable": {"thread_id": str(uuid4())}}

    text = "I would like to request a refund"
    print(text)

    question = HumanMessage(content=text)
    conversation = True

    while conversation:
        response = agent.invoke({"messages": question}, config=config)
        structured_response = response.get("structured_response")
        if structured_response is None and response.get("messages"):
            try:
                content = response["messages"][-1].content
                if isinstance(content, str) and content.strip().startswith("{"):
                    data = json.loads(content)
                    try:
                        structured_response = Answer(**data)
                    except Exception:
                        class Dummy:
                            pass
                        d = Dummy()
                        d.answer = data.get("answer", content)
                        d.conversation = data.get("conversation", False)
                        structured_response = d
            except Exception:
                pass
        if structured_response is None:
            break
        print(getattr(structured_response, "answer", ""))
        conversation = getattr(structured_response, "conversation", False)
        if conversation:
            user_input = input("reply: \n")
            question = HumanMessage(content=user_input)

    print("the job is done!")


if __name__ == "__main__":
    run_conversation()
