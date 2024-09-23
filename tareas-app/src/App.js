import React, { useState } from 'react';

function App() {
  const [tarea, setTarea] = useState('');
  const [listaTareas, setListaTareas] = useState([]);

  const agregarTarea = () => {
    if (tarea.trim()) {
      setListaTareas([...listaTareas, tarea]);
      setTarea(''); 
    }
  };

  return (
    <div style={styles.container}>
      <h1>Lista de Tareas</h1>
      <input
        type="text"
        value={tarea}
        onChange={(e) => setTarea(e.target.value)}
        style={styles.input}
        placeholder="Añadir nueva tarea"
      />
      <button onClick={agregarTarea} style={styles.button}>Agregar Tarea</button>
      <ul style={styles.lista}>
        {listaTareas.map((tarea, index) => (
          <li key={index} style={styles.item}>{tarea}</li>
        ))}
      </ul>
    </div>
  );
}

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    marginTop: '50px',
    width: '300px',
    margin: 'auto',
  },
  input: {
    marginBottom: '10px',
    padding: '10px',
    width: '100%',
  },
  button: {
    padding: '10px',
    marginBottom: '20px',
    cursor: 'pointer',
  },
  lista: {
    listStyleType: 'none',
    padding: 0,
    width: '100%',
  },
  item: {
    padding: '10px',
    border: '1px solid #ccc',
    marginBottom: '5px',
    borderRadius: '5px',
  },
};

export default App;

