import React from 'react'
import { Outlet,Navigate } from 'react-router-dom';
import {useStateContext} from '../context/ContextProvider';
const PrivateRoute = ({ component: Component, ...rest }) => {
    const {userLoggedIn} = useStateContext();
  return (
        userLoggedIn? <Outlet />: <Navigate to="/login" /> 
  )
}

export default PrivateRoute

