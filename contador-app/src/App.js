import React, { useState, useEffect } from 'react';

function App() {
  const [contador, setContador] = useState(0);

  useEffect(() => {
    document.title = `Contador: ${contador}`;
  }, [contador]); 

  const aumentar = () => {
    setContador(contador + 1);
  };

  const disminuir = () => {
    setContador(contador - 1);
  };

  return (
    <div style={styles.container}>
      <h1>Contador: {contador}</h1>
      <button onClick={aumentar} style={styles.button}>Aumentar</button>
      <button onClick={disminuir} style={styles.button}>Disminuir</button>
    </div>
  );
}

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    marginTop: '50px',
  },
  button: {
    margin: '10px',
    padding: '10px 20px',
    fontSize: '16px',
  },
};

export default App;


