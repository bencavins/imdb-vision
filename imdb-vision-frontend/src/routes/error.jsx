import { useRouteError } from "react-router-dom"

export default function ErrorPage() {
  const error = useRouteError()
  console.error(error)

  return (
    <div>
      <h1>Oh no!</h1>
      <p>Something went wrong :(</p>
      <p>
        <i>{error.statusText || error.message}</i>
      </p>
    </div>
  )
}