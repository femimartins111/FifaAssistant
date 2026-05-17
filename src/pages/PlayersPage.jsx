import { useMemo, useState } from 'react';
import PageHeader from '../components/PageHeader';
import PlayerCard from '../components/PlayerCard';
import { useData } from '../context/DataContext';
import { uniqueValues } from '../utils/helpers';

const INITIAL_VISIBLE_COUNT = 25;
const LOAD_MORE_AMOUNT = 25;

export default function PlayersPage() {
  const { players } = useData();

  // searchInput changes while typing.
  // search only changes when Enter is pressed, so the list does not reshuffle every key press.
  const [searchInput, setSearchInput] = useState('');
  const [search, setSearch] = useState('');

  const [teamFilter, setTeamFilter] = useState('All');
  const [positionFilter, setPositionFilter] = useState('All');
  const [visibleCount, setVisibleCount] = useState(INITIAL_VISIBLE_COUNT);

  const teams = useMemo(() => uniqueValues(players, (player) => player.team), [players]);
  const positions = useMemo(() => uniqueValues(players, (player) => player.pos), [players]);

  const filteredPlayers = useMemo(() => {
    const normalizedSearch = search.trim().toLowerCase();

    return players.filter((player) => {
      const playerText = `${player.name ?? ''} ${player.team ?? ''}`.toLowerCase();
      const searchMatch = normalizedSearch === '' || playerText.includes(normalizedSearch);
      const teamMatch = teamFilter === 'All' || player.team === teamFilter;
      const posMatch = positionFilter === 'All' || player.pos === positionFilter;

      return searchMatch && teamMatch && posMatch;
    });
  }, [players, search, teamFilter, positionFilter]);

  const visiblePlayers = useMemo(() => {
    return filteredPlayers.slice(0, visibleCount);
  }, [filteredPlayers, visibleCount]);

  function runSearch() {
    setSearch(searchInput);
    setVisibleCount(INITIAL_VISIBLE_COUNT);
  }

  function handleSearchKeyDown(event) {
    if (event.key === 'Enter') {
      runSearch();
    }
  }

  function handleTeamFilterChange(event) {
    setTeamFilter(event.target.value);
    setVisibleCount(INITIAL_VISIBLE_COUNT);
  }

  function handlePositionFilterChange(event) {
    setPositionFilter(event.target.value);
    setVisibleCount(INITIAL_VISIBLE_COUNT);
  }

  function loadMorePlayers() {
    setVisibleCount((currentCount) => currentCount + LOAD_MORE_AMOUNT);
  }

  return (
    <section>
      <PageHeader
        title="Players"
        description="Search by name, team, and position while showing face image and club badge."
      />

      <div className="toolbar card toolbar-grid-3">
        <input
          type="text"
          value={searchInput}
          onChange={(event) => setSearchInput(event.target.value)}
          onKeyDown={handleSearchKeyDown}
          placeholder="Search players or teams, then press Enter..."
        />

        <select value={teamFilter} onChange={handleTeamFilterChange}>
          <option>All</option>
          {teams.map((team) => (
            <option key={team}>{team}</option>
          ))}
        </select>

        <select value={positionFilter} onChange={handlePositionFilterChange}>
          <option>All</option>
          {positions.map((position) => (
            <option key={position}>{position}</option>
          ))}
        </select>
      </div>

      <div className="entity-grid">
        {visiblePlayers.map((player) => (
          <PlayerCard key={`${player.name}-${player.team}`} player={player} />
        ))}
      </div>

      {visibleCount < filteredPlayers.length && (
        <div style={{ marginTop: '20px', textAlign: 'center' }}>
          <button type="button" onClick={loadMorePlayers}>
            Load More
          </button>
        </div>
      )}
    </section>
  );
}
