import React from 'react';
import UploadFile from '../components/UploadFile';
import { useUpload } from '../hooks/useUpload';

const UploadPage = () => {
    const { uploadResponse, uploadFile } = useUpload();

    return (
        <div className="container">
            <h1>Upload Excel File</h1>
            <UploadFile onUpload={uploadFile} />
            {uploadResponse && <p>{uploadResponse.message}</p>}
        </div>
    );
};

export default UploadPage;
