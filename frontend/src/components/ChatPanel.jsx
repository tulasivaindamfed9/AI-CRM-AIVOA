import { useState } from "react";
import { useDispatch } from "react-redux";
import { setInteraction } from "../redux/interactionSlice";
import { logInteraction,editInteraction } from "../services/api";
import { toast } from "react-toastify";

import "../styles/chat.css";

function ChatPanel() {
  const [message, setMessage] = useState("");

  const [chatHistory, setChatHistory] = useState([
    {
      sender: "ai",
      text: "Hello! Tell me about your interaction with the HCP.",
    },
  ]);
  const [loading, setLoading] = useState(false);

  const dispatch = useDispatch();

  const handleSend = async () => {
  if (!message.trim()) return;

  setChatHistory((prev) => [
    ...prev,
    {
      sender: "user",
      text: message,
    },
  ]);

  try {
    setLoading(true);

    const text = message.trim().toLowerCase();

    const isEdit =
      text.startsWith("edit") ||
      text.startsWith("change") ||
      text.startsWith("update");

    const response = isEdit
      ? await editInteraction(message)
      : await logInteraction(message);

    dispatch(setInteraction(response.data));

    toast.success(
      isEdit
        ? "Interaction updated successfully!"
        : "Interaction logged successfully!"
    );

    setChatHistory((prev) => [
      ...prev,
      {
        sender: "ai",
        text: isEdit
          ? "✅ Interaction updated successfully."
          : "✅ Interaction logged successfully.",
      },
    ]);

    setMessage("");
  } catch (error) {
    console.error(error);

    toast.error("Something went wrong!");

    setChatHistory((prev) => [
      ...prev,
      {
        sender: "ai",
        text: "❌ Sorry, something went wrong. Please try again.",
      },
    ]);
  } finally {
    setLoading(false);
  }
};

  return (
    <div className="chat-card">
      <h5>🤖 AI Assistant</h5>

     <div className="chat-box">
  {chatHistory.map((chat, index) => (
    <div
      key={index}
      className={
        chat.sender === "user"
          ? "user-message"
          : "ai-message"
      }
    >
      {chat.text}
    </div>
  ))}
</div>
      {/* if loading show msg to improve UX */}
      {loading && (
        <div className="alert alert-info mt-3 mb-2 py-2">
          🤖 AI is understanding your message...
        </div>
      )}

      <textarea
        className="form-control mt-3"
        rows="4"
        placeholder="Example: I met Dr. Ramesh today. We discussed diabetes medicine..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        disabled={loading}
      />

      <button
        className="btn btn-primary mt-3 w-100"
        onClick={handleSend}
        disabled={loading}
      >
        {loading ? (
          <>
            <span
              className="spinner-border spinner-border-sm me-2"
              role="status"
            ></span>
            AI is processing...
          </>
        ) : (
          "Send"
        )}
      </button>
    </div>
  );
}

export default ChatPanel;
