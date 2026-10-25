# Stationary-refund-Agent
An AI refund agent for stationary stores, built with LangChain and LangGraph. It checks purchases, applies the 30-day refund policy, works out the refund and issues a ticket. It’s tested with DeepEval and got 100% accuracy across 7 test scenarios.

## Overview
The Stationary Refund Agent is an intelligent, LangChain-powered conversational AI system designed to automate and streamline the stationary product refund process. Built with LangGraph and integrated with DeepEval for comprehensive performance monitoring, this agent handles customer refund requests with high accuracy and reliability.

## Key Features
- **Intelligent Conversation Flow**: Uses structured responses with conversation state management to guide users through the refund process naturally.
- **Automated Purchase Validation**: Validates customer identity and purchase history against a centralized database to ensure only legitimate purchases are considered for refunds.
- **Smart Eligibility Checking**: Enforces a 30-day refund policy, checks item eligibility, and handles multiple items in a single request.
- **Flexible Refund Calculations**: Processes partial and full refunds based on item conditions and eligibility rules.
- **Tool-Driven Architecture**: Leverages LangChain tools for purchase history retrieval, date validation, refund calculation, and ticket issuance.
- **Robust Evaluation Framework**: Includes comprehensive metrics (Answer Correctness, Tool Correctness, Argument Correctness, Plan Adherence, Plan Quality, Step Efficiency, Task Completion) using DeepEval.

## Technical Stack
- **Framework**: LangChain, LangGraph
- **LLM Integration**: OpenAI-compatible models via LangChain
- **Evaluation**: DeepEval
- **Data Validation**: Pydantic
- **Language**: Python 3.14+

## Achievements
- **100% Accuracy**: Achieved perfect accuracy across all test cases in the evaluation dataset.
- **Comprehensive Testing**: Validated against 7 diverse scenarios including valid refunds, invalid users, expired returns, non-purchased items, and information-only queries.
- **Production-Ready Structure**: Organized with modular design separating agent logic, tools, prompts, and evaluation components.

## Use Case
Ideal for e-commerce platforms selling stationary items, this agent can reduce manual customer support workload by automating refund eligibility checks, calculations, and ticket generation while maintaining consistent policy enforcement.
"    write short discription for git hub
