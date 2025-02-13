import axios from "axios";

const API_URL = "http://localhost:5000/chat"; // Flask backend endpoint

export const sendMessage = async (message) => {
  try {
    const response = await axios.post(API_URL, { message });
    return response.data.response; // Assuming backend returns { "response": "..." }
  } catch (error) {
    console.error("API error:", error);
    return "Sorry, something went wrong.";
  }
};
