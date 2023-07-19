import SeriesGridCell from "./SeriesGridCell"

export default function SeriesGridRow({ rowData }) {
  const season_number = rowData[0].season_number

  return (
    <tr>
      <td>S{season_number}</td>
      {rowData.map(element => <SeriesGridCell key={element.id} data={element} />)}
    </tr>
  )
}