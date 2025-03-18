# Making an AI Agent from scratch

# what is AI agent
We will have some predefined functions and LLM knows about these functions,now based on user response LLM executes this function, for More details see this [Mindmap](https://app.eraser.io/workspace/NgmMrdC2eXU2cbfHJ3wW)

Packages used: `openai`, `readline-sync`
# About this Basic AI Agent

A simple Node.js-based AI agent that uses OpenAI's GPT-4 to process user queries and interact with local tools/functions. The agent follows a structured approach of planning, taking actions, and providing outputs based on observations.

## Features

- Interactive command-line interface
- Integration with OpenAI's GPT-4
- Structured conversation flow (Plan → Action → Observation → Output)
- Sample weather information tool implementation
- JSON-formatted responses

## Prerequisites

- Node.js installed on your system
- OpenAI API key

## Installation

1. Clone the repository
2. Install dependencies:
```bash
npm install
```

3. Configure the OpenAI API key:
   Open `index.js` and add your OpenAI API key:
```javascript
const OPENAI_API_KEY = 'your-api-key-here';
```

## Usage

Run the application:
```bash
node index.js
```

The agent will start in interactive mode, waiting for your input. You can ask questions about weather, and the agent will process them following a structured approach.

Example query:
>> What is the weather in Patiala?

## Current Tools

- `getWeatherDetails`: Returns weather information for specific Indian cities:
  - Patiala: 10°C
  - Delhi: 8°C
  - Jaipur: 9°C
  - Udaipur: 12°C
  - Guwahati: 15°C

## Dependencies

- openai: ^4.79.1
- readline-sync: ^1.4.10

## Note

This is a basic implementation with hardcoded weather data. For production use, you should integrate with real weather APIs and implement proper error handling.