import React, { createContext, useState } from 'react';

export const PassengerContext = createContext();

export const PassengerProvider = ({ children }) => {
    const [passengers, setPassengers] = useState([]);

    return (
        <PassengerContext.Provider value={{ passengers, setPassengers }}>
            {children}
        </PassengerContext.Provider>
    );
};
