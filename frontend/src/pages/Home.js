import React from 'react';
import { useNavigate } from 'react-router-dom';

const Home = () => {
    const navigate = useNavigate();

    const handleUploadClick = () => {
        navigate('/upload');
    };

    return (
        <div className="container">
            <h1>Welcome to the Titanic Passenger Management App</h1>
            <p>Upload a CSV file to get started.</p>
            <button className='btn btn-primary' onClick={handleUploadClick}>Upload</button>
        </div>
    );
};

export default Home;
