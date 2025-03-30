import './App.css';
import { useState } from "react";

function App() {
  const [googleWord, setInputValue] = useState("");
  const [results, setResults] = useState([]);

  const startSearch = async () => {
    if (!googleWord) return alert("Please enter a search query");

    try {
      const response = await fetch(`http://localhost:5001/search?q=${googleWord}`);
      const data = await response.json();

      setResults(data.results); // Store the results in state
    } catch (error) {
      console.error("Error fetching search results:", error);
    }
  };

  return (
    <div className="App">
      <h1>Google Search Scrap</h1>
      <input
        type="text"
        value={googleWord}
        onChange={(e) => setInputValue(e.target.value)}
        placeholder="Enter something..."
      />
      <button onClick={startSearch}>Search</button>

      <ul>
        {results.map((result, index) => (
          <li key={index}>{result}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
