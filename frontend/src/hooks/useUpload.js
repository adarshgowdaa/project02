import { useState } from 'react';
import { uploadFile } from '../api/passengerApi';

export const useUpload = () => {
    const [uploadResponse, setUploadResponse] = useState(null);

    const uploadFileHandler = async (file) => {
        const response = await uploadFile(file);
        setUploadResponse(response);
    };

    return { uploadResponse, uploadFile: uploadFileHandler };
};