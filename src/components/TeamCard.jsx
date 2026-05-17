import EntityImage from './EntityImage';
import StatPill from './StatPill';

export default function TeamCard({ team }) {
  return (
    <article className="card entity-card">
      <div className="entity-top single-image">
        <EntityImage src={team.image} alt={team.name} className="team-logo" fallback="Team" />
      </div>
      <h3>{team.name}</h3>
      <div className="pill-grid">
        <StatPill label="OVR" value={team.ovr} />
        <StatPill label="ATT" value={team.att} />
        <StatPill label="MID" value={team.mid} />
        <StatPill label="DEF" value={team.def} />
        <StatPill label="AVG AGE" value={team.avgAge} />
      </div>
    </article>
  );
}
