import userEvent from "@testing-library/user-event";
import React from "react";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { useStateContext } from "../context/ContextProvider";
import axios from "axios";
import {Buffer} from 'buffer';
const baseurl = "http://localhost:8080/api-gateway/web";


const Login = () => {
  function decodeJwt(token) {
    var base64Payload = token.split(".")[1];
    var payloadBuffer = Buffer.from(base64Payload, "base64");
    return JSON.parse(payloadBuffer.toString());
  }
  const {
    handleUserName,
    handleUserLoggedIn,
    handleUserToken,
    handleTokenData,
  } = useStateContext();

  const {
    register,
    handleSubmit,
    watch,
    setError,
    formState: { errors },
  } = useForm();
  const navigate = useNavigate();

  const handleSignUp = () => {
    navigate("/signup");
  };

  const onSubmit = (data) => {
    axios
      .post(`${baseurl}/authenticate`, data)
      .then((response) => {
        if (response.status == 200 && response.statusText == "OK") {
          handleUserName(data["username"]);
          handleUserLoggedIn(true);
          handleUserToken(response["data"]["access_token"]);
          handleTokenData(decodeJwt(response['data']['access_token']))
          navigate("/dashboard");
        }
      })
      .catch((error) => {
        setError(
          "password",
          { type: "manual", message: "Password is incorrect!" },
          { shouldFocus: true }
        );
      });
  };
  return (
    <div className="relative flex flex-col justify-center overflow-hidden min-h-screen">
      <div className="w-full p-6 m-auto bg-white rounded-md shadow-xl ring ring-2 ring-gray-600 lg:max-w-xl">
        <form onSubmit={handleSubmit(onSubmit)} className="mt-6">
          {/* register your input into the hook by invoking the "register" function */}
          <div className="mb-2">
            <label
              htmlFor="username"
              className="block text-sm font-semibold text-gray-800"
            >
              Username
            </label>
            <input
              className="block w-full px-4 py-2 mt-2 text-purple-700 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40"
              {...register("username", { required: true })}
            />
            {errors.username && <p>This is a required field!</p>}
          </div>
          <div className="mb-2">
            <label
              htmlFor="password"
              className="block text-sm font-semibold text-gray-800"
            >
              Password
            </label>
            <input
              type="password"
              {...register("password", { required: true })}
              className="block w-full px-4 py-2 mt-2 text-purple-700 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40"
            />
            {errors.password && <p>{errors.password.message}</p>}
          </div>
          <div>
            <button className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-purple-700 rounded-md hover:bg-purple-600 focus:outline-none focus:bg-purple-600">
              Submit
            </button>
          </div>
        </form>
        <button
          className="w-full px-4 py-2 mt-5 tracking-wide text-white transition-colors duration-200 transform bg-blue-700 rounded-md hover:bg-blue-600 focus:outline-none focus:bg-blue-600"
          onClick={handleSignUp}
        >
          SignUp
        </button>
      </div>
    </div>
  );
};

export default Login;
