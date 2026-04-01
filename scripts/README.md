# Replay Attack Simulation

This script demonstrates a simple replay attack in a real-time client-server system.

## What it shows

- A legitimate message is accepted
- The same message is replayed
- The system incorrectly accepts it again

## Why this is a problem

Without protections such as:
- nonces
- timestamps validation
- session tokens

attackers can reuse valid messages to exploit the system.

## Mitigation

- Enforce strict timestamp validation
- Use nonces or unique request IDs
- Reject duplicate messages