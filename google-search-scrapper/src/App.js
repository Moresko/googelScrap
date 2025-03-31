import './App.css';
import { useState } from "react";
import FruitList from './Fruits';

export default function App() {
  // const [inputValue, setInputValue] = useState("");

  // const handleClick = () => {
  //   alert(`You entered: ${inputValue}`);
  // };

  return (
    <div >
      <FruitList/>
      {/* <input
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        placeholder="Enter something..."
      />
      <button onClick={handleClick} >
        Click Me
      </button> */}
    </div>
  );
}
