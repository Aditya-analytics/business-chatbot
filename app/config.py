import os
from dotenv import load_dotenv

load_dotenv() #Loaded environment variables so that access through os

#---------------------
# API Configuration
#---------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("Gemini Api key not found!")

#----------------------
# Model configuration
#----------------------

MODEL_NAME = "gemini-2.5-flash-lite"

#----------------------
# Retrival configuration
#----------------------
TOP_K_QA = 5 #  Number of chunks for Q&A
TOP_K_SUMMARY = 15 # Number of chunks for summarization

# -----------------------------
# Memory Configuration
# -----------------------------

MEMORY_WINDOW = 5     # Last N interactions to keep