# Huggingface MCP course


## Progress 

- [x] Unit 1
    - [x] https://huggingface.co/learn/mcp-course/unit1/introduction
    - [x] https://huggingface.co/learn/mcp-course/unit1/key-concepts
    - [x] https://huggingface.co/learn/mcp-course/unit1/architectural-components
    - [x] https://huggingface.co/learn/mcp-course/unit1/quiz1
    - [x] https://huggingface.co/learn/mcp-course/unit1/communication-protocol
    - [x] https://huggingface.co/learn/mcp-course/unit1/capabilities
    - [x] https://huggingface.co/learn/mcp-course/unit1/sdk
    - [x] https://huggingface.co/learn/mcp-course/unit1/quiz2
    - [x] https://huggingface.co/learn/mcp-course/unit1/mcp-clients
    - [x] https://huggingface.co/learn/mcp-course/unit1/gradio-mcp
    - [x] https://huggingface.co/learn/mcp-course/unit1/unit1-recap
    - [x] https://huggingface.co/learn/mcp-course/unit1/certificate

- [ ] Unit 2

    - [x] /learn/mcp-course/unit2/introduction: Introduction to Building an MCP Application 
    - [x] /learn/mcp-course/unit2/gradio-server: Building the Gradio MCP Server 
    - [x] /learn/mcp-course/unit2/clients: Using MCP Clients with your application
    - [ ] /learn/mcp-course/unit2/continue-client: Using MCP in the Your AI Coding Assistant 
    - [ ] /learn/mcp-course/unit2/gradio-client: Building an MCP Client with Gradio
    - [ ] /learn/mcp-course/unit2/tiny-agents: Building Tiny Agents with MCP and the Hugging Face Hub
    - [ ] /learn/mcp-course/unit2/lemonade-server: Local Tiny Agents with AMD NPU and iGPU Acceleration

 - [ ] Unit 3
    - [ ] /learn/mcp-course/unit3_1/introduction: Build a Pull Request Agent on the Hugging Face Hub
    - [ ] /learn/mcp-course/unit3_1/setting-up-the-project: Setting up the Project
    - [ ] /learn/mcp-course/unit3_1/creating-the-mcp-server: Creating the MCP Server
    - [ ] /learn/mcp-course/unit3_1/quiz1: Quiz 1 - MCP Server Implementation
    - [ ] /learn/mcp-course/unit3_1/mcp-client: MCP Client
    - [ ] /learn/mcp-course/unit3_1/webhook-listener: Webhook Listener
    - [ ] /learn/mcp-course/unit3_1/quiz2: Quiz 2 - Pull Request Agent Integration
    - [ ] /learn/mcp-course/unit3_1/conclusion: Conclusion

## Unit 1

### Commands

```
uv init

uv venv

source .venv/bin/activate

uv pip install "mcp[cli]"

mcp dev server.py

uv pip install "huggingface_hub[mcp]>=0.32.0"

tiny-agents run agent.json

demo.launch(mcp_server=True)

```

## Unit 2

Configuring Gemini CLI for MCP

```
cd ~
cd .gemini
settings.json

{
  "ide": {
    "hasSeenNudge": true,
    "enabled": true
  },
  "mcpServers": {
    "math": {
      "command": "node",
      "args": [
        "/home/stefano/Documents/Progetti/gemini-cli-mcp/index.js"
      ]
    },
    "sentiment-analysis": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "http://127.0.0.1:7860/gradio_api/mcp/sse"
      ]
    },
    "browser-search": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  },
  "security": {
    "auth": {
      "selectedType": "oauth-personal"
    }
  },
  "ui": {
    "theme": "Default"
  }
}

```

npm install @playwright/mcp per installare l'mcp di Playwright