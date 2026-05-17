const fields = [
  ['OVR', 'ovr'],
  ['POT', 'pot'],
  ['POS', 'pos'],
  ['AGE', 'age'],
  ['Team', 'team'],
];

export default function CompareTable({ leftPlayer, rightPlayer }) {
  if (!leftPlayer || !rightPlayer) {
    return <div className="card">Select two players to compare.</div>;
  }

  return (
    <div className="card">
      <table className="compare-table">
        <thead>
          <tr>
            <th>{leftPlayer.name}</th>
            <th>Stat</th>
            <th>{rightPlayer.name}</th>
          </tr>
        </thead>
        <tbody>
          {fields.map(([label, key]) => (
            <tr key={key}>
              <td>{leftPlayer[key]}</td>
              <td>{label}</td>
              <td>{rightPlayer[key]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
