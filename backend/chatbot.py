import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
from queries import get_products_by_brand, get_suppliers_by_category

load_dotenv()

# Initialize Google Gemini API using LangChain
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GEMINI_API_KEY"))

# Define stopwords (words to ignore in category extraction)
STOPWORDS = {"and", "or", "the", "a"}

def get_response(user_query):
    """
    Processes user queries, retrieves relevant data from the database,
    and ensures structured responses with correct bullet-point formatting.
    """
    user_query_lower = user_query.lower().strip()
    # Handle common greetings
    greetings = ["hi", "hello", "hey", "good morning", "good evening"]
    if any(greet in user_query_lower.split() for greet in greetings):  # Check as a standalone word
        return "Hello! I'm here to assist you. How can I help?"
    elif user_query_lower in ["thanks", "thanks!"]:
        return "You are welcome!"

    else:
        if "brand" in user_query_lower or "brands" in user_query_lower:
            brand = user_query_lower.split("brand")[-1].strip()
            products = get_products_by_brand(brand)

            if products:
                product_details = "\n".join([f"- {p['name']}: ${p['price']}" for p in products])
                response = f"Products under {brand}:\n\n{product_details}"
            else:
                query_context = f"Tell user you couldn't get if you couldn't understand any brand in {user_query} and Just say ' Ask like 'List products of brand 'your brand''. Do this very concisely"
                try:
                    response = llm([HumanMessage(content=query_context)]).content
                except Exception:
                    response = "I'm not sure about that. Let me know how else I can help!"

        elif "supplier" in user_query_lower or "suppliers" in user_query_lower:
            # Extract multiple categories while removing stopwords
            words = user_query_lower.replace("?", "").split()  # Remove ? and split into words
            categories = []

            # Find all words after the keywords
            for i, word in enumerate(words):
                if word in ["provide", "provides", "offering", "offers"]:
                    # Take all words after the keyword and remove stopwords
                    categories = [w for w in words[i + 1:] if w not in STOPWORDS]
                    break

            if not categories:  # If no keyword found, assume the whole query is a category
                categories = [w for w in user_query_lower.split() if w not in STOPWORDS]

            print(f"Extracted Categories: {categories}")  # Debug print

            # Fetch suppliers for each category
            supplier_responses = []
            for category in categories:
                suppliers = get_suppliers_by_category(category)
                if suppliers:
                    supplier_details = "\n".join([f"- {s['name']} (Contact: {s['contact_info']})" for s in suppliers])
                    supplier_responses.append(f"Suppliers for {category}:\n\n{supplier_details}")
                else:
                    query_context = f"Tell user you couldn't get if you couldn't understand any brand in {user_query} and Just say 'Ask like 'Which supplier provides [Your Category]'"
                    try:
                        response = llm([HumanMessage(content=query_context)]).content
                    except Exception:
                        response = "I'm not sure about that. Let me know how else I can help!"

            response = "\n\n".join(supplier_responses)  # Combine responses

        else:
            query_context = f"Tell user you couldn't get if you couldn't understand any category or brand in {user_query} and suggest how he should give prompt. Do this very concisely like ask like 'Which supplier provides 'your category'' or 'List products of brand 'your brand'"
            try:
                response = llm([HumanMessage(content=query_context)]).content
            except Exception:
                response = "I'm not sure about that. Let me know how else I can help!"

    return response
