import React from 'react';
import PassengersTable from '../components/PassengersTable';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>Titanic Passenger Management</h1>
            </header>
            <main>
                <PassengersTable />
            </main>
        </div>
    );
}

export default App;
