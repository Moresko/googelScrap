import React, { useState } from "react";

const AddFruitForm = () => {
  const [inputValue, setInputValue] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!inputValue.trim()) return;

    try {
      const response = await fetch("http://localhost:8000/string", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ value: inputValue }),
      });

      const data = await response.json();
      console.log("Server Response:", data);
    } catch (error) {
      console.error("Error sending string:", error);
    }

    setInputValue(""); // Clear input after sending
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        placeholder="Enter something..."
      />
      <button type="submit">Send</button>
    </form>
  );
};

export default AddFruitForm;
