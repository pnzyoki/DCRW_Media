import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Home from './pages/Landing';
import Admin from './pages/Dashborad';

const App: React.FC = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/admin" element={<Admin />} />
    </Routes>
  );
};

export default App;