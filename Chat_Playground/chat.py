
import os
import base64
from openai import AzureOpenAI

from dotenv import load_dotenv
load_dotenv()

endpoint = os.getenv("CHAT_ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o")
subscription_key = os.getenv("CHAT_AZURE_OPENAI_API_KEY")

# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)

# IMAGE_PATH = "YOUR_IMAGE_PATH"
# encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')

# Prepare the chat prompt
chat_prompt = [
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": "You are an AI assistant that helps people find information."
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Tell me about black water?"
            }
        ]
    },
    {
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": "\"Black water\" is a term that can have different meanings depending on the context. Below are some of the most common interpretations:\n\n---\n\n### 1. **Black Water in Environmental and Wastewater Context**\nIn environmental science and wastewater management, \"black water\" refers to wastewater that contains human waste, typically from toilets. It may also include water from kitchen sinks, dishwashers, and other household drains that contain food waste, grease, and other organic materials. \n\n- **Characteristics**: Black water is considered contaminated and requires treatment before it can be safely released into the environment. It contains pathogens, bacteria, and viruses, making it a potential health hazard.\n- **Treatment**: Specialized sewage treatment plants or septic systems are used to treat black water. In off-grid setups, composting toilets or other eco-friendly solutions can also be employed.\n\n---\n\n### 2. **Blackwater (Corporation)**\n\"Blackwater\" is also the former name of a controversial private military company now known as **Academi**. The company was originally founded in 1997 and became widely known for its role in providing security services during the wars in Iraq and Afghanistan. \n\n- **Controversy**: Blackwater came under intense scrutiny and criticism for its actions, including accusations of human rights violations and excessive use of force.\n- **Rebranding**: The company changed its name to **Xe Services** in 2009 and later rebranded again as **Academi** to distance itself from its troubled reputation.\n\n---\n\n### 3. **Natural Black Water (Tannins in Water)**\nIn a natural context, \"black water\" can refer to water bodies, like rivers or swamps, that appear dark or black due to the presence of organic materials like tannins. These are often found in areas with heavy vegetation, such as tropical rainforests.\n\n- **Examples**: The Rio Negro in the Amazon basin is a famous blackwater river.\n- **Cause**: The dark color comes from the leaching of tannins and other plant materials into the water, not from pollution.\n- **Ecosystem**: Blackwater rivers and swamps often support unique ecosystems adapted to the water's low pH and nutrient levels.\n\n---\n\n### 4. **Black Water (Bottled Water)**\n\"Black water\" is also a term used for certain premium bottled water brands that contain added minerals, such as **fulvic acid**, which gives the water a black or dark color. It is marketed as having health benefits due to its trace minerals.\n\n- **Popular Brands**: BLK is one of the well-known brands of black bottled water.\n- **Claims**: These products often claim to boost energy, improve hydration, and provide antioxidant properties, though scientific evidence for these claims is limited.\n\n---\n\n### "
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "What is black water. give in 2 lines."
            }
        ]
    },
    {
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": "Black water refers to wastewater containing human waste from toilets, often combined with kitchen or other household drains, requiring treatment due to its contamination. It can also describe dark natural water bodies stained by organic tannins or premium bottled water infused with minerals like fulvic acid."
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "What do you know about Mount Everest. Give me in two lines."
            }
        ]
    },
    {
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": "Mount Everest, located in the Himalayas on the border between Nepal and Tibet, is the tallest mountain in the world, standing at 8,849 meters (29,032 feet). It is a popular destination for climbers, though its extreme altitude and harsh conditions make the ascent highly challenging and dangerous."
            }
        ]
    }
]

# Include speech result if speech is enabled
messages = chat_prompt

# Generate the completion
completion = client.chat.completions.create(
    model=deployment,
    messages=messages,
    max_tokens=6553,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
)

print(completion.to_json())