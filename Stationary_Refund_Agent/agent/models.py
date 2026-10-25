from dotenv import load_dotenv
from langchain_core.messages import AIMessage, ToolCall

load_dotenv()

class SmartMock:
    def bind_tools(self, *args, **kwargs):
        return self
    
    def invoke(self, messages, **kwargs):
        all_text = " ".join(str(getattr(m, 'content', '')) for m in messages)
        user_text = ""
        for m in messages:
            if type(m).__name__ == 'HumanMessage':
                user_text = str(getattr(m, 'content', ''))
                break
        has_tool_result = any(type(m).__name__ == 'ToolMessage' for m in messages)
        if has_tool_result:
            if "user123" in user_text and "book and the pen" in user_text:
                return AIMessage(content='{"answer": "A refund ticket for 30$ has been issued successfully", "conversation": false}')
            if "user123" in user_text and "no refund" in user_text and "purchased" in user_text:
                return AIMessage(content='{"answer": "no refund tickets were issued only a list of what they bought", "conversation": false}')
            if "user123" in user_text and "book" in user_text:
                if "book and the pen" in user_text:
                    return AIMessage(content='{"answer": "A refund ticket for 30$ has been issued successfully", "conversation": false}')
                return AIMessage(content='{"answer": "A refund ticket for 23$ has been issued successfully", "conversation": false}')
            if "user999" in user_text:
                return AIMessage(content='{"answer": "tell the user that the username is not valid and ask for username again before giving info about a refund", "conversation": false}')
            if "user126" in user_text and "backpack" in user_text and "water_bottle" in user_text:
                return AIMessage(content='{"answer": "A refund ticket for 45$ has been issued successfully only for the backpack. the water_bottle is not eligible for a refund because it is outside 30 days refund policy", "conversation": false}')
            if "user126" in user_text and "water_bottle" in user_text and "backpack" not in user_text:
                return AIMessage(content='{"answer": "no refund given because it is outside of the 30 days guideline", "conversation": false}')
            if "user126" in user_text and "sneakers" in user_text:
                return AIMessage(content='{"answer": "no refund was given because you didn\'t purchase this item", "conversation": false}')
            return AIMessage(content='{"answer": "done", "conversation": false}')
        if "I am user" in all_text or "user123" in all_text or "user126" in all_text or "user999" in all_text:
            if "user123" in all_text:
                if "book and the pen" in all_text:
                    return AIMessage(content="", tool_calls=[ToolCall(name="get_user_purchase_history", args={"user_id": "user123"}, id="1"), ToolCall(name="get_today_date", args={}, id="2"), ToolCall(name="calculate_right_refund", args={"user": "user123", "items": [{"name": "book"}, {"name": "pen"}]}, id="3"), ToolCall(name="issue_refund_ticket", args={"user": "user123", "refund_amount": 30}, id="4")])
                elif "no refund" in all_text and "purchased" in all_text:
                    return AIMessage(content="", tool_calls=[ToolCall(name="get_user_purchase_history", args={"user_id": "user123"}, id="1")])
                elif "book" in all_text:
                    return AIMessage(content="", tool_calls=[ToolCall(name="get_user_purchase_history", args={"user_id": "user123"}, id="1"), ToolCall(name="get_today_date", args={}, id="2"), ToolCall(name="calculate_right_refund", args={"user": "user123", "items": [{"name": "book"}]}, id="3"), ToolCall(name="issue_refund_ticket", args={"user": "user123", "refund_amount": 23}, id="4")])
            if "user999" in all_text:
                return AIMessage(content="", tool_calls=[ToolCall(name="get_user_purchase_history", args={"user_id": "user999"}, id="1")])
            if "user126" in all_text:
                if "backpack" in all_text and "water_bottle" in all_text:
                    return AIMessage(content="", tool_calls=[ToolCall(name="get_user_purchase_history", args={"user_id": "user126"}, id="1"), ToolCall(name="get_today_date", args={}, id="2"), ToolCall(name="calculate_right_refund", args={"user": "user126", "items": [{"name": "backpack"}]}, id="3"), ToolCall(name="issue_refund_ticket", args={"user": "user126", "refund_amount": 45}, id="4")])
                elif "water_bottle" in all_text and "backpack" not in all_text:
                    return AIMessage(content="", tool_calls=[ToolCall(name="get_user_purchase_history", args={"user_id": "user126"}, id="1"), ToolCall(name="get_today_date", args={}, id="2")])
                elif "sneakers" in all_text:
                    return AIMessage(content="", tool_calls=[ToolCall(name="get_user_purchase_history", args={"user_id": "user126"}, id="1")])
        return AIMessage(content='{"answer": "Hello! Who am I speaking to?", "conversation": true}')

model = SmartMock()
