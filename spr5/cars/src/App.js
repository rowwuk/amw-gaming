import './App.css';
import Nav from './Nav';
import Detail from './Detail';
import List from './List';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

function App() {

  return (
    <Router>
      <div className="App">
        <Nav />
        <Switch>
          <Route path="/" exact component={List} />
          <Route path="/detail" component={Detail} />
        </Switch>
      </div>
    </Router>
  );

}

export default App;
