def get_tier(total_spending: int):
    if total_spending < int(5e5):
        return ""
    if int(5e5) <= total_spending <= int(1e6) - 1:
        return "Bronze"
    if int(1e6) <= total_spending <= int(1.5e6) - 1:
        return "Silver"
    if int(1.5e6) <= total_spending <= int(2e6) - 1:
        return "Gold"
    return "Diamond"