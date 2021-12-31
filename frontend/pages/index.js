import Head from 'next/head'
import React from 'react'
import Navbar from './components/Navbar'
import Login from './components/Login'

export default function Home() {
  return (
    <div className="container">
      <Navbar />
      <br />
      <Login></Login>
    </div>
  )
}
