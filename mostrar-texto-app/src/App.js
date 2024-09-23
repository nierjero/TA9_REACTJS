import React, { useState } from 'react';

function App() {
  // Estado para controlar la visibilidad del texto
  const [mostrarTexto, setMostrarTexto] = useState(false);

  // Función para alternar la visibilidad del texto
  const toggleTexto = () => {
    setMostrarTexto(!mostrarTexto);
  };

  return (
    <div style={styles.container}>
      <button onClick={toggleTexto} style={styles.button}>
        {mostrarTexto ? 'Ocultar Texto' : 'Mostrar Texto'}
      </button>
      {mostrarTexto && <p style={styles.texto}>¡It's metal gear, it's already active!</p>}
    </div>
  );
}

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    marginTop: '50px'
  },
  button: {
    margin: '10px',
    padding: '10px 20px',
    fontSize: '16px'
  },
  texto: {
    marginTop: '20px',
    fontSize: '18px'
  }
};

export default App;

