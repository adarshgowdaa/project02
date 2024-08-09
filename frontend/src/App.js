import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import UploadPage from './pages/UploadPage';
import { PassengerProvider } from './context';

function App() {
    return (
        <PassengerProvider>
            <Router>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/upload" element={<UploadPage />} />
                </Routes>
            </Router>
        </PassengerProvider>
    );
}

export default App;
