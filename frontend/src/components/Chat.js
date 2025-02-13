import React, { useState } from "react";
import { sendMessage } from "../api";
import { TextField, Button, List, ListItem, ListItemText, Paper, Typography } from "@mui/material";
import SendIcon from "@mui/icons-material/Send";
import "../styles/Chat.css"; // Import external CSS for additional styling

const Chat = () => {
    const [input, setInput] = useState("");
    const [messages, setMessages] = useState([]);

    const handleSend = async () => {
        if (!input.trim()) return;

        const userMessage = { text: input, sender: "user" };
        setMessages((prev) => [...prev, userMessage]); // Add user message

        try {
            const response = await sendMessage(input);
            const botMessage = { text: response, sender: "bot" };
            setMessages((prev) => [...prev, botMessage]); // Add bot response
        } catch (error) {
            console.error("Error sending message:", error);
            setMessages((prev) => [...prev, { text: "Sorry, something went wrong.", sender: "bot" }]);
        }

        setInput("");
    };

    return (
        <div className="chat-container">
            <Typography variant="h5" className="chat-title" fontWeight="bold" gutterBottom>
                AI-Chatbot
            </Typography>
            <Paper elevation={3} className="chat-box">
                <List className="chat-list">
                    {messages.map((msg, index) => (
                        <ListItem key={index} className={msg.sender === "user" ? "user-message" : "bot-message"}>
                            <ListItemText primary={msg.text} />
                        </ListItem>
                    ))}
                </List>
            </Paper>

            <div className="input-container">
                <TextField
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    fullWidth
                    placeholder="Ask me anything..."
                    className="chat-input"
                />
                <Button onClick={handleSend} variant="contained" color="primary" className="send-button">
                    <SendIcon />
                </Button>
            </div>
        </div>
    );
};

export default Chat;
