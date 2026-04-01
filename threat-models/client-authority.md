# Client-Authoritative State Vulnerability

## Description
In client-authoritative systems, the client directly controls critical application state (e.g., position, actions, or resources) without sufficient server-side validation.

## Attack Scenario
An attacker modifies client memory or network messages to send invalid state updates, such as:
- Teleporting to arbitrary locations
- Exceeding allowed speed limits
- Triggering actions without proper conditions

## Preconditions
- Client is trusted to provide authoritative state
- Server performs little or no validation
- Communication protocol does not enforce constraints

## Impact
- Unfair advantage or system abuse
- State desynchronization between clients and server
- Potential cascading logic errors

## Mitigation
- Enforce server-authoritative design
- Validate all client inputs against expected constraints
- Reject impossible or inconsistent state transitions

## Detection Indicators
- Sudden large state changes (e.g., position jumps)
- Repeated invalid transitions
- Inconsistent state updates across clients

## OWASP Mapping
- A04: Insecure Design
- A08: Software and Data Integrity Failures