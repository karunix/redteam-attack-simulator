def simulate_ssh_bruteforce(username: str, attempts: int, threshold: int):
    if attempts > threshold:
        return {
            "success": True,
            "username": username,
            "reason": "Brute force threshold exceeded",
        }

    return {"success": False, "username": username, "reason": "Threshold not exceeded"}
