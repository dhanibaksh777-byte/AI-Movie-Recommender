from fastapi import FastAPI
from llm_client import get_chat
from schemas import Recommendation,MovieResponse
from fastapi import HTTPException
from system import SYSTEM_PROMPT
from groq import AuthenticationError
from pydantic import BaseModel,ValidationError
import json


class ChatRequest(BaseModel):
    message : str


app = FastAPI(title="AI movies recommender")


@app.post("/chat")
def chat(request : ChatRequest):
    message = [{"role" : "system", "content" : SYSTEM_PROMPT},
               {"role" : "user", "content" : request.message }]
    try:


        reply = get_chat(message)
        result = json.loads(reply)
        final_reply = MovieResponse(**result)
        return final_reply

    except ValidationError:
        raise HTTPException(status_code=500,detail="schema error!")
    
    
    except json.JSONDecodeError:
        raise HTTPException(status_code=500,detail="groq return invalid json")
    except AuthenticationError:
        raise HTTPException(status_code=500,detail="groq api does'nt exists in .env file")
    except Exception:
        raise HTTPException(status_code=500,detail="currently bot is unavailable!")
    


    



    