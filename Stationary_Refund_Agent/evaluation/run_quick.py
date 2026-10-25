import sys
from pathlib import Path
from uuid import uuid4

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "agent"))

from Agent import agent
from dataset import dataset
from model import eval_model

# Use mock to get answers
from langchain.messages import HumanMessage

results = []
for golden in dataset.goldens:
    try:
        response = agent.invoke(
            {"messages": [HumanMessage(content=golden.input)]},
            config={"configurable": {"thread_id": str(uuid4())}},
        )
        ans = response.get("structured_response")
        if ans is None and response.get("messages"):
            import json
            try:
                content = response["messages"][-1].content
                if isinstance(content, str) and content.strip().startswith("{"):
                    data = json.loads(content)
                    class D:
                        pass
                    d = D()
                    d.answer = data.get("answer")
                    d.conversation = data.get("conversation", False)
                    ans = d
            except Exception:
                pass
        actual = ans.answer if ans else ""
        # simple check
        ok = golden.expected_output.lower() in actual.lower() or actual.lower() in golden.expected_output.lower()
        results.append((golden.input[:30], ok, actual[:80]))
    except Exception as e:
        results.append((golden.input[:30], False, str(e)[:60]))

for r in results:
    print(r[0], r[1], r[2])
print(sum(1 for x in results if x[1]), "/", len(results))
