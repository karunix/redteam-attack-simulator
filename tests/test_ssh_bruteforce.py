from redteam.simulations.ssh_bruteforce import simulate_ssh_bruteforce


def test_bruteforce_detected_when_threshold_exceeded():
    result = simulate_ssh_bruteforce(username="root", attempts=15, threshold=5)

    assert result["success"] is True
    assert "Brute force threshold exceeded" in result["reason"]


def test_bruteforce_not_triggered_when_under_threshold():
    result = simulate_ssh_bruteforce(username="admin", attempts=2, threshold=5)

    assert result["success"] is False
