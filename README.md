# PhantomShield AI  
Smart Insurance System for Delivery Workers

---

## Problem

Delivery workers operate in risky environments (rain, traffic, unsafe zones).  
Existing parametric insurance systems rely heavily on GPS data.

This creates a major vulnerability:
GPS can be spoofed, allowing fraudulent users to trigger false claims.

---

## Solution

PhantomShield replaces GPS-based validation with a trust-based system.

Instead of trusting location, the system evaluates:
- Behavioral patterns
- Environmental conditions
- Network consistency
- Historical reliability

Claims are approved or flagged based on a computed trust score.

---

## How It Works

1. User inputs conditions (rain, traffic, area)
2. System calculates:
   - Risk Score
   - Trust Score
3. Premium is generated dynamically
4. Claim is:
   - Approved (high trust)
   - Flagged (low trust)

---

## Core Idea

The system does not rely on GPS alone.

It uses:

Trust = f(behavior + network + crowd + history)

Fraud is detected through inconsistencies across these signals.

---

## Adversarial Defense & Anti-Spoofing Strategy

### Differentiation

Traditional systems validate location.  
This system validates behavior.

Spoofed users fail because:
- They lack real movement patterns
- Their sensor data is unrealistic
- Their activity does not match nearby users

---

### Data Used (Beyond GPS)

- Weather intensity
- Traffic conditions
- Area risk level
- Behavioral signals (movement, variability)
- Network stability
- Historical usage patterns

---

### Fraud Detection

The system compares expected vs actual behavior.

Example:
- Genuine user → dynamic movement, natural variation
- Spoofed user → static or artificial patterns

Low trust leads to flagging.

---

### UX Balance

Flagging does not mean rejection.

- High trust → instant approval
- Medium trust → verification step
- Low trust → flagged for review

This ensures fairness for genuine workers affected by network issues.

---

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Flask (Python)
- Deployment:
  - Netlify (Frontend)
  - Railway (Backend)

---

## Demo

Frontend: https://phantomshield.netlify.app  
Backend: https://phantomshield-ai-production.up.railway.app  

Note: Backend may take a few seconds to start (free hosting).

---

## Future Improvements

- Real sensor data integration
- Advanced anomaly detection
- Live crowd validation
- Integration with delivery platforms

---

## Summary

PhantomShield introduces a behavior-based trust system that makes insurance more secure, scalable, and resistant to GPS spoofing attacks.
