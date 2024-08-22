import { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [valueBil, setValueBil] = useState('');
  const [valueHasilGenerate, setValueHasilGenerate] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const actionGenerateSegitigaAPI = async () => {
    setLoading(true);
    setError(null);
    try {
      const formData = new FormData();
      formData.append('input_bil', valueBil);

      const response = await axios.post(
        'http://localhost:5000/api/v1/bilangan_operasi_route_api_v1/generate_segitiga',
        formData,
        { headers: { 'Content-Type': 'multipart/form-data' } }
      );

      setValueHasilGenerate(response.data.result);
    } catch (error) {
      setError("Error generating segitiga");
      console.error("Error generating segitiga:", error);
    } finally {
      setLoading(false);
    }
  };

  const actionGenerateBilangaGanjilAPI = async () => {
    setLoading(true);
    setError(null);
    try {
      const formData = new FormData();
      formData.append('input_bil', valueBil);

      const response = await axios.post(
        'http://localhost:5000/api/v1/bilangan_operasi_route_api_v1/generate_bilangan_ganjil',
        formData,
        { headers: { 'Content-Type': 'multipart/form-data' } }
      );

      setValueHasilGenerate(response.data.result);
    } catch (error) {
      setError("Error generating bilangan ganjil");
      console.error("Error generating bilangan ganjil:", error);
    } finally {
      setLoading(false);
    }
  };

  const actionGenerateBilanganPrimaAPI = async () => {
    setLoading(true);
    setError(null);
    try {
      const formData = new FormData();
      formData.append('input_bil', valueBil);

      const response = await axios.post(
        'http://localhost:5000/api/v1/bilangan_operasi_route_api_v1/generate_bilangan_prima',
        formData,
        { headers: { 'Content-Type': 'multipart/form-data' } }
      );

      setValueHasilGenerate(response.data.result);
    } catch (error) {
      setError("Error generating bilangan prima");
      console.error("Error generating bilangan prima:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <input
        type="text"
        name="input_bil"
        value={valueBil}
        onChange={(e) => setValueBil(e.target.value)}
      />
      <div className="container-button" style={{ marginTop: '20px' }}>
        <button onClick={() => {
          if (!valueBil) {
            alert("Input jangan kosong");
          } else {
            actionGenerateSegitigaAPI();
          }
        }}>
          Generate Segitiga
        </button>
        <button onClick={() => {
          if (!valueBil) {
            alert("Input jangan kosong");
          } else {
            actionGenerateBilangaGanjilAPI();
          }
        }}>
          Generate Bilangan Ganjil
        </button>
        <button onClick={() => {
          if (!valueBil) {
            alert("Input jangan kosong");
          } else {
            actionGenerateBilanganPrimaAPI();
          }
        }}>
          Generate Bilangan Prima
        </button>
      </div>
      <h1>Result: </h1>
      {loading ? (
        <h3>Loading...</h3>
      ) : error ? (
        <h3>{error}</h3>
      ) : (
        <div>
          {valueHasilGenerate && valueHasilGenerate.map((item, index) => (
            <div key={index}>{item}</div>
          ))}
        </div>
      )}
    </>
  );
}

export default App;
