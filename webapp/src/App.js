import logo from "./logo.svg";
import "./App.css";
import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom";
import Login from "./pages/Login.jsx";
import Dashboard from "./pages/Dashboard";
import { useStateContext } from "./context/ContextProvider";
import Sidebar from "./components/Sidebar";
import Navbar from "./components/Navbar";
import PrivateRoute from "./components/PrivateRoute";
import PageNotFound from "./components/PageNotFound";
import Signup from "./pages/Signup";
import Profile from "./pages/Profile";



function App() {
  const { username, userLoggedIn } = useStateContext();
  return (
    <div class="flex flex-row">
      <BrowserRouter>
        <div >
          {userLoggedIn ? (
            <div className="w-auto">
              <Sidebar />
                 
            </div>
          ) : (
            <div className="w-0 dark:bg-secondary-dark-bg"></div>
          )}
          </div>
        <div className="flex flex-col w-full">
         { userLoggedIn && (
          <div>
            <Navbar />
          </div>)
          }
         <div className="h-screen border border-blue-500">
            <Routes>
              <Route path="/" element={<Login />} />
              <Route path="/login" element={<Login />} />
              <Route path="/signup" element={<Signup />} />
              <Route element={<PrivateRoute />}>
                <Route element={<Dashboard />} path="/dashboard" />
                <Route element={<Profile />} path="/profile" />
              </Route>
              <Route path="*" element={<PageNotFound />} />
            </Routes>
          </div>
        </div>
      </BrowserRouter>
    </div>
  );
}

export default App;
