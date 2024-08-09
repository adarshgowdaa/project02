import React, { useState } from 'react';

const UploadFile = ({ onUpload }) => {
    const [file, setFile] = useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (file) {
            onUpload(file);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div className="form-group">
                <label htmlFor="file">Upload Excel File</label>
                <input type="file" className="form-control" id="file" onChange={handleFileChange} />
            </div>
            <button type="submit" className="btn btn-primary mt-3">Upload</button>
        </form>
    );
};

export default UploadFile;
