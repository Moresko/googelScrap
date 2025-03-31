import './App.css';
import { useState } from "react";

export default function App() {
  const [inputValue, setInputValue] = useState("");

  const handleClick = () => {
    alert(`You entered: ${inputValue}`);
  };

  return (
    <div >
      <input
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        placeholder="Enter something..."
      />
      <button onClick={handleClick} >
        Click Me
      </button>
    </div>
  );
}
