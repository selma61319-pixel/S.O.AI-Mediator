# S.O.Agent - Autonomous AI Escrow Assistant for Freelancers

S.O.Agent reads freelancer-client chats, understands the agreement using AI, and creates a secure PayPal Sandbox invoice. No more unpaid work, no more confusion.

## Problem
Freelancers agree on price and deadline in chat, but clients don't pay or forget. No contract, no protection.

## Solution
S.O.Agent acts as an autonomous agent:
1. Reads the chat
2. Extracts: amount, task, deadline, client name
3. Generates a PayPal Sandbox invoice link
4. Sends it to the client

## How we used AI
We used OpenAI (GPT) to understand natural language chats.
Example: "I agree to pay $200 for logo design in 3 days"
AI output: amount=200, task=logo design, deadline=3 days
The AI also detects disputes and suggests a fair solution.

## How we used PayPal
We used PayPal Sandbox API to create invoices.
No real money is used. When client pays in Sandbox, freelancer gets notified.
This simulates a real escrow flow safely.

## Tools & Technologies
- Python
- OpenAI API
- PayPal Sandbox API
- GitHub

## How to Run / Setup Instructions
1. Clone the repo: git clone https://github.com/selma61319-pixel/S.O.Agent
2. Install: pip install openai requests
3. Add your keys in main.py: OPENAI_API_KEY and PAYPAL_CLIENT_ID
4. Run: python main.py
5. Paste a chat like: "I agree to pay $200 for logo design in 3 days"

## Demo
Repo link is the demo. Run main.py and test with sample chats.
