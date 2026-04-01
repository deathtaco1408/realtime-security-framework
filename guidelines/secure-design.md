# Secure Design Guidelines for Real-Time Systems

## 1. Treat Clients as Untrusted
Clients operate in environments that can be modified or controlled by attackers. Never assume input is valid.

---

## 2. Enforce Server Authority
Critical application state should be validated and enforced by the server.

Avoid:
- trusting client-reported positions
- accepting client-side calculations without verification

---

## 3. Validate All Inputs
Apply validation to:
- RPC/API calls
- state updates
- user actions

Use:
- bounds checking
- sanity checks
- consistency validation

---

## 4. Protect Against Replay Attacks
Use:
- nonces
- timestamps
- session tokens

Reject duplicate or outdated messages.

---

## 5. Detect Invalid State Transitions
Ensure that:
- actions follow valid sequences
- impossible transitions are rejected

Example:
- moving from idle → attack → idle (valid)
- moving from idle → teleport → attack (invalid)

---

## 6. Monitor Suspicious Behavior
Track:
- repeated invalid inputs
- abnormal patterns
- excessive action rates

---

## Summary
Secure real-time systems require:
- strong trust boundaries
- strict input validation
- server-controlled logic