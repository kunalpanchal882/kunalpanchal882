import axios from "axios";
import { useState } from "react";
import "../index.css";
import ParsedResumeResult from "./ParsedResumeResult";

const ResumeUploader = () => {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setResult(null);
  };

  const handleSubmit = async () => {
    if (!file) return alert("Please upload a resume!");
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://127.0.0.1:8000/parse", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Something went wrong!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Smart Resume Parser</h1>
      <input type="file" accept=".pdf,.doc,.docx" onChange={handleFileChange} />
      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Parsing..." : "Parse Resume"}
      </button>

      {result && (
        <div className="result">
          <ParsedResumeResult data={result} />
        </div>
      )}
    </div>
  );
};

export default ResumeUploader;
