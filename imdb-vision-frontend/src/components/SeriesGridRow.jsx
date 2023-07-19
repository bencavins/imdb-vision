import SeriesGridCell from "./SeriesGridCell"

export default function SeriesGridRow({ rowData }) {
  return (
    <tr>
      {rowData.map(element => <SeriesGridCell data={element} />)}
    </tr>
  )
}