const BASE_URL = 'http://localhost:8000';

export const fetchPassengers = async () => {
    try {
        const response = await fetch(`${BASE_URL}/api/passengers/`);
        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Error fetching passengers:', error);
        throw error;
    }
};

export const fetchPassengerById = async (id) => {
    try {
        const response = await fetch(`${BASE_URL}/api/passenger/${id}/`);
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching passenger:', error);
        return null;
    }
};

export const updatePassenger = async (id, passengerData) => {
    try {
        const response = await fetch(`${BASE_URL}/api/passenger/${id}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(passengerData),
        });
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error updating passenger:', error);
        return null;
    }
};

export const getSurvivedCount = async (gender) => {
    try {
        const response = await fetch(`${BASE_URL}/api/survived`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ gender }),
        });
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching survived count:', error);
        return null;
    }
};

export const uploadFile = async (file) => {
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch(`${BASE_URL}/upload`, {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }

        return await response.json();
    } catch (error) {
        console.error('Error uploading file:', error);
        throw error;
    }
};
