import { BrowserRouter, Routes, Route } from "react-router-dom";
import LogInteraction from "./pages/LogInteraction";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LogInteraction />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;