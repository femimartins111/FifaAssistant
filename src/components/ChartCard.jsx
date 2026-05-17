import {
  Bar,
  BarChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts';

export default function ChartCard({ title, dataKey, data, yDomain }) {
  return (
    <div className="card chart-card">
      <h3>{title}</h3>
      <div className="chart-wrap">
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis domain={yDomain} />
            <Tooltip />
            <Bar dataKey={dataKey} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
