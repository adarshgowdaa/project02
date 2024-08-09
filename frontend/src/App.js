import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import UploadPage from './pages/UploadPage';
import PassengerDetailsPage from './pages/PassengerDetailsPage';

function App() {
    return (
            <Router>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/upload" element={<UploadPage />} />
                    <Route path='/passengers' element={<PassengerDetailsPage />} />
                </Routes>   
            </Router>
    );
}

export default App;
