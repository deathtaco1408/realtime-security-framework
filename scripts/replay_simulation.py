"""
Replay Attack Simulation

This script demonstrates a simple replay attack in a real-time client-server system.
It shows how reusing previously captured messages can bypass validation if protections
such as nonces or timestamps are not implemented.
"""

import time
import copy


class Server:
    def __init__(self):
        self.last_timestamp = 0

    def process_message(self, message):
        timestamp = message["timestamp"]
        action = message["action"]

        # Vulnerable logic: only checks timestamp is increasing
        if timestamp < self.last_timestamp:
            print("[!] Rejected: old message")
            return

        self.last_timestamp = timestamp
        print(f"[+] Accepted action: {action} at time {timestamp}")


def simulate_replay_attack():
    server = Server()

    # Legitimate message
    original_message = {
        "action": "move_forward",
        "timestamp": int(time.time())
    }

    print("Sending legitimate message...")
    server.process_message(original_message)

    # Simulate delay
    time.sleep(1)

    print("\nReplaying old message...")
    replayed_message = copy.deepcopy(original_message)

    # Replay attack: resend the same message
    server.process_message(replayed_message)


if __name__ == "__main__":
    simulate_replay_attack()