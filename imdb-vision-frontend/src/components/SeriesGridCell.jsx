function lerpColor(color1, color2, t) {
  // Parse the input colors to extract the RGB components
  const r1 = parseInt(color1.substr(1, 2), 16);
  const g1 = parseInt(color1.substr(3, 2), 16);
  const b1 = parseInt(color1.substr(5, 2), 16);

  const r2 = parseInt(color2.substr(1, 2), 16);
  const g2 = parseInt(color2.substr(3, 2), 16);
  const b2 = parseInt(color2.substr(5, 2), 16); 

  // Interpolate each RGB component separately
  const r = Math.round(r1 + (r2 - r1) * t);
  const g = Math.round(g1 + (g2 - g1) * t);
  const b = Math.round(b1 + (b2 - b1) * t);

  // Combine the interpolated RGB components to get the final color
  const resultColor = `#${r.toString(16).padStart(2, '0')}${g.toString(16).padStart(2, '0')}${b.toString(16).padStart(2, '0')}`;

  return resultColor;
}

export default function SeriesGridCell({ data }) {

  let color = "white"
  let t = 0

  const red = '#FF0B54'
  const yellow = '#F5FC06'
  const green = '#00C617'

  if (!data.rating) {
    color = "gray"
  } else if (data.rating.average_rating <= 5) {
    color = red
  } else if (data.rating.average_rating <= 7) {
    t = (data.rating.average_rating - 5) / 2.0
    color = lerpColor(red, yellow, t)
  } else if (data.rating.average_rating < 9) {
    t = (data.rating.average_rating - 7) / 2.0
    color = lerpColor(yellow, green, t)
  } else {
    color = green
  }

  const style = {
    backgroundColor: color
  }
  
  return (
    <td style={style}>{data.rating ? data.rating.average_rating : "N/A"}</td>
  )
}