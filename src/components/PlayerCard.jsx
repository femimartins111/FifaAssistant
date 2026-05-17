import EntityImage from './EntityImage';
import StatPill from './StatPill';

export default function PlayerCard({ player }) {
  return (
    <article className="card entity-card">
      <div className="entity-top">
        <EntityImage src={player.playerImage} alt={player.name} className="player-face" fallback="Player" />
        <EntityImage src={player.clubImage} alt={`${player.team} badge`} className="club-badge" fallback="Badge" />
      </div>
      <h3>{player.name}</h3>
      <p className="muted">{player.team}</p>
      <div className="pill-grid">
        <StatPill label="OVR" value={player.ovr} />
        <StatPill label="POT" value={player.pot} />
        <StatPill label="POS" value={player.pos} />
        <StatPill label="AGE" value={player.age} />
      </div>
    </article>
  );
}
