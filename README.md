# AI Movie Recommender

A FastAPI backend that recommends movies based on natural language requests. The user describes what they're in the mood for (a genre, a vibe, a plain-text description) and the API returns exactly 5 structured movie recommendations powered by Groq (Llama 3.3 70B).

## How It Works

1. User sends a plain-text request (e.g. "suggest me some thriller movies").
2. The request is combined with a system prompt that forces the model to return output matching a strict JSON schema.
3. Groq's API generates the recommendations.
4. The raw response is parsed and validated against a Pydantic schema before being returned to the client.

This ensures the API always returns predictable, structured data instead of free-form text.

## Tech Stack

- **FastAPI** — API framework
- **Groq API (Llama 3.3 70B)** — LLM for generating recommendations
- **Pydantic** — request/response schema validation
- **python-dotenv** — environment variable management

## Project Structure

```
.
├── main.py          # FastAPI app and /chat endpoint
├── llm_client.py     # Groq client setup and chat completion call
├── system.py         # System prompt enforcing the JSON schema
├── schemas.py         # Pydantic models for request/response validation
├── requirements.txt
└── .gitignore
```

## Setup

1. Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root:

```
groq_api_key=your_groq_api_key_here
```

3. Run the server:

```bash
uvicorn main:app --reload
```

4. Open the interactive API docs at `http://127.0.0.1:8000/docs`

## Example Request

**POST** `/chat`

```json
{
  "message": "suggest me some romantic movies"
}
```

## Example Response

```json
{
  "user_request": "romantic movie",
  "response": [
    {
      "title": "The Notebook",
      "year": 2004,
      "director": "Nick Cassavetes",
      "genres": ["Drama", "Romance"],
      "reason": "It's a classic tearjerker with a great love story",
      "summary": "A poor but passionate young man falls in love with a rich girl, and they are separated by social class but reunited years later"
    }
  ]
}
```

## Error Handling

The API uses specific exception handling for predictable failure modes:

- **`ValidationError`** — Groq's response doesn't match the expected schema
- **`json.JSONDecodeError`** — Groq returned malformed JSON
- **`AuthenticationError`** — Groq API key is missing or invalid
- **`Exception`** — generic fallback for any other failure

Each returns a `500` response with a clear error detail message rather than crashing the server.

## Notes

This project focuses on structured output generation with an LLM — no RAG or function calling involved, since the use case (mapping a free-text request to a fixed JSON schema) doesn't require either.
