# Azure AI Chat Completion with GPT

## Overview / Use Case
This project demonstrates how to generate **chat-based responses** using **Azure AI Foundry** models and access them programmatically via Python and VS Code.  
The use case is to automate **text generation** for applications like conversational agents, Q&A assistants, or AI-driven educational tools.

## Technology Used
- **Azure AI Foundry**: Hosting and deploying AI models  
- **Azure OpenAI API**: To call deployed models programmatically  
- **Python**: Backend scripting for sending requests and handling responses  
- **VS Code**: Development environment  
- **python-dotenv**: For managing environment variables securely  

## Key Features
- Generate AI-powered text responses using a deployed Azure model  
- Call the model from local Python scripts using **endpoint + API key**  
- Display and handle JSON responses (metadata, usage, filters)  
- Extract only the **raw text response** if metadata is not required  
- Easy to extend for different prompts, models, or workflows  
- Demonstrates integration of **cloud-hosted AI models** into local apps  

## Example Output

Here’s an example of a chat response generated using Azure AI Foundry:

**Prompt:**  
`Tell me about Mount Everest.`

**Raw Text Response (for end-users):**  
Mount Everest, located in the Himalayas on the border between Nepal and Tibet, 
is the tallest mountain in the world at 8,849 meters (29,032 feet). 
It is a popular but dangerous destination for climbers due to its extreme altitude and harsh conditions.

**JSON Response (full output from Azure API):**
```json
{
  "id": "chatcmpl-CLcPzGUKEttTgZK43slCGAQLDVmxi",
  "object": "chat.completion",
  "created": 1759268603,
  "model": "gpt-4o-2024-11-20",
  "choices": [
    {
      "index": 0,
      "finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "Mount Everest, the world's tallest peak at 8,849 meters (29,032 feet), is part of the Himalayan range, straddling Nepal and Tibet. Renowned for its extreme conditions, it attracts climbers worldwide, symbolizing human endurance and exploration."
      },
      "content_filter_results": { "hate": {"filtered": false}, "self_harm": {"filtered": false}, "sexual": {"filtered": false}, "violence": {"filtered": false} }
    }
  ],
  "usage": {
    "prompt_tokens": 756,
    "completion_tokens": 54,
    "total_tokens": 810
  }
}
```

## Why Output is in JSON

The Azure OpenAI API returns responses in JSON format by default because it includes both the generated text and important metadata like:
- Role information (assistant, user, system)
- Tokens usage (prompt, completion, total)
- Content filtering results
- Message indices and finish reasons
This structured format makes it easier to programmatically process, log, or extract the raw text for end-user display while keeping all metadata for auditing, monitoring, or debugging purposes.