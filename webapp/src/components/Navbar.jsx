import React from "react";
import { useStateContext } from "../context/ContextProvider";
import { useNavigate } from "react-router-dom";

const Navbar = () => {
  const {
    username,
    handleUserName,
    userLoggedIn,
    handleUserLoggedIn,
    setUserName,
    setUserLogggedIn,
  } = useStateContext();
  const navigate = useNavigate();
  return (
    <div className="relative border border-blue-500">
      <div className=" flex justify-end p-3 ">
        <button
          type="button"
          className="block p-2 h-50 w-1/6 m-2 bg-gray-500 border hover:bg-gray-400 rounded-md focus:outline-none"
          onClick={()=>{
            handleUserLoggedIn(false);
            handleUserName('');
            navigate("/")
        }}
        >
          Logout
        </button>
      </div>
    </div>
  );
};

export default Navbar;
