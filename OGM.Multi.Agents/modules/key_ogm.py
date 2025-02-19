"""

This module defines how to get Key

"""
########################################################################################
# Importing Libraries
########################################################################################
import os
import openai
import streamlit as st
from dotenv import load_dotenv, find_dotenv

########################################################################################
# Local .env    
########################################################################################

# Open AI Key Function
def get_openai_key_env() -> str:
    """
    Loads the OpenAI API key from the local.env file.

    Returns:
        str: The OpenAI API key.
    """
    try:
        load_dotenv(find_dotenv())
        openai.api_key = os.environ['OPENAI_API_KEY']
        return openai.api_key
    except KeyError as e:
        print(f"Error: Missing environment variable 'OPENAI_API_KEY'. {e}")
        raise
    except Exception as e:
        print(f"Error: Failed to load OpenAI API key. {e}")
        raise
# Pinecone Key Function
def get_pinecone_key_env() -> str:
    """
    Loads the Pinecone API key from the local.env file.

    Returns:
        str: The Pinecone API key.
    """
    try:
        load_dotenv(find_dotenv())
        return os.environ['PINECONE_API_KEY']
    except KeyError as e:
        print(f"Error: Missing environment variable 'PINECONE_API_KEY'. {e}")
        raise
    except Exception as e:
        print(f"Error: Failed to load Pinecone API key. {e}")
        raise
# Voyage Key Function
def get_voyage_key_env() -> str:
    """
    Loads the Voyage API key from the local.env file.

    Returns:
        str: The Voage API key.
    """
    try:
        load_dotenv(find_dotenv())
        return os.environ['VOYAGE_API_KEY']
    except KeyError as e:
        print(f"Error: Missing environment variable 'VOYAGE_API_KEY'. {e}")
        raise
    except Exception as e:
        print(f"Error: Failed to load Voyage API key. {e}")
        raise
# Neo4j Key Function
def get_neo4j_config_env() -> dict:
    """
    Loads the Neo4j configuration from the local.env file.

    Returns:
        dict: A dictionary containing the Neo4j configuration.
    """
    try:
        load_dotenv(find_dotenv())
        config = {
            'uri': os.environ['NEO4J_URI'],
            'username': os.environ['NEO4J_USERNAME'],
            'password': os.environ['NEO4J_PASSWORD'],
            'database': os.environ['NEO4J_DATABASE']
        }
        return config
    except KeyError as e:
        print(f"Error: Missing environment variable. {e}")
        raise
    except Exception as e:
        print(f"Error: Failed to load Neo4j configuration. {e}")
        raise

# Langsmith Key Function
def get_langsmith_key_env() -> str:
    """
    Loads the Langsmith API key from the local.env file.

    Returns:
        str: The Langsmith API key.
    """
    try:
        load_dotenv(find_dotenv())
        return os.environ["LANGCHAIN_API_KEY"]
    except KeyError as e:
        print(f'Error: Missing environment variable "LANGCHAIN_API_KEY". {e}')
        raise
    except Exception as e:
        print(f"Error: Failed to load Langsmith API key. {e}")
        raise

########################################################################################
# Streamlit secrets.toml
########################################################################################
# Open AI Key Function
def get_openai_key_st() -> str:
    """
    Loads the OpenAI API key from the Streamlit secrets.toml file.

    Returns:
        str: The OpenAI API key.
    """
    try:
        return st.secrets['OPENAI_API_KEY']
    except KeyError as e:
        print(f"Error: Missing secret 'OPENAI_API_KEY' in secrets.toml file. {e}")
        raise
    except Exception as e:
        print(f"Error: Failed to load OpenAI API key. {e}")
        raise
# Pinecone Key Function
def get_pinecone_key_st() -> str:
    """
    Loads the Pinecone API key from the Streamlit secrets.toml file.

    Returns:
        str: The Pinecone API key.
    """
    try:
        return st.secrets['PINECONE_API_KEY']
    except KeyError as e:
        print(f"Error: Missing secret 'PINECONE_API_KEY' in secrets.toml file. {e}")
        raise
    except Exception as e:
        print(f"Error: Failed to load Pinecone API key. {e}")
        raise
# Voyage Key Function
def get_voyage_key_st() -> str:
    """
    Loads the Voyage API key from the Streamlit secrets.toml file.

    Returns:
        str: The Voyage API key.
    """
    try:
        return st.secrets['VOYAGE_API_KEY']
    except KeyError as e:
        print(f"Error: Missing secret 'VOYAGE_API_KEY' in secrets.toml file. {e}")
        raise
    except Exception as e:
        print(f"Error: Failed to load Voyage API key. {e}")
        raise
# Neo4j Key Function
def get_neo4j_config_st() -> dict:
    """
    Loads the Neo4j configuration from the Streamlit secrets.toml file.

    Returns:
        dict: A dictionary containing the Neo4j configuration.
    """
    try:
        config = {
            'uri': st.secrets['NEO4J_URI'],
            'username': st.secrets['NEO4J_USERNAME'],
            'password': st.secrets['NEO4J_PASSWORD'],
            'database': st.secrets['NEO4J_DATABASE']
        }
        return config
    except KeyError as e:
        print(f"Error: Missing secret in secrets.toml file. {e}")
        raise
    except Exception as e:
        print(f"Error: Failed to load Neo4j configuration. {e}")
        raise

# Langsmith Key Function
def get_langsmith_key_st() -> str:
    """
    Loads the Langsmith API key from the Streamlit secrets.toml file.

    Returns:
        str: The Langsmith API key.
    """
    try:
        return st.secrets['LANGCHAIN_API_KEY']
    except KeyError as e:
        print(f"Error: Missing secret 'LANGCHAIN_API_KEY' in secrets.toml file. {e}")
        raise
    except Exception as e:
        print(f"Error: Failed to load Langsmith API key. {e}")
        raise

# serper_api_key fuction
def get_serper_api_key_st() -> str:
    """
    Loads the serper_api_key from the Streamlit secrets.toml file.

    Returns:
        str: The Langsmith API key.
    """
    try:
        return st.secrets['SERPER_API_KEY']
    except KeyError as e:
        print(f"Error: Missing secret 'SERPER_API_KEY' in secrets.toml file. {e}")
        raise
    except Exception as e:
        print(f"Error: Failed to load SERPER_API_KEY. {e}")
        raise
# TAVILY_API_KEY fuction
def get_tavily_api_key_st() -> str:
    """
    Loads the tavily_api_key from the Streamlit secrets.toml file.

    Returns:
        str: The Langsmith API key.
    """
    try:
        return st.secrets['TAVILY_API_KEY']
    except KeyError as e:
        print(f"Error: Missing secret 'TAVILY_API_KEY' in secrets.toml file. {e}")
        raise
    except Exception as e:
        print(f"Error: Failed to load TAVILY_API_KEY. {e}")
        raise