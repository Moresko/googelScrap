import React, { useState } from 'react';
import './App.css';

function App() {
  const [googleWord, setGoogleWord] = useState('');

  const pressButton = async (event) => {
    event.preventDefault();

    const response = await fetch('https://api-npyfbs8z7-mores.vercel.app', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ value: googleWord }),
    });

    if (response.ok) {
      const blob = await response.blob();
      const csv = `${googleWord}_scrapped.csv`;
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = csv;  
      link.click();
    }
    setGoogleWord('')
  };

  return (
    <div>
      <form onSubmit={pressButton}>
        <input
          className='inpt'
          type="text"
          value={googleWord}
          onChange={(e) => setGoogleWord(e.target.value)}
          placeholder="vyhladat"
        />
        <button className="btn" type="submit">Stiahnut CSV</button>
      </form>
    </div>
  );
}

export default App;
