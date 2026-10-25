from datetime import date, datetime, timedelta
from langchain.tools import tool
from data import users_data

@tool
def get_today_date() -> str:
    """Get today's date"""
    return date.today().strftime("%Y-%m-%d")

@tool
def get_user_purchase_history(user_id: str = None, user: str = None) -> dict:
    """Get the purchase history of a user"""
    uid = user_id or user
    if not uid:
        return {}
    return users_data.get(uid, {})

@tool
def calculate_right_refund(date_of_purchase: str = None, item_condition: str = None, user: str = None, items: list = None, **kwargs) -> dict:
    """Calculate the refund amount based on the date of purchase and item condition"""
    today = get_today_date.invoke({})
    # If called with user/items, compute for those items
    if user and items:
        uid = user
        history = users_data.get(uid, {})
        results = []
        total = 0
        for it in items:
            name = it.get("name") if isinstance(it, dict) else it
            if name not in history:
                results.append({"item": name, "eligible": False, "reason": "not purchased"})
                continue
            pdate = history[name].get("date")
            price = history[name].get("price", 0)
            try:
                purchase_date = datetime.strptime(pdate, "%Y-%m-%d")
                today_date = datetime.strptime(today, "%Y-%m-%d")
                days_diff = (today_date - purchase_date).days
            except Exception:
                days_diff = 1000
            if days_diff > 30 or days_diff < 0:
                results.append({"item": name, "eligible": False, "reason": "outside 30 days"})
                continue
            # default to like new if not specified
            results.append({"item": name, "eligible": True, "refund_amount": int(price * 0.8), "price": price})
            total += int(price * 0.8)
        return {"results": results, "total": total}
    # original behavior
    try:
        purchase_date = datetime.strptime(date_of_purchase, "%Y-%m-%d")
        today_date = datetime.strptime(today, "%Y-%m-%d")
        days_diff = (today_date - purchase_date).days
    except Exception:
        return {"eligible": False, "reason": "Invalid date", "amount": 0}
    if days_diff > 30 or days_diff < 0:
        return {"eligible": False, "reason": "Item purchased more than 30 days ago or in future", "amount": 0}
    if item_condition == "like new":
        return {"eligible": True, "refund_percentage": 80}
    elif item_condition == "damaged":
        return {"eligible": True, "refund_percentage": 100}
    elif item_condition == "used":
        return {"eligible": True, "refund_percentage": 70}
    else:
        return {"eligible": True, "refund_percentage": 80}  # default

@tool
def issue_refund_ticket(user_id: str = None, items: list = None, total_refund_amount: float = None, user: str = None, refund_amount: float = None, **kwargs) -> dict:
    """Issue a refund ticket for the user"""
    uid = user_id or user
    amount = total_refund_amount if total_refund_amount is not None else refund_amount
    ticket_number = "1234567890"
    return {
        "status": "success",
        "ticket_number": ticket_number,
        "message": f"Refund ticket issued for {uid} for items {items} with total amount {amount}"
    }
