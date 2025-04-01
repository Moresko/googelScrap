import React, { useState } from 'react';

function App() {
  const [keyword, setKeyword] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();

    const response = await fetch('http://localhost:8000/string', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ value: keyword }),
    });

    if (response.ok) {
      const blob = await response.blob();
      
      const filename = `${keyword}_scrape.csv`;

      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = filename;  
      link.click();
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
          placeholder="vyhladat"
        />
        <button type="submit">Stiahnut CSV</button>
      </form>
    </div>
  );
}

export default App;
