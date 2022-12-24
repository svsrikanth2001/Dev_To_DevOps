import userEvent from "@testing-library/user-event";
import React from "react";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { useStateContext } from "../context/ContextProvider";

const Login = () => {
  const {
    username,
    handleUserName,
    userLoggedIn,
    handleUserLoggedIn,
    setUserName,
    setUserLogggedIn,
  } = useStateContext();

  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm();
  const navigate = useNavigate();
  const onSubmit = (data) => {
    handleUserName(data["username"]);
    handleUserLoggedIn(true);
    navigate("/dashboard");
  };
  return (
    <div className="relative flex flex-col justify-center overflow-hidden min-h-screen">
      <div className="w-full p-6 m-auto bg-white rounded-md shadow-xl ring ring-2 ring-gray-600 lg:max-w-xl">
      <form onSubmit={handleSubmit(onSubmit)} className="mt-6">
        {/* register your input into the hook by invoking the "register" function */}
        <div className="mb-2">
          <label htmlFor="username"  className="block text-sm font-semibold text-gray-800">
            Username
          </label>
          <input
           className="block w-full px-4 py-2 mt-2 text-purple-700 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40"
            {...register("username")}
          />
        </div>
        <div className="mb-2">
          <label htmlFor="password"  className="block text-sm font-semibold text-gray-800">
            Password
          </label>
          <input
            type="password"
            {...register("password", { required: true })}
            className="block w-full px-4 py-2 mt-2 text-purple-700 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40"
          />
        </div>
        <div>
          <button className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-purple-700 rounded-md hover:bg-purple-600 focus:outline-none focus:bg-purple-600">
            Submit
          </button>
        </div>
      </form>
      </div>
    </div>
  );
};

export default Login;
