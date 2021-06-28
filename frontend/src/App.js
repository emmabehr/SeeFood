//import logo from './logo.svg';
import octo from './octo.svg';
import './App.css';
import IngredientCapture from './IngredientCapture';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={octo} className="App-logo" alt="logo" />
      </header>
      <main>
        <IngredientCapture />
      </main>
      <footer>
        <div id="edamam-badge" data-color="white"></div>
      </footer>
    </div>
  );
}

export default App;
