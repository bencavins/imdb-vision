import { Outlet } from "react-router-dom"

import Header from "../components/Header"
import Search from "../components/Search"
import "./root.css"

export default function Root() {
  return (
    <>
      <div id="header-box">
        <Header id="header" />
        <Search id="search" />
      </div>
      <Outlet />
    </>
  )
}