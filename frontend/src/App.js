import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Download from "./components/Download/Download";
import Upload from "./components/Upload/Upload";
import './App.css'
import AsidePanel from "./components/AsidePanel/AsidePanel";
import { useEffect, useState } from "react";
import Loader from "./components/Loader/Loader";


function App() {
  const [packButtons, setPackButtons] = useState([
    {name: 'Загрузить файл', route: '/upload'},
    {name: 'E-таблицы', route: '/download'}
  ]);
  const [isLoading, setIsLoading] = useState(true);
  useEffect(() => {
    setIsLoading(false)
  })
  return (
    <>
      <Loader className={isLoading ? 'loader' : 'loader hide'}/>
      <BrowserRouter>
        <AsidePanel packButtons={packButtons}/>
        <main id="main">
        <Routes>
            <Route path="/upload" element={<Upload />} />
            <Route path="/download" element={<Download />} />
            <Route path="*" element={<Navigate to="/upload" replace={true} />} />
        </Routes>
        </main> 
      </BrowserRouter>
    </>
  );
}

export default App;
