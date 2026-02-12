import argparse
import json
from redteam.simulations.ssh_bruteforce import simulate_ssh_bruteforce


def main():
    parser = argparse.ArgumentParser(description="Red Team Attack Simulator")

    subparsers = parser.add_subparsers(dest="command")

    # SSH Brute Force command
    ssh_parser = subparsers.add_parser(
        "ssh-bruteforce", help="Simulate SSH brute force attack"
    )
    ssh_parser.add_argument("--user", required=True, help="Target username")
    ssh_parser.add_argument(
        "--attempts", type=int, required=True, help="Number of login attempts"
    )
    ssh_parser.add_argument(
        "--threshold", type=int, default=5, help="Detection threshold (default: 5)"
    )
    ssh_parser.add_argument(
        "--json", action="store_true", help="Output results in JSON format"
    )

    args = parser.parse_args()

    if args.command == "ssh-bruteforce":
        result = simulate_ssh_bruteforce(
            username=args.user, attempts=args.attempts, threshold=args.threshold
        )

        # Enrich result with metadata
        output = {
            "technique": "SSH Brute Force",
            "mitre_id": "T1110",
            "username": args.user,
            "attempts": args.attempts,
            "threshold": args.threshold,
            "detected": result["success"],
        }

        if args.json:
            print(json.dumps(output, indent=4))
        else:
            print("\n=== SSH Brute Force Simulation ===")
            print(f"Target user: {output['username']}")
            print(f"Attempts: {output['attempts']}")
            print(f"Threshold: {output['threshold']}")
            print(f"MITRE ATT&CK: {output['mitre_id']}")

            if output["detected"]:
                print("Status: DETECTED")
            else:
                print("Status: Not detected")

            print("==================================\n")


if __name__ == "__main__":
    main()
