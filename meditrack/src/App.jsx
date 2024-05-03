import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.scss'
import Dashboard from './components/Dashboard/Dashboard'
import Register from './components/Register/Register'
import Login from './components/Login/Login'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

const router = createBrowserRouter([{
  path: '/dashboard',
  component: Dashboard,
}, {
  path: '/register',
  component: Register,
}, {
  path: '/login',
  component: Login,

}])

function App() {
  

  return (
      <div>
       <Dashboard />
       <Register />
       <Login />
      </div>
  )
}

export default App
