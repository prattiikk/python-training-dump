
FEES = {}


def _now_str():
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S")


def set_fee(sid, amount):
    if not sid or str(sid).strip() == "":
        raise ValueError("Student ID cannot be empty")

    try:
        amount = float(amount)
    except Exception:
        raise ValueError("Amount must be a number")

    if amount < 0:
        raise ValueError("Fee amount must be non-negative")

    FEES.setdefault(sid, {"fee_due": 0.0, "payments": []})
    FEES[sid]["fee_due"] = amount


def pay_fee(sid, amount):
    if not sid or str(sid).strip() == "":
        raise ValueError("Student ID cannot be empty")

    try:
        amount = float(amount)
    except Exception:
        raise ValueError("Amount must be a number")

    if amount <= 0:
        raise ValueError("Payment must be positive")

    FEES.setdefault(sid, {"fee_due": 0.0, "payments": []})
    FEES[sid]["payments"].append((_now_str(), amount))


def payments(sid):
    rec = FEES.get(sid, {"payments": []})
    return list(rec.get("payments", []))


def fee_due(sid):
    rec = FEES.get(sid, {"fee_due": 0.0})
    due = float(rec.get("fee_due", 0.0))
    paid = sum(a for _, a in payments(sid))
    bal = due - paid
    return bal if bal > 0 else 0.0

