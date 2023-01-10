import React, { useEffect } from 'react'
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useStateContext } from "../context/ContextProvider";
const baseurl = "http://localhost:8080/api-gateway/web";
const   Profile = () => {
  const { tokendata,usertoken,handleTokenData } = useStateContext();
  const userid = tokendata["user_id"];
  const {
    register,
    handleSubmit,
    watch,
    setError,reset ,
    formState: { errors }
    

  } = useForm(    );
  const navigate = useNavigate();
  let firstname,lastname = '';


  const config = {
    headers: { Authorization: `Bearer ${usertoken}` }};
    useEffect(() => {
      async function fetchData() {
        const getdata1= {
          service: 'API_BACKEND',
          path: '/applicant',
          method: 'GET',
          query: userid
        }
        const response = await  axios.post(`${baseurl}/execute`, getdata1,config);
        firstname = response.data.data.firstname;
        lastname = response.data.data.lastname;
        reset(response.data.data)
        handleTokenData(response.data.data)
      }
  
      fetchData();
    }, [reset]);
/*
  useEffect( ()=>{
    const getdata1= {
      service: 'API_BACKEND',
      path: '/applicant',
      method: 'GET',
      query: userid
    }
    const response =     axios.post(`${baseurl}/execute`, getdata1,config)
   
 
   console.log(response);
 
   if( response.data.status_code === '200')
  {
        
        console.log(response.data["firstname"]);
        firstname = response.data['firstname'];
        lastname = response.data['lastname'];
  }
  },[])
  */
  
    function onSubmit(data){
    const dataupdated = {
      firstname: data['firstname'],
      lastname: data['lastname'],
      id: userid

    }
    //console.log(dataupdated);
    //console.log(usertoken);
    //console.log(config);
    const calldata = {
      service: 'API_BACKEND',
      path: '/applicant',
      method: 'POST',
      query: userid,
      data: dataupdated

    }
    const getdata= {
      service: 'API_BACKEND',
      path: '/applicant',
      method: 'GET',
      query: userid
    }
    const firstresponse=   axios.post(`${baseurl}/execute`, calldata,config)
    //console.log(firstresponse)

    const secondreponse = axios.post(`${baseurl}/execute`, getdata,config)
    //console.log(secondreponse)
    navigate("/dashboard")
  
  }
  return (
    <div className="relative flex flex-col justify-center overflow-hidden min-h-screen">
      <div className="w-full p-6 m-auto bg-white rounded-md shadow-xl ring ring-2 ring-gray-600 lg:max-w-xl">
        <form onSubmit={handleSubmit(onSubmit)} className="mt-6">
          {/* register your input into the hook by invoking the "register" function */}
          <div className="mb-2">
            <label
              htmlFor="firstname"
              className="block text-sm font-semibold text-gray-800"
            >
              FirstName
            </label>
            <input
              className="block w-full px-4 py-2 mt-2 text-purple-700 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40"
              {...register("firstname", { required: true } )} 
              defaultValue={firstname}
            />
            {errors.firstname && <p>This is a required field!</p>}
          </div>

          <div className="mb-2">
            <label
              htmlFor="lastname"
              className="block text-sm font-semibold text-gray-800"
            >
              LastName
            </label>
            <input
              className="block w-full px-4 py-2 mt-2 text-purple-700 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40"
              {...register("lastname", { required: true })}
              defaultValue={lastname}
            />
            {errors.lastname && <p>This is a required field!</p>}
          </div>
          <div>
            <button className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-purple-700 rounded-md hover:bg-purple-600 focus:outline-none focus:bg-purple-600">
              Update
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Profile;
