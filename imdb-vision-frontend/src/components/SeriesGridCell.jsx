export default function SeriesGridCell({ data }) {

  let color = "white"

  if (!data.rating) {
    color = "gray"
  } else if (data.rating.average_rating < 7.0) {
    color = "red"
  } else if (data.rating.average_rating < 8.0) {
    color = "yellow"
  } else {
    color = "green"
  }

  const style = {
    backgroundColor: color
  }
  
  return (
    <td style={style}>{data.rating ? data.rating.average_rating : "N/A"}</td>
  )
}